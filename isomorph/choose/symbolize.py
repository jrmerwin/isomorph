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
every unit. Thresholds and windows are per unit (each unit's own quantiles and correlation
time), so "P:upq80" means the same thing — crossing this unit's 80th percentile — in vessels
that run at different levels (changelog v1, Tennessee Eastman).

Noise floor (added on Tennessee Eastman, changelog v1): a continuous series is first denoised by a
centred moving average over its *noise window* w, chosen so that the white-noise fraction left after
averaging is at most constants.NOISE_FRACTION of the signal variance: with f = 1 - acf(1) the
white-noise fraction, w = ceil(f / (NOISE_FRACTION * (1 - f))). Clean series (acf(1) ~ 1) get w = 1
and are unchanged; a series whose window would exceed 1% of its length carries no detectable
signal at the sampling scale and emits no events. Every scheme and the faithfulness test operate
on the denoised series.

Schemes for continuous roles: quantile crossings q20/50/80, quantile crossings q10/90,
turning points persisting over the denoised series' correlation time (the first lag at which
its autocorrelation falls below 0.5): a peak is the maximum within +/- one correlation time. All debounced
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


def noise_window(x):
    """Samples to average so that residual white noise is <= NOISE_FRACTION of the signal variance;
    None when the series has no detectable signal at the sampling scale (window > 1% of length)."""
    v = x[~np.isnan(x)]
    if len(v) < 10 or v.std() == 0: return None
    v = v - v.mean()
    a1 = float(np.corrcoef(v[:-1], v[1:])[0, 1])
    if a1 <= 0: return None
    f = 1.0 - a1
    w = int(np.ceil(f / (K.NOISE_FRACTION * (1.0 - f))))
    if w > len(v) // 100: return None
    return max(1, w)


def denoise(x, w):
    if w is None or w <= 1: return x.astype(float)
    return pd.Series(x.astype(float)).rolling(w, center=True, min_periods=1).mean().values


def correlation_time(x, max_lag=5000):
    """First lag at which the series' autocorrelation drops below 0.5 (its own time scale). FFT-based."""
    v = x[~np.isnan(x)].astype(float); v = v - v.mean()
    n = len(v)
    if n < 3 or v.std() == 0: return 1
    m = min(max_lag, n // 2)
    nfft = 1 << int(np.ceil(np.log2(2 * n)))
    f = np.fft.rfft(v, nfft); acov = np.fft.irfft(f * np.conj(f), nfft)[: m + 1]
    acf = acov / acov[0]
    below = np.flatnonzero(acf[1:] < 0.5)
    return int(below[0] + 1) if len(below) else m


def _mad(v):
    v = v[~np.isnan(v)]
    return float(np.median(np.abs(v - np.median(v)))) if len(v) else np.nan


def residual_ratio(x, scheme, thresholds=None, window=None):
    """Reconstruction residual / series spread under a scheme: band medians for quantile schemes, linear
    interpolation between turning points for dsign. Spread is the median absolute deviation on both sides
    (robust): with the standard deviation, a handful of 10-sigma fault excursions on Tennessee Eastman
    made every scheme look unfaithful (0.9+) although the symbols described the bulk of the series
    (changelog v1)."""
    v = x.astype(float); ok = ~np.isnan(v)
    if ok.sum() < 10 or v[ok].std() == 0: return np.inf
    scale = _mad(v)
    # a step-schedule series (constant more than half the time, e.g. a scheduled power demand) has MAD 0;
    # the robust ratio degenerates, so the ordinary std ratio is used for it
    spread = _mad if scale > 0 else (lambda a: float(np.nanstd(a)))
    scale = scale if scale > 0 else float(v[ok].std())
    if scheme.startswith("q"):
        band = np.zeros(len(v), int)
        for th in thresholds: band += (v > th).astype(int)
        rec = np.full(len(v), np.nan)
        for b in np.unique(band[ok]):
            m = ok & (band == b); rec[m] = np.median(v[m])          # band medians: robust to excursions within a band
        return float(spread(v - rec) / scale)
    ev = derivative_sign_events(v, window)
    idx = np.array([i for i, _, _ in ev])
    if len(idx) < 2: return np.inf
    rec = np.interp(np.arange(len(v)), idx, v[idx])
    return float(spread(v - rec) / scale)


def derivative_sign_events(x, window):
    """Turning points of the series that persist over `window` samples: i is a peak if x[i] is the
    maximum over [i - window, i + window] (first index on a plateau), a trough likewise; consecutive
    turning points of the same kind keep only the more extreme one, so the output alternates.
    v1.0 took sign changes of the derivative of a moving average, whose derivative is the difference
    of two samples one window apart and is as noisy as the raw series (changelog v1, Tennessee Eastman)."""
    v = np.asarray(x, float); n = len(v)
    if n < 3: return []
    s = pd.Series(v)
    w = max(1, int(window))
    rmax = s.rolling(2 * w + 1, center=True, min_periods=1).max().values
    rmin = s.rolling(2 * w + 1, center=True, min_periods=1).min().values
    ok = ~np.isnan(v)
    prev = np.r_[np.nan, v[:-1]]
    peaks = np.flatnonzero(ok & (v == rmax) & (v != prev))
    troughs = np.flatnonzero(ok & (v == rmin) & (v != prev))
    cand = sorted([(i, "peak") for i in peaks] + [(i, "trough") for i in troughs])
    out = []
    for i, kind in cand:
        if i == 0 or i == n - 1: continue
        if out and out[-1][1] == kind:                   # same kind twice: keep the more extreme
            j = out[-1][0]
            if (kind == "peak" and v[i] > v[j]) or (kind == "trough" and v[i] < v[j]):
                out[-1] = (i, kind, float(v[i]))
            continue
        out.append((i, kind, float(v[i])))
    return out


def denoised_holders(df, role, holders, cache):
    """Per-column noise window and denoised series for a role; columns with no signal are left out."""
    key = (role, "noise")
    if key not in cache:
        cache[key] = {col: noise_window(df[col].values.astype(float)) for _, col in holders}
    out = []
    for ent, col in holders:
        w = cache[key][col]
        if w is None: continue
        dkey = ("denoised", col)
        if dkey not in cache: cache[dkey] = denoise(df[col].values, w)
        out.append((ent, col, cache[dkey]))
    return out


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
        memo = ("rows", role, scheme)
        if memo in thresholds_cache:
            return list(thresholds_cache[memo])
        series = denoised_holders(df, role, holders, thresholds_cache)    # [(entity, col, denoised x)] — only columns with signal
        if scheme.startswith("q"):
            qs = [int(q) / 100 for q in scheme[1:].split("_")]
            key = (role, scheme)
            if key not in thresholds_cache:     # thresholds per column: each unit's own quantiles (changelog v1, Tennessee Eastman)
                thresholds_cache[key] = {col: quantile_thresholds([x], qs) for _, col, x in series}
            for ent, col, x in series:
                th = thresholds_cache[key][col]
                th = sorted(set(th))                    # equal quantiles (step-like series) would emit the same crossing twice
                for i, e, v in crossings(x, th, K.DEBOUNCE):
                    direction = "up" if e.startswith("up") else "down"
                    full = thresholds_cache[key][col]
                    q = qs[full.index(float(e[len(direction):]))] if float(e[len(direction):]) in full else None
                    label = f"{direction}q{int(round(q * 100))}" if q is not None else e
                    rows.append(dict(t=t[i], entity=ent, type=f"{role}:{label}", value=v))
        elif scheme == "dsign":
            key = (role, "window")
            if key not in thresholds_cache:     # window per column: the series' own correlation time
                thresholds_cache[key] = {col: max(3, int(correlation_time(x))) for _, col, x in series}
            for ent, col, x in series:
                for i, e, v in derivative_sign_events(x, thresholds_cache[key][col]):
                    rows.append(dict(t=t[i], entity=ent, type=f"{role}:{e}", value=v))
        thresholds_cache[memo] = list(rows)
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
    if len(inter_event_gaps(prop)) < 10: return np.inf
    try:
        lags = LagClasses.from_recurrence(streams, lo, p_hi)                       # v2 (3.3)
    except ValueError:
        return np.inf
    rows_p = rows_for(streams, lags, lo, p_hi, None, "ignore", want_gaps=False); rows_c = rows_for(streams, lags, p_hi, c_hi, None, "ignore", want_gaps=False)
    tgt_p, tgt_c = rows_p, rows_c
    if len(tgt_c) < 20 or len(tgt_p) < 50: return np.inf
    vocab = sorted(set(r["tok"] for r in tgt_p + tgt_c))
    cnt, base = pair_counts(tgt_p)
    ctxs = [c for c, b in base.items() if b >= 3 and any(v >= 3 for v in cnt[c].values())]
    return float(fit_bits(FeatureMap(vocab, True, ctxs), tgt_p, tgt_c).sum())


def choose_symbolization(df, layout, splits_frac=(0.5, 0.25), log=print, passes=2, checkpoint=None):
    """Returns (choice per role, thresholds used, trace). `checkpoint`: a json path written after every
    role decision and read at start, so an interrupted run resumes (the search is deterministic)."""
    import json, os
    done = {}
    if checkpoint and os.path.exists(checkpoint):
        ck = json.load(open(checkpoint))
        done = {tuple(k.split("|")): v for k, v in ck["done"].items()}
        log(f"  resuming from checkpoint: {len(done)} decisions already made")
    def save(choice, trace, faith):
        if checkpoint:
            json.dump(dict(done={"|".join(k): v for k, v in done.items()}, choice=choice, trace=trace,
                           faith={f"{r}|{s}": (None if v == np.inf else v) for (r, s), v in faith.items()}), open(checkpoint, "w"), default=str)
    t = df[layout["time"]].values.astype(float); lo, hi = float(t.min()), float(t.max()) + 1
    p_hi, c_hi = lo + (hi - lo) * splits_frac[0], lo + (hi - lo) * (splits_frac[0] + splits_frac[1])
    cache = {}
    cont = [r for r, k in layout["kinds"].items() if k == "continuous"]
    trace = []
    def admissible(role, sch):
        holders = [(e, cols[role]) for e, cols in layout["entities"].items() if role in cols]
        if role in layout.get("system", {}): holders.append((SYSTEM, layout["system"][role]))
        cache_key = (role, sch) if sch.startswith("q") else (role, "window")
        if cache_key not in cache:
            symbolize_role(df, layout, role, sch, cache)   # fills noise windows, thresholds / window
        series = denoised_holders(df, role, holders, cache)
        if not series:
            return False, np.inf                            # no column carries signal at the sampling scale
        if sch.startswith("q"):
            ratios = [residual_ratio(x, sch, thresholds=cache[cache_key][col]) for _, col, x in series]
        else:
            ratios = [residual_ratio(x, sch, window=cache[cache_key][col]) for _, col, x in series]
        return float(np.median(ratios)) <= K.FAITHFULNESS_MAX_RESIDUAL, float(np.median(ratios))
    faith = {}
    # start of the coordinate search: each role's coarsest faithful scheme (fewest events); a role with
    # none is silent from the start. Starting from the finest scheme made every trial table chatter-heavy
    # on noisy data (Tennessee Eastman, changelog v1).
    choice = {r: None for r in layout["kinds"]}
    counts = {}
    for role in cont:
        best_n = None
        for sch in SCHEMES:
            ok, ratio = admissible(role, sch); faith[(role, sch)] = ratio
            if not ok: continue
            n = len(symbolize_role(df, layout, role, sch, cache))
            if best_n is None or n < best_n: best_n, choice[role] = n, sch
        counts[role] = best_n or 0
        log(f"  start {role:10s} {choice[role]} ({counts[role]} events)")
    order = sorted(cont, key=lambda r: -counts[r])
    for p in range(passes):
        changed_any = False
        for role in order:
            if (str(p), role) in done:            # decided in an earlier (interrupted) run
                rec = done[(str(p), role)]
                changed_any |= bool(rec.get("changed")); choice[role] = rec["chosen"]
                trace.append(dict(pass_=p, role=role, scores=rec.get("scores", {}), chosen=rec["chosen"]))
                continue
            scores = {}
            adm = {}
            for sch in SCHEMES:
                ok, ratio = admissible(role, sch); faith[(role, sch)] = ratio; adm[sch] = ok
            if not any(adm.values()):
                choice[role] = None      # no admissible scheme: the role emits no events
                if all(faith[(role, s)] == np.inf for s in SCHEMES):
                    log(f"  pass {p} {role:10s} no detectable signal at the sampling scale (noise window > 1% of length); role emits no events")
                else:
                    log(f"  pass {p} {role:10s} no scheme reconstructs the series within {K.FAITHFULNESS_MAX_RESIDUAL} of its std "
                        f"(residual ratios {', '.join(f'{s}={faith[(role, s)]:.2f}' for s in SCHEMES)}); role emits no events")
                trace.append(dict(pass_=p, role=role, scores={}, chosen=None))
                done[(str(p), role)] = dict(chosen=None, changed=False, scores={}); save(choice, trace, faith); continue
            if sum(adm.values()) == 1:   # one admissible scheme: nothing to compare
                best = next(s for s, ok in adm.items() if ok)
                changed = best != choice[role]; choice[role] = best; changed_any |= changed
                trace.append(dict(pass_=p, role=role, scores={best: "only admissible"}, chosen=best))
                log(f"  pass {p} {role:10s} only {best} is faithful (" + ", ".join(f"{s}={faith[(role, s)]:.2f}" for s in SCHEMES) + f") -> {best}{' *' if changed else ''}")
                done[(str(p), role)] = dict(chosen=best, changed=changed, scores={best: "only admissible"}); save(choice, trace, faith)
                continue
            for sch in SCHEMES:
                if not adm[sch]:
                    scores[sch] = np.inf; continue
                trial = dict(choice); trial[role] = sch
                ev = assemble(df, layout, trial, cache)
                scores[sch] = criterion(ev, role, lo, p_hi, c_hi)
            best = min(scores, key=scores.get)
            cur = choice[role]
            if cur in scores and scores[cur] <= scores[best] + max(1e-6, 1e-4 * abs(scores[best])):
                best = cur                                   # a tie (within solver noise, 1e-4 of the total) is not evidence to change
            changed = best != choice[role]; choice[role] = best; changed_any |= changed
            trace.append(dict(pass_=p, role=role, scores=scores, chosen=best))
            log(f"  pass {p} {role:10s} " + "  ".join((f"{s}={v/1000:.1f}kb" if v < np.inf else f"{s}=unfaithful({faith[(role, s)]:.2f})") for s, v in scores.items()) + f"  -> {best}{' *' if changed else ''}")
            done[(str(p), role)] = dict(chosen=best, changed=changed, scores={k: (None if v == np.inf else v) for k, v in scores.items()}); save(choice, trace, faith)
        if not changed_any:
            log(f"  pass {p} changed nothing: converged, later passes skipped (same result)")
            break
    thresholds = {f"{r}": cache.get((r, choice[r])) for r in cont if choice[r] and choice[r].startswith("q")}
    thresholds.update({f"{r}_window": cache.get((r, "window")) for r in cont if choice[r] == "dsign"})
    thresholds["noise_windows"] = {col: w for r in cont for col, w in cache.get((r, "noise"), {}).items()}
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
                symbolization=dict(rule="total confirmation bits with faithfulness and noise floors (METHOD 3.2, v1)", choice=choice, thresholds=thresholds,
                                   noise_windows={col: w for r in layout["kinds"] for col, w in cache.get((r, "noise"), {}).items()}))
    if sidecar_extra: side.update(sidecar_extra)
    write_dataset(outdir, ev, observation, list(gaps), side)
    return ev
