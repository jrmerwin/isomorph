# Transfer matrix — methods v3 to v8, profile v1 (2026-10-19 to 2026-10-21)

Cells are **net bit-days**: the area between the receiver's own learning curve and the curve of its model
mixed with the translated source model, minus the same area for the source model sent through a permuted
mapping (3.12, v3). The control removes what any smooth foreign model gives a data-starved receiver —
regularisation — and leaves what the correspondence gives.

## v8 (2026-10-21): derangement controls, the curve in receiver horizons — seed 0; datasets 1–9

Cells are now in **bit-horizons** (bits × the receiver's recurrence horizon H) on the receiver's observed training
time, integrated to 200 H or the end of training (3.12, v8); the control is the median of ten *derangements* (no
mapped type keeps its learned counterpart), the group widened only as far as needed. *moved* is the share of
mapped types moved at the narrowest width and at full width. The v7 column is the old bit-day cell, for the
record; the two units are not convertible across receivers (H is 143 min on TEP, 13.7 h on Building 59, 16 s on
PhysioNet). `short`: the receiver trains on fewer than 200 H (HAI 126, battery 161, PhysioNet 10). `damage`: the
receiver's unmapped types got worse under the mixture. The timing loop tag is out of alignment again (3.16, v8).

| source → receiver | zero-shot (learned) | zero-shot (derangement) | raw cell (bit-H) | control cell | **net cell** | moved | v7 net (bit-days) | types mapped | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TEP → HAI | 7.630 (shared 7.261) | 9.003 | 39.91 | 26.19 | **13.72** | 1.00/1.00 | 0.90 | 142/168 | short, damage |
| HAI → TEP | 6.629 (shared 6.381) | 8.471 | 89.42 | 40.83 | **48.59** | 1.00/1.00 | 7.96 | 34/40 | damage |
| TEP → battery | 3.681 (shared 3.681) | 5.425 | 0.15 | -0.35 | **0.50** | 1.00/1.00 | 0.25 | 12/12 | short |
| battery → TEP | 8.772 (shared 3.504) | 9.031 | 26.79 | 18.33 | **8.46** | 1.00/1.00 | 1.65 | 6/40 | damage |
| HAI → battery | 4.721 (shared 4.721) | 4.808 | -0.28 | -0.39 | **0.11** | 1.00/1.00 | -0.03 | 12/12 | short |
| battery → HAI | 9.466 (shared 4.201) | 9.445 | 29.73 | 29.56 | **0.17** | 1.00/1.00 | 0.09 | 10/168 | short |
| TEP → PhysioNet | 5.382 (shared 5.382) | 5.355 | 0.00 | 0.00 | **0.00** | 1.00/1.00 | 0.00 | 10/10 |  |
| PhysioNet → TEP | 6.632 (shared 4.145) | 8.728 | 81.03 | 19.13 | **61.91** | 1.00/1.00 | 18.08 | 4/40 | damage |
| HAI → PhysioNet | 6.998 (shared 6.998) | 6.781 | 0.00 | 0.00 | **0.00** | 1.00/1.00 | -0.02 | 10/10 |  |
| PhysioNet → HAI | 7.542 (shared 6.975) | 8.245 | 37.84 | 32.88 | **4.97** | 1.00/1.00 | 0.39 | 4/168 | short, damage |
| battery → PhysioNet | 4.425 (shared 3.795) | 4.427 | 0.00 | 0.00 | **0.00** | 1.00/1.00 | 0.00 | 2/10 |  |
| PhysioNet → battery | 6.762 (shared 1.619) | 6.789 | -0.27 | -0.29 | **0.02** | 1.00/1.00 | 0.00 | 2/12 | short, damage |
| building A → Building 59 | 8.447 (shared 7.001) | 8.503 | 118.64 | 117.96 | **0.68** | 1.00/1.00 | 8.24 | 22/89 |  |
| Building 59 → building A | 6.126 (shared 4.731) | 6.689 | 20.87 | 16.25 | **4.62** | 1.00/1.00 | 0.30 | 12/20 | damage |
| building B′ → Building 59 | 8.873 (shared 6.667) | 8.888 | 119.17 | 120.51 | **-1.33** | 0.91/1.00 | -2.89 | 26/89 |  |
| Building 59 → building B′ | 7.149 (shared 7.149) | 7.880 | 11.28 | 10.94 | **0.34** | 1.00/1.00 | 0.13 | 22/22 |  |
| TEP → Building 59 | 7.619 (shared 7.619) | 8.349 | 143.70 | 118.68 | **25.03** | 0.99/1.00 | 100.76 | 89/89 |  |
| Building 59 → TEP | 7.361 (shared 7.138) | 9.023 | 104.16 | 33.03 | **71.13** | 1.00/1.00 | 19.26 | 32/40 | damage |
| HAI → Building 59 | 7.316 (shared 7.246) | 7.628 | 129.67 | 121.65 | **8.01** | 0.99/1.00 | 31.29 | 85/89 | damage |
| Building 59 → HAI | 8.460 (shared 7.855) | 10.120 | 49.46 | 23.34 | **26.12** | 0.97/1.00 | 0.72 | 95/168 | short, damage |
| TEP → Fingrid | 4.207 (shared 4.207) | 4.243 | 18.40 | 18.06 | **0.35** | 1.00/1.00 | — | 16/16 |  |
| Fingrid → TEP | 8.799 (shared 5.183) | 8.647 | 35.26 | 32.05 | **3.21** | 1.00/1.00 | — | 10/40 | damage |
| HAI → Fingrid | 4.537 (shared 4.537) | 4.855 | 21.72 | 15.79 | **5.93** | 1.00/1.00 | — | 16/16 |  |
| Fingrid → HAI | 8.238 (shared 5.483) | 8.505 | 34.37 | 33.05 | **1.31** | 1.00/1.00 | — | 10/168 | short, damage |
| battery → Fingrid | 7.132 (shared 4.524) | 7.369 | 11.17 | 9.06 | **2.11** | 1.00/1.00 | — | 8/16 | damage |
| Fingrid → battery | 6.282 (shared 3.395) | 6.426 | -0.22 | -0.27 | **0.05** | 1.00/1.00 | — | 6/12 | short, damage |
| Building 59 → Fingrid | 6.286 (shared 4.137) | 6.779 | 15.32 | 8.20 | **7.12** | 1.00/1.00 | — | 10/16 | damage |
| Fingrid → Building 59 | 8.995 (shared 5.403) | 9.123 | 108.18 | 107.98 | **0.20** | 1.00/1.00 | — | 10/89 |  |

- **Every type is moved in every control** after the leftover swap (Building 59 → HAI first came out uncontrolled at
  0.97: three HAI types share one source counterpart through nearest-quantile crossing). No cell is uncontrolled.
- **The receiver-TEP cells did not collapse.** With derangements that move every type, PhysioNet → TEP is 61.9
  bit-H (raw 81.0, control 19.1), Building 59 → TEP 71.1, HAI → TEP 48.6, battery → TEP 8.5, Fingrid → TEP 3.2.
  The v7 suspicion — that singleton groups made the control the learned mapping — was true of the control and is
  not what makes these cells: a smooth foreign model whose pairing is right about which quantities are slow helps
  TEP's 40-class receiver over its first 20 days, and the deranged pairing helps it less. Whether that is grammar
  is still the open question; it is no longer a control artefact.
- **Building 59 as a receiver reads sanely now:** TEP → 59 25.0, HAI → 59 8.0, building A → 59 0.7, B′ → 59 −1.3 —
  the v7 ordering (the two real regulators far ahead of the synthetic generator) with the trapezoid's 100-bit-day
  artefact gone. Fingrid → 59 0.2.
- **Fingrid:** HAI → Fingrid 5.9 and Building 59 → Fingrid 7.1 are the two cells into the grid that clear the
  control by more than the control's own size; TEP → Fingrid 0.35; Fingrid → TEP 3.2, → HAI 1.3 (short), → battery
  0.05, → Building 59 0.2. Sixteen types through six roles on the receiving side.
- **Lineage** (docs/LINEAGE.md): six taxa; Fingrid shares 22 cross-role shapes (37 in all) with HAI and none with any other taxon,
  so both shape trees place it outermost with PhysioNet; the shape trees keep (TEP, Building 59) innermost; the transfer tree on bit-horizons is `(nasa_battery:0.353,(physionet_slp:0.290,(fingrid:0.132,(hai:0.022,(tennessee_eastman:0.010,building_59:0.010):0.022):0.132):0.290):0.353);`.

## v7 (2026-10-21): loop roles, fine-grid period, admission in horizons — seed 0, ten seeded permutations; datasets 7 (0.25 s) and 8 added

Cards regenerated under v7 (3.16 loop tags in the place prefix and graded in alignment; 3.4 fine grid; section 6
admission in horizons). PhysioNet is now the 0.25-s card (admitted by horizons) and Building 59 is dataset 8. The
column *net ≤ 20 d* is the same cell truncated at the 20-day point, for receivers whose "all" point differs
(Building 59 trains on 273 days, TEP on 60, HAI on 11, the battery on 36, PhysioNet on 2.7).

| source → receiver | zero-shot (learned) | zero-shot (permuted) | raw cell | control cell | **net cell** | net ≤ 20 d | v6 net | types mapped | roles mapped |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TEP → HAI | 7.629 (shared 7.260) | 8.919 | 0.86 | -0.05 | **0.90** | 0.90 | 0.90 | 142/168 | 37/52 |
| HAI → TEP | 7.034 (shared 6.730) | 8.015 | 14.69 | 6.73 | **7.96** | 2.54 | 13.53 | 32/40 | 34/39 |
| TEP → battery | 3.682 (shared 3.682) | 6.340 | 0.04 | -0.21 | **0.25** | 0.25 | 0.25 | 12/12 | 3/3 |
| battery → TEP | 8.772 (shared 3.504) | 9.006 | 5.58 | 3.93 | **1.65** | 0.71 | 1.65 | 6/40 | 3/39 |
| HAI → battery | 4.650 (shared 4.650) | 4.730 | -0.25 | -0.23 | **-0.03** | -0.03 | 0.05 | 12/12 | 3/3 |
| battery → HAI | 9.466 (shared 4.201) | 9.514 | -0.13 | -0.22 | **0.09** | 0.09 | 0.09 | 10/168 | 3/52 |
| TEP → PhysioNet | 5.378 (shared 5.378) | 5.355 | 1.02 | 1.02 | **0.00** | 0.00 | -0.02 | 10/10 | 5/5 |
| PhysioNet → TEP | 6.634 (shared 4.134) | 8.750 | 17.44 | -0.64 | **18.08** | 6.65 | 3.97 | 4/40 | 5/39 |
| HAI → PhysioNet | 6.998 (shared 6.998) | 6.544 | 0.27 | 0.29 | **-0.02** | -0.02 | -0.02 | 10/10 | 5/5 |
| PhysioNet → HAI | 7.542 (shared 7.018) | 8.373 | 0.64 | 0.25 | **0.39** | 0.39 | 0.21 | 4/168 | 5/52 |
| battery → PhysioNet | 4.425 (shared 3.795) | 4.425 | 0.94 | 0.94 | **0.00** | 0.00 | 0.00 | 2/10 | 1/5 |
| PhysioNet → battery | 6.762 (shared 1.619) | 6.762 | -0.28 | -0.28 | **0.00** | 0.00 | 0.17 | 2/12 | 1/3 |
| building A → Building 59 | 8.447 (shared 7.001) | 8.563 | 461.21 | 452.97 | **8.24** | 0.77 | — | 22/89 | 6/23 |
| Building 59 → building A | 6.126 (shared 4.726) | 6.667 | 0.41 | 0.11 | **0.30** | 0.30 | — | 12/20 | 6/10 |
| building B′ → Building 59 | 8.873 (shared 6.667) | 8.980 | 464.30 | 467.19 | **-2.89** | -0.13 | — | 26/89 | type-level |
| Building 59 → building B′ | 7.134 (shared 7.134) | 7.725 | -0.16 | -0.29 | **0.13** | 0.13 | — | 22/22 | type-level |
| TEP → Building 59 | 7.627 (shared 7.627) | 8.489 | 562.31 | 461.55 | **100.76** | 9.89 | — | 89/89 | 23/23 |
| Building 59 → TEP | 7.356 (shared 7.133) | 8.997 | 21.48 | 2.22 | **19.26** | 7.06 | — | 32/40 | 22/39 |
| HAI → Building 59 | 7.333 (shared 7.276) | 7.831 | 494.06 | 462.77 | **31.29** | 3.09 | — | 85/89 | 23/23 |
| Building 59 → HAI | 8.949 (shared 8.246) | 9.881 | 0.71 | -0.01 | **0.72** | 0.72 | — | 93/168 | 23/52 |

- **TEP ↔ HAI under the loop tag.** TEP → HAI holds (0.90); HAI → TEP falls from 13.53 to **7.96**: the +1 on
  differing loop tags moved two of the HAI → TEP role pairings (32 of 40 types against 34) and the mixed curve
  gives up part of its 0.3–0.6 bit advantage. A graded penalty built from tags that fail their own checks on
  both plants (TEP flowsheet 0.55, HAI 0.33) costs a cell; that is the tag's first measured effect, recorded.
- **Building 59 as a receiver: the cells are an artefact of the curve's end point.** Raw areas of 460–560 bit-days
  come from two things the cards show: the zones' first eight days of 2019 are a gap, so the receiver's own model at
  2, 3 and 5 training days is fitted on almost nothing (27.5 bits per event, λ chosen 0, mixed = own = control, no
  credit either way), and the last curve point is 273 days, so the 20-day gap of ~0.7 bits is carried over 253 days
  by the trapezoid. Truncated at 20 days the cells are TEP → 59 **9.9**, HAI → 59
  **3.1**, building A → 59 **0.8**, building B′ → 59
  -0.1. The question the brief asked — did the synthetic generator teach anything — reads: a little from A
  (type-level, 22 of 89 types through 6 roles), nothing from B′, and far more from the two real regulators. Open
  item: the cell should integrate to a fixed last point (20 days) or be reported per training day; the "all" point
  is a building's number as the day count was.
- **Building 59 as a source: 59 → TEP 19.26** (mixed beats TEP's own by 0.3–0.6 bits from 2 to 20 days, the
  control by 0.05–0.25), of the HAI → TEP kind; **59 → HAI 0.72**, 93 of 168 types.
- **PhysioNet at 0.25 s → TEP 18.08**, through five roles (HR ↔ feed_D, SBP ↔ purge_valve, DBP ↔ L, RESP ↔ underflow,
  SO2 ↔ prod_D) and 4 of 40 types: the learned mixture beats TEP's own by 0.3–0.6 bits from 2 to 20 days where the
  within-class permutation (the pressures swapped, the dimensionless pair swapped) does not. The same receiver-side
  shape as HAI → TEP and 59 → TEP: TEP's 40-class model at 1–20 days is helped by a smooth foreign prior whose
  pairing is right about which quantities are slow; whether that is grammar or regularisation the control cannot
  separate when the class has only two members to permute. Damage is flagged (unshared types got worse).
- **The rest at zero**, as before: TEP/HAI ↔ battery, X → PhysioNet, battery ↔ PhysioNet.

The lineage under v7 (docs/LINEAGE.md): 4,358 characters over five taxa; Building 59 shares **104 cross-role
shapes with TEP and 128 with HAI** (and 42 / 58 same-role), the most of any pair; the shape trees put
(TEP, Building 59) together, then HAI, then the battery, with PhysioNet the outgroup, and the transfer tree agrees
on (TEP, Building 59). No shape is present in every taxon; no return shape is shared once the loop tags respell
them. Returns by place signature: Building 59 REACTS → RESPONDS → REACTS 87 of 299; HAI RESPONDS → REACTS →
RESPONDS 42 and REACTS → RESPONDS → REACTS 33 of 118; TEP RESPONDS → RESPONDS → RESPONDS 29 of 106.

## v6 (2026-10-20): gap clipping, cross-scheme spelling, chains and returns — seed 0, ten seeded permutations

Cards regenerated under v6 (3.6 clips a gap instead of dropping the target; 3.15 admits chains and returns);
alignment under 3.12's cross-scheme spelling (a quantile symbol crosses to the source role's symbol of the same
direction and nearest quantile). TCLab is withdrawn from the running order; the battery set is Rosetta member one.

| source → receiver | zero-shot (learned) | zero-shot (permuted) | raw cell | control cell | **net cell** | v5 net | types mapped | roles mapped |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tennessee Eastman → HAI | 7.632 (shared 7.262) | 8.917 | 0.86 | −0.05 | **0.90** | 0.98 | 142/168 (v5: 120) | 37/52 |
| HAI → Tennessee Eastman | 6.629 (shared 6.381) | 8.410 | 17.91 | 4.38 | **13.53** | 14.45 | 34/40 | 36/39 |
| Tennessee Eastman → battery | 3.676 (shared 3.676) | 6.346 | 0.04 | −0.21 | **0.25** | 0.00 | 12/12 (v5: 8) | 3/3: I ↔ cw_flow, T ↔ purge_D, V ↔ underflow_valve |
| battery → Tennessee Eastman | 8.772 (shared 3.504) | 9.006 | 5.59 | 3.94 | **1.65** | 0.00 | 6/40 (v5: 0) | 3/39: AC_valve ↔ V, cw_flow ↔ I, underflow ↔ T |
| HAI → battery | 4.721 (shared 4.721) | 5.359 | −0.22 | −0.28 | **0.05** | −0.00 | 12/12 (v5: 2) | 3/3: I ↔ LCP01D, T ↔ TIT01, V ↔ FCV01D |
| battery → HAI | 9.466 (shared 4.201) | 9.514 | −0.13 | −0.22 | **0.09** | −0.00 | 10/168 (v5: 6) | 3/52: B4002 ↔ V, FT03Z ↔ T, LIT01 ↔ I |
| Tennessee Eastman → PhysioNet (7, provisional) | 5.389 (shared 5.389) | 6.022 | 0.93 | 0.95 | **−0.02** | — | 14/14 | 5/5: DBP ↔ L, HR ↔ purge_valve, RESP ↔ feed, SBP ↔ feed_D, SO2 ↔ prod_F |
| PhysioNet → Tennessee Eastman | 8.087 (shared 2.366) | 8.351 | 10.46 | 6.49 | **3.97** | — | 8/40 | 5/39: L ↔ DBP, feed ↔ RESP, feed_D ↔ SBP, prod_D ↔ SO2, purge_valve ↔ HR |
| HAI → PhysioNet | 5.515 (shared 5.515) | 5.592 | 0.84 | 0.86 | **−0.02** | — | 14/14 | 5/5: DBP ↔ B2016, HR ↔ SIT01, RESP ↔ FT01, SBP ↔ PIT01, SO2 ↔ ST_GOV |
| PhysioNet → HAI | 8.625 (shared 3.670) | 8.866 | 0.22 | 0.01 | **0.21** | — | 10/168 | 5/52: LD ↔ SO2, LIT01 ↔ RESP, PCV02Z ↔ DBP, SIT02 ↔ HR, ST_GOV ↔ SBP |
| battery → PhysioNet | 7.183 (shared 4.251) | 7.269 | 0.74 | 0.74 | **0.00** | — | 8/14 | 2/5: RESP ↔ V, SBP ↔ T |
| PhysioNet → battery | 9.180 (shared 9.087) | 10.682 | 0.01 | −0.16 | **0.17** | — | 8/12 | 2/3: T ↔ SO2, V ↔ RESP |

PhysioNet (dataset 7, 2026-10-21) is below the admission line and carried as a provisional leaf (its card). Its
cells: the dimension suffix pairs pressure with pressure and heart rate with turbine speed (HAI → PhysioNet:
SBP ↔ PIT01, HR ↔ SIT01), every receiver type carries, and the mixed curves do not move (−0.02, −0.02, 0.00). As
a source into TEP it nets 3.97 bit-days through five roles with a learned zero-shot of 8.09 against 8.35
permuted — a receiver-side effect of the kind HAI → TEP shows (raw 10.46, control 6.49), on a source library
of 37 fragments, and not a claim. The lineage with four leaves is in `docs/LINEAGE.md`.

- **TEP ↔ HAI holds.** 0.90 and 13.53 against 0.98 and 14.45 under v5, inside the seed spread of the control,
  with a changed HAI library (2,165 fragments after clipping) and 22 more HAI types carried across by the
  spelling rule. The result does not depend on which v5-or-v6 instrument measured it.
- **The spelling rule did what it was for.** Every battery cell now carries types (12/12 as receiver against 2
  or 8), and TEP → battery is the first cross-kind cell where the learned mapping beats the permuted one by more
  than two bits of zero-shot (3.68 against 6.35) on a receiver whose own model is near its floor. The net cell
  is small (0.25) because a 12-type protocol is learned by the receiver's own model within its first day; the
  zero-shot gap is the evidence, the cell is not. Battery → TEP nets 1.65 through three roles — current ↔
  cooling-water flow, voltage ↔ the A/C feed valve, temperature ↔ separator underflow — a plausible pairing of
  an actuator, a setpoint-held quantity and a slow measurement, and too few roles to claim.
- **HAI ↔ battery stays at zero** (0.05, 0.09): the learned mapping beats the permuted by 0.6 bits as HAI → battery,
  the mixed curves do not move.

### Returns (3.15) — the loop signature across datasets

| dataset | chains admitted (used) | returns | the loop, as a return | spelled |
| --- | --- | --- | --- | --- |
| Tennessee Eastman | 525 (0) | 106 | `cw_flow:downq20 -s-> P:downq20 -m-> cw_flow:upq20` (n 46, cond. lift 3.52, null 11) | SLOW·RELAY → MID·FOLLOW → SLOW·RELAY |
| HAI | 1,437 (0) | 118 | `LIT01:upq80 -s-> LCV01D:upq20 -s-> LIT01:downq80` (n 15, cond. lift 9.01, null 5) | MID·RELAY → MID·RELAY → MID·RELAY |
| NASA battery | 13 (13) | 1 | `I:downq10 -s-> V:downq20 -s-> I:upq10` (n 27, cond. lift 2.10, null 4) | MID-S·RELAY → MID·RELAY → MID-S·RELAY |
| building A | 15 (15) | 1 | `T:down20 -m-> vent:off -s-> T:up20` (n 6, cond. lift 2.65, null 1) | untagged |
| building B′ | 32 (32) | 0 | — | — |

TEP's cooling-water loop and HAI's level loop both appear as returns, the strongest of their datasets' return
inventories (cw_flow ↔ cw_out and cw_flow → P → cw_flow: 31 returns; LIT01 ↔ LCV01D: 20). The thesis line
holds with one correction to its spelling: **neither is LEAD → FOLLOW → LEAD, and no return anywhere is.** An
actuator inside a closed loop is a context *and* a target — it moves the measurement and is moved by it — so the
degree rule of 3.14 tags it RELAY by construction. LEAD belongs to open drivers (feeds, schedules, the HIL load:
chains LEAD → RELAY → RELAY, 76 in TEP and 206 in HAI). A loop closing reads RELAY → FOLLOW → RELAY where the
measurement only follows (TEP's vessels) and RELAY → RELAY → RELAY where it also drives (HAI's level, the
battery's voltage). Whether 3.14 should carry a loop-aware place tag is the next method question, not a tuning.

## v5: place prefix and dimension suffix (alignment hard on kind and dimension, graded on clock and place; control permuted within clock class × dimension)

| source → receiver | zero-shot (learned) | zero-shot (permuted) | raw cell | control cell | **net cell** | v4 net | v3 net | types mapped |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tennessee Eastman → HAI | 7.683 (shared 7.177) | 8.986 | 0.86 | −0.12 | **0.98** | 1.67 | 0.37 | 120/168 |
| HAI → Tennessee Eastman | 6.622 (shared 5.887) | 7.944 | 21.57 | 7.11 | **14.45** | 10.52 | 0.06 | 34/40 |

Seed 0, re-run 2026-10-20 under the current control (ten permutations drawn from the run's seed; the 2026-10-19
cells, 0.83 and 13.37, were under three permutations from a fixed generator). The learned side is unchanged to the
third decimal; the control moved (−0.12 against 0.03; 7.11 against 8.29) and both nets moved with it.

Mixed picture, reported as such. HAI → TEP improved: more TEP roles found a dimensionally and dynamically
compatible HAI counterpart (34 of 40 types mapped against 22), and the mixed curve beats TEP's own model by
0.29–0.64 bits from 1 to 20 receiver days against a stricter control. TEP → HAI fell: the zero-shot is unchanged
(7.68 vs 7.65) but the control is now permuted within (clock class, dimension) and so is 0.9 bits better than
v4's, and the dimension constraint rules out pairs that v4 had used (120 types mapped against 134), so the net
halves. Two caveats on the comparison: v5 also fixed a scale bug that had made the "forbidden" penalty only
partly effective in v3 and v4 (distances were not normalised), so v4's constraints were looser than written;
and the stricter control is the right control, which means part of v4's 1.67 was credit the grammar had not
earned. Five seeds (below), one pair.

### v5 across seeds 0–4 (2026-10-20)

Seeds 1–4 were run under the control as it then was: three permutations from a fixed generator, so the seed
reached the control only through the mapping it permutes (the control has since been seeded and raised to ten
permutations; seed 0 above is under the new one, seeds 1–4 are not yet). Each seed is a full re-run of both
pipelines followed by both transfer directions.

| seed | TEP → HAI net | HAI → TEP net | HAI → TEP raw | HAI → TEP control | HAI → TEP zero-shot (learned / permuted) | HAI roles mapped |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.83 | 13.37 | 21.65 | 8.29 | 6.607 / 7.647 | 37/39 |
| 1 | 0.83 | 15.24 | 21.60 | 6.36 | 6.619 / 7.767 | 36/39 |
| 2 | 0.83 | 15.16 | 21.63 | 6.47 | 6.621 / 7.778 | 36/39 |
| 3 | 0.83 | 13.87 | 21.66 | 7.79 | 6.607 / 7.715 | 37/39 |
| 4 | 0.83 | 15.12 | 21.61 | 6.49 | 6.623 / 7.747 | 36/39 |
| **mean ± sd** | **0.83 ± 0.00** | **14.55 ± 0.87** | 21.63 ± 0.03 | 7.08 ± 0.89 | | |

- **TEP → HAI is seed-free.** All five seeds give the same role map, the same anchors (B4022 ↔ cw_out,
  PIT02 ↔ underflow_valve), 120/168 types mapped, and the same cells to two decimals (raw 0.86, control 0.03,
  net 0.83). The small cell is a property of the pair under v5, not of one draw.
- **HAI → TEP transfers on every seed; the spread is the control's, and it follows one pairing.** The raw cell is
  stable (21.60–21.66) and the learned zero-shot moves by 0.02 bits at most, while the control cell ranges
  6.36–8.29 and the net cell inherits it: 13.37–15.24, mean 14.55 ± 0.87. The split is clean: the two seeds that
  map E_feed ↔ CO_rpm (0 and 3) have controls 8.29 and 7.79; the three that leave E_feed unmapped have 6.36–6.49.
  That pairing adds ~1.5 bit-days of regularisation to the control and nothing to the raw cell, so it carries no
  structure and the net is more honest without it. The lowest seed is still 1.3× the v4 cell (10.52).
- **The role pairings rotate within a dynamical class.** Seeds 1–4 differ from seed 0 on four or five of the
  39 HAI roles, all among HAI's purge and feed roles and TEP's valve roles VXT02/VXT03/VYT02/VYT03 (the same
  tag class, exchanged among themselves), plus E_feed ↔ CO_rpm dropped in three seeds. The alignment is stable
  where it is confident and indifferent where the candidates are interchangeable, which is what a graded
  distance should do.
- **Open item (done the same day):** the control now takes the run's seed and ten permutations; seeds 1–4 are
  to be regenerated under it at the next sweep, and the mean ± sd above will then sample the control as well.

## v5, the Rosetta set's first two members (2026-10-20): TCLab (5) and the NASA battery cells (6)

Seed 0, the seeded ten-permutation control. TCLab is **not admitted** (7.6 h, no period; its card is for the
record) and has less than one training day, so it cannot carry a learning curve as a receiver: those cells are
"not measurable" and only the zero-shot is reported. The battery set is admitted (47.5 observed days) but its
library is 12 fragments built from the 7% of events that survive the gap rule (its card).

| source → receiver | zero-shot (learned) | zero-shot (permuted) | raw cell | control cell | **net cell** | roles mapped | types mapped | role pairings |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TCLab → battery | 6.236 (shared 1.105) | 6.232 | −0.18 | −0.18 | **−0.00** | 2/3 | 2/12 | T ↔ T, Q ↔ I |
| battery → TCLab | 6.654 (shared 0.901) | 6.715 | — | — | not measurable | 3/3 | 2/12 | Q ↔ I, T ↔ T, Tsp ↔ V |
| TEP → battery | 3.585 (shared 3.585) | 3.585 | 0.19 | 0.19 | **0.00** | 3/3 | 8/12 | I ↔ cw_flow, T ↔ purge_D, V ↔ purge_B |
| battery → TEP | 5.322 (shared —) | 5.322 | 25.97 | 25.97 | **0.00** | 3/39 | 0/40 | AC_valve ↔ V, feed ↔ I, prod_H ↔ T |
| HAI → battery | 3.926 (shared 1.854) | 3.917 | −0.01 | −0.01 | **−0.00** | 3/3 | 2/12 | I ↔ FCV02Z, T ↔ TIT01, V ↔ FCV01D |
| battery → HAI | 9.063 (shared 2.715) | 9.073 | 0.03 | 0.04 | **−0.00** | 3/52 | 6/168 | B4005 ↔ V, SIT01 ↔ T, VXT03 ↔ I |
| TEP → TCLab | 3.876 (shared 3.876) | 4.072 | — | — | not measurable | 3/3 | 8/12 | Q ↔ feed, T ↔ purge_D, Tsp ↔ cw_flow |
| TCLab → TEP | 7.435 (shared 1.240) | 7.443 | 8.79 | 8.82 | **−0.04** | 3/39 | 2/40 | cw_flow ↔ Tsp, feed_C ↔ Q, underflow ↔ T |
| HAI → TCLab | 3.484 (shared 3.484) | 3.682 | — | — | not measurable | 3/3 | 12/12 | Q ↔ FT01, T ↔ FCV03D, Tsp ↔ B4002 |
| TCLab → HAI | 9.491 (shared 3.431) | 9.504 | 0.17 | 0.14 | **0.03** | 3/52 | 12/168 | B2016 ↔ T, B4002 ↔ Tsp, B4022 ↔ Q |

**Nothing transfers, and the table says why.** Every net cell is zero to two decimals and every learned zero-shot
is within 0.2 bits of its permuted control. Three instrument facts sit upstream of the physics:

- **The pair's libraries are too small to carry anything.** TCLab has two fragments (a step-test staircase);
  the battery set twelve, from one-twentieth of its events. A source with no motifs has nothing to send, and a
  receiver with 282 test events cannot register what arrives.
- **Role pairings cross, symbol spellings do not.** Battery → TCLab pairs Q ↔ I, T ↔ T, Tsp ↔ V — the physical
  correspondence (actuator ↔ actuator, temperature ↔ temperature) — but T ↔ T is forced by the ⟨Θ⟩ suffix and
  Q, being dimensionless, is free, so with three roles a side this is a coin toss, not evidence. More to the
  point, Q is spelled q20/50/80 and I is spelled q10/90, so the role match carries no types (2 of 12 mapped, both
  of them T's peak and trough); the same happens to battery → TEP (3 roles matched, 0 of 40 types). Symbols cross
  by spelling (3.12), and the symbolization rule chose different spellings for the two actuators.
- **The regulariser is large and the control takes all of it.** Battery → TEP's raw cell is 25.97 bit-days,
  the largest raw number in the collection, and the control is 25.97: a three-role model through any mapping
  smooths TEP's 40-class receiver. The v3 lesson again, at scale, and the control does its job.

What the Rosetta pair tests — whether the thermal and the electrochemical first-order loop share a grammar — is
not yet tested. The order of repair is the one the cards give: a gap rule for fragmented observation (the
battery would then mine ~12,000 events instead of 838); a long TCLab recording (24–48 h, both heaters, a setpoint
schedule); and a decision on whether actuators spelled by different quantile schemes should be allowed to cross
(a spelling rule, 3.12 — not a tuning). Until then the cells stand as the first all-zero row of the matrix,
with the control confirming that zero is zero.

## v4: grammar (parts of speech, role-level alignment, symbols by spelling, control permuted within class)

| source → receiver | zero-shot (learned) | zero-shot (permuted, within class) | raw cell | control cell | **net cell** | v3 net | kind |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Tennessee Eastman → HAI | 7.646 (shared 7.220) | 9.627 | 1.21 | −0.45 | **1.67** | 0.37 | cross kind |
| HAI → Tennessee Eastman | 6.390 (shared 4.700) | 7.435 | 18.42 | 7.90 | **10.52** | 0.06 | cross kind |
| building A → B′ | — | — | — | — | 0.74 | 0.74 | same kind; B′ has scrambled type names, so v4's role-level alignment does not apply and the cell is v3's |
| building B′ → A | — | — | — | — | 5.53 | 5.53 | as above |

Under v4 the mixed curve beats the receiver's own model at **every** point of both cross-kind curves (TEP → HAI:
−1.07 bits at 1 receiver-day, −0.24 at 2, −0.08 at 3–5, −0.01 to −0.02 at 10–11; HAI → TEP: −0.18 to −0.57
bits from 1 to 20 days, mixing weight 0.25), and the within-class permuted control is worse than the learned
mapping at every point (by 0.1–0.6 bits). In v3 the same two cells were at chance. What changed is only the
spelling of the motifs: a part-of-speech prefix on each role, roles aligned to roles of the same part of speech
and symbol kind, and symbols carried across by their spelling, so `up` stays `up` and `q80` stays `q80`.

The role pairings are not physical identities (TEP cooling-water flow ↔ HAI temperature demand; TEP level ↔
HAI pressure; TEP vessel temperature ↔ HAI speed-controller output). They are dynamical: a mid-speed
controlled variable in one plant stands in for a mid-speed controlled variable in the other. That is the
thesis as stated — the same form in different substance — and the net cells say the pairing predicts. One
seed, one pair: the result stands as a first positive, not a universal.

## v3 (type-level alignment, for the record)

| source → receiver | zero-shot (learned mapping) | zero-shot (permuted mapping) | raw cell | control cell | **net cell** | kind |
| --- | --- | --- | --- | --- | --- | --- |
| building A → building B′ | 4.600 | 7.934 | 0.20 | −0.54 | **0.74** | same kind (synthetic buildings) |
| building B′ → building A | 3.075 | 7.780 | 1.73 | −3.80 | **5.53** | same kind |
| Tennessee Eastman → HAI | 8.855 | 9.646 | 0.25 | −0.12 | **0.37** | cross kind (chemical process → boiler/turbine testbed) |
| HAI → Tennessee Eastman | 8.426 | 8.510 | 8.22 | 8.16 | **0.06** | cross kind |

Receivers' own libraries, bits/event on the test split: A 2.167, B′ 1.365, TEP 3.033, HAI 3.721.
Mapping accuracy is measured only where a key exists: A → B′ 0.60 (30 scorable types). Cells for the
pairs 1,2 ↔ 3,4 are not run: a building and a plant are different kinds, and the matrix needs the
within-kind cells first.

## Reading

- **Same kind, same mechanisms: the alignment is real.** Between the two buildings the learned mapping's
  zero-shot beats the permuted mapping's by 3.3–4.7 bits, and the permuted model *hurts* the receiver
  (control cells −0.54 and −3.80), so the learned mapping's modest raw gains are large net gains. B′ (four
  zones, a dehumidifier loop) teaches A far more than A teaches B′ — the richer system is the better source.
- **Cross kind: nothing at the type level.** TEP ↔ HAI mappings are at chance (learned vs permuted zero-shot
  within 0.1–0.8 bits; the anchors pair a purge-gas analyser with a boiler temperature demand). HAI → TEP's
  raw 8.22 bit-days is entirely regularisation: a 10% share of *any* smooth distribution helps TEP's
  over-parameterised 40-class model from 2 to 20 training days, and the permuted mapping does it just as
  well. TEP → HAI's 0.37 is small and confined to the first two receiver days.
- **The control was necessary.** Under v2 the HAI → TEP cell would have entered the matrix as 8.2 bit-days —
  the largest in the collection — and been false. This is the collection's first negative-control result,
  arriving before the datasets designated as negative controls.

## What v3 said about the thesis (superseded by v4 above)

Type-level alignment of lift matrices (3.12) finds correspondences between systems of the same kind and does
not find them across kinds, with 40 vs 168 types and two signature anchors. It does not yet say whether the
cross-kind correspondence is absent or merely not findable this way. The structures that should be shared
between a chemical plant and a boiler — level control, pressure control, actuator → measurement loops — are
a handful of motifs among hundreds of types; the type-level Hungarian match has no way to privilege them. The
candidate route is the one Experiment C pointed to: align at the level of *shapes* (type-free fragment
topology: "actuator rises → measurement falls at lag s, then actuator falls") and transfer the shape prior,
not the lexicon. That is the next method question, and it is a v4 question, not a tuning one.

## Open items raised

1. (v4 did the first half) Parts of speech and role-level alignment lifted the cross-kind cells; syntax motifs — chains and the feedback-return motif — are the second half, not yet built.
2. Pooled lag classes for the pair before alignment (each dataset's own bands reduce comparability).
3. The learning curve's λ is chosen by 2-fold on the receiver's training days and then reused for the control;
   a control-specific λ would be fairer to the control, i.e. more conservative.
4. A within-kind real pair (TEP ↔ a second chemical process, HAI ↔ SWaT) is the missing test between the
   synthetic same-kind result and the cross-kind null.
