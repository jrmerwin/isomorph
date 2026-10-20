"""
Entity streams and lagged contexts (METHOD.md 3.3, 3.6, and the contract's
observation and gap rules).

A stream is one entity's events plus the system-wide events, time-ordered.
For each target event (the entity's own events) the context is the set of
(prior type, lag class) over the most recent occurrence of each type within
the horizon, with a strictly positive gap. Adjacent Markov-1/2 contexts are the
entity's own previous one and two events.

Gap handling. v6 ("clip", METHOD 3.6): a gap of the entity clips the look-back window to
[max(t - H, end of the last gap before t), t): the target keeps the contexts inside its own
observed stretch (lagged and Markov) and loses those on the far side of the gap; it is dropped
only when the clipped window is empty. v1-v5 ("drop"): a window that overlaps any gap of the
entity drops the whole target. A gap recorded against one prior type removes that type's
context in both modes. Legacy profile ignores gaps.
"""
from collections import defaultdict
import numpy as np
import pandas as pd

SYSTEM = "ALL"


class LagClasses:
    def __init__(self, edges, labels=("s", "m", "l")):
        self.edges = list(edges)          # upper edges; the last is the horizon
        self.labels = list(labels)
        self.horizon = self.edges[-1]

    def of(self, gap):
        for e, lab in zip(self.edges, self.labels):
            if gap <= e:                      # closed on the right: a gap equal to the sampling interval has a class (v2)
                return lab
        return None

    @staticmethod
    def fixed_minutes(edges=(5.0, 30.0, 90.0)):
        return LagClasses(edges)

    @staticmethod
    def from_gaps(gaps, horizon_q=0.95):
        """v1 rule: terciles of within-horizon inter-event gaps; horizon = quantile of all gaps."""
        gaps = np.asarray([g for g in gaps if g > 0], float)
        horizon = float(np.quantile(gaps, horizon_q))
        inside = gaps[gaps <= horizon]
        e1, e2 = float(np.quantile(inside, 1 / 3)), float(np.quantile(inside, 2 / 3))
        return LagClasses((e1, e2, horizon))

    @staticmethod
    def from_recurrence(streams, lo, hi, min_occurrences=5):
        """v2 rule (METHOD 3.3): horizon = the median over target types of the type's median recurrence
        gap (time until the same symbol recurs in a stream) on [lo, hi); lag classes = three geometric
        bands between the data's time resolution delta and the horizon: (delta, delta r^(1/3)],
        (delta r^(1/3), delta r^(2/3)], (delta r^(2/3), H], r = H / delta.
        The horizon follows the system's own time scale, not its event density; every type counts once."""
        rec = {}
        for z, s in streams.items():
            sub = s[(s.t >= lo) & (s.t < hi)]
            tg = sub[sub.target == 1]
            for typ, g in tg.groupby("type"):
                d = np.diff(g.t.values.astype(float)); d = d[d > 0]
                if len(d) >= min_occurrences: rec.setdefault(typ, []).append(d)
        if not rec:
            raise ValueError("no target type recurs often enough to set a horizon")
        medians = [float(np.median(np.concatenate(v))) for v in rec.values()]
        H = float(np.median(medians))
        # lag classes: three geometric bands between the data's time resolution (smallest positive gap)
        # and the horizon — time scales are multiplicative; terciles of context gaps put the whole
        # short-lag range, where mechanisms act, into one class once the horizon is hours long
        delta = min(float(np.min(np.concatenate(v))) for v in rec.values())
        allgaps = np.concatenate([np.diff(s[(s.t >= lo) & (s.t < hi)].t.values.astype(float)) for s in streams.values()])
        allgaps = allgaps[allgaps > 0]
        if len(allgaps): delta = min(delta, float(allgaps.min()))
        r = H / delta
        e1, e2 = delta * r ** (1 / 3), delta * r ** (2 / 3)
        return LagClasses((float(e1), float(e2), H))


def context_gaps(streams, lo, hi, H):
    """All (target, prior type) gaps within H on [lo, hi), as one array (no rows built)."""
    out = []
    for z, s in streams.items():
        sub = s[(s.t >= lo) & (s.t < hi)]
        t_arr = sub.t.values.astype(float); toks = sub.type.values; tgt = sub.target.values
        last = {}
        for i in range(len(t_arr)):
            if tgt[i]:
                t = t_arr[i]
                for tm in last.values():
                    g = t - tm
                    if 0 < g <= H: out.append(g)
            last[toks[i]] = t_arr[i]
    return np.asarray(out, float)


_CTX = {}


def ctx_key(tok, c):
    """Interned (type, lag) tuple so context sets share one object per key."""
    k = (tok, c)
    r = _CTX.get(k)
    if r is None: _CTX[k] = r = k
    return r


def streams_of(events, entities, system=SYSTEM):
    out = {}
    for z in entities:
        s = events[(events.entity == z) | (events.entity == system)].sort_values(["t", "tie_rank"]).reset_index(drop=True)
        s["target"] = (s.entity == z).astype(int)
        out[z] = s
    return out


def entity_gaps(gaps, entity):
    """{type or '': [(start, end), ...]} for one entity."""
    g = defaultdict(list)
    if gaps is None or len(gaps) == 0:
        return g
    for _, r in gaps[gaps.entity == entity].iterrows():
        g[str(r.type) if str(r.type) not in ("nan", "") else ""].append((float(r.start), float(r.end)))
    return g


def _overlaps(intervals, lo, hi):
    return any(s < hi and e > lo for s, e in intervals)


def contexts_for_stream(s, lags, entity=None, gaps=None, shift=None, gap_mode="drop", entity_gap_map=None, want_gaps=True):
    """Rows of dicts for every target event: minute/t, tok, ctx (set of (type, lag)),
    m1, m2, event_id, dropped (bool: window spanned a gap).
    shift: optional {type: offset} for the circular null — timestamps shifted modulo the
    stream span (legacy behaviour) or within the entity's observation span (v1, via `span`)."""
    t_arr = s.t.values.astype(float); toks = s.type.values; tgt = s.target.values; ids = s.event_id.values
    if len(t_arr) == 0: return []      # an entity with no events in this split (TCLab: sensor 2 absent from the proposal split)
    if shift is not None:
        lo, hi = t_arr.min(), t_arr.max() + 1
        t_arr = np.array([lo + ((t + shift.get(tok, 0.0) - lo) % (hi - lo)) for t, tok in zip(t_arr, toks)])
        order = np.argsort(t_arr, kind="stable")
        t_arr, toks, tgt, ids = t_arr[order], toks[order], tgt[order], ids[order]
    gmap = entity_gap_map if entity_gap_map is not None else (entity_gaps(gaps, entity) if gaps is not None and entity is not None else {})
    all_gaps = gmap.get("", []) if gmap else []
    rows, own_hist, own_t, last_seen = [], [], [], {}
    H = lags.horizon
    for i in range(len(t_arr)):
        if tgt[i]:
            t = t_arr[i]
            dropped = False; win_lo = t - H
            if gap_mode == "drop" and gmap:
                if _overlaps(all_gaps, t - H, t):
                    dropped = True
            elif gap_mode == "clip" and all_gaps:
                g_end = max((e for s_, e in all_gaps if s_ < t and e > win_lo), default=None)
                if g_end is not None:
                    win_lo = max(win_lo, g_end)
                    if win_lo >= t: dropped = True          # a gap covers the target itself: empty window
                    while own_hist and own_t[-1] < win_lo:   # own history on the far side of the gap
                        own_hist.pop(); own_t.pop()
            ctx = set(); gapd = {}
            if not dropped:
                for tok, tm in last_seen.items():
                    gap = t - tm
                    if 0 < gap <= H and tm >= win_lo:
                        if gap_mode in ("drop", "clip") and gmap and tok in gmap and _overlaps(gmap[tok], tm, t):
                            continue
                        c = lags.of(gap)
                        if c is not None:
                            ctx.add(ctx_key(tok, c))
                            if want_gaps: gapd[tok] = gap
            rows.append(dict(t=t, tok=toks[i], ctx=ctx, gaps=gapd, event_id=int(ids[i]), dropped=dropped,
                             m1=(own_hist[-1] if own_hist and not dropped else None),
                             m2=(tuple(own_hist[-2:]) if len(own_hist) >= 2 and not dropped else None),
                             m3=(tuple(own_hist[-3:]) if len(own_hist) >= 3 and not dropped else None)))
            own_hist.append(toks[i]); own_t.append(t)
        last_seen[toks[i]] = t_arr[i]
    return rows


def pair_counts(rows):
    cnt, base = defaultdict(lambda: defaultdict(int)), defaultdict(int)
    for r in rows:
        for c in r["ctx"]:
            cnt[c][r["tok"]] += 1; base[c] += 1
    return cnt, base


def inter_event_gaps(streams):
    out = []
    for z, s in streams.items():
        t = s[s.target == 1].t.values
        if len(t) > 1:
            out += list(np.diff(t))
    return out
