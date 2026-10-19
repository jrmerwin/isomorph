"""Run the compression-driven choices (METHOD.md 3.1, 3.2) on building A's raw frame and
compare with the hand-set symbolization and entity used so far."""
import os, sys, json, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "datasets/building_a/raw"))
import simulate_building as SA
from isomorph.choose.symbolize import choose_symbolization
from isomorph.choose.entity import choose_entity, sys_layout

df = SA.simulate(7)
layout = dict(time="minute",
              entities={z: {"T": f"T_{z}", "CO2": f"CO2_{z}", "RH": f"RH_{z}", "heater": f"heater_{z}", "vent": f"vent_{z}",
                            "window": f"window_{z}", "occ": f"occ_{z}"} for z in "ABC"},
              system={"setpoint": "setpoint", "T_out": "T_out", "vibration": "vibration"},
              kinds={"T": "continuous", "CO2": "continuous", "RH": "continuous", "heater": "binary", "vent": "binary",
                     "window": "binary", "occ": "count", "setpoint": "categorical", "T_out": "continuous", "vibration": "continuous"},
              observation={"C": (30 * 1440, 60 * 1440)})
t0 = time.time()
print("== symbolization by compression (criterion: confirmation bits on other roles' events) ==")
choice, thresholds, trace = choose_symbolization(df, layout)
print("chosen:", choice); print("thresholds:", thresholds); print(f"({time.time()-t0:.0f}s)")
print("\n== entity by compression ==")
best, scores = choose_entity(df, {"zone": layout, "sys": sys_layout(layout)}, choice)
print("chosen entity layout:", best)
json.dump(dict(choice=choice, thresholds=thresholds, trace=trace, entity=best, entity_scores=scores),
          open(os.path.join(ROOT, "datasets/building_a/out/choices_v1.json"), "w"), indent=1)

from isomorph.choose.symbolize import write_chosen_dataset
out = os.path.join(ROOT, "datasets/building_a_auto")
ev = write_chosen_dataset(df, layout, choice, out, origin="building_a raw frame, symbolization chosen by compression (scripts/choose_building_a.py)")
print("wrote", out, len(ev), "events", ev.type.nunique(), "types")
