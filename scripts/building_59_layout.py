"""
LBNL Building 59, Berkeley (Luo, Wang, Blum, Bourassa, Broughton, Weyandt, Piette & Hong 2022, Scientific Data,
doi:10.1038/s41597-022-01257-x; data doi:10.7941/D1N33Q, CC0 on Dryad / Zenodo 5951008) — the layout isomorph uses.
A real four-storey office building (2015, climate zone 3C): four packaged rooftop units (RTU 1–4) serving ~50
underfloor terminal zones (UFT: a fan and a hot-water valve per zone), with zone temperature sensors, zone cooling
and heating setpoints, CO2 in eleven zones, a site weather station, sub-metered electricity and occupancy counts.
2018-01-01 to 2020-12-31; most HVAC points at 1 min, setpoints at 5 min, weather and meters at 15 min. Dataset 8:
the real building — the same kind of system as the synthetic calibration buildings A and B′, in the world.

Declared at 5-minute means over the calendar year 2019 (the span in which every RTU point, the zone points and
the zone setpoints are all recorded; CO2 from 2019-08-19). Weather (15 min) is interpolated to the grid. A stretch
in which every point of a unit is missing for more than an hour is a gap for that unit; a single point's dropout
is left as missing (no events) and is not declared.

Entity candidates (3.1):
  unit  every zone (roles T, fan, hw_valve, Tsp_c, Tsp_h, co2) and every RTU (roles sa_t, sat_sp, ma_t, ra_t, oa_t,
        oa_damper, oa_flow, sa_flow, sf_spd, rf_spd, plenum_p, static_sp, econ_sp) as a unit; weather, meters and
        occupancy system-wide
  zone  zones only as units; the four RTUs' points system-wide (the air handlers as the zones' common environment)
  sys   one entity, every column its own role
"""
import os, re
import numpy as np
import pandas as pd

SAMPLE_MIN = 5.0
YEAR = 2019
FILES = ["rtu_sa_t", "rtu_sa_t_sp", "rtu_ma_t", "rtu_ra_t", "rtu_oa_t", "rtu_oa_damper", "rtu_oa_fr", "rtu_sa_fr", "rtu_fan_spd",
         "rtu_plenum_p", "rtu_sa_p_sp", "rtu_econ_sp", "uft_fan_spd", "uft_hw_valve", "zone_temp_exterior", "zone_temp_sp_c",
         "zone_temp_sp_h", "zone_co2", "site_weather", "ele", "wifi"]

RTU_ROLES = {  # role: (file, column pattern with {u} = unit number as in the csv, e.g. 001)
    "sa_t": ("rtu_sa_t", "rtu_{u}_sa_temp"), "sat_sp": ("rtu_sa_t_sp", "rtu_{u}_sat_sp_tn"), "ma_t": ("rtu_ma_t", "rtu_{u}_ma_temp"),
    "ra_t": ("rtu_ra_t", "rtu_{u}_ra_temp"), "oa_t": ("rtu_oa_t", "rtu_{u}_oa_temp"), "oa_damper": ("rtu_oa_damper", "rtu_{u}_oadmpr_pct"),
    "oa_flow": ("rtu_oa_fr", "rtu_{u}_oa_flow_tn"), "sa_flow": ("rtu_sa_fr", "rtu_{u}_fltrd_sa_flow_tn"),
    "sf_spd": ("rtu_fan_spd", "rtu_{u}_sf_vfd_spd_fbk_tn"), "rf_spd": ("rtu_fan_spd", "rtu_{u}_rf_vfd_spd_fbk_tn"),
    "plenum_p": ("rtu_plenum_p", "rtu_{u}_fltrd_gnd_lvl_plenum_press_tn"), "static_sp": ("rtu_sa_p_sp", "rtu_{u}_pa_static_stpt_tn"),
    "econ_sp": ("rtu_econ_sp", "rtu_{u}_econ_stpt_tn"),
}
ZONE_ROLES = {"T": ("zone_temp_exterior", "zone_{z}_temp"), "fan": ("uft_fan_spd", "zone_{z}_fan_spd"), "hw_valve": ("uft_hw_valve", "zone_{z}_hw_valve"),
              "Tsp_c": ("zone_temp_sp_c", "zone_{z}_cooling_sp"), "Tsp_h": ("zone_temp_sp_h", "zone_{z}_heating_sp"), "co2": ("zone_co2", "zone_{z}_co2")}
SYSTEM_ROLES = {"T_out": ("site_weather", "air_temp_set_1"), "solar": ("site_weather", "solar_radiation_set_1"), "rh_out": ("site_weather", "relative_humidity_set_1"),
                "hvac_kw_N": ("ele", "hvac_N"), "hvac_kw_S": ("ele", "hvac_S"), "wifi_3S": ("wifi", "wifi_third_south"), "wifi_4S": ("wifi", "wifi_fourth_south")}

# Dimensions (v5 suffix). Temperatures are °F (⟨Θ⟩ regardless of scale); flows cfm; plenum pressure and its setpoint in. w.c.;
# speeds, damper and valve positions in %; CO2 in ppm (dimensionless); meters in kW; solar in W/m²; counts dimensionless.
DIMENSION = {"sa_t": "temperature", "sat_sp": "temperature", "ma_t": "temperature", "ra_t": "temperature", "oa_t": "temperature",
             "oa_damper": None, "oa_flow": "volume_flow", "sa_flow": "volume_flow", "sf_spd": None, "rf_spd": None,
             "plenum_p": "pressure", "static_sp": "pressure", "econ_sp": "temperature",
             "T": "temperature", "fan": None, "hw_valve": None, "Tsp_c": "temperature", "Tsp_h": "temperature", "co2": None,
             "T_out": "temperature", "solar": "irradiance", "rh_out": None, "hvac_kw_N": "power", "hvac_kw_S": "power", "wifi_3S": None, "wifi_4S": None}

# Mechanisms true by construction of a packaged-RTU / underfloor-terminal building (cause -> effect, role names).
MECHANISMS = [
    dict(cause="hw_valve", effect="T", note="zone hot-water valve -> zone temperature (heating)"),
    dict(cause="fan", effect="T", note="zone terminal fan speed -> zone temperature (supply air delivered)"),
    dict(cause="Tsp_h", effect="hw_valve", note="heating setpoint -> valve (zone loop)"),
    dict(cause="Tsp_c", effect="fan", note="cooling setpoint -> terminal fan (zone loop)"),
    dict(cause="oa_damper", effect="ma_t", note="outdoor-air damper -> mixed-air temperature"),
    dict(cause="oa_damper", effect="oa_flow", note="outdoor-air damper -> outdoor-air flow"),
    dict(cause="sf_spd", effect="sa_flow", note="supply fan speed -> supply airflow"),
    dict(cause="sf_spd", effect="plenum_p", note="supply fan speed -> underfloor plenum pressure"),
    dict(cause="static_sp", effect="sf_spd", note="static-pressure setpoint -> supply fan speed (AHU loop)"),
    dict(cause="sat_sp", effect="sa_t", note="supply-air temperature setpoint -> supply-air temperature (AHU loop)"),
    dict(cause="ma_t", effect="sa_t", note="mixed-air temperature -> supply-air temperature"),
]


def _load(raw_dir, name):
    p = os.path.join(raw_dir, name + ".csv")
    d = pd.read_csv(p, low_memory=False)
    d = d.rename(columns={d.columns[0]: "time"}); d["time"] = pd.to_datetime(d["time"], errors="coerce", utc=True)
    d = d.dropna(subset=["time"]).set_index("time").sort_index()
    d = d[[c for c in d.columns if not c.startswith("Unnamed")]]
    return d.apply(pd.to_numeric, errors="coerce")


def load_year(raw_dir, year=YEAR, resample_minutes=SAMPLE_MIN):
    """One frame at `resample_minutes` means over the calendar year, columns named <unit>_<role>; weather interpolated."""
    t0, t1 = pd.Timestamp(f"{year}-01-01", tz="UTC"), pd.Timestamp(f"{year + 1}-01-01", tz="UTC")
    grid = pd.date_range(t0, t1, freq=f"{int(resample_minutes)}min", inclusive="left")
    frames = {}
    for name in FILES:
        if not os.path.exists(os.path.join(raw_dir, name + ".csv")): continue
        d = _load(raw_dir, name); d = d[(d.index >= t0 - pd.Timedelta(hours=1)) & (d.index < t1 + pd.Timedelta(hours=1))]
        step = d.index.to_series().diff().dt.total_seconds().median() if len(d) > 1 else np.nan
        if step and step > resample_minutes * 60:      # weather, meters: interpolate the coarser series to the grid
            r = d.reindex(d.index.union(grid)).interpolate(method="time", limit=int(2 * step / 60 / resample_minutes)).reindex(grid)
        else:                                           # 1-min / 5-min points: means within the grid step
            r = d.resample(f"{int(resample_minutes)}min", label="left", closed="left").mean().reindex(grid)
        frames[name] = r
    out = pd.DataFrame(index=grid)
    units, zones = [], []
    for u in ("001", "002", "003", "004"):
        for role, (f, pat) in RTU_ROLES.items():
            col = pat.format(u=u)
            if f in frames and col in frames[f].columns: out[f"rtu{u[-1]}_{role}"] = frames[f][col].values
        units.append(f"rtu{u[-1]}")
    zone_ids = sorted(set(re.findall(r"zone_(\d+)_temp", " ".join(frames["zone_temp_exterior"].columns)))) if "zone_temp_exterior" in frames else []
    for z in zone_ids:
        any_col = False
        for role, (f, pat) in ZONE_ROLES.items():
            col = pat.format(z=z)
            if f in frames and col in frames[f].columns: out[f"zone{z}_{role}"] = frames[f][col].values; any_col = True
        if any_col: zones.append(f"zone{z}")
    for role, (f, col) in SYSTEM_ROLES.items():
        if f in frames and col in frames[f].columns: out[f"sys_{role}"] = frames[f][col].values
    out = out.reset_index(drop=True)
    out["minute"] = np.arange(len(out)) * resample_minutes
    return out, units, zones


def unit_layout(df, units, zones):
    """Every zone and every RTU a unit with its own roles; weather, meters and occupancy system-wide."""
    ents, kinds = {}, {}
    for u in units:
        cols = {r: f"{u}_{r}" for r in RTU_ROLES if f"{u}_{r}" in df.columns and df[f"{u}_{r}"].notna().any() and df[f"{u}_{r}"].nunique() > 1}
        if cols: ents[u] = cols; kinds.update({r: "continuous" for r in cols})
    for z in zones:
        cols = {r: f"{z}_{r}" for r in ZONE_ROLES if f"{z}_{r}" in df.columns and df[f"{z}_{r}"].notna().any() and df[f"{z}_{r}"].nunique() > 1}
        if cols: ents[z] = cols; kinds.update({r: "continuous" for r in cols})
    system = {r: f"sys_{r}" for r in SYSTEM_ROLES if f"sys_{r}" in df.columns and df[f"sys_{r}"].notna().any() and df[f"sys_{r}"].nunique() > 1}
    kinds.update({r: "continuous" for r in system})
    return dict(time="minute", entities=ents, system=system, kinds=kinds, observation={})


def zone_layout(df, units, zones):
    """Zones as units; the four RTUs' points become system-wide roles (rtu1_sa_t, ...), as the zones' common environment."""
    lay = unit_layout(df, units, zones)
    ents = {z: c for z, c in lay["entities"].items() if z.startswith("zone")}
    system = dict(lay["system"])
    kinds = {r: k for r, k in lay["kinds"].items() if r in ZONE_ROLES or r in SYSTEM_ROLES}
    for u in units:
        for r, col in lay["entities"].get(u, {}).items():
            system[f"{u}_{r}"] = col; kinds[f"{u}_{r}"] = "continuous"
    return dict(time="minute", entities=ents, system=system, kinds=kinds, observation={})


def unit_gaps(df, layout, min_hours=1.0):
    """(entity, start, end, reason) for stretches longer than `min_hours` in which every point of a unit is missing."""
    out = []
    for ent, cols in layout["entities"].items():
        miss = df[list(cols.values())].isna().all(axis=1).values
        if not miss.any(): continue
        edges = np.flatnonzero(np.diff(np.r_[0, miss.astype(int), 0]))
        for s, e in zip(edges[::2], edges[1::2]):
            if (e - s) * SAMPLE_MIN >= min_hours * 60:
                out.append((ent, float(df.minute.values[s]), float(min(df.minute.values[e - 1] + SAMPLE_MIN, df.minute.values[-1] + 1)), "all points of the unit missing"))   # inside the observation window (ends at t.max() + 1)
    return out
