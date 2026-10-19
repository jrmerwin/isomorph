"""
One deterministic pass over one dataset (METHOD.md section 3), producing the
benchmark card (section 4). `profile` is "v1" (the method) or "legacy"
(reproduction of the recorded session runs; see constants.PROFILES).
"""
import json, os, sys, time
import numpy as np
import pandas as pd
from . import constants as K
from .canon.ingest import read_dataset, SYSTEM
from .canon.validate import validate
from .mine.contexts import LagClasses, streams_of, inter_event_gaps
from .mine.library import discover, compositions, rows_for, library_to_json
from .score.model import FeatureMap, Model, fit_bits
from .score import baselines as B


def split_bounds(events, profile):
    lo, hi = float(events.t.min()), float(events.t.max()) + 1.0
    f1, f2, f3 = K.PROFILES[profile]["splits"]
    span = hi - lo
    return lo, lo + span * f1, lo + span * (f1 + f2), hi


def run(dataset_dir, profile="v1", seed=0, log=print, extra_rows=None):
    t0 = time.time()
    prof = K.PROFILES[profile]
    name = os.path.basename(os.path.normpath(dataset_dir))
    events, obs, gaps, side, key = read_dataset(dataset_dir)
    validate(events, obs, gaps, side)
    rng = np.random.default_rng(seed)
    entities = sorted(e for e in obs.entity.unique() if e != SYSTEM)
    streams = streams_of(events, entities)
    gap_mode = "drop" if profile == "v1" else "ignore"
    lo, p_hi, c_hi, hi = split_bounds(events, profile)

    # lag classes (3.3)
    if prof["lag_mode"] == "fixed_minutes":
        lags = LagClasses.fixed_minutes(prof["lag_edges"])
    else:
        prop_streams = {z: s[(s.t >= lo) & (s.t < p_hi)] for z, s in streams.items()}
        lags = LagClasses.from_gaps(inter_event_gaps(prop_streams), K.HORIZON_QUANTILE)
    log(f"[{name}] profile={profile} lags={[round(e, 2) for e in lags.edges]} splits=({lo:.0f},{p_hi:.0f},{c_hi:.0f},{hi:.0f})")

    # discovery (3.5-3.8)
    frags, cands, rows_prop, rows_conf = discover(streams, lags, (lo, p_hi, c_hi), rng, gaps, gap_mode,
                                                  min_count=prof["min_count"], dataset_name=name)
    rows_train = rows_prop + rows_conf
    rows_test = rows_for(streams, lags, c_hi, hi, gaps, gap_mode)
    for r in rows_train + rows_test:
        r["day"] = int(r["t"] // 1440)
    vocab = sorted(set(r["tok"] for r in rows_train + rows_test))        # prediction targets
    all_types = sorted(set(events.type))                                   # targets + system-wide context types
    n_dropped = sum(r["dropped"] for r in rows_train + rows_test)
    log(f"[{name}] candidates={len(cands)} validated fragments={len(frags)} dropped-for-gaps={n_dropped} ({time.time()-t0:.0f}s)")

    # library (3.10): all validated fragments; compositions kept only if they reduce confirmation bits
    frag_ctxs = list(dict.fromkeys(f["ctx"] for f in frags))
    if profile == "legacy":   # session selection: k-grid on confirmation bits (prop -> conf)
        best_k, best = 0, np.inf
        for k in sorted(set([0, 10, 20, 40, 80, 120, 160, len(frags)])):
            if k > len(frags): continue
            b = fit_bits(FeatureMap(vocab, True, [f["ctx"] for f in frags[:k]]), rows_prop, rows_conf).mean()
            if b < best - 1e-4: best_k, best = k, b
        frag_ctxs = list(dict.fromkeys(f["ctx"] for f in frags[:best_k]))
    comps = compositions(frags, rows_train, min_count=prof["min_count"])
    comp_ctxs = [c["ctx"] for c in comps if c["ctx"][0] in frag_ctxs and c["ctx"][1] in frag_ctxs]
    if profile == "v1" and comp_ctxs:
        b_without = fit_bits(FeatureMap(vocab, True, frag_ctxs), rows_prop, rows_conf).mean()
        b_with = fit_bits(FeatureMap(vocab, True, frag_ctxs, comp_ctxs), rows_prop, rows_conf).mean()
        if b_with >= b_without - 1e-4:
            comp_ctxs = []
    unsel_ctxs = list(dict.fromkeys(c for c, y in cands))
    triv_ctxs = B.triviality_contexts(vocab, lags)

    # scoring (3.9), test split evaluated once
    det = B.deterministic_pairs(rows_train)
    is_det = np.array([r["tok"] in det for r in rows_test])
    models = {
        "unigram": B.unigram_bits(rows_train, rows_test, vocab),
        "markov-1": B.markov_bits(rows_train, rows_test, vocab, k=1),
        "markov-2": B.markov_bits(rows_train, rows_test, vocab, k=2),
        "markov-3": None,   # not measured in v1.0: third-order context not tracked yet
        "hawkes": None,
        "logistic markov features": fit_bits(FeatureMap(vocab, True), rows_train, rows_test),
        "logistic triviality library": fit_bits(FeatureMap(vocab, True, triv_ctxs), rows_train, rows_test),
        "logistic library": fit_bits(FeatureMap(vocab, True, frag_ctxs, comp_ctxs), rows_train, rows_test),
        "logistic unselected contexts": fit_bits(FeatureMap(vocab, True, unsel_ctxs), rows_train, rows_test),
    }
    def summarise(bits):
        if bits is None: return "not measured"
        return dict(all=float(bits.mean()), non_deterministic=float(bits[~is_det].mean()) if (~is_det).any() else None,
                    deterministic=float(bits[is_det].mean()) if is_det.any() else None)
    headline = {m: summarise(b) for m, b in models.items()}
    lib_nd = headline["logistic library"]["non_deterministic"]; triv_nd = headline["logistic triviality library"]["non_deterministic"]
    best_base = min(v["non_deterministic"] for k_, v in headline.items() if isinstance(v, dict) and k_ not in ("logistic library", "logistic unselected contexts", "logistic triviality library"))
    gain_over_triviality = triv_nd - lib_nd
    gain_over_best_baseline = best_base - lib_nd

    # recovery (answer key)
    recovery = "not measured"
    if key and "mechanisms" in key:
        mech = {(m["cause"], m["effect"]): set(m.get("lags", lags.labels)) for m in key["mechanisms"]}
        found = set()
        for f in frags:
            k_ = (f["ctx"][0], f["y"])
            if k_ in mech and f["ctx"][1] in mech[k_]: found.add(k_)
        precision = sum(1 for f in frags if (f["ctx"][0], f["y"]) in mech) / max(1, len(frags))
        recovery = dict(recall=len(found) / max(1, len(mech)), precision=precision, n_mechanisms=len(mech), n_found=len(found))

    # library stats
    counts = pd.Series([r["tok"] for r in rows_train]).value_counts()
    chatty = set(counts.index[: max(1, int(np.ceil(0.1 * len(counts))))])
    chatty_share = float(np.mean([f["ctx"][0] in chatty or f["y"] in chatty for f in frags])) if frags else 0.0

    card = dict(
        method_version=K.METHOD_VERSION, profile=profile, seed=seed, dataset=name,
        identity=dict(kind=side.get("kind"), origin=side.get("origin"), time_unit=side.get("time_unit"),
                      span=[lo, hi], entity_key=side.get("entity_key"), entities=entities,
                      symbolization=side.get("symbolization", "fixed (declared in sidecar)")),
        scale=dict(events=int(len(events)), events_per_day=float(len(events) / ((hi - lo) / 1440)), types=len(vocab),
                   n_entities=len(entities), period=side.get("period"), signal_floor="not measured",
                   lag_edges=[float(e) for e in lags.edges], events_dropped_for_gaps=int(n_dropped),
                   test_events=len(rows_test), deterministic_types=sorted(det)),
        headline_bits=headline,
        gain=dict(over_triviality=gain_over_triviality, over_best_baseline=gain_over_best_baseline,
                  best_baseline_bits=best_base, claim=("beats baselines" if gain_over_triviality >= K.CLAIM_MIN_GAIN_BITS and gain_over_best_baseline >= K.CLAIM_MIN_GAIN_BITS else "no gain")),
        library=dict(fragments=len(frags), fragments_used=len(frag_ctxs), compositions_kept=len(comp_ctxs),
                     candidates=len(cands), null_survival=dict(circular=1.0, cycle="not measured", rewire="not measured"),
                     chatty_share=chatty_share),
        recovery=recovery, transfer="not measured (collection step)", lineage="not measured (collection step)",
        elapsed_s=round(time.time() - t0, 1),
    )
    os.makedirs(os.path.join(dataset_dir, "out"), exist_ok=True)
    json.dump(library_to_json(frags, comps), open(os.path.join(dataset_dir, "out", f"library_{profile}.json"), "w"), indent=1)
    json.dump(card, open(os.path.join(dataset_dir, "out", f"benchmark_{profile}.json"), "w"), indent=1)
    return card, dict(frags=frags, frag_ctxs=frag_ctxs, comp_ctxs=comp_ctxs, vocab=vocab, all_types=all_types, lags=lags,
                      rows_train=rows_train, rows_test=rows_test, streams=streams, bounds=(lo, p_hi, c_hi, hi), gaps=gaps, gap_mode=gap_mode)


def card_markdown(card):
    h = card["headline_bits"]
    lines = [f"# Benchmark card — {card['dataset']} (method v{card['method_version']}, profile {card['profile']}, seed {card['seed']})", "",
             f"Kind: {card['identity']['kind']} · entities: {', '.join(card['identity']['entities'])} · types: {card['scale']['types']} · "
             f"events/day: {card['scale']['events_per_day']:.0f} · lag edges: {card['scale']['lag_edges']} · dropped for gaps: {card['scale']['events_dropped_for_gaps']}", "",
             "| model | all | non-deterministic | deterministic |", "| --- | --- | --- | --- |"]
    for m, v in h.items():
        if isinstance(v, dict):
            lines.append(f"| {m} | {v['all']:.3f} | {v['non_deterministic']:.3f} | {v['deterministic'] if v['deterministic'] is None else round(v['deterministic'], 3)} |")
        else:
            lines.append(f"| {m} | {v} | | |")
    g = card["gain"]
    lines += ["", f"Gain over triviality: {g['over_triviality']:.3f} bits · over best baseline ({g['best_baseline_bits']:.3f}): {g['over_best_baseline']:.3f} bits · claim: **{g['claim']}**",
              f"Library: {card['library']['fragments']} fragments ({card['library']['fragments_used']} used), {card['library']['compositions_kept']} compositions, chatty share {card['library']['chatty_share']:.2f}",
              f"Recovery: {card['recovery']}"]
    return "\n".join(lines) + "\n"
