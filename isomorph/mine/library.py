"""
Fragment discovery (METHOD.md 3.5, 3.8, 3.10): lagged-pair candidates on the
proposal split, lift and null tests, confirmation on the confirmation split,
compositions, provenance fields.
"""
from collections import defaultdict
import numpy as np
from .. import constants as K
from .contexts import contexts_for_stream


def pair_counts(rows):
    cnt, base = defaultdict(lambda: defaultdict(int)), defaultdict(int)
    for r in rows:
        for c in r["ctx"]:
            cnt[c][r["tok"]] += 1; base[c] += 1
    return cnt, base


def rows_for(streams, lags, lo, hi, gaps=None, gap_mode="drop", shift=None):
    rows = []
    for z, s in streams.items():
        sub = s[(s.t >= lo) & (s.t < hi)]
        for r in contexts_for_stream(sub, lags, entity=z, gaps=gaps, shift=shift, gap_mode=gap_mode):
            r["entity"] = z; rows.append(r)
    return rows


def circular_null_max(streams, lags, lo, hi, rng, n_draws, gaps=None, gap_mode="drop"):
    """Max count of every (ctx, y) over n_draws per-type circular shifts (legacy semantics:
    one offset per type, applied to every stream, modulo each stream's span)."""
    toks_all = sorted(set(t for s in streams.values() for t in s.type))
    null_max = defaultdict(int)
    for _ in range(n_draws):
        shift = {t: float(rng.uniform(1.0, hi - lo)) for t in toks_all}
        cn, _ = pair_counts(rows_for(streams, lags, lo, hi, gaps, gap_mode, shift=shift))
        for c, d in cn.items():
            for y, v in d.items():
                if v > null_max[(c, y)]:
                    null_max[(c, y)] = v
    return null_max


def discover(streams, lags, splits, rng, gaps=None, gap_mode="drop", min_count=5, dataset_name=""):
    """splits = (prop_lo, prop_hi, conf_hi). Returns (fragments, candidate_contexts, rows_prop, rows_conf)."""
    plo, phi, chi = splits
    rows_prop = rows_for(streams, lags, plo, phi, gaps, gap_mode)
    rows_conf = rows_for(streams, lags, phi, chi, gaps, gap_mode)
    cnt_p, base_p = pair_counts(rows_prop); cnt_c, base_c = pair_counts(rows_conf)
    uni = defaultdict(int)
    for r in rows_prop: uni[r["tok"]] += 1
    n_p = len(rows_prop)
    null_max = circular_null_max(streams, lags, plo, phi, rng, K.N_NULL_DRAWS, gaps, gap_mode)
    frags, cands = [], []
    for c, d in cnt_p.items():
        for y, v in d.items():
            if v < min_count:
                continue
            lift_p = (v / base_p[c]) / (uni[y] / n_p)
            cands.append((c, y))
            if lift_p < K.LIFT_MIN or v <= null_max[(c, y)]:
                continue
            vc = cnt_c[c][y]
            lift_c = ((vc / base_c[c]) / (uni[y] / n_p)) if base_c[c] else 0.0
            if vc >= K.CONFIRM_MIN_COUNT and lift_c >= K.LIFT_MIN:
                frags.append(dict(ctx=c, y=y, count=v, lift=lift_p, lift_conf=lift_c, null_max=int(null_max[(c, y)]),
                                  nulls_survived=["circular"], first_validated_in=dataset_name,
                                  confirmed_in=[], failed_in=[]))
    frags.sort(key=lambda f: -f["lift"] * np.log(f["count"]))
    return frags, cands, rows_prop, rows_conf


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


def library_to_json(frags, comps):
    return dict(fragments=[dict(prior=f["ctx"][0], lag=f["ctx"][1], target=f["y"], count=f["count"], lift=f["lift"],
                                lift_conf=f["lift_conf"], null_max=f["null_max"], nulls_survived=f["nulls_survived"],
                                first_validated_in=f["first_validated_in"], confirmed_in=f["confirmed_in"], failed_in=f["failed_in"])
                           for f in frags],
                compositions=[dict(priors=[list(c["ctx"][0]), list(c["ctx"][1])], target=c["y"], count=c["count"]) for c in comps])
