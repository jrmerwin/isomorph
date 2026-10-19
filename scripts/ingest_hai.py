"""
Dataset 4: HAI 21.03 (real ICS testbed with attacks), https://github.com/icsdataset/hai

    bash scripts/fetch_hai.sh             # clones the source repo and copies hai-21.03/*.csv.gz
    python3 scripts/ingest_hai.py         # choices (3.1, 3.2) + canonical dataset; resumable

The eight time-continuous files are concatenated in chronological order on a compressed time axis (the
unobserved stretches between files are removed) and every file boundary is declared a missing-data gap
for every entity, so no context spans a boundary. Attack labels are excluded from the events and kept as
regime annotations. Span 15.3 days: below the 20-day admission line; admitted on the natural-period clause
if the period rule finds the plant's operating cycle, otherwise flagged on the card.
"""
import os, sys, json, time, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT); sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
import pandas as pd
import hai_layout as L
from isomorph.choose.symbolize import choose_symbolization, write_chosen_dataset
from isomorph.choose.entity import choose_entity, sys_layout
from isomorph.canon.ingest import SYSTEM

RAW = sorted(glob.glob(os.path.join(ROOT, "datasets/hai/raw/*.csv.gz")))
OUT = os.path.join(ROOT, "datasets/hai")
assert RAW, "run scripts/fetch_hai.sh first"

t0 = time.time()
df, bounds, files = L.load_files(RAW)
print(f"HAI 21.03: {len(df)} samples in {len(files)} files, {df.minute.iloc[-1]/1440:.1f} days observed ({time.time()-t0:.0f}s)")
lay = L.process_layout(df)
print("roles:", {e: len(c) for e, c in lay["entities"].items()}, "system:", len(lay["system"]))

os.makedirs(os.path.join(OUT, "out"), exist_ok=True)
final = os.path.join(OUT, "out", "choices_v2.json")
if os.path.exists(final) and json.load(open(final)).get("complete"):
    rec = json.load(open(final)); choice, thresholds, trace = rec["choice"], rec["thresholds"], rec["trace"]
    print("symbolization choice loaded from", final)
else:
    print("== symbolization by compression (3.2) ==")
    choice, thresholds, trace = choose_symbolization(df, lay, checkpoint=os.path.join(OUT, "out", "choice_checkpoint.json"))
    json.dump(dict(choice=choice, thresholds=thresholds, trace=trace, complete=True), open(final, "w"), indent=1, default=str)
print("chosen:", choice); print(f"({time.time()-t0:.0f}s)")

print("\n== entity by compression (3.1) ==")
best, scores = choose_entity(df, {"process": lay, "sys": sys_layout(lay)}, choice)
print("chosen entity layout:", best)
json.dump(dict(choice=choice, thresholds=thresholds, trace=trace, entity=best, entity_scores=scores, complete=True), open(final, "w"), indent=1, default=str)

layout_used = lay if best == "process" else sys_layout(lay)
ch = choice if best == "process" else {r: choice.get(next((b for b in choice if r == b or r.startswith(b + "_")), r)) for r in layout_used["kinds"]}
eps = L.SAMPLE_MIN
gaps = [(ent, "", b - eps, b + eps, "file boundary: unobserved stretch removed") for b in bounds for ent in list(layout_used["entities"]) + [SYSTEM]]
extra = dict(time_unit="minute (compressed: unobserved stretches between files removed)", sample_minutes=L.SAMPLE_MIN, entity_key=best,
             files=files, regimes=L.regimes(df), regime_note="attack episodes (attack, attack_P1/P2/P3 labels); not observed variables, not in the events",
             source="https://github.com/icsdataset/hai hai-21.03 (Shin, Lee, Choi, Min, Kim; KAIST / NSR)",
             span_note="15.3 days observed; below the 20-day admission line, admitted on the natural-period clause if a period is found",
             omitted_columns=[c for c in df.columns if c not in ("time", "minute") and c not in [col for cols in lay["entities"].values() for col in cols.values()] + list(lay["system"].values())])
ev = write_chosen_dataset(df, layout_used, ch, OUT, sidecar_extra=extra, gaps=gaps, kind="real ICS testbed (HAI 21.03)", origin="scripts/ingest_hai.py")
json.dump(dict(mechanisms=L.MECHANISMS, match="role_prefix",
               note="cause -> effect pairs true by construction from the point descriptions (hai_dataset_technical_details.pdf); "
                    "command -> position and start -> running pairs respond within one or two seconds"),
          open(os.path.join(OUT, "answer_key.json"), "w"), indent=1)
print("wrote", OUT, len(ev), "events", ev.type.nunique(), "types", f"({time.time()-t0:.0f}s)")
