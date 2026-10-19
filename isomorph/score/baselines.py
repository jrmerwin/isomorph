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
        if r.get("m3") is not None: counts[3][tuple(r["m3"])][r["tok"]] += 1
    bits = []
    for r in rows_test:
        y = r["tok"]
        p = (counts[0][()][y] + alpha) / (sum(counts[0][()].values()) + alpha * len(vocab))
        ctxs = [(1, (r["m1"],) if r["m1"] is not None else None), (2, tuple(r["m2"]) if r["m2"] is not None else None),
                (3, tuple(r["m3"]) if r.get("m3") is not None else None)]
        for j, ctx in ctxs:
            if j > k or ctx is None: break
            c = counts[j].get(ctx)
            if c is None: break
            p = (c[y] + lam * p) / (sum(c.values()) + lam)
        bits.append(-np.log2(p))
    return np.array(bits)


def unigram_bits(rows_train, rows_test, vocab):
    return markov_bits(rows_train, rows_test, vocab, k=0)


def alternating_pairs(rows, threshold=0.9, min_events=20):
    """Name-free trivial pairs (METHOD 3.11): two types X, Y within an entity stream whose merged
    subsequence strictly alternates (X Y X Y ...) at least `threshold` of the time. Captures on/off
    and up/down partners whatever the types are called."""
    seqs = defaultdict(list)
    for r in rows:
        seqs[r.get("entity", "")].append(r["tok"])
    types = sorted(set(r["tok"] for r in rows))
    pairs = set()
    for i, X in enumerate(types):
        for Y in types[i + 1:]:
            alt = tot = 0
            for s in seqs.values():
                sub = [t for t in s if t == X or t == Y]
                for a, b_ in zip(sub, sub[1:]):
                    tot += 1; alt += (a != b_)
            if tot >= min_events and alt / tot >= threshold:
                pairs.add((X, Y))
    return pairs


def triviality_contexts(vocab, lags, rows=None):
    """Contexts of the trivial library: each type's alternating partner at every lag class."""
    ctxs = set()
    pairs = alternating_pairs(rows) if rows is not None else set()
    for X, Y in pairs:
        for lab in lags.labels:
            ctxs.add((X, lab)); ctxs.add((Y, lab))
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


class DecayFeatureMap:
    """Hawkes-like baseline (METHOD 3.9): for each type x, the feature exp(-gap_x / tau) over the most
    recent occurrence of x within the horizon — exponentially decaying excitation — fed to the same
    multinomial logistic model, with no Markov and no lag-class features. tau = the middle lag edge."""
    def __init__(self, vocab, all_types, tau):
        self.vocab, self.types, self.tau = list(vocab), list(all_types), tau
        self.feats = {("h", t): i for i, t in enumerate(self.types)}
        self.comp_keys = []

    def transform(self, rows):
        from scipy.sparse import csr_matrix
        data, ri, ci = [], [], []
        for i, r in enumerate(rows):
            for t, g in r.get("gaps", {}).items():
                j = self.feats.get(("h", t))
                if j is not None: ri.append(i); ci.append(j); data.append(float(np.exp(-g / self.tau)))
        return csr_matrix((data, (ri, ci)), shape=(len(rows), max(1, len(self.feats))))


def hawkes_bits(rows_train, rows_test, vocab, all_types, tau):
    return fit_bits(DecayFeatureMap(vocab, all_types, tau), rows_train, rows_test)
