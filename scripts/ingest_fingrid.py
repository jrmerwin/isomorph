"""
Dataset 9: Fingrid open data — Nordic grid frequency regulation (one synchronous area, one entity)

    FINGRID_API_KEY=... bash scripts/fetch_fingrid.sh      # one year of six series; the key is never stored
    python3 scripts/ingest_fingrid.py                      # choices (3.2) + canonical dataset; 3.1 has one candidate

Declared at 3-minute samples over 2024-07-01 .. 2025-07-01 (365 days). The synchronous area is one system with one
copy of every role, so the entity rule (3.1) has a single candidate and no comparison is made; the card says so.
"""
import os, sys, json, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT); sys.path.insert(0, os.path.dirname(__file__))
import fingrid_layout as L
from isomorph.choose.symbolize import choose_symbolization, write_chosen_dataset

RAW = os.path.join(ROOT, "datasets/fingrid/raw"); OUT = os.path.join(ROOT, "datasets/fingrid")
assert os.path.isdir(RAW) and os.listdir(RAW), "run scripts/fetch_fingrid.sh first (needs FINGRID_API_KEY)"

t0 = time.time()
df, span = L.load_year(RAW)
lay = L.grid_layout(df)
print(f"Fingrid: {len(df)} samples at {L.SAMPLE_MIN:.0f} min, {df.minute.iloc[-1]/1440:.1f} days ({span['start']} .. {span['end']}); roles {list(lay['kinds'])} ({time.time()-t0:.0f}s)")
print("missing share:", {c: round(float(df[c].isna().mean()), 3) for c in df.columns if c.startswith("grid_")})

os.makedirs(os.path.join(OUT, "out"), exist_ok=True)
final = os.path.join(OUT, "out", "choices_v1.json")
if os.path.exists(final) and json.load(open(final)).get("complete"):
    rec = json.load(open(final)); choice, thresholds, trace = rec["choice"], rec["thresholds"], rec["trace"]
    print("symbolization choice loaded from", final)
else:
    print("== symbolization by compression (3.2) ==")
    choice, thresholds, trace = choose_symbolization(df, lay, checkpoint=os.path.join(OUT, "out", "choice_checkpoint.json"))
    json.dump(dict(choice=choice, thresholds=thresholds, trace=trace, entity="grid", entity_scores="one candidate: the synchronous area is one system (3.1 not compared)", complete=True), open(final, "w"), indent=1, default=str)
print("chosen:", choice); print(f"({time.time()-t0:.0f}s)")
extra = dict(time_unit="minute", sample_minutes=L.SAMPLE_MIN, entity_key="grid", span=span,
             entity_note="one candidate: the Nordic synchronous area is one system with one copy of every role; 3.1 has nothing to compare",
             source="Fingrid open data (data.fingrid.fi, CC BY 4.0): series 177, 343, 344, 349, 350, 194; fetched with a registered key, never stored",
             span_note="365 days at 3-minute samples; the 15-minute reserve series are held within their quarter on the 3-minute grid",
             rosetta="grid frequency regulation: frequency <T⁻¹> -> activated reserve <M L² T⁻³> -> frequency; the loop is the whole synchronous area and the reserve is its only actuator")
ev = write_chosen_dataset(df, lay, choice, OUT, sidecar_extra=extra, gaps=[], kind="real power system (Nordic synchronous area, Fingrid)", origin="scripts/ingest_fingrid.py")
json.dump(dict(mechanisms=L.MECHANISMS, match="role_prefix",
               note="frequency containment and restoration: a deviation activates the reserve, the reserve returns the frequency; seen at 3-min frequency and 15-min reserve resolution"),
          open(os.path.join(OUT, "answer_key.json"), "w"), indent=1)
print("wrote", OUT, len(ev), "events", ev.type.nunique(), "types", f"({time.time()-t0:.0f}s)")
