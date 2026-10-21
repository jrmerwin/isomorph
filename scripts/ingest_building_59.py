"""
Dataset 8: LBNL Building 59 (Luo et al. 2022), https://doi.org/10.7941/D1N33Q (CC0; Zenodo 5951008)

    bash scripts/fetch_building_59.sh         # 263 MB archive from Zenodo; keeps the 27 csv files, the Brick model and the metadata
    python3 scripts/ingest_building_59.py     # choices (3.1, 3.2) + canonical dataset; resumable

Calendar year 2019 at 5-minute means (section 6: 365 days). Stretches in which every point of a unit is missing
for an hour or more are gaps for that unit; single-point dropouts are missing values, not declared.
"""
import os, sys, json, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT); sys.path.insert(0, os.path.dirname(__file__))
import building_59_layout as L
from isomorph.choose.symbolize import choose_symbolization, write_chosen_dataset
from isomorph.choose.entity import choose_entity, sys_layout
from isomorph.canon.ingest import SYSTEM

RAW = os.path.join(ROOT, "datasets/building_59/raw"); OUT = os.path.join(ROOT, "datasets/building_59")
assert os.path.exists(os.path.join(RAW, "rtu_sa_t.csv")), "run scripts/fetch_building_59.sh first"

t0 = time.time()
df, units, zones = L.load_year(RAW)
print(f"Building 59, {L.YEAR}: {len(df)} samples at {L.SAMPLE_MIN:.0f} min; {len(units)} RTUs, {len(zones)} zones, {sum(c.startswith('sys_') for c in df.columns)} system points ({time.time()-t0:.0f}s)")
lay_unit = L.unit_layout(df, units, zones); lay_zone = L.zone_layout(df, units, zones)
print("unit layout:", {e: len(c) for e, c in lay_unit["entities"].items() if e.startswith("rtu")}, "zones:", sum(1 for e in lay_unit["entities"] if e.startswith("zone")), "system:", len(lay_unit["system"]))

os.makedirs(os.path.join(OUT, "out"), exist_ok=True)
final = os.path.join(OUT, "out", "choices_v1.json")
if os.path.exists(final) and json.load(open(final)).get("complete"):
    rec = json.load(open(final)); choice, thresholds, trace = rec["choice"], rec["thresholds"], rec["trace"]
    print("symbolization choice loaded from", final)
else:
    print("== symbolization by compression (3.2) on the unit layout ==")
    choice, thresholds, trace = choose_symbolization(df, lay_unit, checkpoint=os.path.join(OUT, "out", "choice_checkpoint.json"))
    json.dump(dict(choice=choice, thresholds=thresholds, trace=trace, complete=True), open(final, "w"), indent=1, default=str)
print("chosen:", choice); print(f"({time.time()-t0:.0f}s)")

print("\n== entity by compression (3.1) ==")
cands = {"unit": lay_unit, "zone": lay_zone}   # no single-system candidate: 299 roles in one entity are ~1,800 types, and the Markov-only comparison (vocab² adjacent features) does not fit in memory; the physical candidates are unit and zone
best, scores = choose_entity(df, cands, choice)
print("chosen entity layout:", best, scores)
json.dump(dict(choice=choice, thresholds=thresholds, trace=trace, entity=best, entity_scores=scores, complete=True), open(final, "w"), indent=1, default=str)

layout_used = cands[best]
ch = {r: choice.get(next((b for b in choice if r == b or r.startswith(b + "_") or r.endswith("_" + b)), r)) for r in layout_used["kinds"]}
gaps = [(ent, "", s, e, reason) for ent, s, e, reason in L.unit_gaps(df, layout_used)]
extra = dict(time_unit="minute", sample_minutes=L.SAMPLE_MIN, entity_key=best, year=L.YEAR,
             source="LBNL Building 59 (Luo et al. 2022, Scientific Data; doi:10.7941/D1N33Q, CC0; mirrored at Zenodo 5951008)",
             span_note=f"calendar year {L.YEAR} of a 2018-2020 record, 5-minute means; CO2 from 2019-08-19; RTU and zone points at 1 min, setpoints 5 min, weather and meters 15 min (interpolated)",
             units=units, zones=zones, system_points=list(L.SYSTEM_ROLES),
             entity_note="candidates unit (every zone and RTU a unit) and zone (RTU points system-wide); a single-system layout (299 roles, ~1,800 types) is not fittable by the Markov-only comparison and was not run")
ev = write_chosen_dataset(df, layout_used, ch, OUT, sidecar_extra=extra, gaps=gaps, kind="real office building (LBNL Building 59, 4 RTUs, ~50 zones)", origin="scripts/ingest_building_59.py")
json.dump(dict(mechanisms=L.MECHANISMS, match="role_prefix",
               note="cause -> effect pairs true by construction of a packaged-RTU building with underfloor terminals (Brick model and point names)"),
          open(os.path.join(OUT, "answer_key.json"), "w"), indent=1)
print("wrote", OUT, len(ev), "events", ev.type.nunique(), "types", f"({time.time()-t0:.0f}s)")
