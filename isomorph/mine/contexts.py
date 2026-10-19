"""
Entity streams and lagged contexts (METHOD.md 3.3, 3.6, and the contract's
observation and gap rules).

A stream is one entity's events plus the system-wide events, time-ordered.
For each target event (the entity's own events) the context is the set of
(prior type, lag class) over the most recent occurrence of each type within
the horizon, with a strictly positive gap. Adjacent Markov-1/2 contexts are the
entity's own previous one and two events.

Gap handling (v1): a context window [t - horizon, t) that overlaps a gap of
the same entity (any type, or the specific prior type) is dropped: the target
emits no lagged contexts and no Markov contexts. Legacy profile ignores gaps.
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
            if gap < e:
                return lab
        return None

    @staticmethod
    def fixed_minutes(edges=(5.0, 30.0, 90.0)):
        return LagClasses(edges)

    @staticmethod
    def from_gaps(gaps, horizon_q=0.95):
        """Terciles of within-horizon inter-event gaps; horizon = quantile of all gaps."""
        gaps = np.asarray([g for g in gaps if g > 0], float)
        horizon = float(np.quantile(gaps, horizon_q))
        inside = gaps[gaps <= horizon]
        e1, e2 = float(np.quantile(inside, 1 / 3)), float(np.quantile(inside, 2 / 3))
        return LagClasses((e1, e2, horizon))


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


def contexts_for_stream(s, lags, entity=None, gaps=None, shift=None, gap_mode="drop", entity_gap_map=None):
    """Rows of dicts for every target event: minute/t, tok, ctx (set of (type, lag)),
    m1, m2, event_id, dropped (bool: window spanned a gap).
    shift: optional {type: offset} for the circular null — timestamps shifted modulo the
    stream span (legacy behaviour) or within the entity's observation span (v1, via `span`)."""
    t_arr = s.t.values.astype(float); toks = s.type.values; tgt = s.target.values; ids = s.event_id.values
    if shift is not None:
        lo, hi = t_arr.min(), t_arr.max() + 1
        t_arr = np.array([lo + ((t + shift.get(tok, 0.0) - lo) % (hi - lo)) for t, tok in zip(t_arr, toks)])
        order = np.argsort(t_arr, kind="stable")
        t_arr, toks, tgt, ids = t_arr[order], toks[order], tgt[order], ids[order]
    gmap = entity_gap_map if entity_gap_map is not None else (entity_gaps(gaps, entity) if gaps is not None and entity is not None else {})
    all_gaps = gmap.get("", []) if gmap else []
    rows, own_hist, last_seen = [], [], {}
    H = lags.horizon
    for i in range(len(t_arr)):
        if tgt[i]:
            t = t_arr[i]
            dropped = False
            if gap_mode == "drop" and gmap:
                if _overlaps(all_gaps, t - H, t):
                    dropped = True
            ctx = set()
            if not dropped:
                for tok, tm in last_seen.items():
                    gap = t - tm
                    if 0 < gap <= H:
                        if gap_mode == "drop" and gmap and tok in gmap and _overlaps(gmap[tok], tm, t):
                            continue
                        c = lags.of(gap)
                        if c is not None:
                            ctx.add((tok, c))
            rows.append(dict(t=t, tok=toks[i], ctx=ctx, event_id=int(ids[i]), dropped=dropped,
                             m1=(own_hist[-1] if own_hist and not dropped else None),
                             m2=(tuple(own_hist[-2:]) if len(own_hist) >= 2 and not dropped else None)))
            own_hist.append(toks[i])
        last_seen[toks[i]] = t_arr[i]
    return rows


def inter_event_gaps(streams):
    out = []
    for z, s in streams.items():
        t = s[s.target == 1].t.values
        if len(t) > 1:
            out += list(np.diff(t))
    return out
