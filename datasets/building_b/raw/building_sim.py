"""
building_sim.py — configurable version of simulate_building.py, used to make a
SECOND building (B') with different parameters, more zones and an extra loop.
Building A's files were produced by simulate_building.py and are unchanged.

Differences available through cfg: number of zones, time constants, control
thresholds and delays, setpoints and schedule, occupancy size, outdoor climate,
an optional dehumidifier loop (dehum on when RH > rh_on for D_d min, off when
RH < rh_off; removes moisture at k_dh %/min and adds a little heat), a fault
window, a late zone.
"""
import numpy as np
import pandas as pd

MIN_PER_DAY = 1440


def default_cfg():
    return dict(
        seed=7, days=60, zones=["A", "B", "C"], late_zone="C", late_start_day=30,
        fault=dict(zone="B", start=40, end=50, eff=0.1),
        K=dict(k_loss=0.0035, k_heat=0.15, k_win=0.05, k_vent=0.015, k_occ=0.004, k_sol=0.012,
               g_occ=6.0, k_x=0.004, k_xv=0.06, k_xw=0.08,
               m_occ=0.06, k_r=0.005, k_rv=0.05, k_rh=0.02,
               D_h=2, D_v=3, p_w=0.01, noise_T=0.03, noise_CO2=4.0, noise_RH=0.1),
        co2_on=900, co2_off=700, sp_day=21.0, sp_night=17.0, sched=(7, 19), band=1.0,
        window_T=23.5, occ_k=(3, 7), arrive_h=8.5, leave_h=17.5,
        T_out_mean=14, T_out_amp=8, RH_out_mean=55,
        dehum=None,   # or dict(rh_on=65, rh_off=55, D_d=2, k_dh=0.25, heat=0.01)
    )


def outdoor(rng, cfg, N):
    t = np.arange(N)
    ph = 2 * np.pi * (t / MIN_PER_DAY - 0.3)
    weather = np.zeros(N); w = 0.0
    for i in range(N):
        if i % MIN_PER_DAY == 0:
            w = 0.85 * w + rng.normal(0, 2.5)
        weather[i] = w
    T_out = cfg["T_out_mean"] + cfg["T_out_amp"] * np.sin(ph) + weather + rng.normal(0, 0.05, N)
    RH_out = np.clip(cfg["RH_out_mean"] - 15 * np.sin(ph) - 1.5 * weather + rng.normal(0, 0.3, N), 20, 100)
    return T_out, RH_out


def occupancy_schedule(rng, cfg, start_day, N):
    n = np.zeros(N, int)
    for d in range(start_day, cfg["days"]):
        base = d * MIN_PER_DAY
        if (d % 7) < 5:
            k = rng.integers(*cfg["occ_k"])
            arrivals = sorted(rng.normal(cfg["arrive_h"] * 60, 25, k).astype(int))
            leaves = sorted(rng.normal(cfg["leave_h"] * 60, 35, k).astype(int))
            lunch_out = rng.random(k) < 0.7
            for a, l, lo in zip(arrivals, leaves, lunch_out):
                a, l = max(0, a), min(MIN_PER_DAY - 1, l)
                n[base + a: base + l] += 1
                if lo:
                    ls = int(rng.normal(12.3 * 60, 15)); le = ls + int(rng.integers(30, 60))
                    n[base + max(a, ls): base + min(l, le)] -= 1
            if rng.random() < 0.5:
                ms = int(rng.choice([10 * 60, 14 * 60, 15 * 60]) + rng.integers(-20, 20))
                n[base + ms: base + ms + 60] += rng.integers(2, 5)
        elif rng.random() < 0.3:
            a = int(rng.integers(9 * 60, 14 * 60)); n[base + a: base + a + rng.integers(60, 240)] += 1
    return np.clip(n, 0, None)


def simulate(cfg):
    rng = np.random.default_rng(cfg["seed"])
    N = cfg["days"] * MIN_PER_DAY
    K = cfg["K"]
    T_out, RH_out = outdoor(rng, cfg, N)
    t = np.arange(N); day = t // MIN_PER_DAY; mod = t % MIN_PER_DAY
    weekday = (day % 7) < 5
    occ_s = weekday & (mod >= cfg["sched"][0] * 60) & (mod < cfg["sched"][1] * 60)
    setpoint = np.where(occ_s, cfg["sp_day"], cfg["sp_night"])
    solar = np.maximum(0.0, np.sin(2 * np.pi * (t / MIN_PER_DAY - 0.25)))
    cols = {"minute": t, "day": day, "weekday": weekday.astype(int), "T_out": T_out, "RH_out": RH_out, "setpoint": setpoint}
    zones = cfg["zones"]
    occ = {z: occupancy_schedule(rng, cfg, cfg["late_start_day"] if z == cfg["late_zone"] else 0, N) for z in zones}
    st = {z: dict(T=18.0, CO2=450.0, RH=45.0, h=0, v=0, w=0, dh=0, h_cnt=0, v_cnt=0, d_cnt=0, w_timer=0) for z in zones}
    out = {z: {k: np.zeros(N, int if k in ("heater", "vent", "window", "dehum") else float)
               for k in ("T", "CO2", "RH", "heater", "vent", "window", "dehum")} for z in zones}
    dh = cfg["dehum"]; fault = cfg["fault"]
    for i in range(N):
        d = day[i]
        for z in zones:
            s = st[z]
            active = not (z == cfg["late_zone"] and d < cfg["late_start_day"])
            n = occ[z][i] if active else 0
            eff = fault["eff"] if (fault and z == fault["zone"] and fault["start"] <= d < fault["end"]) else 1.0
            sp = setpoint[i] if active else 15.0
            b = cfg["band"]
            if s["h"] == 0:
                s["h_cnt"] = s["h_cnt"] + 1 if s["T"] < sp - b else 0
                if s["h_cnt"] >= K["D_h"]: s["h"], s["h_cnt"] = 1, 0
            else:
                s["h_cnt"] = s["h_cnt"] + 1 if s["T"] > sp + b else 0
                if s["h_cnt"] >= K["D_h"]: s["h"], s["h_cnt"] = 0, 0
            if s["v"] == 0:
                s["v_cnt"] = s["v_cnt"] + 1 if s["CO2"] > cfg["co2_on"] else 0
                if s["v_cnt"] >= K["D_v"]: s["v"], s["v_cnt"] = 1, 0
            else:
                s["v_cnt"] = s["v_cnt"] + 1 if s["CO2"] < cfg["co2_off"] else 0
                if s["v_cnt"] >= K["D_v"]: s["v"], s["v_cnt"] = 0, 0
            if dh:
                if s["dh"] == 0:
                    s["d_cnt"] = s["d_cnt"] + 1 if s["RH"] > dh["rh_on"] else 0
                    if s["d_cnt"] >= dh["D_d"]: s["dh"], s["d_cnt"] = 1, 0
                else:
                    s["d_cnt"] = s["d_cnt"] + 1 if s["RH"] < dh["rh_off"] else 0
                    if s["d_cnt"] >= dh["D_d"]: s["dh"], s["d_cnt"] = 0, 0
            if s["w"] == 0:
                if n > 0 and s["T"] > cfg["window_T"] and rng.random() < K["p_w"]:
                    s["w"], s["w_timer"] = 1, int(rng.integers(10, 41))
            else:
                s["w_timer"] -= 1
                if s["w_timer"] <= 0 or s["T"] < 20: s["w"] = 0
            dT = (K["k_loss"] * (T_out[i] - s["T"]) + K["k_heat"] * s["h"] + K["k_win"] * s["w"] * (T_out[i] - s["T"])
                  + K["k_vent"] * s["v"] * (T_out[i] - s["T"]) + K["k_occ"] * n + K["k_sol"] * solar[i]
                  + (dh["heat"] * s["dh"] if dh else 0) + rng.normal(0, K["noise_T"]))
            dC = (K["g_occ"] * n - K["k_x"] * (s["CO2"] - 420) - K["k_xv"] * eff * s["v"] * (s["CO2"] - 420)
                  - K["k_xw"] * s["w"] * (s["CO2"] - 420) + rng.normal(0, K["noise_CO2"]))
            dR = (K["m_occ"] * n - K["k_r"] * (s["RH"] - RH_out[i]) - K["k_rv"] * s["v"] * (s["RH"] - RH_out[i])
                  - K["k_rh"] * s["h"] - (dh["k_dh"] * s["dh"] if dh else 0) + rng.normal(0, K["noise_RH"]))
            s["T"] += dT; s["CO2"] = max(400.0, s["CO2"] + dC); s["RH"] = float(np.clip(s["RH"] + dR, 10, 95))
            o = out[z]
            o["T"][i], o["CO2"][i], o["RH"][i] = s["T"], s["CO2"], s["RH"]
            o["heater"][i], o["vent"][i], o["window"][i], o["dehum"][i] = s["h"], s["v"], s["w"], s["dh"]
    for z in zones:
        cols[f"occ_{z}"] = occ[z]
        for k, v in out[z].items():
            if k == "dehum" and not dh:
                continue
            cols[f"{k}_{z}"] = v
    if cfg["late_zone"]:
        for k in ("T", "CO2", "RH"):
            cols[f"{k}_{cfg['late_zone']}"][day < cfg["late_start_day"]] = np.nan
    vib = np.zeros(N); x = 0.0
    for i in range(N):
        x = 0.6 * x + rng.normal(0, 1.0); vib[i] = x
    cols["vibration"] = vib
    df = pd.DataFrame(cols)
    df.insert(0, "timestamp", pd.Timestamp("2026-01-05 00:00") + pd.to_timedelta(df["minute"], unit="m"))
    return df


CFG_B = dict(default_cfg())
CFG_B.update(dict(
    seed=11, zones=["Z1", "Z2", "Z3", "Z4"], late_zone=None,
    fault=dict(zone="Z3", start=42, end=50, eff=0.1),
    co2_on=1000, co2_off=750, sp_day=22.0, sp_night=18.0, sched=(8, 18), band=0.8,
    window_T=24.0, occ_k=(4, 9), arrive_h=9.0, leave_h=18.0,
    T_out_mean=12, T_out_amp=9, RH_out_mean=60,
    dehum=dict(rh_on=65, rh_off=55, D_d=2, k_dh=0.25, heat=0.01),
))
CFG_B["K"] = dict(default_cfg()["K"]); CFG_B["K"].update(dict(k_loss=0.005, k_heat=0.12, k_vent=0.02, D_h=3, D_v=2, p_w=0.008, g_occ=5.0))

# symbolization thresholds matched to each building's own control bands
THRESH_B = {"T": [21, 24], "CO2": [800, 1000], "RH": [55, 65], "T_out": [12, 22], "vibration": [-2, 2]}

if __name__ == "__main__":
    import json
    df = simulate(CFG_B)
    df.to_csv("building2_1min.csv.gz", index=False, float_format="%.3f")
    json.dump(CFG_B, open("building2_cfg.json", "w"), indent=1, default=str)
    print(df.shape)
    for z in CFG_B["zones"]:
        for v in ("heater", "vent", "window", "dehum"):
            x = df[f"{v}_{z}"].values
            print(z, v, "on-events", int(((x[1:] == 1) & (x[:-1] == 0)).sum()), "duty", round(float(x.mean()), 3))
