"""
Fingrid open data (https://data.fingrid.fi, CC BY 4.0) — the layout isomorph uses for dataset 9: frequency regulation
of the Nordic synchronous area as seen from Finland, 2024-07-01 to 2025-07-01. The Rosetta member whose measured
quantity is ⟨T⁻¹⟩ and whose loop is the whole synchronous grid: frequency falls, reserve activates, frequency recovers.

Series: 177 frequency (Hz, 3 min); 343 / 344 FCR-N activated down / up (MW, 15 min); 349 / 350 aFRR energy
activation up / down (MW, 15 min); 194 net import / export of electricity (MW, 3 min). Declared at 3-minute samples
(the frequency's and the net transfer's native interval); the 15-minute reserve series are held within their
quarter on the 3-minute grid (a value observed over a quarter is the value at every sample in it).

Entity: the synchronous area is one system with one copy of every role, so 3.1 has one candidate (`grid`) and the
card says so. No system-wide roles besides the entity itself; no gaps declared (missing samples are missing values).
"""
import os, glob
import numpy as np
import pandas as pd

SAMPLE_MIN = 3.0
SERIES = {"f": (177, "frequency"), "fcrn_down": (343, "power"), "fcrn_up": (344, "power"), "afrr_up": (349, "power"), "afrr_down": (350, "power"), "net_ie": (194, "power")}
DIMENSION = {r: d for r, (_, d) in SERIES.items()}

# Mechanisms true by construction of frequency containment and restoration: a deviation activates the reserve, the
# reserve moves the frequency back. Direction is cause -> effect in role names (the key counts any symbol direction).
MECHANISMS = [
    dict(cause="f", effect="fcrn_up", note="frequency below 50 Hz -> FCR-N up-regulation activates (seconds; seen at 3-15 min)"),
    dict(cause="f", effect="fcrn_down", note="frequency above 50 Hz -> FCR-N down-regulation activates"),
    dict(cause="f", effect="afrr_up", note="sustained deviation -> aFRR up activation (minutes)"),
    dict(cause="f", effect="afrr_down", note="sustained deviation -> aFRR down activation"),
    dict(cause="fcrn_up", effect="f", note="up-regulation -> frequency recovers (the loop closing)"),
    dict(cause="fcrn_down", effect="f", note="down-regulation -> frequency recovers"),
    dict(cause="net_ie", effect="f", note="a change in net import/export -> area imbalance -> frequency"),
]


def _read(raw_dir, ds):
    p = sorted(glob.glob(os.path.join(raw_dir, f"{ds}_*.csv")))
    if not p: return None
    d = pd.read_csv(p[-1], sep=";")
    d["t"] = pd.to_datetime(d["startTime"], utc=True); d["value"] = pd.to_numeric(d["value"], errors="coerce")
    return d.drop_duplicates("t").set_index("t")["value"].sort_index()


def load_year(raw_dir, resample_minutes=SAMPLE_MIN):
    """One frame on the 3-minute grid from the first to the last frequency sample; columns grid_<role>."""
    f = _read(raw_dir, 177)
    grid = pd.date_range(f.index.min().floor("3min"), f.index.max().ceil("3min"), freq=f"{int(resample_minutes)}min", inclusive="left")
    out = pd.DataFrame(index=grid)
    for role, (ds, _) in SERIES.items():
        s = _read(raw_dir, ds)
        if s is None: continue
        step = s.index.to_series().diff().dt.total_seconds().median()
        if step and step > resample_minutes * 60:   # 15-min reserves: held within their interval (forward fill, at most one interval)
            out[f"grid_{role}"] = s.reindex(s.index.union(grid)).ffill(limit=int(step / 60 / resample_minutes)).reindex(grid).values
        else:                                        # 3-min series: on the grid as recorded
            out[f"grid_{role}"] = s.reindex(grid).values
    out = out.reset_index(drop=True); out["minute"] = np.arange(len(out)) * resample_minutes
    return out, dict(start=str(grid[0]), end=str(grid[-1]))


def grid_layout(df):
    cols = {r: f"grid_{r}" for r in SERIES if f"grid_{r}" in df.columns and df[f"grid_{r}"].notna().any()}
    return dict(time="minute", entities={"grid": cols}, system={}, kinds={r: "continuous" for r in cols}, observation={})
