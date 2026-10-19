"""
Tennessee Eastman (Downs & Vogel 1993; Ricker's revised model, Bathelt et al. 2014) — the layout
isomorph uses for the 1-year continuous run published by Souza, de Souza & da Silva (2023),
https://github.com/anasouzac/new_tep_datasets (matlab_data_1year.csv: 175,200 samples at 3 min,
XMEAS(1..41), XMV(1..11), STATUS = active fault IDV 0..20).

Variable meanings are the standard table (Downs & Vogel, Table 4/5). The entity candidates are:
  vessel  reactor / separator / stripper, each with roles P (pressure), L (level), T (temperature)
          and the unit-specific extras it has; everything else (feeds, purge, compressor,
          analysers, feed valves) is system-wide
  sys     one entity, every column its own role
STATUS is NOT an observed variable and is kept out of the events; it is recorded in the sidecar
as regime annotations. XMV(5) and XMV(9) are constant in this control structure and are omitted.
"""
import numpy as np
import pandas as pd

SAMPLE_MIN = 3.0

VESSELS = {
    "reactor":   {"P": "XMEAS(7)", "L": "XMEAS(8)", "T": "XMEAS(9)", "cw_out": "XMEAS(21)", "cw_flow": "XMV(10)", "feed": "XMEAS(6)"},
    "separator": {"P": "XMEAS(13)", "L": "XMEAS(12)", "T": "XMEAS(11)", "cw_out": "XMEAS(22)", "cw_flow": "XMV(11)",
                  "underflow": "XMEAS(14)", "underflow_valve": "XMV(7)"},
    "stripper":  {"P": "XMEAS(16)", "L": "XMEAS(15)", "T": "XMEAS(18)", "underflow": "XMEAS(17)", "underflow_valve": "XMV(8)",
                  "steam": "XMEAS(19)"},
}
SYSTEM_ROLES = {
    "A_feed": "XMEAS(1)", "D_feed": "XMEAS(2)", "E_feed": "XMEAS(3)", "AC_feed": "XMEAS(4)", "recycle": "XMEAS(5)",
    "purge": "XMEAS(10)", "compressor": "XMEAS(20)",
    "D_valve": "XMV(1)", "E_valve": "XMV(2)", "A_valve": "XMV(3)", "AC_valve": "XMV(4)", "purge_valve": "XMV(6)",
    # analysers: reactor feed (stream 6) A..F, purge (stream 9) A..H, product (stream 11) D..H
    **{f"feed_{c}": f"XMEAS({23 + i})" for i, c in enumerate("ABCDEF")},
    **{f"purge_{c}": f"XMEAS({29 + i})" for i, c in enumerate("ABCDEFGH")},
    **{f"prod_{c}": f"XMEAS({37 + i})" for i, c in enumerate("DEFGH")},
}
ROLES = sorted(set(r for v in VESSELS.values() for r in v) | set(SYSTEM_ROLES))

# Mechanisms true by construction (Downs & Vogel's table: each manipulated variable and the stream
# it manipulates, plus the two cooling-water loops). Direction is actuator -> measurement. The
# answer key lists cause/effect ROLE names; the pipeline's recovery check matches on type prefixes.
MECHANISMS = [
    dict(cause="D_valve", effect="D_feed", note="XMV(1) sets stream 2 flow"),
    dict(cause="E_valve", effect="E_feed", note="XMV(2) sets stream 3 flow"),
    dict(cause="A_valve", effect="A_feed", note="XMV(3) sets stream 1 flow"),
    dict(cause="AC_valve", effect="AC_feed", note="XMV(4) sets stream 4 flow"),
    dict(cause="purge_valve", effect="purge", note="XMV(6) sets stream 9 flow"),
    dict(cause="underflow_valve", effect="underflow", note="XMV(7)/XMV(8) set streams 10/11 (per vessel)"),
    dict(cause="cw_flow", effect="cw_out", note="cooling water flow -> its outlet temperature (reactor, separator)"),
    dict(cause="cw_flow", effect="T", note="cooling water flow -> vessel temperature (reactor, separator)"),
    dict(cause="steam", effect="T", note="stripper steam -> stripper temperature"),
    dict(cause="underflow", effect="L", note="underflow -> level (separator, stripper)"),
]

FAULTS = {0: "normal", 1: "A/C feed ratio step (stream 4)", 2: "B composition step (stream 4)", 3: "D feed temperature step",
          4: "reactor cooling water inlet temperature step", 5: "condenser cooling water inlet temperature step",
          6: "A feed loss (stream 1)", 7: "C header pressure loss", 8: "A,B,C feed composition random variation",
          9: "D feed temperature random variation", 10: "C feed temperature random variation",
          11: "reactor cooling water inlet temperature random variation", 12: "condenser cooling water inlet temperature random variation",
          13: "reaction kinetics slow drift", 14: "reactor cooling water valve sticking", 15: "condenser cooling water valve sticking",
          16: "unknown", 17: "unknown", 18: "unknown", 19: "unknown", 20: "unknown"}


def load(path):
    df = pd.read_csv(path, index_col=0)
    df["minute"] = np.arange(len(df)) * SAMPLE_MIN
    return df


def vessel_layout():
    kinds = {r: "continuous" for r in ROLES}
    return dict(time="minute", entities={v: dict(cols) for v, cols in VESSELS.items()}, system=dict(SYSTEM_ROLES), kinds=kinds, observation={})


def regimes(df):
    """Fault episodes from STATUS: list of (start_minute, end_minute, fault_id)."""
    f = df["STATUS"].values.astype(int); ch = np.flatnonzero(np.diff(f) != 0) + 1
    starts = np.r_[0, ch]; ends = np.r_[ch, len(f)]
    return [dict(start=float(s * SAMPLE_MIN), end=float(e * SAMPLE_MIN), fault=int(f[s]), label=FAULTS[int(f[s])]) for s, e in zip(starts, ends)]
