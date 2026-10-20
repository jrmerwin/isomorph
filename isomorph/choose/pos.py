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


# ---------------------------------------------------------------------------------------------
# v5: the structural prefix (place in the coupling web) and the dimension suffix.
# ---------------------------------------------------------------------------------------------

# SI dimension vectors as (M, L, T, Theta, N, I, J); a None suffix means dimensionless or unknown.
DIMENSIONS = {
    "pressure": (1, -1, -2, 0, 0, 0, 0), "length": (0, 1, 0, 0, 0, 0, 0), "temperature": (0, 0, 0, 1, 0, 0, 0),
    "volume_flow": (0, 3, -1, 0, 0, 0, 0), "mass_flow": (1, 0, -1, 0, 0, 0, 0), "power": (1, 2, -3, 0, 0, 0, 0),
    "frequency": (0, 0, -1, 0, 0, 0, 0), "velocity": (0, 1, -1, 0, 0, 0, 0), "voltage": (1, 2, -3, 0, -1, 0, 0),
    "time": (0, 0, 1, 0, 0, 0, 0), "mass": (1, 0, 0, 0, 0, 0, 0), "volume": (0, 3, 0, 0, 0, 0, 0),
    "current": (0, 0, 0, 0, 0, 1, 0),
}


def dim_label(vec):
    if vec is None: return None
    names = "M L T Θ N I J".split()
    sup = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")
    return " ".join(f"{n}{str(e).translate(sup) if e != 1 else ''}" for n, e in zip(names, vec) if e != 0) or "1"


def place_tags(fragments, roles, binding_share_common=0.5, lead_ratio=2.0):
    """Structural prefix per role from the validated library: LOCAL/COMMON from the share of its fragments
    with binding evidence (rewire null, 3.8), LEAD/FOLLOW/RELAY/ISOLATED from its out- and in-degree."""
    from collections import defaultdict
    out_deg, in_deg, bound, total = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
    for f in fragments:
        rp, rt = f["prior"].split(":")[0], f["target"].split(":")[0]
        out_deg[rp] += 1; in_deg[rt] += 1
        total[rt] += 1; bound[rt] += 1 if f.get("binding_evidence") else 0
    tags = {}
    for r in roles:
        o, i = out_deg.get(r, 0), in_deg.get(r, 0)
        if o == 0 and i == 0: infl = "ISOLATED"
        elif i == 0 or o >= lead_ratio * i: infl = "LEAD"
        elif o == 0 or i >= lead_ratio * o: infl = "FOLLOW"
        else: infl = "RELAY"
        loc = None if total.get(r, 0) == 0 else ("LOCAL" if bound[r] / total[r] >= binding_share_common else "COMMON")
        tags[r] = dict(influence=infl, locality=loc, out_degree=o, in_degree=i, binding_share=(round(bound[r] / total[r], 2) if total.get(r) else None))
    return tags


def full_tag(tags, role):
    """'MID·LOCAL·LEAD ⟨M L⁻¹ T⁻²⟩' — clock prefix · place prefix · dimension suffix."""
    t = tags.get(role)
    if not t: return None
    parts = [t["cls"]]
    if t.get("locality"): parts.append(t["locality"])
    if t.get("influence"): parts.append(t["influence"])
    s = "·".join(parts)
    if t.get("dimension"): s += f" ⟨{dim_label(tuple(t['dimension']))}⟩"
    return s
