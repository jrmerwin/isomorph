"""
Disjoint stretches for the diagonal (METHOD 3.12, v9): a second canonical dataset per receiver, built under the
receiver's own recorded choices (entity and symbolization are never revisited; thresholds are the stretch's own
quantiles under the same scheme), written to datasets/<name>_stretch.

    python3 scripts/make_stretch.py tennessee_eastman    # days 120-240 of the 1-year file (240-365 untouched)
    python3 scripts/make_stretch.py building_59          # calendar year 2018
    python3 scripts/make_stretch.py buildings            # A and B' under generator seed 1
    python3 scripts/make_stretch.py nasa_battery         # the other FY08Q4-era cells (B0025-B0028, archive group 2)
    python3 scripts/make_stretch.py fingrid              # 2025-07-01 .. 2026-07-01, the year after (the year before lacks the reserve series)
"""
import os, sys, json, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT); sys.path.insert(0, os.path.dirname(__file__))
import numpy as np, pandas as pd
from isomorph.choose.symbolize import write_chosen_dataset
from isomorph.choose.entity import sys_layout
from isomorph.canon.ingest import SYSTEM, write_dataset

which = sys.argv[1]


def choices(name):
    rec = json.load(open(os.path.join(ROOT, "datasets", name, "out", "choices_v1.json")))
    return rec["choice"], rec.get("entity")


if which == "tennessee_eastman":
    import tep_layout as L
    choice, best = choices("tennessee_eastman")
    df_full = L.load(os.path.join(ROOT, "datasets/tennessee_eastman/raw/matlab_data_1year.csv"))
    i0, i1 = int(120 * 1440 / L.SAMPLE_MIN), int(240 * 1440 / L.SAMPLE_MIN)
    df = df_full.iloc[i0:i1].reset_index(drop=True); df["minute"] = np.arange(len(df)) * L.SAMPLE_MIN
    lay = L.vessel_layout(); layout_used = lay if best == "vessel" else sys_layout(lay)
    ch = choice if best == "vessel" else {r: choice.get(next((b for b in choice if r == b or r.startswith(b + "_")), r)) for r in layout_used["kinds"]}
    OUT = os.path.join(ROOT, "datasets/tennessee_eastman_stretch")
    extra = dict(time_unit="minute", sample_minutes=L.SAMPLE_MIN, entity_key=best, stretch_of="tennessee_eastman", span_note="days 120-240 of the 1-year run (the diagonal's source stretch, 3.12 v9); days 240-365 untouched",
                 regimes=[dict(r, start=r["start"] - 120 * 1440, end=r["end"] - 120 * 1440) for r in L.regimes(df_full) if 120 * 1440 <= r["start"] < 240 * 1440])
    ev = write_chosen_dataset(df, layout_used, ch, OUT, sidecar_extra=extra, kind="simulated plant (Tennessee Eastman), stretch days 120-240", origin="scripts/make_stretch.py tennessee_eastman")
    json.dump(json.load(open(os.path.join(ROOT, "datasets/tennessee_eastman/answer_key.json"))), open(os.path.join(OUT, "answer_key.json"), "w"), indent=1)

elif which == "building_59":
    import building_59_layout as L
    choice, best = choices("building_59")
    df, units, zones = L.load_year(os.path.join(ROOT, "datasets/building_59/raw"), year=2018)
    cands = {"unit": L.unit_layout(df, units, zones), "zone": L.zone_layout(df, units, zones)}
    layout_used = cands[best]
    ch = {r: choice.get(next((b for b in choice if r == b or r.startswith(b + "_") or r.endswith("_" + b)), r)) for r in layout_used["kinds"]}
    gaps = [(ent, "", s, e, reason) for ent, s, e, reason in L.unit_gaps(df, layout_used)]
    OUT = os.path.join(ROOT, "datasets/building_59_stretch")
    extra = dict(time_unit="minute", sample_minutes=L.SAMPLE_MIN, entity_key=best, year=2018, stretch_of="building_59", span_note="calendar year 2018 (the diagonal's source stretch); setpoints from 2018-09-15, no CO2")
    ev = write_chosen_dataset(df, layout_used, ch, OUT, sidecar_extra=extra, gaps=gaps, kind="real office building (LBNL Building 59), stretch 2018", origin="scripts/make_stretch.py building_59")
    json.dump(json.load(open(os.path.join(ROOT, "datasets/building_59/answer_key.json"))), open(os.path.join(OUT, "answer_key.json"), "w"), indent=1)

elif which == "fingrid":
    import fingrid_layout as L
    choice, _ = choices("fingrid")
    df, span = L.load_year(os.path.join(ROOT, "datasets/fingrid_stretch/raw"))
    lay = L.grid_layout(df)
    OUT = os.path.join(ROOT, "datasets/fingrid_stretch")
    extra = dict(time_unit="minute", sample_minutes=L.SAMPLE_MIN, entity_key="grid", span=span, stretch_of="fingrid",
                 span_note="2025-07-01 .. 2026-07-01, the adjacent year AFTER the receiver year (the diagonal's source stretch): the year before has FCR-N activations for four months and aFRR for one, since those series begin in spring 2024")
    ev = write_chosen_dataset(df, lay, choice, OUT, sidecar_extra=extra, gaps=[], kind="real power system (Nordic synchronous area, Fingrid), stretch 2025-26", origin="scripts/make_stretch.py fingrid")
    json.dump(json.load(open(os.path.join(ROOT, "datasets/fingrid/answer_key.json"))), open(os.path.join(OUT, "answer_key.json"), "w"), indent=1)

elif which == "nasa_battery":
    import battery_layout as L
    choice, best = choices("nasa_battery")
    raw = os.path.join(ROOT, "datasets/nasa_battery_stretch/raw")
    paths = sorted(glob.glob(os.path.join(raw, "B00*.mat")))
    assert paths, "unpack archive group 2 (BatteryAgingARC_25_26_27_28_P1) into datasets/nasa_battery_stretch/raw first"
    L.CELLS = [os.path.basename(p)[:-4] for p in paths]
    df, bounds, cycles = L.load_cells(paths)
    lay = L.cell_layout(df); layout_used = lay if best == "cell" else sys_layout(lay)
    ch = choice if best == "cell" else {r: choice.get(next((b for b in choice if r == b or r.startswith(b + "_")), r)) for r in layout_used["kinds"]}
    eps = L.SAMPLE_MIN
    obs_of = {ent: layout_used.get("observation", {}).get(ent, (df.minute.min(), df.minute.max() + eps)) for ent in layout_used["entities"]}; obs_of[SYSTEM] = (df.minute.min(), df.minute.max() + eps)
    gaps = [(ent, "", b - eps, b + eps, "unobserved stretch removed") for b in bounds for ent, (s_, e_) in obs_of.items() if s_ < b - eps and b + eps <= e_]
    OUT = os.path.join(ROOT, "datasets/nasa_battery_stretch")
    extra = dict(time_unit="minute (compressed)", sample_minutes=L.SAMPLE_MIN, entity_key=best, stretch_of="nasa_battery", cells=L.CELLS, span_note="archive group 2 (B0025-B0028), the diagonal's source stretch")
    ev = write_chosen_dataset(df, layout_used, ch, OUT, sidecar_extra=extra, gaps=gaps, kind="real battery test bed (NASA PCoE), stretch B0025-28", origin="scripts/make_stretch.py nasa_battery")
    json.dump(json.load(open(os.path.join(ROOT, "datasets/nasa_battery/answer_key.json"))), open(os.path.join(OUT, "answer_key.json"), "w"), indent=1)

elif which == "buildings":
    from isomorph.canon.ingest import from_building_frame
    sys.path.insert(0, os.path.join(ROOT, "datasets/building_a/raw")); import simulate_building as SA
    dfA = SA.simulate(1)
    THRESH_A = {"T": [20, 23], "CO2": [700, 900], "RH": [50, 70], "T_out": [10, 20], "vibration": [-2, 2]}
    evA, obsA, gapsA = from_building_frame(dfA, ["A", "B", "C"], THRESH_A, ("heater", "vent", "window"), late_zone="C", late_start_day=30, dropout_vars=("T_B",))
    sideA = json.load(open(os.path.join(ROOT, "datasets/building_a/sidecar.json"))); sideA.update(origin="datasets/building_a/raw/simulate_building.py seed 1 (stretch)", generator_seed=1, stretch_of="building_a")
    write_dataset(os.path.join(ROOT, "datasets/building_a_stretch"), evA, obsA, gapsA, sideA, answer_key=json.load(open(os.path.join(ROOT, "datasets/building_a/answer_key.json"))))
    sys.path.insert(0, os.path.join(ROOT, "datasets/building_b/raw")); import building_sim as SB
    cfg = dict(SB.CFG_B); cfg["seed"] = 1; dfB = SB.simulate(cfg)
    rng = np.random.default_rng(99)
    evB_plain, _, _ = from_building_frame(dfB, cfg["zones"], SB.THRESH_B, ("heater", "vent", "window", "dehum"))
    types = sorted(evB_plain.type.unique()); codes = [f"x{c:02d}" for c in rng.permutation(len(types))]
    zmap = {z: f"u{i+1}" for i, z in enumerate(rng.permutation(cfg["zones"]))}
    keyB = json.load(open(os.path.join(ROOT, "datasets/building_b/answer_key.json")))
    true_to_code = {v["true"]: k for k, v in keyB["token"].items()}                 # the same scrambling as the receiver
    extra_codes = iter(f"x{90 + i:02d}" for i in range(10))
    scr = dict(type={t: true_to_code.get(t) or next(extra_codes) for t in types}, entity=zmap)
    evB, obsB, gapsB = from_building_frame(dfB, cfg["zones"], SB.THRESH_B, ("heater", "vent", "window", "dehum"), scramble=scr)
    sideB = json.load(open(os.path.join(ROOT, "datasets/building_b/sidecar.json"))); sideB.update(origin="datasets/building_b/raw/building_sim.py CFG_B seed 1 (stretch), names scrambled as the receiver", generator_seed=1, stretch_of="building_b")
    write_dataset(os.path.join(ROOT, "datasets/building_b_stretch"), evB, obsB, gapsB, sideB, answer_key=keyB)
    print("buildings: A stretch", len(evA), "events; B' stretch", len(evB), "events,", evB.type.nunique(), "types")
else:
    sys.exit(f"unknown stretch {which}")
print("stretch written:", which)
