"""
Parts of speech for variables (METHOD.md 3.14, v4).

A role's tag is computed from its series alone, in dimensionless terms relative to the system's own
clock, so that two systems' vocabularies share an alphabet before any alignment: a TEP pressure and a
HAI pressure are both "MID-R" (mid-speed, mean-reverting) whatever they are called or measured in.

Intrinsic features of a column (raw series x, denoised series xs, horizon H in samples):
  const_frac   share of zero increments of the raw series            -> SET if >= POS_CONST_FRAC (schedules, setpoints, booleans)
  signal       noise window exists (3.2)                             -> TEX if not (no signal at the sampling scale)
  speed        correlation time of xs / H                            -> FAST < POS_FAST, SLOW > POS_SLOW, else MID
  saturation   share of samples within 1% of range of the min or max -> S appended if >= POS_SAT_SHARE (actuator-like limits)
Tag classes: SET, TEX, {FAST,MID,SLOW}[-S]. A role's tag is the majority over the units that carry it.
(A reversion feature — median-crossing recurrence relative to H — was tried and dropped: H is itself a
recurrence time of threshold crossings, so every symbol-emitting series "reverts"; speed carries it.)
Coarse class (for alignment fallbacks): SET, TEX, FAST, MID, SLOW.
"""
import numpy as np
from .. import constants as K
from .symbolize import noise_window, denoise, correlation_time


def tag_series(x, H_samples):
    x = np.asarray(x, float); ok = ~np.isnan(x)
    v = x[ok]
    if len(v) < 10 or v.std() == 0:
        return dict(cls="TEX", coarse="TEX", features=dict(reason="constant or empty"))
    d = np.diff(v); const_frac = float(np.mean(d == 0))
    feats = dict(const_frac=round(const_frac, 3))
    if const_frac >= K.POS_CONST_FRAC:
        feats.update(speed=None); return dict(cls="SET", coarse="SET", features=feats)
    w = noise_window(x)
    if w is None:
        return dict(cls="TEX", coarse="TEX", features=dict(feats, noise_window=None))
    xs = denoise(x, w)[ok]
    tau = correlation_time(xs)
    speed_ratio = tau / max(1.0, H_samples)
    speed = "FAST" if speed_ratio < K.POS_FAST else ("SLOW" if speed_ratio > K.POS_SLOW else "MID")
    rng = v.max() - v.min()
    sat = float(np.mean((v <= v.min() + 0.01 * rng) | (v >= v.max() - 0.01 * rng)))
    cls = speed + ("-S" if sat >= K.POS_SAT_SHARE else "")
    feats.update(noise_window=int(w), corr_time=int(tau), speed_ratio=round(speed_ratio, 3), saturation=round(sat, 3))
    return dict(cls=cls, coarse=speed, features=feats)


def tag_layout(df, layout, H_samples):
    """{role: {cls, coarse, per_column: {col: tag}}} for every continuous/binary role of a layout."""
    from collections import Counter
    out = {}
    roles = list(layout["kinds"])
    for role in roles:
        cols = [cols_[role] for cols_ in layout["entities"].values() if role in cols_]
        if role in layout.get("system", {}): cols.append(layout["system"][role])
        per = {}
        for c in cols:
            if c not in df.columns: continue
            if layout["kinds"][role] == "binary":
                per[c] = dict(cls="SET", coarse="SET", features=dict(binary=True))
            else:
                per[c] = tag_series(df[c].values, H_samples)
        if not per: continue
        cls = Counter(t["cls"] for t in per.values()).most_common(1)[0][0]
        coarse = Counter(t["coarse"] for t in per.values()).most_common(1)[0][0]
        out[role] = dict(cls=cls, coarse=coarse, per_column=per)
    return out


def type_tag(tags, typ, coarse=False):
    """Tag of an event type 'role:symbol' from a role->tag map; None if the role is untagged."""
    t = tags.get(typ) or tags.get(typ.split(":")[0])
    if t is None: return None
    return t["coarse"] if coarse else t["cls"]


def shape_of(prior, lag, target, tags):
    """Type-free, tag-prefixed shape of a fragment: 'MID-R.up.q80 -s-> MID-R.down.q20'."""
    def part(t):
        role, sym = t.split(":", 1)
        tag = type_tag(tags, t) or "?"
        if sym in ("peak", "trough", "on", "off", "up", "down"): return f"{tag}.{sym}"
        d = "up" if sym.startswith("up") else "down"
        return f"{tag}.{d}.{sym[len(d):]}"
    same = prior.split(":")[0] == target.split(":")[0]
    return f"{part(prior)} -{lag}-> {part(target)}" + (" [same role]" if same else "")
