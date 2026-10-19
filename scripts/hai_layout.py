"""
HAI 21.03 (HIL-based Augmented ICS security dataset; Shin et al., KAIST/NSR), https://github.com/icsdataset/hai
— the layout isomorph uses. A real testbed: Emerson boiler (P1), GE turbine rotor kit (P2), FESTO water
treatment (P3), coupled by a dSPACE HIL simulator of steam-turbine and pumped-storage generation (P4).
1-second samples, 79 process points, 8 time-continuous files (3 normal, 5 with 50 attacks), 15.3 days in all;
declared here at 1-minute means (see load_files).

Entity candidates:
  process  P1 boiler / P2 turbine / P3 water treatment as units, each with its own roles (point names);
           P4 (the HIL simulator: load schedule, demand, output power, frequency deviation) is the common
           environment driving both boiler and turbine and is system-wide, like outdoor temperature and the
           setpoint schedule in the buildings
  sys      one entity, every point its own role
Roles shared by name across units where the quantity is the same kind: LIT01 (tank level, P1 and P3),
PIT01 (pressure, P1 and P3), FIT/FT flows are not shared (different conversions). Constant points and the
attack labels are excluded; labels become regime annotations.
"""
import numpy as np
import pandas as pd

SAMPLE_MIN = 1.0          # dataset declared at 1-minute means (source is 1 s; see load_files)

# points by process, with the technical-details description (hai_dataset_technical_details.pdf, HAI 21.03 column)
P1 = {  # boiler
    "B2004": "HX outlet pressure setpoint", "B2016": "pressure demand (thermal power control)", "B3004": "return tank level setpoint",
    "B3005": "return tank discharge flow setpoint", "B4002": "HX outlet temperature setpoint", "B4005": "temperature PID output",
    "B400B": "heating tank outflow setpoint", "B4022": "temperature demand (thermal power control)",
    "FCV01D": "FCV01 position command", "FCV01Z": "FCV01 position", "FCV02D": "FCV02 position command", "FCV02Z": "FCV02 position",
    "FCV03D": "FCV03 position command", "FCV03Z": "FCV03 position", "FT01": "return tank flow (mmH2O)", "FT01Z": "return tank inflow (l/h)",
    "FT02": "heating tank flow (mmH2O)", "FT02Z": "heating tank outflow (l/h)", "FT03": "return tank flow (mmH2O)", "FT03Z": "return tank outflow (l/h)",
    "LCV01D": "LCV01 position command", "LCV01Z": "LCV01 position", "LIT01": "return tank level", "PCV01D": "PCV01 position command",
    "PCV01Z": "PCV01 position", "PCV02D": "PCV02 position command", "PCV02Z": "PCV02 position", "PIT01": "HX outlet pressure",
    "PIT02": "heating pump supply pressure", "PP01AD": "main pump A start command", "PP01AR": "main pump A running", "PP01BD": "main pump B start command",
    "PP01BR": "main pump B running", "PP02D": "heating pump start command", "PP02R": "heating pump running", "STSP": "boiler DCS start/stop",
    "TIT01": "HX outlet temperature", "TIT02": "heating tank temperature",
}
P2 = {  # turbine
    "24Vdc": "DCS 24V", "ASD": "auto speed demand", "AutoGO": "auto start", "CO_rpm": "speed controller output", "Emerg": "emergency button",
    "HILout": "HIL output to turbine", "MSD": "manual speed demand", "ManualGO": "manual start", "OnOff": "turbine DCS on/off", "RTR": "rpm trip rate",
    "SIT01": "turbine rpm (probe 1)", "SIT02": "turbine rpm (probe 2)", "TripEx": "trip exit", "VT01": "key phasor phase lag",
    "VTR01": "vibration limit 1", "VTR02": "vibration limit 2", "VTR03": "vibration limit 3", "VTR04": "vibration limit 4",
    "VXT02": "shaft X displacement, wheel 1", "VXT03": "shaft X displacement, wheel 2", "VYT02": "shaft Y displacement, wheel 1", "VYT03": "shaft Y displacement, wheel 2",
}
P3 = {  # water treatment
    "FIT01": "inflow to upper tank", "LCP01D": "pump LCP01 speed command", "LCV01D": "valve LCV01 position command", "LH": "high level setpoint",
    "LIT01": "upper tank level", "LL": "low level setpoint", "PIT01": "inflow pressure",
}
P4 = {  # HIL simulator (system-wide)
    "HT_FD": "HTM frequency deviation", "HT_LD": "HTM load demand", "HT_PO": "HTM output power", "HT_PS": "HTM scheduled power",
    "LD": "total load demand", "ST_FD": "STM frequency deviation", "ST_GOV": "STM gate opening", "ST_LD": "STM load demand",
    "ST_PO": "STM output power", "ST_PS": "STM scheduled power", "ST_PT01": "STM steam pressure", "ST_TT01": "STM steam temperature",
}
PROCESSES = {"P1": P1, "P2": P2, "P3": P3}
BINARY = {"PP01AD", "PP01AR", "PP01BD", "PP01BR", "PP02D", "PP02R", "STSP", "AutoGO", "Emerg", "ManualGO", "OnOff", "TripEx"}

# Mechanisms true by construction from the point descriptions (cause -> effect, role names).
# D -> Z pairs (command -> position) and start -> running pairs respond within a second or two.
MECHANISMS = [
    dict(cause="FCV01D", effect="FCV01Z", note="valve command -> position (P1)"),
    dict(cause="FCV02D", effect="FCV02Z", note="valve command -> position (P1)"),
    dict(cause="FCV03D", effect="FCV03Z", note="valve command -> position (P1)"),
    dict(cause="LCV01D", effect="LCV01Z", note="valve command -> position (P1)"),
    dict(cause="PCV01D", effect="PCV01Z", note="valve command -> position (P1)"),
    dict(cause="PP01AD", effect="PP01AR", note="pump start command -> running (P1)"),
    dict(cause="PP02D", effect="PP02R", note="pump start command -> running (P1)"),
    dict(cause="LCV01Z", effect="LIT01", note="level control valve -> return tank level (P1)"),
    dict(cause="PCV01Z", effect="PIT01", note="pressure control valve -> HX outlet pressure (P1)"),
    dict(cause="B4005", effect="FCV03D", note="temperature PID output -> FCV03 command (P1)"),
    dict(cause="FCV03Z", effect="TIT01", note="FCV03 position -> HX outlet temperature (P1)"),
    dict(cause="LCP01D", effect="FIT01", note="pump speed command -> inflow (P3)"),
    dict(cause="FIT01", effect="LIT01", note="inflow -> upper tank level (P3)"),
    dict(cause="LCV01D", effect="LIT01", note="drain valve command -> upper tank level (P3)"),
    dict(cause="CO_rpm", effect="SIT01", note="speed controller output -> turbine rpm (P2)"),
]


def load_files(paths, resample_minutes=1):
    """Concatenate the time-continuous files in chronological order on a COMPRESSED time axis (minutes):
    each file starts where the previous ended, so unobserved stretches between files are removed; the
    boundaries are returned so they can be declared as missing-data gaps. Each file is first resampled to
    `resample_minutes` means (booleans: last value in the bin; attack flags: max) — the dataset is declared
    at 1-minute resolution: at 1 s the turbine's vibration and rpm channels (correlation times 7-40 s) emit
    ~1.5 million crossings in 15 days, texture of a rotating machine rather than structure, while the
    boiler and water-treatment dynamics act over 15-70 min. Returns (df, boundaries, files)."""
    parts = []
    for p in paths:
        d = pd.read_csv(p); d["time"] = pd.to_datetime(d["time"])
        bins = (d["time"] - d["time"].iloc[0]).dt.total_seconds() // (60 * resample_minutes)
        cols = [c for c in d.columns if c not in ("time",)]
        agg = {}
        for c in cols:
            base = c.split("_", 1)[1] if "_" in c else c
            if c.startswith("attack"): agg[c] = "max"
            elif base in BINARY: agg[c] = "last"
            else: agg[c] = "mean"
        g = d.groupby(bins)
        r = g.agg(agg); r["time"] = g["time"].first().values
        parts.append(r.reset_index(drop=True))
    parts.sort(key=lambda d: d.time.iloc[0])
    out, bounds, files, t0 = [], [], [], 0.0
    for d in parts:
        n = len(d)
        d = d.copy(); d["minute"] = t0 + np.arange(n) * SAMPLE_MIN
        files.append(dict(start_minute=float(t0), end_minute=float(t0 + n * SAMPLE_MIN), first=str(d.time.iloc[0]), last=str(d.time.iloc[-1]), rows=int(n)))
        t0 += n * SAMPLE_MIN
        bounds.append(t0); out.append(d)
    return pd.concat(out, ignore_index=True), bounds[:-1], files


def process_layout(df):
    """Entities P1/P2/P3 with role = point name; P4 system-wide; constant points dropped; kinds by name."""
    ents, kinds = {}, {}
    for proc, pts in PROCESSES.items():
        cols = {}
        for pt in pts:
            col = f"{proc}_{pt}"
            if col in df.columns and df[col].nunique(dropna=True) > 1:
                cols[pt] = col; kinds[pt] = "binary" if pt in BINARY else "continuous"
        ents[proc] = cols
    system = {}
    for pt in P4:
        col = f"P4_{pt}"
        if col in df.columns and df[col].nunique(dropna=True) > 1:
            system[pt] = col; kinds[pt] = "continuous"
    return dict(time="minute", entities=ents, system=system, kinds=kinds, observation={})


def regimes(df):
    """Attack episodes: list of (start, end, processes attacked)."""
    a = df["attack"].values.astype(int); ch = np.flatnonzero(np.diff(a) != 0) + 1
    starts = np.r_[0, ch]; ends = np.r_[ch, len(a)]
    out = []
    for s, e in zip(starts, ends):
        if a[s]:
            procs = [p for p in ("P1", "P2", "P3") if f"attack_{p}" in df.columns and df[f"attack_{p}"].values[s:e].max() > 0]
            out.append(dict(start=float(df.minute.values[s]), end=float(df.minute.values[e - 1] + SAMPLE_MIN), processes=procs))
    return out
