"""
TCLab (Arduino Temperature Control Lab; Hedengren, Park, Martin et al., BYU; https://apmonitor.com/heat.htm) —
the layout isomorph uses. A real kit: two transistor heaters (Q1, Q2, 0–100 % power) each with a thermistor on
it (T1, T2, °C), on one board, so each heater warms its own sensor strongly and the other weakly. 1-second
samples; sensor LSB 0.1 °C. Dataset 5 of the collection, the first of the Rosetta set: a thermal first-order loop.

The public recordings are short runs of the kit on different boards and in different rooms (10 min to 4 h):
open-loop step tests, and one closed-loop PID run that also carries the setpoint. They are concatenated in a
fixed order on a compressed time axis with every file boundary declared a gap (as HAI's files were), and the
dataset is declared at 5-second means (at 1 s successive readings differ by less than a sensor LSB, so the 1-s
series is quantisation texture; the heater-to-sensor time constant is 1–3 min).

Entity candidates:
  heater  h1 / h2 as units, each with roles Q (its heater power), T (its sensor), Tsp (its setpoint, closed-loop run only)
  sys     one entity, every column its own role
No system-wide roles: ambient temperature is not recorded.
"""
import os
import numpy as np
import pandas as pd

SAMPLE_SEC = 5
SAMPLE_MIN = SAMPLE_SEC / 60.0      # dataset declared at 5-second means; time unit is the minute

FILES = {   # provenance for the sidecar; concatenation order is the rule in load_files (longest recording first)
    "apm_do_dyn3.csv": "APMonitor dynamic optimisation course: 4-h heater-1 step sequence (sensor 2 absent, T2 = 0)",
    "apm_pds_data6.csv": "APMonitor process data science course: 1-h heater-1 step sequence, both sensors",
    "byu_prism_pid_train.csv": "BYU PRISM Transformer_MPC: 90-min closed-loop PID run on heater 1 with setpoint (no time column; 1 s assumed)",
    "apm_do_dyn2.csv": "APMonitor dynamic optimisation course: 10-min two-heater step test (columns H1, H2)",
    "apm_pdc_data2.csv": "APMonitor process dynamics and control course: 10-min two-heater step test",
    "apm_pdc_data3.csv": "APMonitor process dynamics and control course: 10-min heater-1 step test, both sensors",
    "apm_pdc_data4.csv": "APMonitor process dynamics and control course: 14-min step test",
    "apm_pds_data5.csv": "APMonitor process data science course: 10-min step test",
    "kantor_cbe30338.csv": "Kantor, CBE 30338 (Notre Dame): 13-min step test",
}
COLUMNS = ["Q1", "Q2", "T1", "T2", "Tsp1", "Tsp2"]
RENAME = {"time": "Time", "H1": "Q1", "H2": "Q2", "Q": "Q1", "T": "T1", "Tsp": "Tsp1"}

# Mechanisms true by construction (heater -> its own sensor; setpoint -> PID output -> sensor in the closed-loop run).
MECHANISMS = [
    dict(cause="Q", effect="T", note="heater power -> its own sensor temperature (first-order lag, 1-3 min)"),
    dict(cause="Tsp", effect="Q", note="setpoint -> PID heater output (closed-loop run only)"),
    dict(cause="Tsp", effect="T", note="setpoint -> sensor temperature through the loop (closed-loop run only)"),
]

# Dimensions (v5 suffix): heater power is a percentage (dimensionless); temperatures and setpoints are <Θ>.
DIMENSION = {"Q": None, "T": "temperature", "Tsp": "temperature"}


def load_files(raw_dir, resample_sec=SAMPLE_SEC):
    """Concatenate the recordings, longest first, on a COMPRESSED time axis (minutes): each file starts where the
    previous ended; the boundaries are returned so they can be declared as missing-data gaps. Each file is first
    binned to `resample_sec` means. Columns a file lacks, and columns constant within a file (an absent sensor
    reads 0; an unused heater reads 0), are NaN for that file. Returns (df, boundaries, files)."""
    loaded = []
    for fn, note in FILES.items():
        p = os.path.join(raw_dir, fn)
        if not os.path.exists(p): continue
        d = pd.read_csv(p).rename(columns=RENAME)
        if "Time" not in d.columns: d["Time"] = np.arange(len(d), dtype=float)
        loaded.append((fn, note, d))
    loaded.sort(key=lambda x: (-len(x[2]), x[0]))      # rule: longest recording first, ties by name (the files have no common clock)
    out, bounds, files, t0 = [], [], [], 0.0
    for fn, note, d in loaded:
        for c in COLUMNS:
            if c not in d.columns: d[c] = np.nan
            elif d[c].nunique(dropna=True) <= 1: d[c] = np.nan
        bins = (d["Time"] // resample_sec).astype(int)
        r = d.groupby(bins)[COLUMNS].mean().reset_index(drop=True)
        n = len(r); r["minute"] = t0 + np.arange(n) * SAMPLE_MIN
        present = [c for c in COLUMNS if r[c].notna().any()]
        files.append(dict(file=fn, note=note, start_minute=float(t0), end_minute=float(t0 + n * SAMPLE_MIN), rows=int(n), columns=present))
        t0 += n * SAMPLE_MIN; bounds.append(t0); out.append(r)
    return pd.concat(out, ignore_index=True), bounds[:-1], files


def heater_layout(df):
    """Entities h1/h2 with roles Q, T (and Tsp where a setpoint was recorded); kinds continuous."""
    ents, kinds = {}, {}
    for h in (1, 2):
        cols = {}
        for role, col in (("Q", f"Q{h}"), ("T", f"T{h}"), ("Tsp", f"Tsp{h}")):
            if col in df.columns and df[col].notna().any():
                cols[role] = col; kinds[role] = "continuous"
        ents[f"h{h}"] = cols
    return dict(time="minute", entities=ents, system={}, kinds=kinds, observation={})


def absent_stretches(df, files, layout):
    """(entity, start, end, reason) for every file in which an entity has no data at all (sensor absent)."""
    out = []
    for f in files:
        for ent, cols in layout["entities"].items():
            if not any(c in f["columns"] for c in cols.values()):
                out.append((ent, f["start_minute"], f["end_minute"], f"{f['file']}: no data for {ent}"))
    return out
