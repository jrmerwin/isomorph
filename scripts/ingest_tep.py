"""
Dataset 3: Tennessee Eastman, continuous 1-year run (Souza et al. 2023; Ricker's revised model).

    python3 scripts/fetch_tep.sh            # clones the source repo and copies the raw csv
    python3 scripts/ingest_tep.py           # choices (3.1, 3.2) + canonical dataset

Declared span: the FIRST 120 DAYS of the run (57,600 samples at 3 min). That is the scale the method
was calibrated at (buildings: 60 days) and keeps the choice stage tractable; days 120-365 are kept
untouched as a continuation for the open item on online refitting. The fault label STATUS is not an
observed variable: it is excluded from the events and written to the sidecar as regime annotations.
"""
import os, sys, json, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT); sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
import pandas as pd
import tep_layout as L
from isomorph.choose.symbolize import choose_symbolization, write_chosen_dataset
from isomorph.choose.entity import choose_entity, sys_layout

RAW = os.path.join(ROOT, "datasets/tennessee_eastman/raw/matlab_data_1year.csv")
OUT = os.path.join(ROOT, "datasets/tennessee_eastman")
DAYS = 120

df_full = L.load(RAW)
df = df_full.iloc[: int(DAYS * 1440 / L.SAMPLE_MIN)].reset_index(drop=True)
print(f"TEP: {len(df_full)} samples in file; using the first {DAYS} days = {len(df)} samples")
lay = L.vessel_layout()

t0 = time.time()
print("== symbolization by compression (3.2: faithfulness + noise floors, total confirmation bits) ==")
choice, thresholds, trace = choose_symbolization(df, lay)
print("chosen:", {k: v for k, v in choice.items()}); print(f"({time.time()-t0:.0f}s)")

print("\n== entity by compression (3.1) ==")
best, scores = choose_entity(df, {"vessel": lay, "sys": sys_layout(lay)}, choice)
print("chosen entity layout:", best)
os.makedirs(os.path.join(OUT, "out"), exist_ok=True)
json.dump(dict(days=DAYS, choice=choice, thresholds=thresholds, trace=trace, entity=best, entity_scores=scores),
          open(os.path.join(OUT, "out", "choices_v1.json"), "w"), indent=1, default=str)

layout_used = lay if best == "vessel" else sys_layout(lay)
ch = choice if best == "vessel" else {r: choice.get(next((b for b in choice if r == b or r.startswith(b + "_")), r)) for r in layout_used["kinds"]}
reg = [r for r in L.regimes(df_full) if r["start"] < DAYS * 1440]
extra = dict(time_unit="minute", sample_minutes=L.SAMPLE_MIN, entity_key=best,
             regimes=reg, regime_note="STATUS fault label per episode (IDV 0..20); not an observed variable, not in the events",
             source="https://github.com/anasouzac/new_tep_datasets matlab_data_1year.csv (Souza, de Souza & da Silva 2023), Ricker revised TEP model",
             span_note=f"first {DAYS} days of a 365-day run; days {DAYS}-365 held as a continuation",
             omitted_columns=["XMV(5)", "XMV(9)", "STATUS"], variables=dict(vessels=L.VESSELS, system=L.SYSTEM_ROLES))
ev = write_chosen_dataset(df, layout_used, ch, OUT, sidecar_extra=extra, kind="simulated plant (Tennessee Eastman)",
                          origin="scripts/ingest_tep.py")
json.dump(dict(mechanisms=[dict(cause=m["cause"], effect=m["effect"], note=m["note"]) for m in L.MECHANISMS],
               note="actuator -> measurement pairs true by construction (Downs & Vogel variable table); role names, any lag class; "
                    "flow loops respond within one 3-min sample and are expected to be invisible to strictly-positive-gap contexts",
               faults=L.FAULTS, match="role_prefix"),
          open(os.path.join(OUT, "answer_key.json"), "w"), indent=1)
print("wrote", OUT, len(ev), "events", ev.type.nunique(), "types", f"({time.time()-t0:.0f}s)")
