"""
Canonical data contract (METHOD.md section 2).

A dataset directory holds:
  events.csv       event_id, t, entity, type, value, tie_rank
  observation.csv  entity, start, end            (intervals an entity was observed)
  gaps.csv         entity, type, start, end, reason   (missing-data intervals; type "" = all types)
  sidecar.json     time_unit, entity_key, period, system_wide_types, tie_rule, kind, origin, ...
  answer_key.json  optional

`type` on a gap is a v1 clarification of the contract: a dropout on one sensor
is recorded against that sensor's event types rather than widened to the whole
entity. An empty type means the whole entity.
"""
import json
import os
import numpy as np
import pandas as pd

EVENT_COLUMNS = ["event_id", "t", "entity", "type", "value", "tie_rank"]
SYSTEM = "ALL"


def canonical_tie_rank(df):
    """tie_rank = rank within equal t by (entity, type), lexicographic."""
    df = df.sort_values(["t", "entity", "type"], kind="stable").reset_index(drop=True)
    df["tie_rank"] = df.groupby("t").cumcount()
    return df


def make_events(rows, tie_rule="canonical"):
    """rows: iterable of dicts with t, entity, type, value (optional), source_order (optional)."""
    df = pd.DataFrame(rows)
    df["t"] = df["t"].astype(float).round(9)     # ties are ranked on the time as written: nine decimals of the time unit survive the csv round trip exactly
    if "value" not in df:
        df["value"] = np.nan
    if tie_rule == "source" and "source_order" in df:
        df = df.sort_values(["t", "source_order"], kind="stable").reset_index(drop=True)
        df["tie_rank"] = df.groupby("t").cumcount()
    else:
        df = canonical_tie_rank(df)
    df["event_id"] = np.arange(len(df))
    return df[EVENT_COLUMNS]


def runs_of(mask, t):
    """Contiguous True runs of a boolean array over times t -> list of (start, end)."""
    out, start = [], None
    for i, m in enumerate(mask):
        if m and start is None:
            start = t[i]
        if not m and start is not None:
            out.append((start, t[i])); start = None
    if start is not None:
        out.append((start, t[-1] + (t[1] - t[0] if len(t) > 1 else 1)))
    return out


def write_dataset(outdir, events, observation, gaps, sidecar, answer_key=None):
    os.makedirs(outdir, exist_ok=True)
    events.to_csv(os.path.join(outdir, "events.csv"), index=False)
    pd.DataFrame(observation, columns=["entity", "start", "end"]).to_csv(os.path.join(outdir, "observation.csv"), index=False)
    pd.DataFrame(gaps, columns=["entity", "type", "start", "end", "reason"]).to_csv(os.path.join(outdir, "gaps.csv"), index=False)
    json.dump(sidecar, open(os.path.join(outdir, "sidecar.json"), "w"), indent=1)
    if answer_key is not None:
        json.dump(answer_key, open(os.path.join(outdir, "answer_key.json"), "w"), indent=1)


def read_dataset(d):
    ev = pd.read_csv(os.path.join(d, "events.csv"))
    ev["type"] = ev["type"].astype(str); ev["entity"] = ev["entity"].astype(str)
    obs = pd.read_csv(os.path.join(d, "observation.csv"))
    gaps = pd.read_csv(os.path.join(d, "gaps.csv"), keep_default_na=False) if os.path.getsize(os.path.join(d, "gaps.csv")) > 0 else pd.DataFrame(columns=["entity", "type", "start", "end", "reason"])
    side = json.load(open(os.path.join(d, "sidecar.json")))
    key_path = os.path.join(d, "answer_key.json")
    key = json.load(open(key_path)) if os.path.exists(key_path) else None
    return ev, obs, gaps, side, key


# ------------------------------------------------------------------ building adapters
def crossings(x, thresholds, debounce=3):
    """Debounced threshold crossings on a sampled series (NaN breaks the state). Run-length
    implementation: a change of side counts when the new side persists for `debounce` samples;
    identical to the per-sample scan of v1.0, 100x faster on second-resolution data."""
    x = np.asarray(x, float); n = len(x)
    ev = []
    if n == 0: return ev
    nan = np.isnan(x)
    for th in thresholds:
        state = np.where(nan, -1, (x > th).astype(int))        # -1 nan, 0 below, 1 above
        change = np.flatnonzero(np.diff(state) != 0) + 1
        starts = np.r_[0, change]; ends = np.r_[change, n]
        side = None
        for a, b in zip(starts, ends):
            v = state[a]
            if v == -1:
                side = None; continue
            if side is None:
                side = v; continue
            if v != side and b - a >= debounce:
                ev.append((int(a), f"{'up' if v else 'down'}{th}", float(x[a]))); side = v
    ev.sort()
    return ev


def from_building_frame(df, zones, thresholds, switches, late_zone=None, late_start_day=None,
                        dropout_vars=(), scramble=None):
    """Symbolize a building simulation frame into the canonical contract.
    thresholds: {"T": [..], "CO2": [..], "RH": [..], "T_out": [..], "vibration": [..]}
    switches: per-zone binary columns, e.g. ("heater", "vent", "window") or with "dehum".
    scramble: optional dict mapping true type -> opaque code and zone -> opaque code."""
    rows = []
    minute = df["minute"].values
    def add(i, entity, typ, value):
        rows.append(dict(t=float(minute[i]), entity=entity, type=typ, value=float(value)))
    for z in zones:
        for sw in switches:
            col = f"{sw}_{z}"
            if col not in df:
                continue
            x = df[col].values
            for i in np.where((x[1:] == 1) & (x[:-1] == 0))[0] + 1: add(i, z, f"{sw}:on", 1)
            for i in np.where((x[1:] == 0) & (x[:-1] == 1))[0] + 1: add(i, z, f"{sw}:off", 0)
        occ = df[f"occ_{z}"].values; d = np.diff(occ)
        for i in np.where(d > 0)[0] + 1:
            for _ in range(int(d[i - 1])): add(i, z, "occ:arrive", occ[i])
        for i in np.where(d < 0)[0] + 1:
            for _ in range(int(-d[i - 1])): add(i, z, "occ:leave", occ[i])
        for var in ("T", "CO2", "RH"):
            for i, e, v in crossings(df[f"{var}_{z}"].values, thresholds[var]): add(i, z, f"{var}:{e}", v)
    sp = df["setpoint"].values; d = np.diff(sp)
    for i in np.where(d > 0)[0] + 1: add(i, SYSTEM, "setpoint:up", sp[i])
    for i in np.where(d < 0)[0] + 1: add(i, SYSTEM, "setpoint:down", sp[i])
    for var in ("T_out", "vibration"):
        for i, e, v in crossings(df[var].values, thresholds[var]): add(i, SYSTEM, f"{var}:{e}", v)
    # observation intervals
    t0, t1 = float(minute[0]), float(minute[-1] + 1)
    observation = []
    for z in zones:
        if z == late_zone:
            observation.append((z, float(late_start_day * 1440), t1))
        else:
            observation.append((z, t0, t1))
    observation.append((SYSTEM, t0, t1))
    # gaps: NaN runs on dropout variables, scoped to that variable's event types
    gaps = []
    for col in dropout_vars:
        var, z = col.rsplit("_", 1)
        x = df[col].values
        mask = np.isnan(x)
        if z == late_zone:
            mask = mask & (df["day"].values >= late_start_day)
        for s, e in runs_of(mask, minute.astype(float)):
            for th in thresholds[var]:
                gaps.append((z, f"{var}:up{th}", s, e, "dropout")); gaps.append((z, f"{var}:down{th}", s, e, "dropout"))
    events = make_events(rows)
    # the contract: an entity has no events outside its observation intervals (an uninstrumented
    # zone's switches may toggle in the simulator, but nobody recorded them)
    keep = np.zeros(len(events), bool)
    for ent, s, e in observation:
        keep |= (events.entity.values == ent) & (events.t.values >= s) & (events.t.values < e)
    events = events[keep].reset_index(drop=True)
    events["event_id"] = np.arange(len(events))
    if scramble:
        events["type"] = events["type"].map(lambda t: scramble["type"].get(t, t))
        events["entity"] = events["entity"].map(lambda z: scramble["entity"].get(z, z))
        observation = [(scramble["entity"].get(z, z), s, e) for z, s, e in observation]
        gaps = [(scramble["entity"].get(z, z), scramble["type"].get(t, t), s, e, r) for z, t, s, e, r in gaps]
    return events, observation, gaps
