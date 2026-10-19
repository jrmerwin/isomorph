"""
simulate_building.py — a semi-real multivariate time series: a small office
building with three zones served by individual heaters and ventilation units.

Why this system: it has real physical delays (minutes to tens of minutes),
identical sub-units (zones) so entity binding and cross-unit transfer are
meaningful, a daily/weekly cycle, cascades built from shared sub-processes
(the "thermal loop" and the "air-quality loop" compose into longer chains such
as arrive -> CO2 high -> vent on -> zone cools -> heater on), a fault regime
(zone B damper stuck for ten days), a zone that comes online late (cold-start
transfer), one chatty sensor unrelated to anything (hub analogue), and one
sensor with dropouts. Every mechanism is listed in GROUND_TRUTH.md.

Resolution 1 minute, 60 days. Deterministic given SEED.

Per zone z, per minute (k's in GROUND_TRUTH.md):
  T_z    += k_loss (T_out - T_z) + k_heat h_z + k_win w_z (T_out - T_z)
            + k_vent v_z (T_out - T_z) + k_occ n_z + noise
  CO2_z  += g_occ n_z - k_x (CO2_z - 420) - k_xv eff_z v_z (CO2_z - 420)
            - k_xw w_z (CO2_z - 420) + noise
  RH_z   += m_occ n_z - k_r (RH_z - RH_out) - k_rv v_z (RH_z - RH_out)
            - k_rh h_z + noise
Control (with delays):
  heater on  when T_z < setpoint_z - 1 for D_h minutes; off when T_z > setpoint_z + 1 for D_h
  vent   on  when CO2_z > 900 for D_v minutes;            off when CO2_z < 700 for D_v
  window opened by an occupant with prob p_w per minute when T_z > 24 and n_z > 0;
         closed after 10-40 min or when T_z < 20
Solar gain k_sol * max(0, sin(day phase)) peaking at 13:00. Setpoint 21 C during the occupied schedule (07:00-19:00 weekdays), 17 C otherwise.
"""
import json
import numpy as np
import pandas as pd

import os
SEED = int(os.environ.get("SEED", 7))
OUT_PREFIX = os.environ.get("OUT_PREFIX", "building")
DAYS = 60
MIN_PER_DAY = 1440
N = DAYS * MIN_PER_DAY
ZONES = ["A", "B", "C"]
ZONE_C_START_DAY = 30          # zone C instrumented (and occupied) from this day
FAULT_ZONE, FAULT_START, FAULT_END = "B", 40, 50   # damper stuck: vent effectiveness x0.1

K = dict(k_loss=0.0035, k_heat=0.15, k_win=0.05, k_vent=0.015, k_occ=0.004, k_sol=0.012,
         g_occ=6.0, k_x=0.004, k_xv=0.06, k_xw=0.08,
         m_occ=0.06, k_r=0.005, k_rv=0.05, k_rh=0.02,
         D_h=2, D_v=3, p_w=0.01,
         noise_T=0.03, noise_CO2=4.0, noise_RH=0.1)


def outdoor(rng):
    t = np.arange(N)
    day_phase = 2 * np.pi * (t / MIN_PER_DAY - 0.3)
    weather = np.zeros(N)
    w = 0.0
    for i in range(N):
        if i % MIN_PER_DAY == 0:
            w = 0.85 * w + rng.normal(0, 2.5)
        weather[i] = w
    T_out = 14 + 8 * np.sin(day_phase) + weather + rng.normal(0, 0.05, N)
    RH_out = np.clip(55 - 15 * np.sin(day_phase) - 1.5 * weather + rng.normal(0, 0.3, N), 20, 100)
    return T_out, RH_out


def occupancy_schedule(rng, start_day):
    """Minute-level head count for one zone: weekday office pattern with random arrivals,
    lunch, departures, occasional meetings; sparse on weekends."""
    n = np.zeros(N, int)
    for d in range(start_day, DAYS):
        base = d * MIN_PER_DAY
        weekday = (d % 7) < 5
        if weekday:
            k = rng.integers(3, 7)
            arrivals = sorted(rng.normal(8.5 * 60, 25, k).astype(int))
            leaves = sorted(rng.normal(17.5 * 60, 35, k).astype(int))
            lunch_out = rng.random(k) < 0.7
            for a, l, lo in zip(arrivals, leaves, lunch_out):
                a, l = max(0, a), min(MIN_PER_DAY - 1, l)
                n[base + a: base + l] += 1
                if lo:
                    ls = int(rng.normal(12.3 * 60, 15)); le = ls + int(rng.integers(30, 60))
                    n[base + max(a, ls): base + min(l, le)] -= 1
            if rng.random() < 0.5:   # a meeting: extra people for an hour
                ms = int(rng.choice([10 * 60, 14 * 60, 15 * 60]) + rng.integers(-20, 20))
                n[base + ms: base + ms + 60] += rng.integers(2, 5)
        else:
            if rng.random() < 0.3:
                a = int(rng.integers(9 * 60, 14 * 60)); n[base + a: base + a + rng.integers(60, 240)] += 1
    return np.clip(n, 0, None)


def simulate(seed=SEED):
    rng = np.random.default_rng(seed)
    T_out, RH_out = outdoor(rng)
    t = np.arange(N)
    solar = np.maximum(0.0, np.sin(2 * np.pi * (t / MIN_PER_DAY - 0.25)))  # peaks at 13:00
    day = t // MIN_PER_DAY
    minute_of_day = t % MIN_PER_DAY
    weekday = (day % 7) < 5
    occupied_sched = weekday & (minute_of_day >= 7 * 60) & (minute_of_day < 19 * 60)
    setpoint = np.where(occupied_sched, 21.0, 17.0)

    cols = {"minute": t, "day": day, "weekday": weekday.astype(int), "T_out": T_out, "RH_out": RH_out,
            "setpoint": setpoint}
    occ = {z: occupancy_schedule(rng, ZONE_C_START_DAY if z == "C" else 0) for z in ZONES}
    state = {z: dict(T=18.0, CO2=450.0, RH=45.0, h=0, v=0, w=0, h_cnt=0, v_cnt=0, w_timer=0) for z in ZONES}
    out = {z: dict(T=np.zeros(N), CO2=np.zeros(N), RH=np.zeros(N), heater=np.zeros(N, int),
                   vent=np.zeros(N, int), window=np.zeros(N, int)) for z in ZONES}
    for i in range(N):
        d = day[i]
        for z in ZONES:
            s = state[z]
            active = not (z == "C" and d < ZONE_C_START_DAY)
            n = occ[z][i] if active else 0
            eff = 0.1 if (z == FAULT_ZONE and FAULT_START <= d < FAULT_END) else 1.0
            sp = setpoint[i] if active else 15.0
            # control with delays
            if s["h"] == 0:
                s["h_cnt"] = s["h_cnt"] + 1 if s["T"] < sp - 1 else 0
                if s["h_cnt"] >= K["D_h"]:
                    s["h"], s["h_cnt"] = 1, 0
            else:
                s["h_cnt"] = s["h_cnt"] + 1 if s["T"] > sp + 1 else 0
                if s["h_cnt"] >= K["D_h"]:
                    s["h"], s["h_cnt"] = 0, 0
            if s["v"] == 0:
                s["v_cnt"] = s["v_cnt"] + 1 if s["CO2"] > 900 else 0
                if s["v_cnt"] >= K["D_v"]:
                    s["v"], s["v_cnt"] = 1, 0
            else:
                s["v_cnt"] = s["v_cnt"] + 1 if s["CO2"] < 700 else 0
                if s["v_cnt"] >= K["D_v"]:
                    s["v"], s["v_cnt"] = 0, 0
            if s["w"] == 0:
                if n > 0 and s["T"] > 23.5 and rng.random() < K["p_w"]:
                    s["w"], s["w_timer"] = 1, int(rng.integers(10, 41))
            else:
                s["w_timer"] -= 1
                if s["w_timer"] <= 0 or s["T"] < 20:
                    s["w"] = 0
            # physics
            dT = (K["k_loss"] * (T_out[i] - s["T"]) + K["k_heat"] * s["h"] + K["k_win"] * s["w"] * (T_out[i] - s["T"])
                  + K["k_vent"] * s["v"] * (T_out[i] - s["T"]) + K["k_occ"] * n + K["k_sol"] * solar[i] + rng.normal(0, K["noise_T"]))
            dC = (K["g_occ"] * n - K["k_x"] * (s["CO2"] - 420) - K["k_xv"] * eff * s["v"] * (s["CO2"] - 420)
                  - K["k_xw"] * s["w"] * (s["CO2"] - 420) + rng.normal(0, K["noise_CO2"]))
            dR = (K["m_occ"] * n - K["k_r"] * (s["RH"] - RH_out[i]) - K["k_rv"] * s["v"] * (s["RH"] - RH_out[i])
                  - K["k_rh"] * s["h"] + rng.normal(0, K["noise_RH"]))
            s["T"] += dT; s["CO2"] = max(400.0, s["CO2"] + dC); s["RH"] = float(np.clip(s["RH"] + dR, 10, 95))
            o = out[z]
            o["T"][i], o["CO2"][i], o["RH"][i] = s["T"], s["CO2"], s["RH"]
            o["heater"][i], o["vent"][i], o["window"][i] = s["h"], s["v"], s["w"]
    for z in ZONES:
        cols[f"occ_{z}"] = occ[z]
        for k, v in out[z].items():
            cols[f"{k}_{z}"] = v
    # zone C not instrumented before its start day: NaN
    for k in ("T", "CO2", "RH"):
        cols[f"{k}_C"][day < ZONE_C_START_DAY] = np.nan
    # chatty sensor: a vibration channel with its own fast dynamics, unrelated to the building
    vib = np.zeros(N); x = 0.0
    for i in range(N):
        x = 0.6 * x + rng.normal(0, 1.0); vib[i] = x
    cols["vibration"] = vib
    # dropouts on T_B: ~1% of minutes in random 5-20 minute gaps
    T_B = cols["T_B"].copy(); gaps = 0
    while gaps < 0.01 * N:
        s0 = int(rng.integers(N)); L = int(rng.integers(5, 21)); T_B[s0:s0 + L] = np.nan; gaps += L
    cols["T_B"] = T_B
    cols["power_kW"] = sum(1.5 * cols[f"heater_{z}"] + 0.3 * cols[f"vent_{z}"] for z in ZONES)
    df = pd.DataFrame(cols)
    df.insert(0, "timestamp", pd.Timestamp("2026-01-05 00:00") + pd.to_timedelta(df["minute"], unit="m"))
    return df


if __name__ == "__main__":
    df = simulate()
    df.to_csv(f"{OUT_PREFIX}_1min.csv.gz", index=False, float_format="%.3f")
    json.dump(dict(SEED=SEED, DAYS=DAYS, ZONES=ZONES, ZONE_C_START_DAY=ZONE_C_START_DAY,
                   FAULT=dict(zone=FAULT_ZONE, start_day=FAULT_START, end_day=FAULT_END), K=K),
              open(f"{OUT_PREFIX}_sim_params.json" if OUT_PREFIX != "building" else "sim_params.json", "w"), indent=2)
    print(df.shape); print(df.describe().T[["mean", "min", "max"]].round(2))
