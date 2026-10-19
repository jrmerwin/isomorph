"""Build the two calibration datasets through the canonical contract.
Building A: simulate_building.py (seed 7), thresholds matched to its control bands.
Building B': building_sim.CFG_B, its own thresholds, names scrambled; the answer key
carries the role mapping to A."""
import json, os, sys
import numpy as np, pandas as pd
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from isomorph.canon.ingest import from_building_frame, write_dataset

# ---- building A
sys.path.insert(0, os.path.join(ROOT, "datasets/building_a/raw"))
import simulate_building as SA
dfA = SA.simulate(7)
THRESH_A = {"T": [20, 23], "CO2": [700, 900], "RH": [50, 70], "T_out": [10, 20], "vibration": [-2, 2]}
evA, obsA, gapsA = from_building_frame(dfA, ["A", "B", "C"], THRESH_A, ("heater", "vent", "window"),
                                       late_zone="C", late_start_day=30, dropout_vars=("T_B",))
MECH_A = [  # cause, effect, lag classes (fixed-minute classes: s<5, m<30, l<90)
    dict(cause="setpoint:up", effect="heater:on", lags=["s"]),
    dict(cause="heater:on", effect="T:up20", lags=["s", "m"]),
    dict(cause="heater:on", effect="heater:off", lags=["m", "l"]),
    dict(cause="occ:arrive", effect="CO2:up900", lags=["s", "m"]),
    dict(cause="CO2:up900", effect="vent:on", lags=["s"]),
    dict(cause="vent:on", effect="CO2:down900", lags=["s", "m"]),
    dict(cause="CO2:down700", effect="vent:off", lags=["s"]),
    dict(cause="occ:leave", effect="vent:off", lags=["s", "m"]),
    dict(cause="vent:on", effect="T:down20", lags=["m", "l"]),
    dict(cause="window:on", effect="heater:on", lags=["m", "l"]),
    dict(cause="window:on", effect="CO2:down700", lags=["s", "m"]),
    dict(cause="setpoint:down", effect="T:down20", lags=["m", "l"]),
]
sideA = dict(time_unit="minute", entity_key="zone", period=1440.0, system_wide_types=["setpoint:up", "setpoint:down"] +
             [f"T_out:{e}{t}" for t in THRESH_A["T_out"] for e in ("up", "down")] + [f"vibration:{e}{t}" for t in THRESH_A["vibration"] for e in ("up", "down")],
             tie_rule="canonical", kind="synthetic", origin="datasets/building_a/raw/simulate_building.py seed 7",
             symbolization="fixed thresholds matched to control bands (session default)", generator_seed=7)
write_dataset(os.path.join(ROOT, "datasets/building_a"), evA, obsA, gapsA, sideA, answer_key=dict(mechanisms=MECH_A))
print("building_a:", len(evA), "events", len(obsA), "observation intervals", len(gapsA), "gaps")

# ---- building B'
sys.path.insert(0, os.path.join(ROOT, "datasets/building_b/raw"))
import building_sim as SB
dfB = SB.simulate(SB.CFG_B)
rng = np.random.default_rng(99)
ROLE = {"T:up21": "T:up20", "T:down21": "T:down20", "T:up24": "T:up23", "T:down24": "T:down23",
        "CO2:up800": "CO2:up700", "CO2:down800": "CO2:down700", "CO2:up1000": "CO2:up900", "CO2:down1000": "CO2:down900",
        "RH:up55": "RH:up50", "RH:down55": "RH:down50", "RH:up65": "RH:up70", "RH:down65": "RH:down70",
        "T_out:up12": "T_out:up10", "T_out:down12": "T_out:down10", "T_out:up22": "T_out:up20", "T_out:down22": "T_out:down20"}
for t in ("vibration:up-2", "vibration:down-2", "vibration:up2", "vibration:down2", "occ:arrive", "occ:leave", "setpoint:up", "setpoint:down"):
    ROLE[t] = t
for sw in ("heater", "vent", "window"):
    ROLE[f"{sw}:on"] = f"{sw}:on"; ROLE[f"{sw}:off"] = f"{sw}:off"
ROLE["dehum:on"] = None; ROLE["dehum:off"] = None
evB_plain, _, _ = from_building_frame(dfB, SB.CFG_B["zones"], SB.THRESH_B, ("heater", "vent", "window", "dehum"))
types = sorted(evB_plain.type.unique())
codes = [f"x{c:02d}" for c in rng.permutation(len(types))]
zmap = {z: f"u{i+1}" for i, z in enumerate(rng.permutation(SB.CFG_B["zones"]))}
scr = dict(type=dict(zip(types, codes)), entity=zmap)
evB, obsB, gapsB = from_building_frame(dfB, SB.CFG_B["zones"], SB.THRESH_B, ("heater", "vent", "window", "dehum"), scramble=scr)
sideB = dict(time_unit="minute", entity_key="zone (scrambled)", period=1440.0,
             system_wide_types=sorted(set(evB[evB.entity == "ALL"].type)), tie_rule="canonical", kind="synthetic",
             origin="datasets/building_b/raw/building_sim.py CFG_B (seed 11), names scrambled with seed 99",
             symbolization="fixed thresholds matched to its own control bands", generator_seed=11)
keyB = dict(token={scr["type"][t]: dict(true=t, A_role=ROLE.get(t)) for t in types}, zone={v: k for k, v in zmap.items()},
            role_mapping_to="building_a")
write_dataset(os.path.join(ROOT, "datasets/building_b"), evB, obsB, gapsB, sideB, answer_key=keyB)
print("building_b:", len(evB), "events", evB.type.nunique(), "scrambled types")
