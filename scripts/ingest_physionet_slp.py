"""
Dataset 7: MIT-BIH Polysomnographic Database (PhysioNet slpdb 1.0.0)

    bash scripts/fetch_physionet_slp.sh       # 18 records, ~350 MB, not committed; needs `pip install wfdb` to read
    python3 scripts/ingest_physionet_slp.py   # choices (3.1, 3.2) + canonical dataset; resumable

Records (different nights) are concatenated on a compressed time axis, every boundary a gap for every entity;
each record is observed only on its own stretch. Sleep stages and apnea events are regime annotations, not
events. ~89 h: below the 20-day line; admitted on the natural-period clause if the period rule finds a cycle
(breathing, ~4 s; the sleep cycle, ~90 min), otherwise flagged.
"""
import os, sys, json, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT); sys.path.insert(0, os.path.dirname(__file__))
import physionet_slp_layout as L
from isomorph.choose.symbolize import choose_symbolization, write_chosen_dataset
from isomorph.choose.entity import choose_entity, sys_layout
from isomorph.canon.ingest import SYSTEM

RAW = os.path.join(ROOT, "datasets/physionet_slp/raw"); OUT = os.path.join(ROOT, "datasets/physionet_slp")
assert os.path.exists(os.path.join(RAW, "RECORDS")), "run scripts/fetch_physionet_slp.sh first"

t0 = time.time()
df, bounds, files, regimes = L.load_records(RAW)
print(f"slpdb: {len(df)} seconds in {len(files)} records ({df.minute.iloc[-1]/60:.1f} h observed), {len(regimes)} regime annotations ({time.time()-t0:.0f}s)")
lay = L.record_layout(df, files)
print("roles per record:", {e: list(c) for e, c in lay["entities"].items()})

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
best, scores = choose_entity(df, {"record": lay, "sys": sys_layout(lay)}, choice)
print("chosen entity layout:", best)
json.dump(dict(choice=choice, thresholds=thresholds, trace=trace, entity=best, entity_scores=scores, complete=True), open(final, "w"), indent=1, default=str)

layout_used = lay if best == "record" else sys_layout(lay)
ch = choice if best == "record" else {r: choice.get(next((b for b in choice if r == b or r.startswith(b + "_")), r)) for r in layout_used["kinds"]}
eps = L.SAMPLE_MIN
obs_of = {ent: layout_used.get("observation", {}).get(ent, (df.minute.min(), df.minute.max() + eps)) for ent in layout_used["entities"]}
obs_of[SYSTEM] = (df.minute.min(), df.minute.max() + eps)
gaps = [(ent, "", b - eps, b + eps, "record boundary: different nights")
        for b in bounds for ent, (s_, e_) in obs_of.items() if s_ < b - eps and b + eps <= e_]
extra = dict(time_unit="minute (compressed: records concatenated)", sample_minutes=L.SAMPLE_MIN, entity_key=best,
             files=[{k: v for k, v in f.items() if k != "comments"} for f in files], regimes=regimes,
             regime_note="sleep stages (30-s epochs, merged into runs) and apnea / arousal events from the .st annotations; not observed variables, not in the events",
             source="https://physionet.org/content/slpdb/1.0.0/ (Ichimaru & Moody 1999), read with wfdb",
             span_note=f"{df.minute.iloc[-1]/60:.1f} h observed in {len(files)} records; below the 20-day line, admitted only on the natural-period clause",
             rosetta="physiological regulator: arterial pressure <M L⁻¹ T⁻²> <-> heart rate <T⁻¹> (baroreflex), respiration (dimensionless, uncalibrated) -> both; SO2 where recorded",
             omitted_channels="EEG, EOG, EMG, SV: not cardiorespiratory regulator quantities")
ev = write_chosen_dataset(df, layout_used, ch, OUT, sidecar_extra=extra, gaps=gaps, kind="real physiological records (MIT-BIH polysomnographic, 18 nights)", origin="scripts/ingest_physionet_slp.py")
json.dump(dict(mechanisms=L.MECHANISMS, match="role_prefix",
               note="cause -> effect pairs from cardiorespiratory physiology; the baroreflex closes within 1-2 beats, the respiratory couplings within a breath"),
          open(os.path.join(OUT, "answer_key.json"), "w"), indent=1)
print("wrote", OUT, len(ev), "events", ev.type.nunique(), "types", f"({time.time()-t0:.0f}s)")
