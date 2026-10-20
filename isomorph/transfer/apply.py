"""
Transfer measurement for an ordered pair (A, B) (METHOD.md 3.12):
zero-shot bits of A's fitted model on B's test split through a mapping; a
mixture with B's own model as B's training days grow (learning curve); negative
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


def permuted_mappings(mapping, rng, n, tagsB=None):
    """Random-mapping controls (METHOD 3.12, v3): the same receiver types stay mapped, but their source
    targets are shuffled among them, so the translated source model keeps its size and smoothness and loses
    only the correspondence. What a permuted mapping gains is regularisation, not shared structure.
    With tags (v4) the shuffle is WITHIN each receiver tag class, so the control keeps the grammar and
    loses only the word-level correspondence — a stricter control."""
    from ..choose.pos import type_tag
    keys = [t for t, v in mapping.items() if v is not None]
    groups = {}
    for t in keys:
        groups.setdefault(type_tag(tagsB, t) if tagsB else None, []).append(t)
    out = []
    for _ in range(n):
        m = dict(mapping)
        for g in groups.values():
            vals = [mapping[t] for t in g]; perm = list(rng.permutation(vals)); m.update(dict(zip(g, perm)))
        out.append(m)
    return out


def transfer(modelA, B, mapping, toksB, min_count=5, days=K.LEARNING_CURVE_DAYS, rng=None, n_controls=K.N_CONTROL_MAPPINGS, tagsB=None):
    """B: dict from pipeline.run's second return (streams, lags, bounds, gaps, gap_mode, rows_test, vocab).
    Reports the learned-mapping curve and cell, the same for `n_controls` permuted mappings (same lambda per
    day point, median over controls), and the cell NET of the control — the headline transfer figure."""
    rng = np.random.default_rng(0) if rng is None else rng
    lo, p_hi, c_hi, hi = B["bounds"]
    rows_test = B["rows_test"]
    P_A = proba_through_mapping(modelA, rows_test, mapping, toksB)
    controls = permuted_mappings(mapping, rng, n_controls, tagsB)
    P_C = [proba_through_mapping(modelA, rows_test, m, toksB) for m in controls]
    unshared = np.array([mapping.get(r["tok"]) is None for r in rows_test])
    b0 = bits_of(P_A, rows_test, toksB)
    out = dict(zero_shot=dict(all=float(b0.mean()), shared=float(b0[~unshared].mean()) if (~unshared).any() else None,
                              unshared=float(b0[unshared].mean()) if unshared.any() else None,
                              control=float(np.median([bits_of(P, rows_test, toksB).mean() for P in P_C])) if P_C else None), curve=[])
    train_days_total = int((c_hi - lo) // 1440)
    for k in days:
        kd = train_days_total if k is None else min(k, train_days_total)
        rows_tr = rows_for(B["streams"], B["lags"], lo, lo + kd * 1440, B["gaps"], B["gap_mode"])
        for r in rows_tr: r["day"] = int(r["t"] // 1440)
        fm = FeatureMap(toksB, True, own_contexts(rows_tr, min_count))
        # lambda chosen on B's own training days (2-fold by day parity; 0.5 when one day)
        lam = 0.5
        if kd >= 2:
            score = np.zeros(len(LAMBDAS))
            for fold in (0, 1):
                tr = [r for r in rows_tr if r["day"] % 2 == fold]; va = [r for r in rows_tr if r["day"] % 2 != fold]
                if not tr or not va: continue
                Pv_own = Model(fm).fit(tr).proba(va); Pv_A = proba_through_mapping(modelA, va, mapping, toksB)
                yv = np.array([fm.vocab.index(r["tok"]) for r in va])
                for li, l in enumerate(LAMBDAS):
                    Pm = l * Pv_A + (1 - l) * Pv_own
                    score[li] += -np.log2(np.maximum(Pm[np.arange(len(yv)), yv], 1e-9)).sum()
            lam = LAMBDAS[int(np.argmin(score))]
        P_own = Model(fm).fit(rows_tr).proba(rows_test)
        b_own = bits_of(P_own, rows_test, toksB); b_mix = bits_of(lam * P_A + (1 - lam) * P_own, rows_test, toksB)
        b_ctl = [bits_of(lam * P + (1 - lam) * P_own, rows_test, toksB).mean() for P in P_C]
        out["curve"].append(dict(days=kd, lam=lam, own=float(b_own.mean()), mixed=float(b_mix.mean()),
                                 mixed_control=float(np.median(b_ctl)) if b_ctl else None,
                                 own_shared=float(b_own[~unshared].mean()), mixed_shared=float(b_mix[~unshared].mean()),
                                 own_unshared=float(b_own[unshared].mean()) if unshared.any() else None,
                                 mixed_unshared=float(b_mix[unshared].mean()) if unshared.any() else None))
    xs = [c["days"] for c in out["curve"]]; ys = [c["own"] - c["mixed"] for c in out["curve"]]
    out["cell_bit_days"] = float(np.trapezoid(ys, xs)) if len(xs) > 1 else 0.0
    if P_C:
        yc = [c["own"] - c["mixed_control"] for c in out["curve"]]
        out["cell_control_bit_days"] = float(np.trapezoid(yc, xs)) if len(xs) > 1 else 0.0
        out["cell_net_bit_days"] = out["cell_bit_days"] - out["cell_control_bit_days"]
    out["damage"] = any((c["mixed_unshared"] or 0) > (c["own_unshared"] or 0) + 1e-9 for c in out["curve"] if c["own_unshared"] is not None)
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
