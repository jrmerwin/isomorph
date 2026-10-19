"""Contract checks. Raises ValueError with every violation listed."""
import numpy as np
import pandas as pd


def validate(events, observation, gaps, sidecar):
    errs = []
    if list(events.columns) != ["event_id", "t", "entity", "type", "value", "tie_rank"]:
        errs.append(f"events.csv columns are {list(events.columns)}")
    if events["event_id"].duplicated().any():
        errs.append("event_id not unique")
    if not events["t"].is_monotonic_increasing:
        errs.append("events not sorted by t")
    ties = events.groupby("t")["tie_rank"].apply(lambda s: sorted(s.tolist()) == list(range(len(s))))
    if not ties.all():
        errs.append("tie_rank is not 0..k-1 within equal t")
    obs = pd.DataFrame(observation, columns=["entity", "start", "end"]) if not isinstance(observation, pd.DataFrame) else observation
    if (obs["end"] <= obs["start"]).any():
        errs.append("observation interval with end <= start")
    ents = set(events["entity"])
    missing = ents - set(obs["entity"])
    if missing:
        errs.append(f"entities with events but no observation interval: {sorted(missing)}")
    # every event inside an observation interval of its entity
    for ent, g in events.groupby("entity"):
        iv = obs[obs.entity == ent]
        inside = np.zeros(len(g), bool)
        for s, e in zip(iv["start"], iv["end"]):
            inside |= (g["t"].values >= s) & (g["t"].values < e)
        if not inside.all():
            errs.append(f"{int((~inside).sum())} events of entity {ent} outside its observation intervals")
    gp = pd.DataFrame(gaps, columns=["entity", "type", "start", "end", "reason"]) if not isinstance(gaps, pd.DataFrame) else gaps
    if len(gp):
        if (gp["end"] <= gp["start"]).any():
            errs.append("gap with end <= start")
        for _, r in gp.iterrows():
            iv = obs[obs.entity == r.entity]
            if not ((iv["start"] <= r.start) & (iv["end"] >= r.end)).any():
                errs.append(f"gap {r.entity} [{r.start},{r.end}) not inside an observation interval")
                break
    for k in ("time_unit", "entity_key", "period", "system_wide_types", "tie_rule", "kind"):
        if k not in sidecar:
            errs.append(f"sidecar missing {k}")
    if errs:
        raise ValueError("contract violations:\n  " + "\n  ".join(errs))
    return True
