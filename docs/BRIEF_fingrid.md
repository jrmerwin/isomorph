# Brief — fingrid (method v8, a view)

*Lifts are odds ratios on the proposal split (3.6-3.8), confirmed on the confirmation split; absence is informative only above the signal floor (3.5); `no gain` means found but already carried by the trivial alternation model (3.11); loop-rule verdicts are recorded, not promoted (3.16); cells are bit-horizons net of the larger of two controls, with share of the receiver's ceiling where a diagonal exists (3.12).*

## Identity

- kind: real power system (Nordic synchronous area, Fingrid); standing: admitted (365 days)
- entity: grid (1 units); H = 90.0 min; lag edges [9.32, 28.96, 90.0] min
- periods: slow —, fast 14.97; admission: {'days': 364.98, 'slow_periods': None, 'horizons': 5839.7, 'test_horizons': 1459.9, 'admitted': True, 'by': 'days'}
- claim: **no gain** — library 1.615 bits, triviality 1.603, best baseline 2.588; gain over triviality -0.012
- events 79367, types 16, signal floor 584

## Vocabulary

| role | full tag | quantity | scheme | loop tags (timing / determinism) |
| --- | --- | --- | --- | --- |
| afrr_down | MID-S·COMMON·RELAY ⟨M L² T⁻³⟩ | power | dsign | REACTS / REACTS |
| afrr_up | MID-S·COMMON·RELAY ⟨M L² T⁻³⟩ | power | q20_50_80 | RESPONDS / RESPONDS |
| f | MID·COMMON·RELAY ⟨T⁻¹⟩ | frequency | dsign | REACTS / REACTS |
| fcrn_down | MID-S·COMMON·LEAD ⟨M L² T⁻³⟩ | power | dsign | — / — |
| fcrn_up | MID-S·COMMON·LEAD ⟨M L² T⁻³⟩ | power | dsign | — / — |
| net_ie | SLOW·ISOLATED ⟨M L² T⁻³⟩ | power | dsign | — / — |

## Couplings (validated fragments)

| prior | lag | target | lift | conf. lift | n | binding | shape | confirmed in | failed in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fcrn_down:trough | s | f:peak | 9.671 | 10.093 | 1311 | None | `MID-S.trough -s-> MID.peak` | — | tennessee_eastman, hai, building_59 |
| fcrn_down:peak | s | f:trough | 9.657 | 9.962 | 1319 | None | `MID-S.peak -s-> MID.trough` | — | tennessee_eastman, hai, building_59 |
| fcrn_up:peak | s | f:trough | 7.646 | 9.219 | 801 | None | `MID-S.peak -s-> MID.trough` | — | tennessee_eastman, hai |
| fcrn_up:trough | s | f:peak | 7.332 | 9.323 | 861 | None | `MID-S.trough -s-> MID.peak` | — | tennessee_eastman, hai |
| afrr_up:upq80 | m | afrr_up:downq80 | 5.868 | 6.196 | 680 | None | `MID-S.up.q80 -m-> MID-S.down.q80 [same role]` | tennessee_eastman, hai, nasa_battery, building_59 | — |
| afrr_up:upq80 | s | afrr_down:peak | 4.518 | 4.586 | 457 | None | `MID-S.up.q80 -s-> MID-S.peak` | — | tennessee_eastman, hai |
| f:trough | s | afrr_down:peak | 4.221 | 4.074 | 1089 | None | `MID.trough -s-> MID-S.peak` | — | tennessee_eastman, hai |
| afrr_up:downq20 | m | afrr_up:upq20 | 3.523 | 3.856 | 922 | None | `MID-S.down.q20 -m-> MID-S.up.q20 [same role]` | tennessee_eastman, hai, nasa_battery, building_59 | — |
| afrr_down:trough | m | afrr_up:upq20 | 3.465 | 3.777 | 1365 | None | `MID-S.trough -m-> MID-S.up.q20` | — | tennessee_eastman, hai |
| f:peak | s | afrr_down:trough | 3.464 | 3.609 | 1148 | None | `MID.peak -s-> MID-S.trough` | — | tennessee_eastman, hai |
| afrr_up:upq20 | m | afrr_down:peak | 3.404 | 3.435 | 1216 | None | `MID-S.up.q20 -m-> MID-S.peak` | — | tennessee_eastman, hai |
| afrr_up:upq50 | s | afrr_up:upq80 | 3.239 | 3.154 | 380 | None | `MID-S.up.q50 -s-> MID-S.up.q80 [same role]` | tennessee_eastman, hai | — |
| afrr_up:downq80 | s | afrr_up:downq50 | 3.213 | 2.692 | 305 | None | `MID-S.down.q80 -s-> MID-S.down.q50 [same role]` | tennessee_eastman, hai | — |
| afrr_down:trough | m | afrr_up:upq50 | 3.197 | 3.403 | 1327 | None | `MID-S.trough -m-> MID-S.up.q50` | — | tennessee_eastman, hai |
| afrr_up:upq20 | s | fcrn_down:peak | 3.169 | 3.306 | 795 | None | `MID-S.up.q20 -s-> MID-S.peak` | nasa_battery | tennessee_eastman, hai, building_59 |
| afrr_up:upq50 | m | afrr_down:peak | 3.086 | 3.067 | 1111 | None | `MID-S.up.q50 -m-> MID-S.peak` | — | tennessee_eastman, hai |
| f:trough | s | afrr_up:upq80 | 2.971 | 3.395 | 403 | None | `MID.trough -s-> MID-S.up.q80` | — | tennessee_eastman, hai, building_59 |
| afrr_up:downq20 | m | afrr_up:upq50 | 2.842 | 3.143 | 784 | None | `MID-S.down.q20 -m-> MID-S.up.q50 [same role]` | tennessee_eastman | hai |
| afrr_down:peak | m | afrr_up:downq80 | 2.834 | 2.952 | 709 | None | `MID-S.peak -m-> MID-S.down.q80` | — | tennessee_eastman, hai |
| afrr_up:upq80 | s | f:trough | 2.819 | 2.702 | 375 | None | `MID-S.up.q80 -s-> MID.trough` | — | tennessee_eastman, hai, building_59 |
| afrr_up:downq80 | m | afrr_up:downq20 | 2.779 | 2.951 | 616 | None | `MID-S.down.q80 -m-> MID-S.down.q20 [same role]` | — | tennessee_eastman, hai, nasa_battery, building_59 |
| afrr_up:downq50 | m | afrr_up:upq50 | 2.778 | 2.924 | 844 | None | `MID-S.down.q50 -m-> MID-S.up.q50 [same role]` | tennessee_eastman, hai | — |
| afrr_up:upq50 | m | afrr_up:upq80 | 2.769 | 2.741 | 524 | None | `MID-S.up.q50 -m-> MID-S.up.q80 [same role]` | hai | tennessee_eastman |
| afrr_up:upq50 | s | fcrn_down:peak | 2.741 | 2.79 | 706 | None | `MID-S.up.q50 -s-> MID-S.peak` | — | tennessee_eastman, hai |
| fcrn_down:peak | m | afrr_down:peak | 2.721 | 2.773 | 1387 | None | `MID-S.peak -m-> MID-S.peak` | — | tennessee_eastman, hai |
| afrr_up:upq20 | m | afrr_up:upq80 | 2.721 | 2.657 | 511 | None | `MID-S.up.q20 -m-> MID-S.up.q80 [same role]` | building_59 | tennessee_eastman, hai, nasa_battery |
| fcrn_down:peak | m | afrr_up:upq80 | 2.642 | 2.745 | 708 | None | `MID-S.peak -m-> MID-S.up.q80` | — | tennessee_eastman, hai, nasa_battery, building_59 |
| f:peak | s | afrr_up:downq20 | 2.616 | 3.034 | 584 | None | `MID.peak -s-> MID-S.down.q20` | — | tennessee_eastman, hai, building_59 |
| afrr_up:upq50 | s | afrr_down:peak | 2.608 | 2.906 | 582 | None | `MID-S.up.q50 -s-> MID-S.peak` | — | tennessee_eastman, hai |
| afrr_up:downq80 | m | afrr_up:downq50 | 2.589 | 2.881 | 605 | None | `MID-S.down.q80 -m-> MID-S.down.q50 [same role]` | hai | tennessee_eastman |
| afrr_up:downq50 | m | afrr_up:upq20 | 2.571 | 2.88 | 741 | None | `MID-S.down.q50 -m-> MID-S.up.q20 [same role]` | tennessee_eastman | hai |
| f:peak | s | afrr_up:downq50 | 2.549 | 2.94 | 600 | None | `MID.peak -s-> MID-S.down.q50` | — | tennessee_eastman, hai |
| fcrn_up:peak | m | afrr_up:upq50 | 2.452 | 2.919 | 1288 | None | `MID-S.peak -m-> MID-S.up.q50` | — | tennessee_eastman, hai |
| fcrn_up:peak | m | afrr_up:upq20 | 2.414 | 2.845 | 1203 | None | `MID-S.peak -m-> MID-S.up.q20` | — | tennessee_eastman, hai |
| afrr_up:downq80 | s | f:peak | 2.395 | 2.415 | 421 | None | `MID-S.down.q80 -s-> MID.peak` | — | tennessee_eastman, hai, building_59 |
| f:trough | m | afrr_up:downq80 | 2.361 | 2.308 | 779 | None | `MID.trough -m-> MID-S.down.q80` | — | tennessee_eastman, hai, building_59 |
| fcrn_up:peak | m | f:trough | 2.306 | 2.351 | 2244 | None | `MID-S.peak -m-> MID.trough` | — | tennessee_eastman, hai |
| f:trough | m | fcrn_down:trough | 2.209 | 2.235 | 1600 | None | `MID.trough -m-> MID-S.trough` | — | tennessee_eastman, hai, building_59 |
| afrr_up:upq20 | s | afrr_up:upq80 | 2.197 | 1.978 | 251 | None | `MID-S.up.q20 -s-> MID-S.up.q80 [same role]` | tennessee_eastman, building_59 | hai, nasa_battery |
| fcrn_up:peak | m | afrr_up:upq80 | 2.18 | 2.423 | 848 | None | `MID-S.peak -m-> MID-S.up.q80` | — | tennessee_eastman, hai |
| fcrn_up:trough | m | f:peak | 2.15 | 2.02 | 2197 | None | `MID-S.trough -m-> MID.peak` | — | tennessee_eastman, hai |
| fcrn_down:trough | m | afrr_down:trough | 2.113 | 2.24 | 1394 | None | `MID-S.trough -m-> MID-S.trough` | — | tennessee_eastman, hai |
| f:peak | m | fcrn_down:peak | 2.104 | 2.104 | 1746 | None | `MID.peak -m-> MID-S.peak` | — | tennessee_eastman, hai, building_59 |
| f:peak | s | fcrn_up:peak | 2.076 | 1.69 | 965 | None | `MID.peak -s-> MID-S.peak` | tennessee_eastman | hai |
| f:peak | m | afrr_up:upq20 | 2.059 | 2.259 | 997 | None | `MID.peak -m-> MID-S.up.q20` | — | tennessee_eastman, hai, building_59 |
| afrr_down:peak | m | afrr_up:downq50 | 1.965 | 2.135 | 664 | None | `MID-S.peak -m-> MID-S.down.q50` | — | tennessee_eastman, hai |
| f:peak | m | afrr_up:upq50 | 1.94 | 2.04 | 990 | None | `MID.peak -m-> MID-S.up.q50` | — | tennessee_eastman, hai |
| fcrn_down:peak | m | f:trough | 1.926 | 1.85 | 1291 | None | `MID-S.peak -m-> MID.trough` | — | tennessee_eastman, hai, building_59 |
| afrr_down:trough | m | afrr_up:upq80 | 1.903 | 1.613 | 585 | None | `MID-S.trough -m-> MID-S.up.q80` | — | tennessee_eastman, hai |
| f:trough | s | fcrn_up:trough | 1.901 | 1.52 | 688 | None | `MID.trough -s-> MID-S.trough` | tennessee_eastman | hai |
| afrr_down:peak | m | f:peak | 1.848 | 1.919 | 1157 | None | `MID-S.peak -m-> MID.peak` | — | tennessee_eastman, hai |
| fcrn_down:trough | m | afrr_up:upq20 | 1.829 | 2.026 | 813 | None | `MID-S.trough -m-> MID-S.up.q20` | — | tennessee_eastman, hai, nasa_battery, building_59 |
| afrr_up:upq50 | s | f:trough | 1.827 | 1.805 | 536 | None | `MID-S.up.q50 -s-> MID.trough` | — | tennessee_eastman, hai |
| afrr_up:upq20 | s | afrr_down:peak | 1.794 | 2.003 | 390 | None | `MID-S.up.q20 -s-> MID-S.peak` | — | tennessee_eastman, hai |
| f:trough | m | f:peak | 1.792 | 1.868 | 1479 | None | `MID.trough -m-> MID.peak [same role]` | — | tennessee_eastman, hai, building_59 |
| fcrn_down:trough | m | afrr_up:downq50 | 1.775 | 1.957 | 832 | None | `MID-S.trough -m-> MID-S.down.q50` | — | tennessee_eastman, hai |
| fcrn_up:trough | m | afrr_down:trough | 1.769 | 2.155 | 1374 | None | `MID-S.trough -m-> MID-S.trough` | — | tennessee_eastman, hai |
| afrr_up:upq20 | s | f:trough | 1.763 | 1.778 | 504 | None | `MID-S.up.q20 -s-> MID.trough` | — | tennessee_eastman, hai, building_59 |
| f:trough | m | fcrn_up:trough | 1.758 | 1.8 | 1548 | None | `MID.trough -m-> MID-S.trough` | — | tennessee_eastman, hai |
| f:peak | m | f:trough | 1.749 | 1.773 | 1653 | None | `MID.peak -m-> MID.trough [same role]` | — | tennessee_eastman, hai, building_59 |
| afrr_down:trough | m | f:trough | 1.718 | 1.83 | 1321 | None | `MID-S.trough -m-> MID.trough` | — | tennessee_eastman, hai |
| afrr_up:upq20 | l | afrr_up:downq80 | 1.594 | 1.543 | 858 | None | `MID-S.up.q20 -l-> MID-S.down.q80 [same role]` | building_59 | tennessee_eastman, hai, nasa_battery |
| afrr_up:upq80 | l | afrr_up:downq50 | 1.566 | 1.642 | 963 | None | `MID-S.up.q80 -l-> MID-S.down.q50 [same role]` | hai | tennessee_eastman |
| afrr_up:upq20 | l | afrr_up:downq20 | 1.559 | 1.688 | 1075 | None | `MID-S.up.q20 -l-> MID-S.down.q20 [same role]` | tennessee_eastman | hai, nasa_battery, building_59 |
| afrr_up:downq20 | l | afrr_down:peak | 1.556 | 1.587 | 1656 | None | `MID-S.down.q20 -l-> MID-S.peak` | — | tennessee_eastman, hai |
| fcrn_down:trough | l | afrr_down:peak | 1.549 | 1.584 | 2493 | None | `MID-S.trough -l-> MID-S.peak` | — | tennessee_eastman, hai |
| afrr_up:upq80 | l | afrr_up:downq20 | 1.544 | 1.655 | 900 | None | `MID-S.up.q80 -l-> MID-S.down.q20 [same role]` | hai, building_59 | tennessee_eastman, nasa_battery |
| afrr_up:downq80 | m | afrr_down:trough | 1.538 | 1.678 | 506 | None | `MID-S.down.q80 -m-> MID-S.trough` | — | tennessee_eastman, hai |
| afrr_down:trough | l | afrr_down:peak | 1.529 | 1.575 | 2128 | None | `MID-S.trough -l-> MID-S.peak [same role]` | — | tennessee_eastman, hai |
| afrr_up:upq50 | l | afrr_up:downq20 | 1.518 | 1.655 | 1127 | None | `MID-S.up.q50 -l-> MID-S.down.q20 [same role]` | tennessee_eastman, hai | — |
| afrr_up:upq20 | l | afrr_up:downq50 | 1.514 | 1.661 | 1101 | None | `MID-S.up.q20 -l-> MID-S.down.q50 [same role]` | tennessee_eastman | hai |

## Loops (returns; verdicts recorded, not promoted)

| X | l1 | Y | l2 | X′ | n | cond. lift | timing (g1 / g2) | determinism (p1 / p2) | used |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| afrr_up:upq80 | s | f:trough | m | afrr_up:downq80 | 202 | 2.46 | Y reacts (6.0 / 24.0) | Y reacts (0.261 / 0.089) | True |
| afrr_up:upq80 | s | afrr_down:peak | m | afrr_up:downq80 | 226 | 2.243 | Y reacts (3.0 / 15.0) | Y reacts (0.336 / 0.114) | True |
| afrr_up:upq20 | s | afrr_down:peak | m | afrr_up:downq50 | 173 | 1.716 | Y reacts (3.0 / 15.0) | unresolved (0.147 / 0.111) | True |

Chains (non-return): 12.

## Absences

- silent roles: none
- roles never a target: ['net_ie']
- keyed pairs not found: net_ie → f
- signal floor: 584 (absence is informative only for pairs whose support would exceed the signal floor)

## Regimes

none recorded

## Matrix row

Cells in (this system as receiver):

| source | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fingrid_stretch (diagonal) | 135.88 | 159.28 | 92.83 | -43.05 | -66.45 | marginal | — | 16/16 |  |
| tennessee_eastman | 0.35 | 0.35 | 18.35 | 10.89 | 18.00 | derangement | 0.00 | 16/16 |  |
| hai | 5.93 | 5.93 | 21.72 | 12.43 | 15.79 | derangement | 0.04 | 16/16 |  |
| nasa_battery | -1.73 | 2.11 | 11.17 | 12.90 | 9.06 | marginal | -0.01 | 8/16 | damage |
| building_59 | 3.98 | 7.08 | 15.24 | 11.26 | 8.16 | marginal | 0.03 | 10/16 | damage |
| alibaba_2018 | -1.50 | -1.50 | 11.27 | 7.10 | 12.77 | derangement | -0.01 | 6/16 | damage |

Cells out (this system as source):

| receiver | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tennessee_eastman | -8.10 | 3.20 | 35.27 | 43.36 | 32.06 | marginal | -0.05 | 10/40 | damage |
| hai | 1.30 | 1.30 | 34.39 | 30.34 | 33.09 | derangement | — | 10/168 | short, damage |
| nasa_battery | 0.05 | 0.05 | -0.22 | -0.31 | -0.27 | derangement | 0.02 | 6/12 | short, damage |
| building_59 | -1.89 | 0.20 | 108.18 | 110.07 | 107.98 | marginal | -0.02 | 10/89 |  |
| alibaba_2018 | 1.87 | 1.96 | 1.56 | -0.31 | -0.40 | marginal | — | 6/27 | damage |

Nearest taxa by distance: shape_jaccard: hai 0.967, tennessee_eastman 1.0, nasa_battery 1.0; shape_bray_curtis: hai 0.964, tennessee_eastman 1.0, nasa_battery 1.0; transfer_net: hai 0.216, building_59 0.489, tennessee_eastman 1.0
