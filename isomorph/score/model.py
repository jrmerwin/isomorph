"""Predictive model (METHOD.md 3.9): multinomial logistic regression over
indicator features (Markov-1/2 adjacent contexts + library contexts [+ compositions] [+ chains, v6])."""
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.linear_model import LogisticRegression
from .. import constants as K


class FeatureMap:
    def __init__(self, vocab, use_markov=True, frag_ctxs=(), comp_ctxs=(), chain_keys=()):
        self.vocab = list(vocab); self.feats = {}
        if use_markov:
            for t in vocab: self.feats[("m1", t)] = len(self.feats)
            for a in vocab:
                for b in vocab: self.feats[("m2", a, b)] = len(self.feats)
        for c in frag_ctxs: self.feats.setdefault(("f", c), len(self.feats))
        for c in comp_ctxs: self.feats.setdefault(("c", c), len(self.feats))
        for h in chain_keys: self.feats.setdefault(("h", h), len(self.feats))     # v6: chains and returns (3.15)
        self.comp_keys = [k for k in self.feats if k[0] == "c"]
        self.has_chains = any(k[0] == "h" for k in self.feats)

    def transform(self, rows):
        data, ri, ci = [], [], []
        for i, r in enumerate(rows):
            keys = []
            if r["m1"] is not None: keys.append(("m1", r["m1"]))
            if r["m2"] is not None: keys.append(("m2",) + tuple(r["m2"]))
            for c in r["ctx"]:
                if ("f", c) in self.feats: keys.append(("f", c))
            if self.comp_keys:
                cset = r["ctx"]
                for k in self.comp_keys:
                    if k[1][0] in cset and k[1][1] in cset: keys.append(k)
            if self.has_chains:
                for h in r.get("chains", ()):
                    if ("h", h) in self.feats: keys.append(("h", h))
            for k in keys:
                j = self.feats.get(k)
                if j is not None: ri.append(i); ci.append(j); data.append(1.0)
        return csr_matrix((data, (ri, ci)), shape=(len(rows), max(1, len(self.feats))))


class Model:
    def __init__(self, fm, C=K.LOGISTIC_C):
        self.fm, self.C = fm, C
        self.ydict = {t: i for i, t in enumerate(fm.vocab)}

    def fit(self, rows):
        self.clf = LogisticRegression(C=self.C, max_iter=2000)
        self.clf.fit(self.fm.transform(rows), np.array([self.ydict[r["tok"]] for r in rows]))
        self.cls = {c: i for i, c in enumerate(self.clf.classes_)}
        return self

    def proba(self, rows):
        P = self.clf.predict_proba(self.fm.transform(rows))
        out = np.full((len(rows), len(self.fm.vocab)), 1e-9)
        for c, i in self.cls.items(): out[:, c] = P[:, i]
        return out / out.sum(1, keepdims=True)

    def bits(self, rows):
        P = self.proba(rows)
        y = np.array([self.ydict[r["tok"]] for r in rows])
        return -np.log2(np.maximum(P[np.arange(len(rows)), y], 1e-9))


def fit_bits(fm, rows_train, rows_test):
    return Model(fm).fit(rows_train).bits(rows_test)
