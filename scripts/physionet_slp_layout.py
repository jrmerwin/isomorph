"""
MIT-BIH Polysomnographic Database (slpdb 1.0.0; Ichimaru & Moody 1999; https://physionet.org/content/slpdb/) —
the layout isomorph uses. 18 overnight records of 16 subjects (men, 32–56 y, under evaluation for sleep apnea)
at 250 Hz: ECG with beat annotations (.ecg), invasive radial-artery blood pressure, one or two respiration
channels (nasal thermistor, chest/abdominal effort or their sum), EEG, and in five records SV and SO2; sleep
stages and apnea events annotated every 30 s (.st). ~89 h in all. Dataset 7 of the collection, the physiological
member of the Rosetta set: the baroreflex (pressure -> heart rate -> pressure) as a return in flesh.

Declared at 0.25-second samples (v2; the v1 card was at 1 s). Beat-level quantities — heart rate from the beat annotations, systolic and
diastolic pressure as the maximum and minimum of the arterial waveform between successive beats — are
interpolated linearly to the 1-s grid (the usual beat-to-beat resampling); respiration is the 1-s mean of the
waveform (uncalibrated, dimensionless); SO2 the 1-s mean where recorded. Implausible beats (RR outside 0.3–2 s)
and pressures (outside 40–250 mmHg) are missing. EEG, EOG, EMG and SV are not cardiorespiratory regulator
quantities and are left out.

Entity candidates:
  record  each overnight record as a unit with roles HR, SBP, DBP, RESP (and SO2 where recorded)
  sys     one entity, every column its own role
Records are concatenated on a compressed time axis (different nights), boundaries as gaps.
"""
import os
import numpy as np
import pandas as pd

SAMPLE_SEC = 0.25           # v2 card (2026-10-21): 0.25-s samples; at 1 s a 4-s breathing wave has acf(1) ~ 0 and the noise floor erases it
SAMPLE_MIN = SAMPLE_SEC / 60.0
FS = 250
BEAT_SYMBOLS = set("NLRBAaJSVrFejnE/fQ?")       # wfdb beat annotation symbols; everything else is a non-beat marker
ROLES = {"HR": "frequency", "SBP": "pressure", "DBP": "pressure", "RESP": None, "SO2": None}
RESP_PREFERENCE = ("Resp (nasal)", "Resp (sum)", "Resp (abdominal)", "Resp (abdomen)", "Resp (chest)")
STAGES = {"W": "awake", "1": "stage 1", "2": "stage 2", "3": "stage 3", "4": "stage 4", "R": "REM"}
EVENTS = {"H": "hypopnea", "HA": "hypopnea with arousal", "OA": "obstructive apnea", "X": "obstructive apnea with arousal",
          "CA": "central apnea", "CAA": "central apnea with arousal", "L": "leg movements", "LA": "leg movements with arousal",
          "A": "arousal", "MT": "movement time"}

# Mechanisms true by physiology (cause -> effect, role names). The baroreflex closes within one or two beats; the
# respiratory couplings act within a breath (3–5 s).
MECHANISMS = [
    dict(cause="SBP", effect="HR", note="baroreflex: a rise in arterial pressure slows the heart within 1-2 beats"),
    dict(cause="HR", effect="SBP", note="heart rate -> cardiac output -> arterial pressure"),
    dict(cause="RESP", effect="HR", note="respiratory sinus arrhythmia: inspiration speeds the heart"),
    dict(cause="RESP", effect="SBP", note="respiratory modulation of arterial pressure (intrathoracic pressure)"),
    dict(cause="RESP", effect="SO2", note="apnea -> desaturation, tens of seconds later (records with SO2 only)"),
]
DIMENSION = dict(ROLES)


def read_record(raw_dir, rec):
    """One record -> (df at 1-s with columns HR, SBP, DBP, RESP[, SO2], 'sec'), stage epochs, apnea events."""
    import wfdb
    p = os.path.join(raw_dir, rec)
    r = wfdb.rdrecord(p)
    sig = r.p_signal; names = list(r.sig_name)
    n_sec = int(np.ceil(r.sig_len / (FS * SAMPLE_SEC)))          # number of samples at the declared step
    out = pd.DataFrame(dict(sec=np.arange(n_sec, dtype=float) * SAMPLE_SEC))
    # beats -> HR, SBP, DBP on the beat grid, then to 1 s
    ann = wfdb.rdann(p, "ecg")
    beats = np.array([s for s, sym in zip(ann.sample, ann.symbol) if sym in BEAT_SYMBOLS], float)
    t_beat = beats / FS
    rr = np.diff(t_beat)
    hr = np.where((rr >= 0.3) & (rr <= 2.0), 60.0 / rr, np.nan)          # at the second beat of each interval
    bp = sig[:, names.index("BP")] if "BP" in names else None
    sbp = np.full(len(rr), np.nan); dbp = np.full(len(rr), np.nan)
    if bp is not None:
        for i in range(len(rr)):
            a, b = int(beats[i]), int(beats[i + 1])
            if b > a:
                w = bp[a:b]
                if np.isfinite(w).any():
                    sbp[i], dbp[i] = np.nanmax(w), np.nanmin(w)
        bad = ~((sbp >= 40) & (sbp <= 250) & (dbp >= 20) & (dbp <= 200)); sbp[bad] = np.nan; dbp[bad] = np.nan
    tb = t_beat[1:]
    grid = out.sec.values + SAMPLE_SEC / 2
    for col, v in (("HR", hr), ("SBP", sbp), ("DBP", dbp)):
        ok = np.isfinite(v)
        out[col] = np.interp(grid, tb[ok], v[ok], left=np.nan, right=np.nan) if ok.sum() > 2 else np.nan
        # no beat within 2 s of a grid point -> missing (interpolation across a dropout is not a measurement)
        if ok.sum() > 2:
            idx = np.searchsorted(tb[ok], grid); lo = np.clip(idx - 1, 0, ok.sum() - 1); hi = np.clip(idx, 0, ok.sum() - 1)
            far = np.minimum(np.abs(grid - tb[ok][lo]), np.abs(tb[ok][hi] - grid)) > 2.0
            out.loc[far, col] = np.nan
    # waveform channels -> 1-s means
    def mean_1s(x):   # mean of the waveform within each declared step (a step of 0.25 s is 62.5 samples: binned by time)
        idx = np.floor(np.arange(len(x)) / (FS * SAMPLE_SEC)).astype(int)
        m = np.full(n_sec, np.nan); sums = np.bincount(idx, weights=x, minlength=n_sec)[:n_sec]; cnt = np.bincount(idx, minlength=n_sec)[:n_sec]
        ok = cnt > 0; m[ok] = sums[ok] / cnt[ok]
        return m
    resp_ch = next((c for c in RESP_PREFERENCE if c in names), None)
    out["RESP"] = mean_1s(sig[:, names.index(resp_ch)]) if resp_ch else np.nan
    out["SO2"] = mean_1s(sig[:, names.index("SO2")]) if "SO2" in names else np.nan
    if "SO2" in names: out.loc[(out.SO2 < 50) | (out.SO2 > 100), "SO2"] = np.nan
    # sleep stages and events (30-s epochs)
    st = wfdb.rdann(p, "st")
    stages, events = [], []
    for s, note in zip(st.sample, st.aux_note):
        toks = note.strip().split()
        if not toks: continue
        t0 = s / FS
        if toks[0] in STAGES: stages.append((t0, t0 + 30.0, STAGES[toks[0]]))
        for e in toks[1:] if toks[0] in STAGES else toks:
            if e in EVENTS: events.append((t0, t0 + 30.0, EVENTS[e]))
    meta = dict(record=rec, seconds=n_sec, channels=names, resp_channel=resp_ch, beats=int(len(beats)), comments=r.comments)
    return out, stages, events, meta


def load_records(raw_dir, records=None):
    """All records on a COMPRESSED axis in minutes (each starts where the previous ended); boundaries, regimes, files."""
    recs = records or [l.strip() for l in open(os.path.join(raw_dir, "RECORDS")) if l.strip()]
    out, bounds, files, regimes, t0s = [], [], [], [], 0          # offset kept in whole seconds: minute = (offset + sec) / 60 exactly
    for rec in recs:
        if not os.path.exists(os.path.join(raw_dir, rec + ".dat")): continue
        d, stages, events, meta = read_record(raw_dir, rec)
        n = len(d); d = d.copy(); t0 = t0s / 60.0; d["minute"] = (t0s + d.sec.values) / 60.0      # t0s in whole seconds
        cols = [c for c in ROLES if c in d.columns and d[c].notna().any()]
        for c in ROLES:
            if c in d.columns and c not in cols: d[c] = np.nan
        d = d.rename(columns={c: f"{rec}_{c}" for c in ROLES})
        files.append(dict(file=rec, start_minute=float(t0), end_minute=float(t0 + n * SAMPLE_MIN), rows=int(n), roles=cols, **meta))
        def _runs(items):
            runs = []
            for s, e, lab in sorted(items):
                if runs and runs[-1][2] == lab and abs(runs[-1][1] - s) < 0.1: runs[-1][1] = e   # epochs are stamped a few ms apart
                else: runs.append([s, e, lab])
            return runs
        for s, e, lab in _runs(stages): regimes.append(dict(record=rec, kind="stage", label=lab, start=float(t0 + s / 60), end=float(t0 + e / 60)))
        for s, e, lab in _runs(events): regimes.append(dict(record=rec, kind="event", label=lab, start=float(t0 + s / 60), end=float(t0 + e / 60)))
        t0s += int(np.ceil(n * SAMPLE_SEC)); bounds.append(t0s / 60.0); out.append(d.drop(columns=["sec"]))
    df = pd.concat(out, ignore_index=True)
    return df, bounds[:-1], files, regimes


def record_layout(df, files):
    """Entities = records; roles HR, SBP, DBP, RESP, SO2 where recorded; each record observed on its own stretch."""
    ents, obs, kinds = {}, {}, {}
    for f in files:
        cols = {r: f"{f['file']}_{r}" for r in f["roles"]}
        ents[f["file"]] = cols; obs[f["file"]] = (f["start_minute"], f["end_minute"])
        for r in cols: kinds[r] = "continuous"
    return dict(time="minute", entities=ents, system={}, kinds=kinds, observation=obs)
