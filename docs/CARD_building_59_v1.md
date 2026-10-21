# Benchmark card — LBNL Building 59 (dataset 8), method v7, profile v1, seed 0

Run 2026-10-21. Source: Luo, Wang, Blum, Bourassa, Broughton, Weyandt, Piette & Hong 2022, *Scientific Data*
(doi:10.1038/s41597-022-01257-x); data doi:10.7941/D1N33Q (Dryad, CC0; mirrored at Zenodo 5951008, which is what
the fetch script reads — Dryad's file streams refuse unauthenticated downloads). A four-storey office building in
Berkeley (2015, climate zone 3C): four packaged rooftop units serving ~50 underfloor terminal zones, each with a
fan and a hot-water valve; zone temperatures, cooling and heating setpoints, CO2 in eleven zones; a site weather
station, sub-metered electricity, occupancy counts. 2018–2020, most HVAC points at 1 min. **The real building:**
the calibration buildings A and B′ are synthetic models of this kind of system.

## Declarations

- **Calendar year 2019 at 5-minute means.** Every RTU point, the zone points and the zone setpoints are recorded
  through 2019 (setpoints begin 2018-09, CO2 2019-08); RTU and zone points at 1 min are averaged, setpoints at 5
  min are on the grid, weather and meters at 15 min are interpolated. 2018 and 2020 are held as continuations.
- **Entity by 3.1 between `unit`** (every zone and every RTU a unit with its own roles; weather, meters and
  occupancy system-wide) **and `zone`** (zones only, the four RTUs' points system-wide): unit 4.937 vs zone 5.093
  bits/event Markov-only → **unit**, 55 entities. A single-system layout was not run: 299 roles make ~1,800 types,
  beyond what the Markov-only comparison (adjacent-pair features over the vocabulary squared) can fit.
- **Gaps**: a stretch of an hour or more in which every point of a unit is missing is a gap for that unit (147,
  mostly the first eight days of the year for the zones); a single point's dropout is a missing value, not
  declared. Solar radiation emits no events (no scheme reconstructs it within half its spread at 5-min means:
  the diurnal ramp is too smooth for turning points and too skewed for quantiles).

## Identity and scale

| | |
| --- | --- |
| Entity | **unit** (rtu1–4; zone016 … zone072, 51 zones), 55 entities |
| Symbolization (3.2) | 23 roles: quantile q20/50/80 for temperatures, flows, speeds, pressure and setpoints; q10/90 for the damper, the fan, the valve and the north meter (limit-hitting actuators); turning points for mixed, return and outdoor air temperatures; solar silent |
| Events | 276,110 in 365 days (757/day); 89 target types (111 with the system-wide) |
| Lag classes (3.3) | 27 min / 2.5 h / 13.7 h (recurrence horizon 13.7 h) |
| Period (3.4) | slow 1,367 min (the day, as in the synthetic buildings' 1,440); no fast period |
| Admission (section 6) | 365 days · 641 H (test 160 H) · 385 slow periods → **admitted** |
| Nulls (3.8) | circular 0.29; cycle 0.30; rewire 0.32 |
| Discovery | 12,504 candidates → **1,285 validated fragments** (237 used), 0 compositions; chatty share 0.17 |
| Syntax (3.15) | 25,019 chain candidates → 2,897 with conditional lift → 2,799 above the null → **1,044 admitted, 299 returns**; none reduce confirmation bits |
| Test split | 70,277 events (the last 91 days), evaluated once |

## Headline (bits per event on the test split)

| model | all |
| --- | --- |
| unigram | 5.843 |
| markov-1 / -2 / -3 | 3.614 / 3.533 / 3.821 |
| hawkes-like decay features | 3.368 |
| logistic markov features | **3.235** |
| logistic triviality library (3.11) | 2.638 |
| logistic library | 2.760 |
| logistic unselected contexts | 2.758 |

Gain over triviality **−0.122** bits; over the best baseline (logistic Markov, 3.235) +0.476 → claim: **no gain**.

## Reading the result

**Recovery 9 of 11** — the best in the collection: valve → zone temperature, fan → zone temperature, heating
setpoint → valve, cooling setpoint → fan, damper → mixed-air temperature, damper → outdoor-air flow, supply fan →
airflow, supply fan → plenum pressure, mixed-air → supply-air temperature are all in the library. The two not
found are the AHU setpoint loops (static-pressure setpoint → fan speed, supply-air setpoint → supply-air
temperature): the setpoints are `SET` roles that step a few times a year.

**The triviality baseline carries the building.** 50 thermostatic zones cycling between their bands are 50
copies of an alternation, and the alternation model at 2.638 beats the library at 2.760, as it did on building A
(gain 0.005) and HAI. Over the Markov baselines the library gains 0.48 bits, the largest such margin so far; the
rule reports the smaller number.

**Loop roles (3.16) — the first plant on which the checks pass.** 214 of 299 returns resolved. Tags: **oa_damper
REACTS** (37 to 24), **fan REACTS** (5 to 1), oa_flow, sa_flow, rf_spd REACTS; **T RESPONDS** (11 to 7), ma_t,
ra_t, plenum_p, sf_spd RESPONDS; hw_valve and sa_t tied (9 to 9, 18 to 18), untagged.

| check | result | chance |
| --- | --- | --- |
| dimension: REACTS roles dimensionless | 3 of 6 (0.50) | 0.5 |
| dimension: RESPONDS roles dimensioned | 4 of 5 (**0.80**) | 0.5 |
| flowsheet: actuator on the REACTS side of actuator–measurement returns | 35 of 56 (**0.63**) | 0.5 |

The strongest returns are the economizer loop and they read as 3.16 said negative feedback would:
`oa_damper:downq90 -s-> ma_t:peak -s-> oa_damper:upq90` (n 13, cond. lift 12.1), spelled
`MID-S·REACTS.down.q90 -s-> MID·RESPONDS.peak -s-> MID-S·REACTS.up.q90 [return]` — the damper closes, the
mixed-air temperature peaks, the damper reopens — and the damper's returns through the return-fan speed and the
return-air temperature (lifts 10.5, 8.5) with the damper on REACTS and the temperatures on RESPONDS. The supply-fan
loop reads the other way (`sf_spd:upq80 -s-> plenum_p:upq80 -s-> sf_spd:downq80`, n 31: the fan responds, the
plenum pressure reacts), which is what a fan on a static-pressure loop with a slow VFD ramp does: the pressure
answers within a sample, the fan's speed ramps.

## Open items raised by this dataset (not rules)

1. **Single-system candidates at this width.** 3.1 asks for a `sys` candidate; 299 roles cannot be fitted by the
   Markov-only comparison. A rule for when the single-system candidate is skipped (types above some count), or
   a cheaper comparison for it, is needed before the next wide dataset.
2. **Zones as a population.** 51 thermostatic zones give the triviality baseline 50 alternations; the same
   question HAI and the battery raised, with the largest numbers yet.
3. **Setpoint loops at the AHU** step a few times a year and are not recovered; a year is not long enough for
   `SET` roles that change seasonally — the 2018 and 2020 continuations would be the test.
