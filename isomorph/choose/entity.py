"""
Entity by compression (METHOD.md 3.1, v1 implementation).

Candidates are alternative layouts of the same raw frame: a wide frame offers the
groupings its column names allow (e.g. "zone": one entity per zone with roles T, CO2, ...;
"sys": one entity holding every column as its own role). A long frame offers each
categorical column with 2..1000 distinct values plus "sys". For each candidate the events
are assembled under the same symbolization and scored by confirmation-split bits with
Markov features only; lowest wins; ties within 0.02 bits go to more entities.
"""
import numpy as np
from .. import constants as K
from ..canon.ingest import SYSTEM
from ..mine.contexts import LagClasses, streams_of, inter_event_gaps
from ..mine.library import rows_for
from ..score.model import FeatureMap, fit_bits
from .symbolize import assemble


def sys_layout(layout):
    """Collapse a multi-entity layout into one entity: every column becomes its own role."""
    kinds, cols = {}, {}
    for ent, roles in layout["entities"].items():
        for role, col in roles.items():
            kinds[f"{role}_{ent}"] = layout["kinds"][role]; cols[f"{role}_{ent}"] = col
    for role, col in layout.get("system", {}).items():
        kinds[role] = layout["kinds"][role]
    return dict(time=layout["time"], entities={"sys": cols}, system=layout.get("system", {}), kinds=kinds,
                observation={})


def markov_bits(ev, lo, p_hi, c_hi):
    entities = sorted(e for e in ev.entity.unique() if e != SYSTEM)
    streams = streams_of(ev, entities)
    prop = {z: s[(s.t >= lo) & (s.t < p_hi)] for z, s in streams.items()}
    lags = LagClasses.from_recurrence(streams, lo, p_hi)                           # v2 (3.3)
    rows_p = rows_for(streams, lags, lo, p_hi, None, "ignore", want_gaps=False); rows_c = rows_for(streams, lags, p_hi, c_hi, None, "ignore", want_gaps=False)
    vocab = sorted(set(r["tok"] for r in rows_p + rows_c))
    return float(fit_bits(FeatureMap(vocab, True), rows_p, rows_c).mean()), len(entities)


def choose_entity(df, candidates, choice, splits_frac=(0.5, 0.25), log=print):
    """candidates: {name: layout}. `choice`: symbolization per role name (roles are translated for the
    sys layout by suffix). Returns (winner name, scores)."""
    t = df[candidates[next(iter(candidates))]["time"]].values.astype(float); lo, hi = float(t.min()), float(t.max()) + 1
    p_hi, c_hi = lo + (hi - lo) * splits_frac[0], lo + (hi - lo) * (splits_frac[0] + splits_frac[1])
    scores = {}
    for name, lay in candidates.items():
        ch = {}
        for role in lay["kinds"]:
            base = role
            for r in choice:
                if role == r or role.startswith(r + "_"): base = r
            ch[role] = choice.get(base)
        ev = assemble(df, lay, ch, {})
        bits, n_ent = markov_bits(ev, lo, p_hi, c_hi)
        scores[name] = dict(bits=bits, entities=n_ent)
        log(f"  entity candidate {name:8s} entities={n_ent:3d} confirmation bits (Markov only) {bits:.3f}")
    best = min(scores, key=lambda n: scores[n]["bits"])
    for n, s in scores.items():   # ties within tolerance -> more entities
        if abs(s["bits"] - scores[best]["bits"]) <= 0.02 and s["entities"] > scores[best]["entities"]:
            best = n
    return best, scores
