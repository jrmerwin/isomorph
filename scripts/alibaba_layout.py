"""
Alibaba cluster-trace-v2018, machine_usage (https://github.com/alibaba/clusterdata; OSS mirror, ~9 GB csv) — the
layout isomorph uses for dataset 10, the collection's first NEGATIVE CONTROL (METHOD section 6): resource usage of
~4,000 machines over 8 days at ~60-second samples; here a deterministic subsample of 200 machines (every 20th id)
as units, roles cpu, mem, net_in, net_out, disk_io — all percentages or normalised, so every role is dimensionless
and the dimension constraint of 3.12 maps nothing hard. No regulator: a cluster scheduler places jobs, nothing in
these columns closes a loop on another column. Declared prediction (section 6 / RUNBOOK v9): as a source into
TEP its structure cell is ≈ 0 (below 5 bit-H).

Declared at 1-minute means (the native step). Entity candidates: `machine` (200 units) and `sys` (one entity, every
column its own role) — 3.1 compares them as for any dataset.
"""
import os
import numpy as np
import pandas as pd

SAMPLE_MIN = 1.0
ROLES = {"cpu": "cpu_util_percent", "mem": "mem_util_percent", "net_in": "net_in", "net_out": "net_out", "disk_io": "disk_io_percent"}
DIMENSION = {r: None for r in ROLES}
MECHANISMS = []     # no key: a negative control has nothing true by construction


def load(raw_dir, resample_minutes=SAMPLE_MIN):
    d = pd.read_csv(os.path.join(raw_dir, "machine_usage_sub200.csv"))
    d["minute"] = (d.time_stamp // 60).astype(int)
    machines = sorted(d.machine_id.unique(), key=lambda m: int(m.split("_")[1]))
    grid = np.arange(d.minute.min(), d.minute.max() + 1)
    frames = []
    for role, col in ROLES.items():
        w = d.pivot_table(index="minute", columns="machine_id", values=col, aggfunc="mean").reindex(grid)
        w.columns = [f"{m}_{role}" for m in w.columns]; frames.append(w)
    out = pd.concat(frames, axis=1).reset_index(drop=True); out["minute"] = (grid - grid[0]) * resample_minutes
    return out, machines


def machine_layout(df, machines):
    ents, kinds = {}, {}
    for m in machines:
        cols = {r: f"{m}_{r}" for r in ROLES if f"{m}_{r}" in df.columns and df[f"{m}_{r}"].notna().any() and df[f"{m}_{r}"].nunique() > 1}
        if cols: ents[m] = cols; kinds.update({r: "continuous" for r in cols})
    return dict(time="minute", entities=ents, system={}, kinds=kinds, observation={})
