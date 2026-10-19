"""Fixed baselines (METHOD.md 3.9, 3.11): unigram, interpolated-backoff Markov-k
on the entity stream, Markov-features logistic, triviality library. Hawkes is
listed by the method and is `not measured` until implemented (section 7, open items)."""
from collections import defaultdict
import numpy as np
from .model import FeatureMap, fit_bits


def markov_bits(rows_train, rows_test, vocab, k=2, lam=1.0, alpha=0.5):
    counts = [defaultdict(lambda: defaultdict(float)) for _ in range(4)]
    for r in rows_train:
        counts[0][()][r["tok"]] += 1
        if r["m1"] is not None: counts[1][(r["m1"],)][r["tok"]] += 1
        if r["m2"] is not None: counts[2][tuple(r["m2"])][r["tok"]] += 1
    bits = []
    for r in rows_test:
        y = r["tok"]
        p = (counts[0][()][y] + alpha) / (sum(counts[0][()].values()) + alpha * len(vocab))
        ctxs = [(1, (r["m1"],) if r["m1"] is not None else None), (2, tuple(r["m2"]) if r["m2"] is not None else None)]
        for j, ctx in ctxs:
            if j > k or ctx is None: break
            c = counts[j].get(ctx)
            if c is None: break
            p = (c[y] + lam * p) / (sum(c.values()) + lam)
        bits.append(-np.log2(p))
    return np.array(bits)


def unigram_bits(rows_train, rows_test, vocab):
    return markov_bits(rows_train, rows_test, vocab, k=0)


def triviality_contexts(vocab, lags):
    """Symmetric pairs: X:on <-> X:off, V:upT <-> V:downT, at every lag class."""
    ctxs = set()
    for t in vocab:
        if ":" not in t: continue
        var, ev = t.split(":", 1)
        partner = None
        if ev == "on": partner = f"{var}:off"
        elif ev == "off": partner = f"{var}:on"
        elif ev.startswith("up"): partner = f"{var}:down{ev[2:]}"
        elif ev.startswith("down"): partner = f"{var}:up{ev[4:]}"
        if partner in vocab:
            for lab in lags.labels:
                ctxs.add((partner, lab))
    return sorted(ctxs)


def deterministic_pairs(rows, threshold=0.95):
    """Types followed by one other type more than `threshold` of the time (entity stream)."""
    nxt = defaultdict(lambda: defaultdict(int))
    for r in rows:
        if r["m1"] is not None: nxt[r["m1"]][r["tok"]] += 1
    det = set()
    for a, d in nxt.items():
        tot = sum(d.values()); b, v = max(d.items(), key=lambda kv: kv[1])
        if tot >= 20 and v / tot > threshold: det.add(b)
    return det
