"""
Dataset 6: NASA PCoE Battery Data Set, group FY08Q4 (B0005, B0006, B0007, B0018)

    bash scripts/fetch_battery.sh         # 210 MB archive; keeps the four .mat files
    python3 scripts/ingest_battery.py     # choices (3.1, 3.2) + canonical dataset; resumable

Charge and discharge cycles at 1-minute means on a compressed time axis; every unobserved stretch (rests,
impedance tests, the gap between the two campaigns) is a gap for every entity, so no context spans one.
A charge/discharge pair is the natural period (~3 h); 168 pairs for three cells and 132 for the fourth.
"""
import os, sys, json, time, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT); sys.path.insert(0, os.path.dirname(__file__))
import battery_layout as L
from isomorph.choose.symbolize import choose_symbolization, write_chosen_dataset
from isomorph.choose.entity import choose_entity, sys_layout
from isomorph.canon.ingest import SYSTEM

RAW = sorted(glob.glob(os.path.join(ROOT, "datasets/nasa_battery/raw/B00*.mat"))); OUT = os.path.join(ROOT, "datasets/nasa_battery")
assert RAW, "run scripts/fetch_battery.sh first"

t0 = time.time()
df, bounds, cycles = L.load_cells(RAW)
print(f"NASA battery FY08Q4: {len(df)} minutes observed ({len(df)/1440:.1f} days) over {len(cycles)} charge/discharge cycles, {len(bounds)} boundaries ({time.time()-t0:.0f}s)")
lay = L.cell_layout(df)
print("entities:", {e: list(c) for e, c in lay["entities"].items()}, "observation:", lay["observation"])

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
best, scores = choose_entity(df, {"cell": lay, "sys": sys_layout(lay)}, choice)
print("chosen entity layout:", best)
json.dump(dict(choice=choice, thresholds=thresholds, trace=trace, entity=best, entity_scores=scores, complete=True), open(final, "w"), indent=1, default=str)

layout_used = lay if best == "cell" else sys_layout(lay)
ch = choice if best == "cell" else {r: choice.get(next((b for b in choice if r == b or r.startswith(b + "_")), r)) for r in layout_used["kinds"]}
eps = L.SAMPLE_MIN
obs_of = {ent: layout_used.get("observation", {}).get(ent, (df.minute.min(), df.minute.max() + eps)) for ent in layout_used["entities"]}
obs_of[SYSTEM] = (df.minute.min(), df.minute.max() + eps)
gaps = [(ent, "", b - eps, b + eps, "unobserved stretch removed (rest, impedance test or campaign gap)")
        for b in bounds for ent, (s_, e_) in obs_of.items() if s_ < b - eps and b + eps <= e_]   # a gap must lie inside the entity's observation interval
per_cell = {c: dict(charge=sum(1 for x in cycles if x["cell"] == c and x["type"] == "charge"), discharge=sum(1 for x in cycles if x["cell"] == c and x["type"] == "discharge"),
                    capacity_Ah=[x["capacity_Ah"] for x in cycles if x["cell"] == c and x["type"] == "discharge"]) for c in L.CELLS}
extra = dict(time_unit="minute (compressed: unobserved stretches removed; real_minute kept in the cycle list)", sample_minutes=L.SAMPLE_MIN, entity_key=best,
             cycles=per_cell, cycle_list=cycles,
             source="NASA Ames PCoE Battery Data Set, 1. BatteryAgingARC-FY08Q4 (Saha & Goebel 2007), https://data.nasa.gov/dataset/li-ion-battery-aging-datasets",
             span_note=f"{len(df)/1440:.1f} days observed; the charge/discharge pair (~3 h) is the natural period, 168 pairs for B0005-7 and 132 for B0018",
             rosetta="electrochemical loop: current (ACT) <I> -> terminal voltage <M L² T⁻³ I⁻¹> and cell temperature <Θ>; ageing (capacity fade) as the slow regime")
ev = write_chosen_dataset(df, layout_used, ch, OUT, sidecar_extra=extra, gaps=gaps, kind="real battery test bed (NASA PCoE, 4 cells)", origin="scripts/ingest_battery.py")
json.dump(dict(mechanisms=L.MECHANISMS, match="role_prefix",
               note="current -> voltage and current -> temperature are true by construction of the protocol; voltage -> current holds in the constant-voltage phase of every charge"),
          open(os.path.join(OUT, "answer_key.json"), "w"), indent=1)
print("wrote", OUT, len(ev), "events", ev.type.nunique(), "types", f"({time.time()-t0:.0f}s)")
