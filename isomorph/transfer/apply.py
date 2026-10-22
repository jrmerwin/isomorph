"""
Transfer measurement for an ordered pair (A, B) (METHOD.md 3.12):
zero-shot bits of A's fitted model on B's test split through a mapping; a
mixture with B's own model as B's observed training time grows in its own horizons (learning curve, v8); negative
transfer on B's types with no A counterpart; mapping accuracy when an answer key
gives roles. The matrix cell is the area between B's own curve and the mixed
curve in bit-days (trapezoid over the training-day points).

Mixing weight: global in v1.0 (per-fragment weights are an open item, section 7).
"""
import numpy as np
from .. import constants as K
from ..score.model import FeatureMap, Model
from ..mine.library import pair_counts, rows_for

LAMBDAS = (0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0)


def translate_rows(rows, mapping):
    """Re-express B rows in A's vocabulary (unmapped tokens drop out of contexts)."""
    out = []
    for r in rows:
        m2 = None
        if r["m2"] is not None and all(mapping.get(t) for t in r["m2"]):
            m2 = tuple(mapping[t] for t in r["m2"])
        out.append(dict(m1=mapping.get(r["m1"]) if r["m1"] else None, m2=m2,
                        ctx=set((mapping[t], c) for t, c in r["ctx"] if mapping.get(t)), tok=r["tok"]))
    return out


def proba_through_mapping(modelA, rows_B, mapping, toksB):
    """A's predictive distribution over B's types for B rows."""
    PA = modelA.proba(translate_rows(rows_B, mapping))
    P = np.full((len(rows_B), len(toksB)), 1e-3)
    for j, t in enumerate(toksB):
        a = mapping.get(t)
        if a is not None and a in modelA.ydict:
            P[:, j] = PA[:, modelA.ydict[a]]
    return P / P.sum(1, keepdims=True)


def bits_of(P, rows, toksB):
    yd = {t: i for i, t in enumerate(toksB)}
    y = np.array([yd[r["tok"]] for r in rows])
    return -np.log2(np.maximum(P[np.arange(len(rows)), y], 1e-9))


def own_contexts(rows, min_count):
    cnt, base = pair_counts(rows)
    return [c for c, b in base.items() if b >= min_count and any(v >= min_count for v in cnt[c].values())]


def _derange(vals, rng, tries=60):
    """A permutation of `vals` in which no position keeps its value, or None if none exists (all values equal)."""
    n = len(vals)
    if n < 2 or len(set(vals)) < 2: return None
    for _ in range(tries):
        perm = list(rng.permutation(vals))
        if all(a != b for a, b in zip(perm, vals)): return perm
    if len(set(vals)) == n:          # distinct values: a cyclic shift of a random order is always a derangement
        order = list(rng.permutation(n)); shifted = order[1:] + order[:1]
        out = [None] * n
        for src, dst in zip(order, shifted): out[dst] = vals[src]
        return out
    return None


def permuted_mappings(mapping, rng, n, tagsB=None):
    """Controls (METHOD 3.12, v8): each control mapping is a DERANGEMENT of the learned one — no mapped receiver
    type keeps its learned source counterpart — so that a pairing through singleton groups is not its own control
    (v7: PhysioNet -> TEP 18.08 net through four types). The group is widened only as far as needed: within
    (clock class, dimension) first, then within the clock class across dimensions, then across all mapped types.
    Returns (controls, info): info has the cumulative share of types moved at each width and `uncontrolled`
    (True when some mapped type cannot be moved at any width, e.g. a single mapped type)."""
    from ..choose.pos import type_tag
    keys = [t for t, v in mapping.items() if v is not None]
    def width_key(t, width):
        role = t.split(":")[0]; tb = (tagsB or {}).get(role, {})
        clock = type_tag(tagsB, t) if tagsB else None; dim = tuple(tb["dimension"]) if tb.get("dimension") else None
        return (clock, dim) if width == 0 else (clock,) if width == 1 else ("all",)
    out = []; moved_share = {0: [], 1: [], 2: []}; uncontrolled = False
    for _ in range(n):
        m = dict(mapping); unmoved = list(keys)
        for width in (0, 1, 2):
            groups = {}
            for t in unmoved: groups.setdefault(width_key(t, width), []).append(t)
            still = []
            for g in groups.values():
                vals = [mapping[t] for t in g]; perm = _derange(vals, rng)
                if perm is None:
                    if width == 2 and len(keys) > len(g):   # leftovers (types sharing one source counterpart): swap each with a moved type whose value differs
                        for t in g:
                            partners = [u for u in keys if u not in g and mapping[u] != mapping[t] and m[u] != mapping[t]]
                            if partners:
                                u = partners[int(rng.integers(len(partners)))]; m[t], m[u] = m[u], m[t]
                                if m[t] == mapping[t] or m[u] == mapping[u]: still.append(t)   # keep honest: an unmoved type stays counted
                            else: still.append(t)
                        continue
                    still.extend(g); continue
                m.update(dict(zip(g, perm)))
            moved_share[width].append(1.0 - len(still) / len(keys) if keys else 1.0)
            unmoved = still
            if not unmoved: 
                for w in range(width + 1, 3): moved_share[w].append(1.0)
                break
        if unmoved: uncontrolled = True
        out.append(m)
    info = dict(moved_share={f"width_{w}": (float(np.mean(v)) if v else None) for w, v in moved_share.items()},
                uncontrolled=bool(uncontrolled or len(keys) < 2), n_mapped=len(keys))
    return out, info


def observed_training_time(B, lo, c_hi, n_grid=2000):
    """3.12 (v8): training time on the receiver's OBSERVED clock — per entity the time inside its observation
    window and outside its gaps, averaged over the entities; returns (t_grid, observed_minutes at each t)."""
    obs = B.get("obs"); gaps = B.get("gaps"); ents = list(B["streams"].keys())
    grid = np.linspace(lo, c_hi, n_grid)
    total = np.zeros(n_grid)
    for z in ents:
        if obs is not None and (obs.entity == z).any():
            s_, e_ = float(obs[obs.entity == z].start.iloc[0]), float(obs[obs.entity == z].end.iloc[0])
        else: s_, e_ = lo, c_hi
        o = np.clip(grid, s_, e_) - min(max(s_, lo), c_hi)
        o = np.maximum(o, 0.0)
        if gaps is not None and len(gaps):
            for _, g in gaps[(gaps.entity == z) & ((gaps.type.astype(str) == "") | (gaps.type.astype(str) == "nan"))].iterrows():
                gs, ge = max(float(g.start), lo), min(float(g.end), c_hi)
                if ge > gs: o -= np.clip(grid, gs, ge) - gs
        total += np.maximum(o, 0.0)
    return grid, total / max(len(ents), 1)


def marginal_through_mapping(marginalA, rows_B, mapping, toksB):
    """3.12 (v9), the marginal control: the source model reduced to its type frequencies through the learned mapping —
    per mapped receiver type the translated source frequency and nothing lagged; unmapped types as in proba_through_mapping."""
    P = np.full((len(rows_B), len(toksB)), 1e-3)
    for j, t in enumerate(toksB):
        a = mapping.get(t)
        if a is not None and a in marginalA: P[:, j] = max(marginalA[a], 1e-9)
    return P / P.sum(1, keepdims=True)


def transfer(modelA, B, mapping, toksB, min_count=5, horizons=K.LEARNING_CURVE_HORIZONS, rng=None, n_controls=K.N_CONTROL_MAPPINGS, tagsB=None, marginalA=None):
    """B: dict from pipeline.run's second return (streams, lags, bounds, gaps, obs, gap_mode, rows_test, vocab).
    v8 (3.12): the learned-mapping learning curve on the receiver's observed training time at 1 ... 200 of its
    recurrence horizons H, the same for `n_controls` derangement controls (same lambda per point, median), and the
    cell NET of the control, in bit-horizons (bits x H); the area runs to 200 H or the end of training."""
    rng = np.random.default_rng(0) if rng is None else rng
    lo, p_hi, c_hi, hi = B["bounds"]; H = float(B["lags"].horizon)
    rows_test = B["rows_test"]
    P_A = proba_through_mapping(modelA, rows_test, mapping, toksB)
    controls, cinfo = permuted_mappings(mapping, rng, n_controls, tagsB)
    P_C = [proba_through_mapping(modelA, rows_test, m, toksB) for m in controls]
    P_M = marginal_through_mapping(marginalA, rows_test, mapping, toksB) if marginalA else None   # v9: the marginal control
    unshared = np.array([mapping.get(r["tok"]) is None for r in rows_test])
    b0 = bits_of(P_A, rows_test, toksB)
    out = dict(zero_shot=dict(all=float(b0.mean()), shared=float(b0[~unshared].mean()) if (~unshared).any() else None,
                              unshared=float(b0[unshared].mean()) if unshared.any() else None,
                              control=float(np.median([bits_of(P, rows_test, toksB).mean() for P in P_C])) if P_C else None,
                              marginal=float(bits_of(P_M, rows_test, toksB).mean()) if P_M is not None else None),
               curve=[], horizon_minutes=H, control=cinfo, uncontrolled=cinfo["uncontrolled"])
    grid, observed = observed_training_time(B, lo, c_hi)
    T_obs = float(observed[-1])                       # observed training time, minutes
    out["observed_training_horizons"] = T_obs / H; out["short"] = bool(T_obs < horizons[-1] * H)
    if T_obs < 1.0 * H:
        out.update(cell_bit_horizons=None, cell_control_bit_horizons=None, cell_net_bit_horizons=None, cell_marginal_bit_horizons=None, cell_structure_bit_horizons=None, damage=False,
                   note=f"receiver has {T_obs / H:.2f} observed training horizons; the curve needs at least 1")
        return out
    points = [k for k in horizons if k * H <= T_obs]
    if not points or points[-1] * H < T_obs and len(points) < len(horizons): points.append(T_obs / H)   # training end below 200 H
    for k in points:
        t_k = float(np.interp(k * H, observed, grid))          # the clock time at which k H of observed training has accrued
        rows_tr = rows_for(B["streams"], B["lags"], lo, t_k, B["gaps"], B["gap_mode"])
        for r in rows_tr: r["block"] = int((r["t"] - lo) // H)
        fm = FeatureMap(toksB, True, own_contexts(rows_tr, min_count))
        lam = 0.5
        if k >= 2:   # lambda chosen on the receiver's own training data: 2-fold by the parity of the H-block
            score = np.zeros(len(LAMBDAS))
            for fold in (0, 1):
                tr = [r for r in rows_tr if r["block"] % 2 == fold]; va = [r for r in rows_tr if r["block"] % 2 != fold]
                if not tr or not va: continue
                Pv_own = Model(fm).fit(tr).proba(va); Pv_A = proba_through_mapping(modelA, va, mapping, toksB)
                yv = np.array([fm.vocab.index(r["tok"]) for r in va])
                for li, l in enumerate(LAMBDAS):
                    Pm = l * Pv_A + (1 - l) * Pv_own
                    score[li] += -np.log2(np.maximum(Pm[np.arange(len(yv)), yv], 1e-9)).sum()
            lam = LAMBDAS[int(np.argmin(score))]
        if not rows_tr:
            out["curve"].append(dict(horizons=float(k), minutes=t_k - lo, lam=lam, own=None, mixed=None, mixed_control=None, own_shared=None, mixed_shared=None, own_unshared=None, mixed_unshared=None, empty=True)); continue
        P_own = Model(fm).fit(rows_tr).proba(rows_test)
        b_own = bits_of(P_own, rows_test, toksB); b_mix = bits_of(lam * P_A + (1 - lam) * P_own, rows_test, toksB)
        b_ctl = [bits_of(lam * P + (1 - lam) * P_own, rows_test, toksB).mean() for P in P_C]
        b_mar = float(bits_of(lam * P_M + (1 - lam) * P_own, rows_test, toksB).mean()) if P_M is not None else None
        out["curve"].append(dict(horizons=float(k), minutes=t_k - lo, lam=lam, own=float(b_own.mean()), mixed=float(b_mix.mean()),
                                 mixed_control=float(np.median(b_ctl)) if b_ctl else None, mixed_marginal=b_mar,
                                 own_shared=float(b_own[~unshared].mean()), mixed_shared=float(b_mix[~unshared].mean()),
                                 own_unshared=float(b_own[unshared].mean()) if unshared.any() else None,
                                 mixed_unshared=float(b_mix[unshared].mean()) if unshared.any() else None))
    pts = [c for c in out["curve"] if c.get("own") is not None]
    xs = [c["horizons"] for c in pts]; ys = [c["own"] - c["mixed"] for c in pts]
    out["cell_bit_horizons"] = float(np.trapezoid(ys, xs)) if len(xs) > 1 else 0.0
    if P_C:
        yc = [c["own"] - c["mixed_control"] for c in pts]
        out["cell_control_bit_horizons"] = float(np.trapezoid(yc, xs)) if len(xs) > 1 else 0.0
        out["cell_net_bit_horizons"] = None if cinfo["uncontrolled"] else out["cell_bit_horizons"] - out["cell_control_bit_horizons"]
    if P_M is not None:   # v9: marginal control and the structure cell = learned net of the larger control
        ym = [c["own"] - c["mixed_marginal"] for c in pts]
        out["cell_marginal_bit_horizons"] = float(np.trapezoid(ym, xs)) if len(xs) > 1 else 0.0
        larger = max([v for v in (out.get("cell_control_bit_horizons"), out["cell_marginal_bit_horizons"]) if v is not None] or [None]) if not cinfo["uncontrolled"] else out["cell_marginal_bit_horizons"]
        out["cell_structure_bit_horizons"] = None if larger is None else out["cell_bit_horizons"] - larger
        out["larger_control"] = ("marginal" if (cinfo["uncontrolled"] or out["cell_marginal_bit_horizons"] >= (out.get("cell_control_bit_horizons") or -1e9)) else "derangement")
    out["damage"] = any((c["mixed_unshared"] or 0) > (c["own_unshared"] or 0) + 1e-9 for c in pts if c["own_unshared"] is not None)
    return out


def mapping_accuracy(mapping, key, toksA):
    """key['token'][B type]['A_role'] gives the true A type (None = no counterpart)."""
    tok = key["token"]; ok = tot = 0; none_ok = none_tot = 0
    for t, m in mapping.items():
        role = tok.get(t, {}).get("A_role")
        if role is None:
            none_tot += 1; none_ok += (m is None)
        elif role in toksA:
            tot += 1; ok += (m == role)
    return dict(accuracy=ok / max(1, tot), n_scorable=tot, unshared_correct=none_ok / max(1, none_tot) if none_tot else None)
