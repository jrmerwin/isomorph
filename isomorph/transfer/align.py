"""
Alignment of two datasets' type vocabularies from structure alone (METHOD.md 3.12):
lagged-pair lift matrices per lag class, z-scored, padded to equal size;
signature-initialised Hungarian assignment refined to a fixed point; restarts;
anchors = the N_ANCHORS B types with the largest signature margin, fixed to their
best A match.
"""
import numpy as np
from scipy.optimize import linear_sum_assignment
from .. import constants as K
from ..mine.library import pair_counts

LAGS = ("s", "m", "l")
BIG = 1e6   # a forbidden assignment, in units of the median distance (distances are normalised before penalties are added)


def lift_matrices(rows, toks, labels=LAGS, min_count=3):
    cnt, base = pair_counts(rows)
    uni = {}; n = len(rows)
    for r in rows: uni[r["tok"]] = uni.get(r["tok"], 0) + 1
    idx = {t: i for i, t in enumerate(toks)}
    M = {c: np.zeros((len(toks), len(toks))) for c in labels}
    for (a, c), d in cnt.items():
        if a not in idx: continue
        for y, v in d.items():
            if v >= min_count and y in idx:
                M[c][idx[a], idx[y]] = np.log((v / base[(a, c)]) / (uni[y] / n))
    return M


def pad(M, n):
    out = {}
    for c, A in M.items():
        P = np.zeros((n, n)); P[:A.shape[0], :A.shape[1]] = A; out[c] = P
    return out


def zscore(M):
    return {c: (A - A.mean()) / (A.std() + 1e-9) for c, A in M.items()}


def signatures(M):
    n = next(iter(M.values())).shape[0]
    S = []
    for i in range(n):
        parts = []
        for c in LAGS:
            A = M[c]
            parts += [np.sort(A[i, :]), np.sort(A[:, i]), np.array([(A[i, :] > 0).sum(), (A[:, i] > 0).sum(), A[i, :].sum(), A[:, i].sum()], float)]
        S.append(np.concatenate(parts))
    return np.array(S)


def compatibility(toksA, toksB, tagsA, tagsB, n):
    """n x n boolean: may B type j map to A type i? Same tag class; a B class with no A counterpart falls
    back to the coarse class (speed), then to anything. Padded (dummy) nodes are compatible with all.
    (METHOD 3.12, v4: the prefix keeps an actuator-driven edge from aligning with a sensor-sensor edge.)"""
    from ..choose.pos import type_tag
    C = np.ones((n, n), bool)
    if not tagsA or not tagsB: return C
    clsA = [type_tag(tagsA, t) for t in toksA]; coA = [type_tag(tagsA, t, coarse=True) for t in toksA]
    for j, tb in enumerate(toksB):
        cb, cob = type_tag(tagsB, tb), type_tag(tagsB, tb, coarse=True)
        if cb is None: continue
        exact = [i for i, c in enumerate(clsA) if c == cb]
        coarse = [i for i, c in enumerate(coA) if c == cob]
        allowed = exact or coarse
        if not allowed: continue
        row = np.zeros(n, bool); row[allowed] = True; row[len(toksA):] = True
        C[j, :] = row
    return C


def anchors_by_margin(MA, MB, nB, nA, n_anchors=K.N_ANCHORS, compat=None):
    """B types whose best A match beats their second-best by the largest margin (signature distance),
    among compatible pairs."""
    SA, SB = signatures(MA), signatures(MB)
    scale = SA[:nA].std(0) + 1e-6
    D = (((SA[None, :nA, :] - SB[:nB, None, :]) / scale) ** 2).sum(-1)
    if compat is not None:
        D = np.where(compat[:nB, :nA], D, np.inf)
    margins = []
    for j in range(nB):
        d = np.sort(D[j])
        if not np.isfinite(d[0]) or len(d) < 2 or not np.isfinite(d[1]): continue
        margins.append((d[1] - d[0], j, int(np.argmin(D[j]))))
    margins.sort(reverse=True)
    anchors, used = {}, set()
    for _, j, i in margins:            # distinct A targets, greedily by margin
        if i in used: continue
        anchors[j] = i; used.add(i)
        if len(anchors) >= n_anchors: break
    return anchors


def align(MA, MB, rng, anchors=None, restarts=K.ALIGN_RESTARTS, iters=K.ALIGN_ITERS, compat=None, soft=None):
    n = next(iter(MA.values())).shape[0]
    SA, SB = signatures(MA), signatures(MB)
    scale = SA.std(0) + 1e-6
    D = (((SA[None, :, :] - SB[:, None, :]) / scale) ** 2).sum(-1)
    D = D / max(1e-12, float(np.median(D[np.isfinite(D)])))     # distances in units of their median, so penalties have a fixed meaning
    forbid = None if compat is None else np.where(compat, 0.0, BIG)
    if soft is not None and soft.any():      # graded preferences, in units of the typical distance
        forbid = soft.copy() if forbid is None else forbid + soft
    if forbid is not None: D = D + forbid
    if anchors:
        for j, i in anchors.items():
            D[j, :] += BIG; D[j, i] -= BIG
    def objective(pi):
        P = np.zeros((n, n)); P[np.arange(n), pi] = 1
        return sum(np.linalg.norm(MB[c] - P @ MA[c] @ P.T) ** 2 for c in LAGS)
    def refine(pi):
        for _ in range(iters):
            cost = np.zeros((n, n))
            for c in LAGS:
                A, Bm = MA[c], MB[c]
                rowsA, colsA = A[:, pi], A[pi, :].T
                for j in range(n):
                    cost[j, :] += ((rowsA - Bm[j, :][None, :]) ** 2).sum(1) + ((colsA - Bm[:, j][None, :]) ** 2).sum(1)
            cost = cost / max(1e-12, float(np.median(cost)))
            if forbid is not None: cost += forbid
            if anchors:
                for j, i in anchors.items():
                    cost[j, :] += BIG; cost[j, i] -= BIG
            rj, ci = linear_sum_assignment(cost)
            new = np.empty(n, int); new[rj] = ci
            if np.array_equal(new, pi): break
            pi = new
        return pi
    rj, ci = linear_sum_assignment(D)
    pi0 = np.empty(n, int); pi0[rj] = ci
    best, best_obj = None, np.inf
    for start in [pi0] + [rng.permutation(n) for _ in range(restarts)]:
        pi = refine(start); o = objective(pi)
        if o < best_obj: best, best_obj = pi, o
    return best, best_obj


def align_datasets(rowsA, toksA, rowsB, toksB, rng, use_anchors=True, tagsA=None, tagsB=None):
    """Returns mapping {B type: A type or None}, anchors used, alignment objective. With tags (3.14) a
    B type may only map to an A type of the same part-of-speech class."""
    n = max(len(toksA), len(toksB))
    MA = zscore(pad(lift_matrices(rowsA, toksA), n)); MB = zscore(pad(lift_matrices(rowsB, toksB), n))
    compat = compatibility(toksA, toksB, tagsA, tagsB, n) if (tagsA and tagsB) else None
    anchors = anchors_by_margin(MA, MB, len(toksB), len(toksA), compat=compat) if use_anchors else None
    pi, obj = align(MA, MB, rng, anchors, compat=compat)
    mapping = {t: (toksA[pi[j]] if pi[j] < len(toksA) else None) for j, t in enumerate(toksB)}
    anchor_names = {toksB[j]: toksA[i] for j, i in (anchors or {}).items()}
    return mapping, anchor_names, obj


# ---------------------------------------------------------------------------------------------
# Role-level alignment (METHOD 3.12, v4): roles map to roles of the same part of speech and the
# same symbol kind; symbols cross by their spelling (up stays up, q80 stays q80, peak stays peak).
# ---------------------------------------------------------------------------------------------

def role_of(t): return t.split(":", 1)[0]
def sym_of(t): return t.split(":", 1)[1] if ":" in t else ""


def symbol_kind(syms):
    s = set(syms)
    if s <= {"peak", "trough"}: return "turning"
    if s <= {"on", "off"}: return "binary"
    if all(x.startswith(("up", "down")) for x in s): return "quantile"
    return "other"


def role_lift_matrices(rows, toks, roles, labels=LAGS):
    """Role x role lift per lag class: mean over the symbol pairs of the type-level lift matrix."""
    M = lift_matrices(rows, toks)
    idx = {t: i for i, t in enumerate(toks)}
    members = {r: [idx[t] for t in toks if role_of(t) == r] for r in roles}
    out = {}
    for c in labels:
        R = np.zeros((len(roles), len(roles)))
        for a, ra in enumerate(roles):
            for b, rb in enumerate(roles):
                sub = M[c][np.ix_(members[ra], members[rb])]
                R[a, b] = sub.mean() if sub.size else 0.0
        out[c] = R
    return out


def align_roles(rowsA, toksA, rowsB, toksB, rng, tagsA=None, tagsB=None, use_anchors=True):
    """Returns (type mapping {B type: A type or None}, role mapping, anchors, objective)."""
    from ..choose.pos import type_tag
    rolesA = sorted(set(role_of(t) for t in toksA)); rolesB = sorted(set(role_of(t) for t in toksB))
    symsA = {r: sorted(sym_of(t) for t in toksA if role_of(t) == r) for r in rolesA}
    symsB = {r: sorted(sym_of(t) for t in toksB if role_of(t) == r) for r in rolesB}
    n = len(rolesA) + len(rolesB)      # dummies on BOTH sides, so any role may map to no counterpart (kinds and dimensions need not balance)
    MA = zscore(pad(role_lift_matrices(rowsA, toksA, rolesA), n)); MB = zscore(pad(role_lift_matrices(rowsB, toksB, rolesB), n))
    # compatibility (v5): HARD on symbol kind and on the dimension suffix when both sides know it (categorical
    # facts); GRADED on the clock class (exact 0, coarse speed 1, neither 2) and on the place prefix (+1 when the
    # influence differs). Hard clock classes made the assignment infeasible (several receiver roles allowed the
    # same single source role), so the Hungarian had to violate them anyway.
    C = np.ones((n, n), bool)
    soft = np.zeros((n, n))
    for j, rb in enumerate(rolesB):
        kind_ok = [i for i, ra in enumerate(rolesA) if symbol_kind(symsA[ra]) == symbol_kind(symsB[rb])]
        allowed = kind_ok
        if tagsA and tagsB:
            tb = tagsB.get(rb, {}); db = tb.get("dimension")
            if db is not None:
                dim_ok = [i for i in kind_ok if (tagsA.get(rolesA[i], {}).get("dimension") in (None, db))]
                allowed = dim_ok or kind_ok
            cb = type_tag(tagsB, rb + ":x"); cob = type_tag(tagsB, rb + ":x", coarse=True); infl = tb.get("influence")
            for i in allowed:
                ta = tagsA.get(rolesA[i], {})
                ca, coa = type_tag(tagsA, rolesA[i] + ":x"), type_tag(tagsA, rolesA[i] + ":x", coarse=True)
                if cb is not None and ca is not None:
                    soft[j, i] += 0.0 if ca == cb else (1.0 if coa == cob else 2.0)
                if infl and ta.get("influence") not in (None, infl):
                    soft[j, i] += 1.0
        row = np.zeros(n, bool); row[allowed] = True; row[len(rolesA):] = True
        C[j, :] = row
        soft[j, len(rolesA):] += K.ALIGN_UNMATCHED_PENALTY    # mapping to no counterpart costs more than any graded mismatch
    anchors = anchors_by_margin(MA, MB, len(rolesB), len(rolesA), compat=C) if use_anchors else None
    pi, obj = align(MA, MB, rng, anchors, compat=C, soft=soft)
    role_map = {rb: (rolesA[pi[j]] if pi[j] < len(rolesA) else None) for j, rb in enumerate(rolesB)}
    setA = set(toksA)
    mapping = {}
    for t in toksB:
        ra = role_map.get(role_of(t))
        cand = f"{ra}:{sym_of(t)}" if ra else None
        if cand in setA: mapping[t] = cand
        elif ra and symbol_kind([sym_of(t)]) == "quantile" and symbol_kind(symsA[ra]) == "quantile":
            mapping[t] = cross_scheme(ra, sym_of(t), symsA[ra])    # v6: different quantile schemes, by direction and nearest quantile
        else: mapping[t] = None
    anchor_names = {rolesB[j]: rolesA[i] for j, i in (anchors or {}).items()}
    return mapping, role_map, anchor_names, obj


def _quantile(sym):
    d = "up" if sym.startswith("up") else "down"
    q = sym[len(d):].lstrip("q")
    try: return d, float(q)
    except ValueError: return d, None


def cross_scheme(ra, sym, syms_a):
    """3.12 (v6): a quantile symbol crosses to the source role's symbol of the same direction and nearest
    quantile (upq10 -> upq20, upq90 -> upq80, q50 -> q50); a tie (q50 against q10/q90) crosses to nothing."""
    d, q = _quantile(sym)
    if q is None: return None
    cands = [(abs(qa - q), sa) for sa in syms_a for da, qa in [_quantile(sa)] if da == d and qa is not None]
    if not cands: return None
    cands.sort(); best = cands[0][0]
    if len(cands) > 1 and cands[1][0] == best: return None
    return f"{ra}:{cands[0][1]}"


def has_roles(toks):
    """Types are role:symbol with at least two symbols per role somewhere (else fall back to type-level)."""
    from collections import Counter
    c = Counter(role_of(t) for t in toks if ":" in t)
    return len(c) >= 2 and max(c.values()) >= 2
