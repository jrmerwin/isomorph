"""
Dataset 5: TCLab, public recordings of the Arduino Temperature Control Lab (BYU), https://apmonitor.com/heat.htm

    bash scripts/fetch_tclab.sh           # nine recordings from APMonitor course uploads and two GitHub repositories
    python3 scripts/ingest_tclab.py       # choices (3.1, 3.2) + canonical dataset; resumable

Recordings are concatenated in a fixed order on a compressed time axis, every file boundary a gap for every
entity, and stretches where a sensor was absent are gaps for that entity. ~7 h in all: far below the 20-day
line; admitted only on the natural-period clause if the period rule finds the step cadence, else flagged.
"""
import os, sys, json, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT); sys.path.insert(0, os.path.dirname(__file__))
import tclab_layout as L
from isomorph.choose.symbolize import choose_symbolization, write_chosen_dataset
from isomorph.choose.entity import choose_entity, sys_layout
from isomorph.canon.ingest import SYSTEM

RAW = os.path.join(ROOT, "datasets/tclab/raw"); OUT = os.path.join(ROOT, "datasets/tclab")
assert os.path.isdir(RAW) and os.listdir(RAW), "run scripts/fetch_tclab.sh first"

t0 = time.time()
df, bounds, files = L.load_files(RAW)
print(f"TCLab: {len(df)} samples at {L.SAMPLE_SEC}s in {len(files)} files, {df.minute.iloc[-1]/60:.1f} h observed ({time.time()-t0:.0f}s)")
lay = L.heater_layout(df)
print("roles:", {e: list(c) for e, c in lay["entities"].items()})

os.makedirs(os.path.join(OUT, "out"), exist_ok=True)
final = os.path.join(OUT, "out", "choices_v1.json")
if os.path.exists(final) and json.load(open(final)).get("complete"):
    rec = json.load(open(final)); choice, thresholds, trace = rec["choice"], rec["thresholds"], rec["trace"]
    print("symbolization choice loaded from", final)
else:
    print("== symbolization by compression (3.2) ==")
    choice, thresholds, trace = choose_symbolization(df, lay, checkpoint=os.path.join(OUT, "out", "choice_checkpoint.json"))
    json.dump(dict(choice=choice, thresholds=thresholds, trace=trace, complete=True), open(final, "w"), indent=1, default=str)
print("chosen:", choice); print(f"({time.time()-t0:.0f}s)")

print("\n== entity by compression (3.1) ==")
best, scores = choose_entity(df, {"heater": lay, "sys": sys_layout(lay)}, choice)
print("chosen entity layout:", best)
json.dump(dict(choice=choice, thresholds=thresholds, trace=trace, entity=best, entity_scores=scores, complete=True), open(final, "w"), indent=1, default=str)

layout_used = lay if best == "heater" else sys_layout(lay)
ch = choice if best == "heater" else {r: choice.get(next((b for b in choice if r == b or r.startswith(b + "_")), r)) for r in layout_used["kinds"]}
eps = L.SAMPLE_MIN
gaps = [(ent, "", b - eps, b + eps, "file boundary: separate recording") for b in bounds for ent in list(layout_used["entities"]) + [SYSTEM]]
if best == "heater":
    gaps += [(ent, "", s, e, reason) for ent, s, e, reason in L.absent_stretches(df, files, lay)]
extra = dict(time_unit="minute (compressed: separate recordings concatenated)", sample_minutes=L.SAMPLE_MIN, entity_key=best,
             files=files, source="APMonitor TCLab course uploads (apmonitor.com/pdc, /do, /pds), BYU-PRISM/Transformer_MPC and jckantor/cbe30338-book on GitHub",
             span_note=f"{df.minute.iloc[-1]/60:.1f} h observed in {len(files)} recordings; far below the 20-day line, admitted only on the natural-period clause",
             rosetta="thermal first-order loop: heater (ACT, dimensionless power) -> sensor temperature <Θ>")
ev = write_chosen_dataset(df, layout_used, ch, OUT, sidecar_extra=extra, gaps=gaps, kind="real lab kit (TCLab, two heaters)", origin="scripts/ingest_tclab.py")
json.dump(dict(mechanisms=L.MECHANISMS, match="role_prefix",
               note="heater -> its own sensor is true by construction; the setpoint pairs hold only in the closed-loop recording"),
          open(os.path.join(OUT, "answer_key.json"), "w"), indent=1)
print("wrote", OUT, len(ev), "events", ev.type.nunique(), "types", f"({time.time()-t0:.0f}s)")
