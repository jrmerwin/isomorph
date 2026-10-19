"""
Null models (METHOD.md 3.8), period estimation (3.4) and the signal floor (3.5).

circular  each type's timestamps shifted by one independent random offset, modulo the
          stream span (per entity stream) — tests cross-type alignment beyond each
          type's own rate
cycle     offsets restricted to whole periods — tests alignment beyond the shared cycle
rewire    within each type, entity labels permuted across events (per-entity, per-type
          counts preserved; which entity an event belongs to is scrambled) — tests
          whether a fragment's evidence is bound to the entity. Recorded as an attribute
          (binding_evidence), not used as a gate: it is blind by construction to
          system-wide causes and uninformative when units run on a synchronized
          schedule (changelog v1).
"""
from collections import defaultdict
import numpy as np
from .contexts import contexts_for_stream, streams_of, pair_counts


def period_estimate(events, lo, hi, resolution=0.01, threshold=0.2):
    """Autocorrelation of the whole-system event rate at `resolution` of the span;
    the first local maximum above `threshold` with lag < span/4, else None."""
    span = hi - lo
    nb = int(round(1 / resolution))
    counts, _ = np.histogram(events.t.values, bins=nb, range=(lo, hi))
    x = counts - counts.mean()
    if x.std() == 0:
        return None
    acf = np.correlate(x, x, mode="full")[nb - 1:] / (x.var() * nb)
    max_lag = nb // 4
    for k in range(2, max_lag):
        if acf[k] > threshold and acf[k] >= acf[k - 1] and acf[k] >= acf[k + 1]:
            return float(k * span / nb)
    return None


def _counts_under_shift(streams, lags, lo, hi, shift, gaps, gap_mode):
    rows = []
    for z, s in streams.items():
        sub = s[(s.t >= lo) & (s.t < hi)]
        rows += contexts_for_stream(sub, lags, entity=z, gaps=gaps, shift=shift, gap_mode=gap_mode)
    return pair_counts(rows)[0]


def null_max_circular(streams, lags, lo, hi, rng, n_draws, gaps, gap_mode, period=None):
    toks = sorted(set(t for s in streams.values() for t in s.type))
    mx = defaultdict(int)
    for _ in range(n_draws):
        if period:
            # whole-period offsets, DISTINCT across types where the span allows, so that no
            # pair of types keeps its relative alignment (equal offsets would preserve it)
            n_per = max(2, int((hi - lo) // period))
            pool = np.concatenate([np.arange(1, n_per), -np.arange(1, n_per)])   # both directions, all distinct
            offs = rng.permutation(pool) if len(pool) >= len(toks) else rng.choice(pool, size=len(toks))
            shift = {t: float(period * offs[i % len(offs)]) for i, t in enumerate(toks)}
        else:
            shift = {t: float(rng.uniform(1.0, hi - lo)) for t in toks}
        cn = _counts_under_shift(streams, lags, lo, hi, shift, gaps, gap_mode)
        for c, d in cn.items():
            for y, v in d.items():
                if v > mx[(c, y)]: mx[(c, y)] = v
    return mx


def null_max_rewire(events, entities, lags, lo, hi, rng, n_draws, gaps, gap_mode, system="ALL"):
    mx = defaultdict(int)
    ev = events[(events.t >= lo) & (events.t < hi)].copy()
    for _ in range(n_draws):
        e2 = ev.copy()
        ent = e2.entity.values.copy()
        for t in e2.type.unique():
            idx = np.where((e2.type.values == t) & (ent != system))[0]
            if len(idx) > 1:
                ent[idx] = ent[rng.permutation(idx)]
        e2["entity"] = ent
        streams = streams_of(e2, entities, system)
        cn = _counts_under_shift(streams, lags, lo, hi, None, gaps, "ignore" if gap_mode == "ignore" else "drop")
        for c, d in cn.items():
            for y, v in d.items():
                if v > mx[(c, y)]: mx[(c, y)] = v
    return mx


def signal_floor(null_max, cnt_p, rng, n_pairs=50):
    """Median over random (context, target) pairs with any proposal count of the support
    needed to exceed the circular null's maximum (= max + 1)."""
    keys = [(c, y) for c, d in cnt_p.items() for y in d]
    if not keys:
        return 1
    pick = [keys[i] for i in rng.choice(len(keys), size=min(n_pairs, len(keys)), replace=False)]
    return int(np.median([null_max.get(k, 0) + 1 for k in pick]))
