"""
Fragment discovery (METHOD.md 3.5-3.10): lagged-pair candidates on the proposal
split, lift and null tests (every applicable null), confirmation on the
confirmation split, compositions, provenance fields.
"""
from collections import defaultdict
import numpy as np
from .. import constants as K
from .contexts import contexts_for_stream, pair_counts
from .nulls import null_max_circular, null_max_rewire, signal_floor


def rows_for(streams, lags, lo, hi, gaps=None, gap_mode="drop", shift=None, want_gaps=True):
    rows = []
    for z, s in streams.items():
        sub = s[(s.t >= lo) & (s.t < hi)]
        for r in contexts_for_stream(sub, lags, entity=z, gaps=gaps, shift=shift, gap_mode=gap_mode, want_gaps=want_gaps):
            r["entity"] = z; rows.append(r)
    return rows


def discover(streams, lags, splits, rng, gaps=None, gap_mode="drop", min_count=5, dataset_name="",
             nulls=("circular",), period=None, events=None, entities=None, floor_mode="fixed"):
    """splits = (prop_lo, prop_hi, conf_hi). nulls: subset of circular / cycle / rewire.
    Returns (fragments, candidate_contexts, rows_prop, rows_conf, info)."""
    plo, phi, chi = splits
    rows_prop = rows_for(streams, lags, plo, phi, gaps, gap_mode)
    rows_conf = rows_for(streams, lags, phi, chi, gaps, gap_mode)
    cnt_p, base_p = pair_counts(rows_prop); cnt_c, base_c = pair_counts(rows_conf)
    uni = defaultdict(int)
    for r in rows_prop: uni[r["tok"]] += 1
    n_p = len(rows_prop)
    nm = {}
    nm["circular"] = null_max_circular(streams, lags, plo, phi, rng, K.N_NULL_DRAWS, gaps, gap_mode)
    periods = [p for p in (period if isinstance(period, (list, tuple)) else [period]) if p]
    if "cycle" in nulls and periods:          # v7: the cycle null gate at each period found (slow, then fast)
        for i, p in enumerate(periods):
            nm["cycle" if i == 0 else "cycle_fast"] = null_max_circular(streams, lags, plo, phi, rng, K.N_NULL_DRAWS, gaps, gap_mode, period=p)
    if "rewire" in nulls and events is not None and entities is not None and len(entities) > 1:
        nm["rewire"] = null_max_rewire(events, entities, lags, plo, phi, rng, K.N_NULL_DRAWS, gaps, gap_mode)
    floor = signal_floor(nm["circular"], cnt_p, rng, K.FLOOR_PAIRS)
    if floor_mode == "floor":
        min_count = max(floor, 1)
    frags, cands = [], []
    survival = {k: 0 for k in nm}; n_lift_ok = 0
    for c, d in cnt_p.items():
        for y, v in d.items():
            if v < min_count:
                continue
            lift_p = (v / base_p[c]) / (uni[y] / n_p)
            cands.append((c, y))
            if lift_p < K.LIFT_MIN:
                continue
            n_lift_ok += 1
            passed = [k for k in nm if v > nm[k][(c, y)]]
            for k in passed: survival[k] += 1
            gates = [k for k in nm if k != "rewire"]
            if any(k not in passed for k in gates):
                continue
            vc = cnt_c[c][y]
            lift_c = ((vc / base_c[c]) / (uni[y] / n_p)) if base_c[c] else 0.0
            if vc >= K.CONFIRM_MIN_COUNT and lift_c >= K.LIFT_MIN:
                frags.append(dict(ctx=c, y=y, count=v, lift=lift_p, lift_conf=lift_c,
                                  null_max={k: int(nm[k][(c, y)]) for k in nm}, nulls_survived=sorted(passed),
                                  binding_evidence=("rewire" in passed) if "rewire" in nm else None,
                                  first_validated_in=dataset_name, confirmed_in=[], failed_in=[]))
    frags.sort(key=lambda f: -f["lift"] * np.log(f["count"]))
    info = dict(signal_floor=floor, min_count=min_count, nulls_run=sorted(nm),
                null_survival={k: (survival[k] / n_lift_ok if n_lift_ok else None) for k in nm}, n_lift_ok=n_lift_ok)
    return frags, cands, rows_prop, rows_conf, info


def compositions(frags, rows, min_count=5):
    by_y = defaultdict(list)
    for f in frags: by_y[f["y"]].append(f["ctx"])
    comps = defaultdict(int)
    for r in rows:
        cs = [c for c in by_y.get(r["tok"], []) if c in r["ctx"]]
        for i in range(len(cs)):
            for j in range(i + 1, len(cs)):
                comps[(cs[i], cs[j], r["tok"])] += 1
    return [dict(ctx=(a, b), y=y, count=v) for (a, b, y), v in comps.items() if v >= min_count]


def library_to_json(frags, comps, chains=(), chain_keys_used=()):
    from .syntax import chains_to_json
    return dict(chains=chains_to_json(chains, chain_keys_used), fragments=[dict(prior=f["ctx"][0], lag=f["ctx"][1], target=f["y"], count=f["count"], lift=f["lift"],
                                lift_conf=f["lift_conf"], null_max=f["null_max"], nulls_survived=f["nulls_survived"],
                                binding_evidence=f.get("binding_evidence"),
                                first_validated_in=f["first_validated_in"], confirmed_in=f["confirmed_in"], failed_in=f["failed_in"])
                           for f in frags],
                compositions=[dict(priors=[list(c["ctx"][0]), list(c["ctx"][1])], target=c["y"], count=c["count"]) for c in comps])
