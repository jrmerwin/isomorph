"""
Symbolization by compression (METHOD.md 3.2, v1 implementation).

A raw wide frame is described by a `layout`:
    layout = dict(
        time="minute",                                  # time column, dataset units
        entities={"A": {"T": "T_A", "CO2": "CO2_A", "heater": "heater_A", "occ": "occ_A"}, ...},
        system={"setpoint": "setpoint", "T_out": "T_out", "vibration": "vibration"},
        kinds={"T": "continuous", "CO2": "continuous", "heater": "binary", "occ": "count", "setpoint": "categorical", ...},
        observation={"C": (43200, 86400)},              # optional per-entity observed interval
    )
A *role* (T, CO2, heater, ...) is one variable that may appear in every entity; a scheme is
chosen per role, shared across entities, so that the same mechanism gets the same symbols in
every unit.

Schemes for continuous roles: quantile crossings q20/50/80, quantile crossings q10/90,
sign changes of the smoothed derivative (window = 1% of the series length). All debounced
(constants.DEBOUNCE). Binary roles emit on/off; count roles emit +/- steps; categorical roles
emit transitions. PELT change-points are not in v1.0 (changelog).

Criterion for role V: TOTAL confirmation-split bits of the whole event table (every role's
events, V's included) under the trial scheme, with Markov features + all lagged contexts with
count >= 3. Total, not per event: a scheme that floods the table with chatter pays for every
event it adds, and a scheme that makes the rest of the system predictable is rewarded. Roles
are optimised one at a time in order of event count, two passes.
"""
import numpy as np
import pandas as pd
from .. import constants as K
from ..canon.ingest import make_events, crossings, SYSTEM
from ..mine.contexts import LagClasses, streams_of, inter_event_gaps
from ..mine.library import rows_for
from ..mine.contexts import pair_counts
from ..score.model import FeatureMap, fit_bits

SCHEMES = ("q20_50_80", "q10_90", "dsign")


def quantile_thresholds(series_list, qs):
    x = np.concatenate([s[~np.isnan(s)] for s in series_list])
    return [float(np.round(np.quantile(x, q), 3)) for q in qs]


def correlation_time(x, max_lag=5000):
    """First lag at which the series' autocorrelation drops below 0.5 (its own time scale)."""
    v = x[~np.isnan(x)]; v = v - v.mean()
    if v.std() == 0: return 1
    for k in range(1, min(max_lag, len(v) // 2)):
        if np.corrcoef(v[:-k], v[k:])[0, 1] < 0.5: return k
    return max_lag


def residual_ratio(x, scheme, thresholds=None, window=None):
    """Reconstruction residual std / series std under a scheme: band means for quantile schemes,
    linear interpolation between smoothed-series extrema for dsign."""
    v = x.astype(float); ok = ~np.isnan(v)
    if ok.sum() < 10 or v[ok].std() == 0: return np.inf
    if scheme.startswith("q"):
        band = np.zeros(len(v), int)
        for th in thresholds: band += (v > th).astype(int)
        rec = np.full(len(v), np.nan)
        for b in np.unique(band[ok]):
            m = ok & (band == b); rec[m] = v[m].mean()
        return float(np.nanstd(v - rec) / v[ok].std())
    ev = derivative_sign_events(v, window)
    idx = np.array([i for i, _, _ in ev]); 
    if len(idx) < 2: return np.inf
    rec = np.interp(np.arange(len(v)), idx, v[idx])
    return float(np.nanstd(v - rec) / v[ok].std())


def derivative_sign_events(x, window):
    """Local extrema of the smoothed series: 'peak' / 'trough'."""
    xs = pd.Series(x).rolling(window, center=True, min_periods=1).mean().values
    d = np.diff(xs); ev = []
    sign = None; i = 1
    while i < len(d):
        if np.isnan(d[i]) or np.isnan(d[i - 1]):
            sign = None; i += 1; continue
        s = 1 if d[i] > 0 else (-1 if d[i] < 0 else 0)
        if s != 0 and sign is not None and s != sign:
            ev.append((i, "trough" if s > 0 else "peak", float(x[i])))
        if s != 0: sign = s
        i += 1
    return ev


def symbolize_role(df, layout, role, scheme, thresholds_cache):
    """Rows for one role under one scheme, over every entity that has it (and system)."""
    rows = []; t = df[layout["time"]].values.astype(float)
    kind = layout["kinds"][role]
    holders = [(e, cols[role]) for e, cols in layout["entities"].items() if role in cols]
    if role in layout.get("system", {}):
        holders.append((SYSTEM, layout["system"][role]))
    if kind == "continuous":
        if scheme is None:
            return rows
        if scheme.startswith("q"):
            qs = [int(q) / 100 for q in scheme[1:].split("_")]
            key = (role, scheme)
            if key not in thresholds_cache:
                thresholds_cache[key] = quantile_thresholds([df[c].values.astype(float) for _, c in holders], qs)
            th = thresholds_cache[key]
            for ent, col in holders:
                for i, e, v in crossings(df[col].values.astype(float), th, K.DEBOUNCE):
                    rows.append(dict(t=t[i], entity=ent, type=f"{role}:{e}", value=v))
        elif scheme == "dsign":
            key = (role, "window")
            if key not in thresholds_cache:
                thresholds_cache[key] = max(3, int(np.median([correlation_time(df[c].values.astype(float)) for _, c in holders])))
            w = thresholds_cache[key]
            for ent, col in holders:
                for i, e, v in derivative_sign_events(df[col].values.astype(float), w):
                    rows.append(dict(t=t[i], entity=ent, type=f"{role}:{e}", value=v))
    elif kind == "binary":
        for ent, col in holders:
            x = df[col].values
            for i in np.where((x[1:] == 1) & (x[:-1] == 0))[0] + 1: rows.append(dict(t=t[i], entity=ent, type=f"{role}:on", value=1.0))
            for i in np.where((x[1:] == 0) & (x[:-1] == 1))[0] + 1: rows.append(dict(t=t[i], entity=ent, type=f"{role}:off", value=0.0))
    elif kind == "count":
        for ent, col in holders:
            x = df[col].values; d = np.diff(x)
            for i in np.where(d > 0)[0] + 1:
                for _ in range(int(d[i - 1])): rows.append(dict(t=t[i], entity=ent, type=f"{role}:up", value=float(x[i])))
            for i in np.where(d < 0)[0] + 1:
                for _ in range(int(-d[i - 1])): rows.append(dict(t=t[i], entity=ent, type=f"{role}:down", value=float(x[i])))
    elif kind == "categorical":
        for ent, col in holders:
            x = df[col].values; d = np.diff(x)
            for i in np.where(d > 0)[0] + 1: rows.append(dict(t=t[i], entity=ent, type=f"{role}:up", value=float(x[i])))
            for i in np.where(d < 0)[0] + 1: rows.append(dict(t=t[i], entity=ent, type=f"{role}:down", value=float(x[i])))
    return rows


def assemble(df, layout, choice, cache):
    rows = []
    for role in layout["kinds"]:
        rows += symbolize_role(df, layout, role, choice.get(role), cache)
    ev = make_events(rows)
    obs = layout.get("observation", {})
    keep = np.ones(len(ev), bool)
    for ent, (s, e) in obs.items():
        keep &= ~((ev.entity.values == ent) & ((ev.t.values < s) | (ev.t.values >= e)))
    ev = ev[keep].reset_index(drop=True); ev["event_id"] = np.arange(len(ev))
    return ev


def criterion(ev, role, lo, p_hi, c_hi, log=None):
    """Total confirmation bits of the whole table (see module docstring)."""
    entities = sorted(e for e in ev.entity.unique() if e != SYSTEM) + [SYSTEM]   # system-wide events are targets here
    streams = streams_of(ev, entities)
    prop = {z: s[(s.t >= lo) & (s.t < p_hi)] for z, s in streams.items()}
    gaps_ = inter_event_gaps(prop)
    if len(gaps_) < 10: return np.inf
    lags = LagClasses.from_gaps(gaps_, K.HORIZON_QUANTILE)
    rows_p = rows_for(streams, lags, lo, p_hi, None, "ignore"); rows_c = rows_for(streams, lags, p_hi, c_hi, None, "ignore")
    tgt_p, tgt_c = rows_p, rows_c
    if len(tgt_c) < 20 or len(tgt_p) < 50: return np.inf
    vocab = sorted(set(r["tok"] for r in tgt_p + tgt_c))
    cnt, base = pair_counts(tgt_p)
    ctxs = [c for c, b in base.items() if b >= 3 and any(v >= 3 for v in cnt[c].values())]
    return float(fit_bits(FeatureMap(vocab, True, ctxs), tgt_p, tgt_c).sum())


def choose_symbolization(df, layout, splits_frac=(0.5, 0.25), log=print, passes=2):
    """Returns (choice per role, thresholds used, trace)."""
    t = df[layout["time"]].values.astype(float); lo, hi = float(t.min()), float(t.max()) + 1
    p_hi, c_hi = lo + (hi - lo) * splits_frac[0], lo + (hi - lo) * (splits_frac[0] + splits_frac[1])
    cache = {}
    cont = [r for r, k in layout["kinds"].items() if k == "continuous"]
    choice = {r: (SCHEMES[0] if k == "continuous" else None) for r, k in layout["kinds"].items()}
    # order of event count under the initial choice
    ev0 = assemble(df, layout, choice, cache)
    counts = {r: int((ev0.type.str.split(":").str[0] == r).sum()) for r in cont}
    order = sorted(cont, key=lambda r: -counts[r])
    trace = []
    def admissible(role, sch):
        holders = [cols[role] for cols in layout["entities"].values() if role in cols]
        if role in layout.get("system", {}): holders.append(layout["system"][role])
        cache_key = (role, sch) if sch.startswith("q") else (role, "window")
        if cache_key not in cache:
            symbolize_role(df, layout, role, sch, cache)   # fills thresholds / window
        if sch.startswith("q"):
            ratios = [residual_ratio(df[c].values, sch, thresholds=cache[cache_key]) for c in holders]
        else:
            ratios = [residual_ratio(df[c].values, sch, window=cache[cache_key]) for c in holders]
        return float(np.median(ratios)) <= K.FAITHFULNESS_MAX_RESIDUAL, float(np.median(ratios))
    faith = {}
    for p in range(passes):
        for role in order:
            scores = {}
            for sch in SCHEMES:
                ok, ratio = admissible(role, sch); faith[(role, sch)] = ratio
                if not ok:
                    scores[sch] = np.inf; continue
                trial = dict(choice); trial[role] = sch
                ev = assemble(df, layout, trial, cache)
                scores[sch] = criterion(ev, role, lo, p_hi, c_hi)
            if all(v == np.inf for v in scores.values()):
                choice[role] = None      # no admissible scheme: the role emits no events
                log(f"  pass {p} {role:10s} no scheme reconstructs the series within {K.FAITHFULNESS_MAX_RESIDUAL} of its std "
                    f"(residual ratios {', '.join(f'{s}={faith[(role, s)]:.2f}' for s in SCHEMES)}); role emits no events")
                trace.append(dict(pass_=p, role=role, scores={}, chosen=None)); continue
            best = min(scores, key=scores.get)
            changed = best != choice[role]; choice[role] = best
            trace.append(dict(pass_=p, role=role, scores=scores, chosen=best))
            log(f"  pass {p} {role:10s} " + "  ".join((f"{s}={v/1000:.1f}kb" if v < np.inf else f"{s}=unfaithful({faith[(role, s)]:.2f})") for s, v in scores.items()) + f"  -> {best}{' *' if changed else ''}")
    thresholds = {f"{r}": cache.get((r, choice[r])) for r in cont if choice[r] and choice[r].startswith("q")}
    thresholds.update({f"{r}_window": cache.get((r, "window")) for r in cont if choice[r] == "dsign"})
    return choice, thresholds, trace


def write_chosen_dataset(df, layout, choice, outdir, sidecar_extra=None, gaps=(), kind="synthetic", origin=""):
    """Assemble events under `choice` and write the canonical files."""
    import os, json
    from ..canon.ingest import write_dataset
    cache = {}
    ev = assemble(df, layout, choice, cache)
    t = df[layout["time"]].values.astype(float); lo, hi = float(t.min()), float(t.max()) + 1
    observation = []
    for ent in layout["entities"]:
        s, e = layout.get("observation", {}).get(ent, (lo, hi)); observation.append((ent, float(s), float(e)))
    observation.append((SYSTEM, lo, hi))
    thresholds = {r: cache.get((r, choice[r])) for r in layout["kinds"] if choice.get(r) and str(choice[r]).startswith("q")}
    side = dict(time_unit="dataset time units", entity_key="auto", period="auto",
                system_wide_types=sorted(set(ev[ev.entity == SYSTEM].type)), tie_rule="canonical", kind=kind, origin=origin,
                symbolization=dict(rule="confirmation bits on other roles (METHOD 3.2, v1)", choice=choice, thresholds=thresholds))
    if sidecar_extra: side.update(sidecar_extra)
    write_dataset(outdir, ev, observation, list(gaps), side)
    return ev
