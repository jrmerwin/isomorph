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


def anchors_by_margin(MA, MB, nB, nA, n_anchors=K.N_ANCHORS):
    """B types whose best A match beats their second-best by the largest margin (signature distance)."""
    SA, SB = signatures(MA), signatures(MB)
    scale = SA[:nA].std(0) + 1e-6
    D = (((SA[None, :nA, :] - SB[:nB, None, :]) / scale) ** 2).sum(-1)
    margins = []
    for j in range(nB):
        d = np.sort(D[j]); margins.append((d[1] - d[0], j, int(np.argmin(D[j]))))
    margins.sort(reverse=True)
    anchors, used = {}, set()
    for _, j, i in margins:            # distinct A targets, greedily by margin
        if i in used: continue
        anchors[j] = i; used.add(i)
        if len(anchors) >= n_anchors: break
    return anchors


def align(MA, MB, rng, anchors=None, restarts=K.ALIGN_RESTARTS, iters=K.ALIGN_ITERS):
    n = next(iter(MA.values())).shape[0]
    SA, SB = signatures(MA), signatures(MB)
    scale = SA.std(0) + 1e-6
    D = (((SA[None, :, :] - SB[:, None, :]) / scale) ** 2).sum(-1)
    if anchors:
        for j, i in anchors.items():
            D[j, :] += 1e6; D[j, i] -= 1e6
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
            if anchors:
                for j, i in anchors.items():
                    cost[j, :] += 1e6; cost[j, i] -= 1e6
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


def align_datasets(rowsA, toksA, rowsB, toksB, rng, use_anchors=True):
    """Returns mapping {B type: A type or None}, anchors used, accuracy helper inputs."""
    n = max(len(toksA), len(toksB))
    MA = zscore(pad(lift_matrices(rowsA, toksA), n)); MB = zscore(pad(lift_matrices(rowsB, toksB), n))
    anchors = anchors_by_margin(MA, MB, len(toksB), len(toksA)) if use_anchors else None
    pi, obj = align(MA, MB, rng, anchors)
    mapping = {t: (toksA[pi[j]] if pi[j] < len(toksA) else None) for j, t in enumerate(toksB)}
    anchor_names = {toksB[j]: toksA[i] for j, i in (anchors or {}).items()}
    return mapping, anchor_names, obj
