"""
Syntax motifs (METHOD.md 3.15, v6): chains and returns.

A chain A -l1-> B -l2-> C is a composition of two validated fragments (A,l1)->B and (B,l2)->C: the library
drives the search, so every chain carries the provenance of its links. A chain instance at a target event C
(time t) is: B is C's most recent context at lag class l2 (time tb), and A's most recent occurrence before tb
is within lag class l1 of tb, with no gap of the entity between them. The chain must say more than its last
link: conditional lift P(C | B at l2 and A at l1 of that B) / P(C | B at l2) >= LIFT_MIN on the proposal
split, triple count above the circular null's maximum over N_NULL_DRAWS draws, and the same conditional lift
with count >= CONFIRM_MIN_COUNT on the confirmation split. Admitted chains are indicator features of the model,
kept (like compositions) only if they reduce confirmation bits.

A return is a chain whose ends are the same role in opposite directions with a different role in the middle
(X up -> Y -> X down): the signature of a loop closing. Returns are admitted by the same rule and marked.
Length is capped at CHAIN_MAX_NODES (three) in v6.
"""
from bisect import bisect_left
from collections import defaultdict
import numpy as np
from .. import constants as K
from .contexts import contexts_for_stream, ctx_key, entity_gaps, _overlaps


def _role(t): return t.split(":", 1)[0]
def _sym(t): return t.split(":", 1)[1] if ":" in t else ""


def direction(sym):
    """+1 for up / peak / on, -1 for down / trough / off, 0 otherwise."""
    if sym.startswith("up") or sym in ("peak", "on"): return 1
    if sym.startswith("down") or sym in ("trough", "off"): return -1
    return 0


def is_return(a, b, c):
    """Same role at both ends, opposite direction, a different role in the middle (3.15)."""
    return _role(a) == _role(c) and _role(b) != _role(a) and direction(_sym(a)) * direction(_sym(c)) == -1


def candidates(frags):
    """Every (A, l1, B, l2, C) with (A,l1)->B and (B,l2)->C both validated fragments."""
    by_target = defaultdict(list)
    for f in frags: by_target[f["y"]].append(f["ctx"])
    seen, out = set(), []
    for f2 in frags:
        b, l2 = f2["ctx"]; c = f2["y"]
        for (a, l1) in by_target.get(b, []):
            key = (a, l1, b, l2, c)
            if key not in seen:
                seen.add(key); out.append(key)
    return out


def times_by_tok(streams, lo, hi, shift=None):
    """{entity: {type: sorted times}} of the events in [lo, hi), shifted exactly as contexts_for_stream shifts them."""
    out = {}
    for z, s in streams.items():
        sub = s[(s.t >= lo) & (s.t < hi)]
        t = sub.t.values.astype(float); toks = sub.type.values
        if len(t) and shift is not None:
            l, h = t.min(), t.max() + 1
            t = np.array([l + ((x + shift.get(k, 0.0) - l) % (h - l)) for x, k in zip(t, toks)])
        d = defaultdict(list)
        for x, k in zip(t, toks): d[k].append(x)
        out[z] = {k: np.sort(np.asarray(v, float)) for k, v in d.items()}
    return out


def _index(chains):
    by_link = defaultdict(list)
    for key in chains: by_link[ctx_key(key[2], key[3])].append(key)
    return by_link


def _instances(r, times, lags, by_link, gaps, gcache, want_gaps=False):
    """Yield (key, hit_link[, g1, g2]) for every chain whose last link (B at l2) is in the row's context; hit_link is
    True when the first link also holds (A at l1 before that B, no entity gap between). With want_gaps the realised
    gaps of the two legs follow: g1 = tb - ta (the leg into B), g2 = t - tb (the leg into C)."""
    z = r["entity"]; H = lags.horizon
    tz = times.get(z, {})
    for ck in r["ctx"]:
        lst = by_link.get(ck)
        if not lst: continue
        for key in lst:
            a, l1, b, l2, c = key
            g2 = r["gaps"][b]; tb = r["t"] - g2
            ta_arr = tz.get(a); ok = False; d = None
            if ta_arr is not None and len(ta_arr):
                i = bisect_left(ta_arr, tb) - 1
                if i >= 0:
                    d = tb - ta_arr[i]
                    if 0 < d <= H and lags.of(d) == l1:
                        if gaps is None or len(gaps) == 0: ok = True
                        else:
                            if z not in gcache: gcache[z] = entity_gaps(gaps, z).get("", [])
                            ok = not _overlaps(gcache[z], ta_arr[i], tb)
            yield (key, ok, d, g2) if want_gaps else (key, ok)


def count_triples(rows, times, lags, chains, gaps=None):
    """Per chain: [n_B, n_BC, n_AB, n_ABC] over the rows (B at l2 in context; C the target; A at l1 of that B)."""
    by_link = _index(chains); n = {key: [0, 0, 0, 0] for key in chains}; gcache = {}
    for r in rows:
        for key, ok in _instances(r, times, lags, by_link, gaps, gcache):
            cnt = n[key]; hit = r["tok"] == key[4]
            cnt[0] += 1
            if hit: cnt[1] += 1
            if ok:
                cnt[2] += 1
                if hit: cnt[3] += 1
    return n


def cond_lift(c):
    n_b, n_bc, n_ab, n_abc = c
    if not (n_b and n_bc and n_ab): return 0.0
    return (n_abc / n_ab) / (n_bc / n_b)


def mark_rows(rows, times, lags, chains, gaps=None):
    """r['chains'] = set of admitted chain keys whose full triple condition holds at the row (model features)."""
    chains = [h["key"] if isinstance(h, dict) else h for h in chains]
    by_link = _index(chains); gcache = {}
    for r in rows:
        present = set()
        for key, ok in _instances(r, times, lags, by_link, gaps, gcache):
            if ok: present.add(key)
        r["chains"] = present
    return rows


def discover_chains(frags, streams, lags, splits, rng, gaps, gap_mode, rows_prop, rows_conf, log=print):
    """Admitted chains (3.15) and the counts behind them. Returns (chains, info)."""
    plo, phi, chi = splits
    cands = candidates(frags)
    info = dict(candidates=len(cands), lift_ok=0, null_passed=0, admitted=0, returns=0)
    if not cands: return [], info
    times_p = times_by_tok(streams, plo, phi)
    n_p = count_triples(rows_prop, times_p, lags, cands, gaps)
    surv = [k for k in cands if n_p[k][3] >= K.CONFIRM_MIN_COUNT and cond_lift(n_p[k]) >= K.LIFT_MIN]
    info["lift_ok"] = len(surv)
    mx = {k: 0 for k in surv}
    if surv:   # circular null on the triple count: every type shifted by its own offset, as for pairs (3.8)
        toks = sorted(set(t for s in streams.values() for t in s.type))
        for _ in range(K.N_NULL_DRAWS):
            shift = {t: float(rng.uniform(1.0, phi - plo)) for t in toks}
            rows_s = []
            for z, s in streams.items():
                sub = s[(s.t >= plo) & (s.t < phi)]
                for r in contexts_for_stream(sub, lags, entity=z, gaps=gaps, shift=shift, gap_mode=gap_mode, want_gaps=True):
                    r["entity"] = z; rows_s.append(r)
            n_s = count_triples(rows_s, times_by_tok(streams, plo, phi, shift), lags, surv, gaps)
            for k in surv: mx[k] = max(mx[k], n_s[k][3])
    passed = [k for k in surv if n_p[k][3] > mx[k]]
    info["null_passed"] = len(passed)
    n_c = count_triples(rows_conf, times_by_tok(streams, phi, chi), lags, passed, gaps) if passed else {}
    chains = []
    for k in passed:
        if n_c[k][3] >= K.CONFIRM_MIN_COUNT and cond_lift(n_c[k]) >= K.LIFT_MIN:
            a, l1, b, l2, c = k
            chains.append(dict(key=k, a=a, l1=l1, b=b, l2=l2, c=c, count=int(n_p[k][3]), cond_lift=float(cond_lift(n_p[k])),
                               count_conf=int(n_c[k][3]), cond_lift_conf=float(cond_lift(n_c[k])), null_max=int(mx[k]),
                               is_return=bool(is_return(a, b, c)),
                               link_counts=dict(n_B=int(n_p[k][0]), n_BC=int(n_p[k][1]), n_AB=int(n_p[k][2]))))
    # 3.16 (v7): the fast side and the slow side of every return, from the realised gaps of its confirmed triples
    rets = [h["key"] for h in chains if h["is_return"]]
    if rets:
        lg = leg_gaps(rows_conf, times_by_tok(streams, phi, chi), lags, rets, gaps)
        for h in chains:
            if h["is_return"]:
                v, m1, m2 = loop_verdict(*lg[h["key"]]); h["verdict"], h["g1"], h["g2"] = v, m1, m2
    chains.sort(key=lambda h: -h["cond_lift"] * np.log(max(h["count"], 2)))
    info["admitted"] = len(chains); info["returns"] = sum(h["is_return"] for h in chains)
    info["returns_resolved"] = sum(1 for h in chains if h["is_return"] and h.get("verdict") != "unresolved")
    return chains, info


def leg_gaps(rows, times, lags, keys, gaps=None):
    """{key: ([g1...], [g2...])} over the confirmed triples (first link holds, target is C) of each chain."""
    by_link = _index(keys); out = {k: ([], []) for k in keys}; gcache = {}
    for r in rows:
        for key, ok, g1, g2 in _instances(r, times, lags, by_link, gaps, gcache, want_gaps=True):
            if ok and r["tok"] == key[4]:
                out[key][0].append(g1); out[key][1].append(g2)
    return out


def loop_verdict(g1, g2, ratio=K.LOOP_GAP_RATIO):
    """3.16: the leg with the shorter median realised gap marks the side that reacts. g1: into the middle (Y);
    g2: into the far end (X'). 'Y reacts' when g1 <= g2 / ratio, 'X reacts' when g2 <= g1 / ratio, else unresolved."""
    if not g1 or not g2: return "unresolved", None, None
    m1, m2 = float(np.median(g1)), float(np.median(g2))
    if m1 <= m2 / ratio: return "Y reacts", m1, m2
    if m2 <= m1 / ratio: return "X reacts", m1, m2
    return "unresolved", m1, m2


def loop_tags(chains):
    """Per role: the majority loop tag (REACTS / RESPONDS) over the resolved returns it takes part in, as end or
    middle; a tie is unresolved (no tag). Returns ({role: tag}, {role: {REACTS: n, RESPONDS: n}})."""
    from collections import Counter, defaultdict
    votes = defaultdict(Counter)
    for h in chains:
        if not h.get("is_return") or h.get("verdict") in (None, "unresolved"): continue
        x, y = _role(h["a"]), _role(h["b"])
        if h["verdict"] == "Y reacts": votes[y]["REACTS"] += 1; votes[x]["RESPONDS"] += 1
        else: votes[x]["REACTS"] += 1; votes[y]["RESPONDS"] += 1
    tags = {}
    for r, c in votes.items():
        if c["REACTS"] != c["RESPONDS"]: tags[r] = "REACTS" if c["REACTS"] > c["RESPONDS"] else "RESPONDS"
    return tags, {r: dict(c) for r, c in votes.items()}


def chains_to_json(chains, used_keys=()):
    used = set(used_keys)
    return [dict(a=h["a"], l1=h["l1"], b=h["b"], l2=h["l2"], c=h["c"], count=h["count"], cond_lift=h["cond_lift"],
                 count_conf=h["count_conf"], cond_lift_conf=h["cond_lift_conf"], null_max=h["null_max"],
                 is_return=h["is_return"], used=(h["key"] in used), link_counts=h["link_counts"], shape=h.get("shape"),
                 g1=h.get("g1"), g2=h.get("g2"), verdict=h.get("verdict"))
            for h in chains]
