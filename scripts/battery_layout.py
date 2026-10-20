"""
NASA Ames PCoE Battery Data Set (Saha & Goebel 2007; https://data.nasa.gov/dataset/li-ion-battery-aging-datasets),
group FY08Q4 — the layout isomorph uses. Four 18650 Li-ion cells cycled to end of life at 24 °C ambient:
B0005, B0006, B0007 together (April–May 2008; 170 charge, 168 discharge cycles each) and B0018 alone
(July–August 2008; 134 / 132). A charge is 1.5 A constant current to 4.2 V, then constant voltage until the
current falls to 20 mA (~2 h); a discharge is 2 A constant current to a cell-specific cutoff voltage (~1 h).
Impedance cycles (EIS) carry no time series of the same kind and are left out. Dataset 6 of the collection, the
electrochemical member of the Rosetta set: current (ACT) -> voltage and temperature, the analogue of filling a tank.

Samples arrive every 3–20 s within a cycle; the dataset is declared at 1-minute means on a COMPRESSED time axis
(every unobserved stretch — rests, impedance tests, the gap between the two campaigns — removed and declared a gap).

Entity candidates:
  cell  B0005 / B0006 / B0007 / B0018 as units, each with roles V (terminal voltage), I (current), T (cell temperature)
  sys   one entity, every column its own role
"""
import os
from datetime import datetime
import numpy as np
import pandas as pd

SAMPLE_MIN = 1.0
CELLS = ["B0005", "B0006", "B0007", "B0018"]
ROLES = {"V": "Voltage_measured", "I": "Current_measured", "T": "Temperature_measured"}
EPOCH = datetime(2008, 1, 1)

MECHANISMS = [
    dict(cause="I", effect="V", note="current step -> terminal voltage (ohmic drop plus polarisation)"),
    dict(cause="I", effect="T", note="current -> cell temperature (resistive heating)"),
    dict(cause="V", effect="I", note="voltage reaching 4.2 V -> current taper (constant-voltage phase of a charge)"),
]
DIMENSION = {"V": "voltage", "I": "current", "T": "temperature"}


def _stamp(v):
    y, mo, d, h, mi, s = [float(x) for x in v]
    return datetime(int(y), int(mo), int(d), int(h), int(mi)) .timestamp() + s


def load_cells(paths, resample_minutes=1):
    """Read the .mat files, bin every charge/discharge cycle to `resample_minutes` means on the real clock, pivot
    to one row per minute with columns <cell>_<role>, then compress the axis. Returns (df, boundaries, cycles)."""
    from scipy.io import loadmat
    frames, cycles = [], []
    for p in paths:
        name = os.path.basename(p)[:-4]
        rec = loadmat(p, simplify_cells=True)[name]["cycle"]
        for i, c in enumerate(rec):
            if c["type"] not in ("charge", "discharge"): continue
            d = c["data"]; t = np.asarray(d["Time"], float)
            if t.ndim == 0 or len(t) < 2: continue
            abs_min = (_stamp(c["time"]) - EPOCH.timestamp()) / 60.0 + t / 60.0
            f = pd.DataFrame({r: np.asarray(d[col], float) for r, col in ROLES.items()})
            f["bin"] = np.floor(abs_min / resample_minutes).astype(int)
            g = f.groupby("bin")[list(ROLES)].mean(); g["cell"] = name
            frames.append(g.reset_index())
            cap = d.get("Capacity") if c["type"] == "discharge" else None
            cycles.append(dict(cell=name, index=int(i), type=c["type"], start_abs_min=float(abs_min[0]), end_abs_min=float(abs_min[-1]),
                               samples=int(len(t)), capacity_Ah=(None if cap is None else float(np.ravel(cap)[0]))))
    allf = pd.concat(frames, ignore_index=True)
    wide = allf.pivot_table(index="bin", columns="cell", values=list(ROLES), aggfunc="mean")
    wide.columns = [f"{cell}_{role}" for role, cell in wide.columns]
    wide = wide.sort_index()
    bins = wide.index.values
    minute = np.arange(len(bins)) * SAMPLE_MIN
    jumps = np.flatnonzero(np.diff(bins) > 1) + 1          # the compressed minute at which a new observed stretch begins
    bounds = [float(minute[j]) for j in jumps]
    wide = wide.reset_index(drop=True); wide["minute"] = minute; wide["real_minute"] = bins * float(resample_minutes)
    return wide, bounds, cycles


def cell_layout(df):
    """Entities = cells with roles V, I, T; each cell observed from its first to its last recorded minute."""
    ents, obs = {}, {}
    for cell in CELLS:
        cols = {r: f"{cell}_{r}" for r in ROLES if f"{cell}_{r}" in df.columns and df[f"{cell}_{r}"].notna().any()}
        if not cols: continue
        ents[cell] = cols
        seen = df.index[df[list(cols.values())].notna().any(axis=1)]
        obs[cell] = (float(df.minute.iloc[seen[0]]), float(df.minute.iloc[seen[-1]] + SAMPLE_MIN))
    return dict(time="minute", entities=ents, system={}, kinds={r: "continuous" for r in ROLES}, observation=obs)
