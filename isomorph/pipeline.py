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
from .mine.nulls import period_estimate
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
    gap_mode = "clip" if profile == "v1" else "ignore"      # v6 (3.6): a gap clips the window; v1-v5 dropped the target
    lo, p_hi, c_hi, hi = split_bounds(events, profile)

    # lag classes (3.3)
    if prof["lag_mode"] == "fixed_minutes":
        lags = LagClasses.fixed_minutes(prof["lag_edges"])
    elif prof["lag_mode"] == "recurrence":          # v2 (METHOD 3.3)
        lags = LagClasses.from_recurrence(streams, lo, p_hi)
    else:                                            # v1 rule, kept for the record
        prop_streams = {z: s[(s.t >= lo) & (s.t < p_hi)] for z, s in streams.items()}
        lags = LagClasses.from_gaps(inter_event_gaps(prop_streams), K.HORIZON_QUANTILE)
    log(f"[{name}] profile={profile} lags={[round(e, 2) for e in lags.edges]} splits=({lo:.0f},{p_hi:.0f},{c_hi:.0f},{hi:.0f})")

    # discovery (3.5-3.8)
    period = side.get("period")
    if profile == "v1" and (period in (None, "auto")):
        period = period_estimate(events, lo, p_hi)
    nulls = ("circular", "cycle", "rewire") if profile == "v1" else ("circular",)
    frags, cands, rows_prop, rows_conf, dinfo = discover(streams, lags, (lo, p_hi, c_hi), rng, gaps, gap_mode,
                                                         min_count=prof["min_count"], dataset_name=name, nulls=nulls,
                                                         period=period if isinstance(period, (int, float)) else None,
                                                         events=events, entities=entities, floor_mode=prof["min_count_mode"])
    log(f"[{name}] period={period} floor={dinfo['signal_floor']} min_count={dinfo['min_count']} nulls={dinfo['nulls_run']} survival={ {k: (round(v, 2) if v is not None else None) for k, v in dinfo['null_survival'].items()} }")
    rows_train = rows_prop + rows_conf
    rows_test = rows_for(streams, lags, c_hi, hi, gaps, gap_mode)
    for r in rows_train + rows_test:
        r["day"] = int(r["t"] // 1440)
    vocab = sorted(set(r["tok"] for r in rows_train + rows_test))        # prediction targets
    all_types = sorted(set(events.type))                                   # targets + system-wide context types (also used by the decay baseline)
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
    comps = compositions(frags, rows_train, min_count=dinfo["min_count"])
    comp_ctxs = [c["ctx"] for c in comps if c["ctx"][0] in frag_ctxs and c["ctx"][1] in frag_ctxs]
    if profile == "v1" and comp_ctxs:
        b_without = fit_bits(FeatureMap(vocab, True, frag_ctxs), rows_prop, rows_conf).mean()
        b_with = fit_bits(FeatureMap(vocab, True, frag_ctxs, comp_ctxs), rows_prop, rows_conf).mean()
        if b_with >= b_without - 1e-4:
            comp_ctxs = []
    # syntax (3.15, v6): chains of two validated fragments, and returns; kept as features only if they reduce confirmation bits
    chains, cinfo, chain_keys_used = [], dict(candidates=0, lift_ok=0, null_passed=0, admitted=0, returns=0), []
    if profile == "v1" and frags:
        from .mine.syntax import discover_chains, mark_rows, times_by_tok
        chains, cinfo = discover_chains(frags, streams, lags, (lo, p_hi, c_hi), rng, gaps, gap_mode, rows_prop, rows_conf, log)
        if chains:
            mark_rows(rows_train, times_by_tok(streams, lo, c_hi), lags, chains, gaps)
            mark_rows(rows_test, times_by_tok(streams, c_hi, hi), lags, chains, gaps)
            chain_keys = [h["key"] for h in chains]
            b_without = fit_bits(FeatureMap(vocab, True, frag_ctxs, comp_ctxs), rows_prop, rows_conf).mean()
            b_with = fit_bits(FeatureMap(vocab, True, frag_ctxs, comp_ctxs, chain_keys), rows_prop, rows_conf).mean()
            chain_keys_used = chain_keys if b_with < b_without - 1e-4 else []
    log(f"[{name}] chains: {cinfo['candidates']} candidates, {cinfo['lift_ok']} with conditional lift, {cinfo['null_passed']} above the null, "
        f"{cinfo['admitted']} admitted ({cinfo['returns']} returns), {len(chain_keys_used)} used as features")
    unsel_ctxs = list(dict.fromkeys(c for c, y in cands))
    triv_ctxs = B.triviality_contexts(vocab, lags, rows_train)
    triv_pairs = B.alternating_pairs(rows_train)

    # scoring (3.9), test split evaluated once
    det = B.deterministic_pairs(rows_train)
    is_det = np.array([r["tok"] in det for r in rows_test])
    models = {
        "unigram": B.unigram_bits(rows_train, rows_test, vocab),
        "markov-1": B.markov_bits(rows_train, rows_test, vocab, k=1),
        "markov-2": B.markov_bits(rows_train, rows_test, vocab, k=2),
        "markov-3": B.markov_bits(rows_train, rows_test, vocab, k=3),
        "hawkes-like decay features": B.hawkes_bits(rows_train, rows_test, vocab, all_types, tau=lags.edges[1]),
        "logistic markov features": fit_bits(FeatureMap(vocab, True), rows_train, rows_test),
        "logistic triviality library": fit_bits(FeatureMap(vocab, True, triv_ctxs), rows_train, rows_test),
        "logistic library": fit_bits(FeatureMap(vocab, True, frag_ctxs, comp_ctxs, chain_keys_used), rows_train, rows_test),
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
        # match="role_prefix": the key names roles (cause role -> effect role, any event direction); default: full types
        nm = (lambda s: s.split(":")[0]) if key.get("match") == "role_prefix" else (lambda s: s)
        found = set()
        for f in frags:
            k_ = (nm(f["ctx"][0]), nm(f["y"]))
            if k_ in mech and f["ctx"][1] in mech[k_]: found.add(k_)
        precision = sum(1 for f in frags if (nm(f["ctx"][0]), nm(f["y"])) in mech) / max(1, len(frags))
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
                   n_entities=len(entities), period=period, signal_floor=dinfo["signal_floor"], min_count=dinfo["min_count"],
                   lag_edges=[float(e) for e in lags.edges], events_dropped_for_gaps=int(n_dropped),
                   test_events=len(rows_test), deterministic_types=sorted(det)),
        headline_bits=headline,
        gain=dict(over_triviality=gain_over_triviality, over_best_baseline=gain_over_best_baseline,
                  best_baseline_bits=best_base, claim=("beats baselines" if gain_over_triviality >= K.CLAIM_MIN_GAIN_BITS and gain_over_best_baseline >= K.CLAIM_MIN_GAIN_BITS else "no gain")),
        library=dict(fragments=len(frags), fragments_used=len(frag_ctxs), compositions_kept=len(comp_ctxs),
                     chains=len(chains), chains_used=len(chain_keys_used), returns=cinfo["returns"], chain_search=cinfo,
                     candidates=len(cands), nulls_run=dinfo["nulls_run"], null_survival=dinfo["null_survival"],
                     trivial_pairs=sorted(list(pq) for pq in triv_pairs),
                     chatty_share=chatty_share),
        recovery=recovery, transfer="not measured (collection step)", lineage="not measured (collection step)",
        elapsed_s=round(time.time() - t0, 1),
    )
    os.makedirs(os.path.join(dataset_dir, "out"), exist_ok=True)
    lib_json = library_to_json(frags, comps, chains, chain_keys_used)
    if side.get("tags"):   # v4+: tag-prefixed shapes travel with the library, so a re-run never strips them
        from .choose.pos import shape_of, shape_of_chain
        from collections import Counter
        for f in lib_json["fragments"]: f["shape"] = shape_of(f["prior"], f["lag"], f["target"], side["tags"])
        lib_json["shape_counts"] = dict(Counter(f["shape"] for f in lib_json["fragments"]).most_common())
        for h in lib_json["chains"]: h["shape"] = shape_of_chain(h["a"], h["l1"], h["b"], h["l2"], h["c"], side["tags"], h["is_return"])
    json.dump(lib_json, open(os.path.join(dataset_dir, "out", f"library_{profile}.json"), "w"), indent=1)
    json.dump(card, open(os.path.join(dataset_dir, "out", f"benchmark_{profile}.json"), "w"), indent=1)
    state = dict(frags=frags, frag_ctxs=frag_ctxs, comp_ctxs=comp_ctxs, chains=chains, chain_keys_used=chain_keys_used, vocab=vocab, all_types=all_types, lags=lags,
                 rows_train=rows_train, rows_test=rows_test, streams=streams, bounds=(lo, p_hi, c_hi, hi), gaps=gaps, gap_mode=gap_mode)
    try:   # state cache for the collection step (not committed; keyed by version/profile/seed in the card)
        import pickle
        with open(os.path.join(dataset_dir, "out", f"state_{profile}_{seed}.pkl"), "wb") as fh:
            pickle.dump(dict(method_version=K.METHOD_VERSION, profile=profile, seed=seed, state=state), fh, protocol=5)
    except Exception as e:
        log(f"[{name}] state cache not written: {e}")
    return card, state


def load_state(dataset_dir, profile="v1", seed=0):
    """Cached (card, state) from the last run() with this version/profile/seed, else None."""
    import pickle
    pk = os.path.join(dataset_dir, "out", f"state_{profile}_{seed}.pkl"); bj = os.path.join(dataset_dir, "out", f"benchmark_{profile}.json")
    if not (os.path.exists(pk) and os.path.exists(bj)): return None
    rec = pickle.load(open(pk, "rb")); card = json.load(open(bj))
    # valid if produced at or after the last change to the per-dataset rules (collection-step versions do not touch cards)
    if rec.get("method_version", 0) < K.CARD_RULES_VERSION or card.get("method_version", 0) < K.CARD_RULES_VERSION or card.get("seed") != seed: return None
    return card, rec["state"]


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
              f"Syntax (3.15): {card['library'].get('chains', 0)} chains ({card['library'].get('chains_used', 0)} used), {card['library'].get('returns', 0)} returns",
              f"Recovery: {card['recovery']}"]
    return "\n".join(lines) + "\n"
