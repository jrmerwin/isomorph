# Brief — building_59 (method v8, a view)

*Lifts are odds ratios on the proposal split (3.6-3.8), confirmed on the confirmation split; absence is informative only above the signal floor (3.5); `no gain` means found but already carried by the trivial alternation model (3.11); loop-rule verdicts are recorded, not promoted (3.16); cells are bit-horizons net of the larger of two controls, with share of the receiver's ceiling where a diagonal exists (3.12).*

## Identity

- kind: real office building (LBNL Building 59, 4 RTUs, ~50 zones); standing: admitted (365 days)
- entity: unit (55 units); H = 820.0 min; lag edges [27.37, 149.81, 820.0] min
- periods: slow 1366.9, fast —; admission: {'days': 364.97, 'slow_periods': 384.5, 'horizons': 640.9, 'test_horizons': 160.2, 'admitted': True, 'by': 'days'}
- claim: **no gain** — library 2.760 bits, triviality 2.638, best baseline 3.235; gain over triviality -0.122
- events 276110, types 89, signal floor 68

## Vocabulary

| role | full tag | quantity | scheme | loop tags (timing / determinism) |
| --- | --- | --- | --- | --- |
| T | MID·LOCAL·RELAY ⟨Θ⟩ | temperature | q20_50_80 | RESPONDS / REACTS |
| T_out | MID·LEAD ⟨Θ⟩ | temperature | q20_50_80 | — / — |
| Tsp_c | SET·LOCAL·RELAY ⟨Θ⟩ | temperature | q20_50_80 | — / RESPONDS |
| Tsp_h | SET·LOCAL·LEAD ⟨Θ⟩ | temperature | q20_50_80 | — / — |
| co2 | MID·ISOLATED | — | q20_50_80 | — / — |
| econ_sp | SET·ISOLATED ⟨Θ⟩ | temperature | q20_50_80 | — / — |
| fan | SET·LOCAL·RELAY | — | q10_90 | REACTS / — |
| hvac_kw_N | SLOW-S·LEAD ⟨M L² T⁻³⟩ | power | q10_90 | — / — |
| hvac_kw_S | MID-S·LEAD ⟨M L² T⁻³⟩ | power | q20_50_80 | — / — |
| hw_valve | MID-S·LOCAL·RELAY | — | q10_90 | — / RESPONDS |
| ma_t | MID·LOCAL·RELAY ⟨Θ⟩ | temperature | dsign | RESPONDS / RESPONDS |
| oa_damper | MID-S·COMMON·RELAY | — | q10_90 | REACTS / REACTS |
| oa_flow | MID·COMMON·RELAY ⟨L³ T⁻¹⟩ | volume_flow | q20_50_80 | REACTS / REACTS |
| oa_t | MID·COMMON·LEAD ⟨Θ⟩ | temperature | dsign | REACTS / — |
| plenum_p | MID·LOCAL·RELAY ⟨M L⁻¹ T⁻²⟩ | pressure | q20_50_80 | RESPONDS / REACTS |
| ra_t | MID·LOCAL·RELAY ⟨Θ⟩ | temperature | dsign | RESPONDS / RESPONDS |
| rf_spd | SLOW·COMMON·RELAY | — | q20_50_80 | REACTS / REACTS |
| rh_out | SLOW·LEAD | — | q20_50_80 | — / — |
| sa_flow | SLOW·COMMON·RELAY ⟨L³ T⁻¹⟩ | volume_flow | q20_50_80 | REACTS / RESPONDS |
| sa_t | MID·LOCAL·RELAY ⟨Θ⟩ | temperature | q20_50_80 | — / RESPONDS |
| sat_sp | SET·ISOLATED ⟨Θ⟩ | temperature | q10_90 | — / — |
| sf_spd | SLOW·COMMON·RELAY | — | q20_50_80 | RESPONDS / RESPONDS |
| solar | MID-S·ISOLATED ⟨M T⁻³⟩ | irradiance | silent | — / — |
| static_sp | SET·ISOLATED ⟨M L⁻¹ T⁻²⟩ | pressure | q20_50_80 | — / — |

## Couplings (validated fragments)

| prior | lag | target | lift | conf. lift | n | binding | shape | confirmed in | failed in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fan:upq90 | m | fan:downq90 | 154.575 | 153.787 | 84 | True | `SET.up.q90 -m-> SET.down.q90 [same role]` | tennessee_eastman | hai |
| fan:upq10 | s | Tsp_c:downq80 | 96.152 | 72.078 | 215 | True | `SET.up.q10 -s-> SET.down.q80` | — | hai |
| fan:upq10 | s | Tsp_c:downq20 | 86.319 | 82.548 | 201 | True | `SET.up.q10 -s-> SET.down.q20` | — | hai |
| fan:upq10 | s | Tsp_h:upq20 | 72.234 | 12.137 | 88 | True | `SET.up.q10 -s-> SET.up.q20` | — | tennessee_eastman, hai |
| sa_t:downq50 | s | sa_t:upq50 | 48.814 | 11.971 | 179 | True | `MID.down.q50 -s-> MID.up.q50 [same role]` | — | tennessee_eastman, hai |
| hw_valve:upq10 | s | Tsp_h:upq20 | 47.304 | 9.718 | 140 | True | `MID-S.up.q10 -s-> SET.up.q20` | — | tennessee_eastman, hai |
| fan:downq90 | s | fan:downq10 | 45.706 | 50.788 | 61 | True | `SET.down.q90 -s-> SET.down.q10 [same role]` | tennessee_eastman | hai |
| hw_valve:upq10 | s | Tsp_c:downq80 | 45.286 | 25.149 | 246 | True | `MID-S.up.q10 -s-> SET.down.q80` | — | hai |
| oa_damper:upq90 | s | oa_damper:downq90 | 45.129 | 35.079 | 79 | True | `MID-S.up.q90 -s-> MID-S.down.q90 [same role]` | tennessee_eastman | hai |
| oa_damper:downq10 | s | oa_damper:upq10 | 44.645 | 38.401 | 49 | True | `MID-S.down.q10 -s-> MID-S.up.q10 [same role]` | tennessee_eastman, hai | — |
| hw_valve:upq10 | s | Tsp_c:downq50 | 43.217 | 21.325 | 51 | True | `MID-S.up.q10 -s-> SET.down.q50` | — | hai |
| oa_damper:downq90 | s | oa_damper:downq10 | 42.344 | 49.472 | 67 | True | `MID-S.down.q90 -s-> MID-S.down.q10 [same role]` | tennessee_eastman | hai |
| oa_damper:upq10 | s | oa_damper:upq90 | 42.141 | 58.821 | 76 | True | `MID-S.up.q10 -s-> MID-S.up.q90 [same role]` | tennessee_eastman | hai |
| fan:upq90 | l | fan:downq90 | 41.834 | 52.162 | 283 | True | `SET.up.q90 -l-> SET.down.q90 [same role]` | — | tennessee_eastman, hai |
| fan:upq10 | s | fan:upq90 | 41.542 | 52.936 | 123 | True | `SET.up.q10 -s-> SET.up.q90 [same role]` | tennessee_eastman | hai |
| hw_valve:upq10 | s | Tsp_c:downq20 | 40.304 | 30.187 | 228 | True | `MID-S.up.q10 -s-> SET.down.q20` | — | hai |
| sa_t:downq20 | s | sa_t:upq20 | 38.992 | 30.529 | 325 | True | `MID.down.q20 -s-> MID.up.q20 [same role]` | tennessee_eastman | hai |
| sa_t:upq50 | s | sa_t:downq50 | 37.091 | 68.402 | 100 | True | `MID.up.q50 -s-> MID.down.q50 [same role]` | — | tennessee_eastman, hai |
| oa_flow:downq20 | s | oa_flow:upq20 | 31.633 | 18.629 | 137 | True | `MID.down.q20 -s-> MID.up.q20 [same role]` | tennessee_eastman, hai | — |
| sf_spd:upq80 | s | sf_spd:downq80 | 31.099 | 22.603 | 243 | True | `SLOW.up.q80 -s-> SLOW.down.q80 [same role]` | hai | tennessee_eastman |
| oa_damper:downq90 | s | oa_damper:upq90 | 30.75 | 25.941 | 63 | True | `MID-S.down.q90 -s-> MID-S.up.q90 [same role]` | — | tennessee_eastman, hai |
| sa_flow:downq20 | s | sa_flow:upq20 | 29.738 | 22.134 | 228 | True | `SLOW.down.q20 -s-> SLOW.up.q20 [same role]` | hai | tennessee_eastman |
| oa_damper:upq90 | m | oa_damper:downq90 | 27.387 | 22.196 | 181 | True | `MID-S.up.q90 -m-> MID-S.down.q90 [same role]` | tennessee_eastman | hai |
| oa_damper:upq10 | s | oa_damper:downq10 | 26.564 | 24.508 | 37 | True | `MID-S.up.q10 -s-> MID-S.down.q10 [same role]` | hai | tennessee_eastman |
| rf_spd:downq20 | s | rf_spd:upq20 | 26.275 | 24.003 | 301 | True | `SLOW.down.q20 -s-> SLOW.up.q20 [same role]` | hai | tennessee_eastman |
| Tsp_c:upq20 | s | fan:downq10 | 26.021 | 30.57 | 46 | True | `SET.up.q20 -s-> SET.down.q10` | — | hai |
| Tsp_c:upq80 | s | fan:downq10 | 25.394 | 33.717 | 55 | True | `SET.up.q80 -s-> SET.down.q10` | — | hai |
| rf_spd:upq80 | s | rf_spd:downq80 | 25.04 | 18.461 | 492 | True | `SLOW.up.q80 -s-> SLOW.down.q80 [same role]` | hai | tennessee_eastman |
| sf_spd:downq20 | s | sf_spd:upq20 | 24.989 | 20.502 | 233 | True | `SLOW.down.q20 -s-> SLOW.up.q20 [same role]` | — | tennessee_eastman, hai |
| fan:upq10 | s | Tsp_c:downq50 | 24.703 | 36.527 | 12 | True | `SET.up.q10 -s-> SET.down.q50` | — | hai |
| sa_flow:upq80 | s | sa_flow:downq80 | 24.313 | 18.688 | 311 | True | `SLOW.up.q80 -s-> SLOW.down.q80 [same role]` | hai | tennessee_eastman |
| oa_flow:upq20 | s | oa_flow:downq20 | 23.103 | 9.47 | 111 | True | `MID.up.q20 -s-> MID.down.q20 [same role]` | hai | tennessee_eastman |
| Tsp_h:downq20 | s | fan:downq10 | 21.534 | 16.27 | 30 | True | `SET.down.q20 -s-> SET.down.q10` | — | tennessee_eastman, hai |
| T:upq80 | m | fan:upq90 | 21.094 | 28.759 | 279 | True | `MID.up.q80 -m-> SET.up.q90` | — | tennessee_eastman, hai |
| sf_spd:downq20 | s | sa_flow:downq20 | 20.261 | 12.495 | 179 | True | `SLOW.down.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| plenum_p:downq20 | s | plenum_p:upq20 | 20.017 | 17.295 | 599 | True | `MID.down.q20 -s-> MID.up.q20 [same role]` | — | tennessee_eastman, hai |
| T:downq80 | s | fan:downq90 | 19.828 | 40.333 | 67 | True | `MID.down.q80 -s-> SET.down.q90` | — | tennessee_eastman, hai |
| oa_damper:downq10 | m | oa_damper:upq10 | 18.826 | 14.846 | 73 | True | `MID-S.down.q10 -m-> MID-S.up.q10 [same role]` | tennessee_eastman, hai | — |
| sa_t:downq50 | m | sa_t:upq50 | 18.753 | 11.888 | 206 | True | `MID.down.q50 -m-> MID.up.q50 [same role]` | tennessee_eastman | hai |
| sf_spd:downq80 | s | sf_spd:upq80 | 18.745 | 19.818 | 160 | True | `SLOW.down.q80 -s-> SLOW.up.q80 [same role]` | hai | tennessee_eastman |
| sa_flow:upq20 | s | sa_flow:downq20 | 18.193 | 10.078 | 162 | True | `SLOW.up.q20 -s-> SLOW.down.q20 [same role]` | — | tennessee_eastman, hai |
| sa_flow:upq20 | s | sf_spd:upq20 | 18.089 | 10.015 | 170 | True | `SLOW.up.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_flow:downq20 | m | oa_flow:upq20 | 18.078 | 7.035 | 292 | True | `MID.down.q20 -m-> MID.up.q20 [same role]` | tennessee_eastman, hai | — |
| sa_t:upq20 | s | sa_t:downq20 | 17.935 | 19.696 | 122 | True | `MID.up.q20 -s-> MID.down.q20 [same role]` | — | tennessee_eastman, hai |
| sa_flow:downq20 | s | sf_spd:upq20 | 17.92 | 13.521 | 145 | True | `SLOW.down.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| sf_spd:upq20 | s | sf_spd:downq20 | 17.877 | 11.327 | 151 | True | `SLOW.up.q20 -s-> SLOW.down.q20 [same role]` | — | tennessee_eastman, hai |
| sf_spd:downq20 | s | sa_flow:upq20 | 17.092 | 16.152 | 151 | True | `SLOW.down.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| sa_flow:downq80 | s | sa_flow:upq80 | 16.849 | 14.813 | 200 | True | `SLOW.down.q80 -s-> SLOW.up.q80 [same role]` | hai | tennessee_eastman |
| oa_flow:upq20 | s | oa_damper:upq10 | 16.194 | 25.119 | 32 | True | `MID.up.q20 -s-> MID-S.up.q10` | — | tennessee_eastman, hai |
| rf_spd:upq20 | s | rf_spd:downq20 | 15.538 | 10.918 | 185 | True | `SLOW.up.q20 -s-> SLOW.down.q20 [same role]` | — | tennessee_eastman, hai |
| ma_t:peak | s | oa_damper:upq10 | 15.286 | 21.557 | 41 | True | `MID.peak -s-> MID-S.up.q10` | — | tennessee_eastman, hai |
| sa_flow:upq80 | s | sf_spd:upq80 | 15.21 | 7.104 | 151 | True | `SLOW.up.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| hw_valve:upq90 | s | hw_valve:downq90 | 14.824 | 12.842 | 537 | True | `MID-S.up.q90 -s-> MID-S.down.q90 [same role]` | hai | tennessee_eastman, fingrid |
| oa_flow:upq80 | s | oa_flow:downq80 | 14.405 | 12.779 | 103 | True | `MID.up.q80 -s-> MID.down.q80 [same role]` | tennessee_eastman, hai | — |
| T:upq80 | s | fan:upq10 | 14.286 | 22.654 | 197 | True | `MID.up.q80 -s-> SET.up.q10` | — | tennessee_eastman, hai |
| oa_flow:upq50 | s | oa_flow:downq50 | 14.277 | 5.449 | 186 | True | `MID.up.q50 -s-> MID.down.q50 [same role]` | hai | tennessee_eastman |
| sa_t:downq20 | m | sa_t:upq20 | 14.237 | 14.663 | 356 | True | `MID.down.q20 -m-> MID.up.q20 [same role]` | tennessee_eastman | hai |
| Tsp_c:upq50 | s | fan:downq10 | 14.236 | 17.083 | 6 | True | `SET.up.q50 -s-> SET.down.q10` | — | hai |
| sa_flow:downq20 | m | sa_flow:upq20 | 13.995 | 9.745 | 348 | True | `SLOW.down.q20 -m-> SLOW.up.q20 [same role]` | hai | tennessee_eastman |
| fan:upq10 | m | fan:downq10 | 13.854 | 7.946 | 157 | True | `SET.up.q10 -m-> SET.down.q10 [same role]` | — | tennessee_eastman, hai |
| T:upq20 | s | hw_valve:downq90 | 13.758 | 11.515 | 708 | True | `MID.up.q20 -s-> MID-S.down.q90` | — | tennessee_eastman, hai |
| plenum_p:upq80 | s | plenum_p:downq80 | 13.7 | 11.325 | 973 | True | `MID.up.q80 -s-> MID.down.q80 [same role]` | — | tennessee_eastman, hai |
| T:downq20 | s | hw_valve:upq90 | 13.603 | 10.268 | 873 | True | `MID.down.q20 -s-> MID-S.up.q90` | — | tennessee_eastman, hai |
| oa_flow:downq50 | s | oa_flow:upq50 | 13.585 | 10.941 | 172 | True | `MID.down.q50 -s-> MID.up.q50 [same role]` | hai | tennessee_eastman |
| sa_flow:downq20 | m | sf_spd:upq20 | 13.374 | 10.183 | 351 | True | `SLOW.down.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| fan:downq90 | l | Tsp_c:upq50 | 13.319 | 14.288 | 10 | True | `SET.down.q90 -l-> SET.up.q50` | — | hai |
| rf_spd:downq80 | s | rf_spd:upq80 | 13.285 | 13.506 | 255 | True | `SLOW.down.q80 -s-> SLOW.up.q80 [same role]` | hai | tennessee_eastman |
| sa_t:upq50 | m | sa_t:downq50 | 13.227 | 15.086 | 148 | True | `MID.up.q50 -m-> MID.down.q50 [same role]` | tennessee_eastman | hai |
| plenum_p:upq20 | s | plenum_p:downq20 | 13.174 | 8.978 | 406 | True | `MID.up.q20 -s-> MID.down.q20 [same role]` | hai | tennessee_eastman |
| sf_spd:downq20 | m | sf_spd:upq20 | 13.12 | 9.701 | 372 | True | `SLOW.down.q20 -m-> SLOW.up.q20 [same role]` | — | tennessee_eastman, hai |
| sa_t:upq20 | m | sa_t:downq20 | 12.974 | 11.93 | 325 | True | `MID.up.q20 -m-> MID.down.q20 [same role]` | tennessee_eastman | hai |
| oa_flow:upq20 | m | oa_flow:downq20 | 12.927 | 4.578 | 212 | True | `MID.up.q20 -m-> MID.down.q20 [same role]` | hai | tennessee_eastman |
| T:upq80 | s | T:downq80 | 12.865 | 9.864 | 717 | True | `MID.up.q80 -s-> MID.down.q80 [same role]` | tennessee_eastman, hai | — |
| oa_flow:downq80 | s | oa_damper:downq10 | 12.852 | 18.728 | 35 | True | `MID.down.q80 -s-> MID-S.down.q10` | — | tennessee_eastman, hai |
| oa_damper:upq10 | m | oa_damper:downq90 | 12.576 | 18.906 | 57 | True | `MID-S.up.q10 -m-> MID-S.down.q90 [same role]` | tennessee_eastman | hai |
| sa_t:downq20 | s | oa_damper:downq90 | 12.527 | 14.776 | 47 | True | `MID.down.q20 -s-> MID-S.down.q90` | — | tennessee_eastman, hai |
| sf_spd:downq20 | m | sa_flow:upq20 | 12.469 | 8.97 | 335 | True | `SLOW.down.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| sa_flow:upq20 | s | rf_spd:upq20 | 12.43 | 7.385 | 140 | True | `SLOW.up.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_damper:downq90 | m | oa_damper:upq90 | 12.307 | 10.107 | 80 | True | `MID-S.down.q90 -m-> MID-S.up.q90 [same role]` | tennessee_eastman | hai |
| sf_spd:upq20 | s | sa_flow:downq20 | 12.245 | 7.89 | 98 | True | `SLOW.up.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| oa_t:peak | s | ra_t:peak | 12.229 | 8.694 | 69 | False | `MID.peak -s-> MID.peak` | — | tennessee_eastman, hai, fingrid |
| sa_flow:downq20 | s | rf_spd:downq20 | 12.142 | 7.582 | 118 | True | `SLOW.down.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| rf_spd:downq20 | m | rf_spd:upq20 | 11.857 | 8.082 | 465 | True | `SLOW.down.q20 -m-> SLOW.up.q20 [same role]` | — | tennessee_eastman, hai |
| oa_flow:downq80 | s | oa_flow:upq80 | 11.791 | 8.834 | 93 | True | `MID.down.q80 -s-> MID.up.q80 [same role]` | hai | tennessee_eastman |
| T:downq80 | s | fan:downq10 | 11.572 | 20.398 | 139 | True | `MID.down.q80 -s-> SET.down.q10` | — | tennessee_eastman, hai |
| sa_flow:downq50 | s | sa_flow:upq50 | 11.54 | 9.183 | 488 | True | `SLOW.down.q50 -s-> SLOW.up.q50 [same role]` | hai | tennessee_eastman |
| sf_spd:downq50 | s | sf_spd:upq50 | 11.526 | 8.978 | 448 | True | `SLOW.down.q50 -s-> SLOW.up.q50 [same role]` | hai | tennessee_eastman |
| rf_spd:downq20 | s | sa_flow:upq20 | 11.373 | 10.731 | 103 | True | `SLOW.down.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| hw_valve:upq90 | m | hw_valve:downq90 | 11.364 | 10.545 | 1342 | True | `MID-S.up.q90 -m-> MID-S.down.q90 [same role]` | hai, fingrid | tennessee_eastman |
| oa_damper:upq90 | m | oa_damper:downq10 | 11.363 | 13.203 | 58 | True | `MID-S.up.q90 -m-> MID-S.down.q10 [same role]` | tennessee_eastman | hai |
| sf_spd:upq20 | s | rf_spd:upq20 | 11.36 | 8.884 | 115 | True | `SLOW.up.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| fan:downq90 | l | Tsp_c:upq80 | 11.298 | 7.686 | 41 | True | `SET.down.q90 -l-> SET.up.q80` | — | hai |
| sf_spd:upq80 | m | sf_spd:downq80 | 11.207 | 9.543 | 290 | True | `SLOW.up.q80 -m-> SLOW.down.q80 [same role]` | hai | tennessee_eastman |
| sf_spd:downq20 | s | rf_spd:downq20 | 11.162 | 8.655 | 125 | False | `SLOW.down.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| fan:upq10 | l | fan:downq10 | 11.133 | 12.014 | 696 | True | `SET.up.q10 -l-> SET.down.q10 [same role]` | — | tennessee_eastman, hai |
| sa_flow:upq20 | m | sa_flow:downq20 | 11.085 | 6.603 | 285 | True | `SLOW.up.q20 -m-> SLOW.down.q20 [same role]` | hai | tennessee_eastman |
| sf_spd:upq50 | s | sf_spd:downq50 | 10.995 | 8.604 | 393 | True | `SLOW.up.q50 -s-> SLOW.down.q50 [same role]` | hai | tennessee_eastman |
| sf_spd:downq80 | s | sa_flow:downq80 | 10.912 | 6.751 | 120 | True | `SLOW.down.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sf_spd:upq20 | m | sf_spd:downq20 | 10.822 | 6.385 | 327 | True | `SLOW.up.q20 -m-> SLOW.down.q20 [same role]` | — | tennessee_eastman, hai |
| sa_flow:upq50 | s | sa_flow:downq50 | 10.786 | 7.162 | 492 | True | `SLOW.up.q50 -s-> SLOW.down.q50 [same role]` | — | tennessee_eastman, hai |
| sa_flow:upq20 | m | sf_spd:downq20 | 10.761 | 7.126 | 292 | True | `SLOW.up.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| rf_spd:upq20 | s | sf_spd:upq20 | 10.692 | 7.313 | 106 | True | `SLOW.up.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| sf_spd:upq20 | s | plenum_p:upq20 | 10.555 | 3.116 | 175 | True | `SLOW.up.q20 -s-> MID.up.q20` | — | tennessee_eastman, hai |
| rf_spd:downq20 | s | sa_flow:downq20 | 10.489 | 9.684 | 95 | True | `SLOW.down.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| oa_flow:downq20 | s | oa_damper:downq10 | 10.47 | 25.648 | 19 | True | `MID.down.q20 -s-> MID-S.down.q10` | — | tennessee_eastman, hai |
| rf_spd:upq20 | s | sa_flow:upq20 | 10.433 | 6.388 | 98 | False | `SLOW.up.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_flow:upq20 | s | oa_damper:upq90 | 10.427 | 25.557 | 27 | True | `MID.up.q20 -s-> MID-S.up.q90` | — | tennessee_eastman, hai |
| fan:upq90 | l | Tsp_c:upq50 | 10.407 | 13.534 | 11 | True | `SET.up.q90 -l-> SET.up.q50` | — | hai |
| sf_spd:upq20 | m | sa_flow:downq20 | 10.374 | 5.63 | 297 | True | `SLOW.up.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| sa_flow:upq80 | s | sf_spd:downq80 | 10.346 | 11.776 | 103 | True | `SLOW.up.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_flow:upq20 | s | sf_spd:downq20 | 10.321 | 6.288 | 97 | True | `SLOW.up.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| T_out:upq80 | s | oa_damper:upq90 | 10.318 | 5.442 | 26 | False | `MID.up.q80 -s-> MID-S.up.q90` | — | tennessee_eastman, hai |
| oa_t:peak | m | ra_t:peak | 10.299 | 6.884 | 247 | True | `MID.peak -m-> MID.peak` | — | tennessee_eastman, hai, fingrid |
| oa_flow:upq80 | s | oa_damper:upq90 | 10.259 | 31.151 | 32 | True | `MID.up.q80 -s-> MID-S.up.q90` | — | tennessee_eastman, hai |
| Tsp_c:upq50 | s | hw_valve:downq10 | 10.219 | 7.007 | 14 | True | `SET.up.q50 -s-> MID-S.down.q10` | — | hai |
| oa_damper:upq10 | s | oa_flow:upq80 | 10.163 | 9.893 | 41 | False | `MID-S.up.q10 -s-> MID.up.q80` | — | tennessee_eastman, hai |
| oa_flow:upq20 | s | oa_flow:upq80 | 10.013 | 25.42 | 58 | True | `MID.up.q20 -s-> MID.up.q80 [same role]` | tennessee_eastman | hai |
| oa_damper:downq90 | s | oa_flow:downq80 | 10.008 | 9.036 | 47 | False | `MID-S.down.q90 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_damper:upq10 | m | oa_damper:downq10 | 9.999 | 8.874 | 35 | True | `MID-S.up.q10 -m-> MID-S.down.q10 [same role]` | tennessee_eastman, hai | — |
| sf_spd:upq80 | s | sa_flow:downq80 | 9.96 | 9.856 | 100 | True | `SLOW.up.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_flow:upq50 | s | oa_damper:upq10 | 9.921 | 20.274 | 31 | True | `MID.up.q50 -s-> MID-S.up.q10` | — | tennessee_eastman, hai |
| ma_t:trough | s | sa_t:upq50 | 9.88 | 2.229 | 48 | True | `MID.trough -s-> MID.up.q50` | — | tennessee_eastman, hai |
| plenum_p:downq50 | s | plenum_p:upq50 | 9.845 | 8.996 | 909 | True | `MID.down.q50 -s-> MID.up.q50 [same role]` | hai | tennessee_eastman |
| sa_flow:upq80 | m | sa_flow:downq80 | 9.824 | 7.376 | 397 | True | `SLOW.up.q80 -m-> SLOW.down.q80 [same role]` | hai | tennessee_eastman |
| hw_valve:downq90 | m | hw_valve:upq90 | 9.734 | 7.022 | 1142 | True | `MID-S.down.q90 -m-> MID-S.up.q90 [same role]` | hai | tennessee_eastman, fingrid |
| rf_spd:downq20 | m | sa_flow:upq20 | 9.708 | 6.226 | 301 | True | `SLOW.down.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| plenum_p:upq50 | s | plenum_p:downq50 | 9.539 | 6.926 | 928 | True | `MID.up.q50 -s-> MID.down.q50 [same role]` | — | tennessee_eastman, hai |
| sf_spd:downq80 | m | sf_spd:upq80 | 9.513 | 9.819 | 255 | True | `SLOW.down.q80 -m-> SLOW.up.q80 [same role]` | hai | tennessee_eastman |
| fan:downq90 | m | T:downq80 | 9.449 | 13.267 | 228 | True | `SET.down.q90 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| rf_spd:upq20 | m | rf_spd:downq20 | 9.443 | 7.026 | 380 | True | `SLOW.up.q20 -m-> SLOW.down.q20 [same role]` | — | tennessee_eastman, hai |
| plenum_p:downq80 | s | plenum_p:upq80 | 9.349 | 8.302 | 663 | True | `MID.down.q80 -s-> MID.up.q80 [same role]` | — | tennessee_eastman, hai |
| sa_flow:downq20 | m | rf_spd:upq20 | 9.347 | 6.048 | 294 | True | `SLOW.down.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| rf_spd:downq20 | s | sf_spd:upq20 | 9.206 | 8.184 | 88 | False | `SLOW.down.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| rf_spd:downq80 | s | sa_flow:downq80 | 9.162 | 6.002 | 134 | True | `SLOW.down.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_flow:downq20 | s | rf_spd:upq20 | 9.074 | 7.368 | 88 | True | `SLOW.down.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_flow:downq50 | s | oa_damper:downq10 | 9.014 | 20.27 | 28 | True | `MID.down.q50 -s-> MID-S.down.q10` | — | tennessee_eastman, hai |
| sf_spd:upq20 | m | sa_flow:upq20 | 9.011 | 6.313 | 258 | True | `SLOW.up.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| sf_spd:downq20 | m | sa_flow:downq20 | 9.008 | 6.093 | 242 | True | `SLOW.down.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| oa_flow:upq80 | m | oa_damper:upq90 | 8.961 | 12.215 | 112 | True | `MID.up.q80 -m-> MID-S.up.q90` | tennessee_eastman | hai |
| rf_spd:downq20 | m | sf_spd:upq20 | 8.954 | 6.7 | 293 | True | `SLOW.down.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| rf_spd:upq80 | s | sa_flow:downq80 | 8.95 | 6.382 | 134 | True | `SLOW.up.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rf_spd:downq50 | s | rf_spd:upq50 | 8.937 | 7.7 | 758 | True | `SLOW.down.q50 -s-> SLOW.up.q50 [same role]` | hai | tennessee_eastman |
| oa_damper:upq10 | s | oa_damper:downq90 | 8.872 | 11.648 | 16 | False | `MID-S.up.q10 -s-> MID-S.down.q90 [same role]` | — | tennessee_eastman, hai |
| sf_spd:downq20 | m | rf_spd:upq20 | 8.858 | 6.422 | 301 | True | `SLOW.down.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_damper:downq10 | m | oa_damper:upq90 | 8.856 | 11.653 | 45 | True | `MID-S.down.q10 -m-> MID-S.up.q90 [same role]` | tennessee_eastman | hai |
| Tsp_c:upq80 | m | T:downq20 | 8.79 | 8.391 | 88 | True | `SET.up.q80 -m-> MID.down.q20` | — | hai |
| rf_spd:downq20 | s | sf_spd:downq20 | 8.788 | 8.432 | 84 | False | `SLOW.down.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| sa_flow:downq80 | m | sa_flow:upq80 | 8.755 | 7.76 | 353 | True | `SLOW.down.q80 -m-> SLOW.up.q80 [same role]` | hai | tennessee_eastman |
| oa_damper:upq90 | s | sa_t:upq20 | 8.743 | 13.999 | 34 | True | `MID-S.up.q90 -s-> MID.up.q20` | — | tennessee_eastman, hai |
| rf_spd:upq50 | s | rf_spd:downq50 | 8.624 | 5.249 | 748 | True | `SLOW.up.q50 -s-> SLOW.down.q50 [same role]` | hai | tennessee_eastman |
| fan:downq90 | s | T:downq80 | 8.478 | 7.95 | 46 | True | `SET.down.q90 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_damper:downq90 | m | oa_damper:upq10 | 8.467 | 9.01 | 42 | True | `MID-S.down.q90 -m-> MID-S.up.q10 [same role]` | tennessee_eastman | hai |
| Tsp_c:upq20 | m | T:downq20 | 8.424 | 6.499 | 88 | True | `SET.up.q20 -m-> MID.down.q20` | — | hai |
| Tsp_h:downq20 | s | hw_valve:downq10 | 8.391 | 5.005 | 38 | True | `SET.down.q20 -s-> MID-S.down.q10` | — | tennessee_eastman, hai |
| sa_t:downq50 | s | oa_damper:downq90 | 8.352 | 7.321 | 21 | True | `MID.down.q50 -s-> MID-S.down.q90` | — | tennessee_eastman, hai |
| oa_t:peak | s | ma_t:peak | 8.325 | 12.161 | 71 | True | `MID.peak -s-> MID.peak` | hai | tennessee_eastman, fingrid |
| rf_spd:upq80 | m | rf_spd:downq80 | 8.319 | 7.731 | 556 | True | `SLOW.up.q80 -m-> SLOW.down.q80 [same role]` | hai | tennessee_eastman |
| fan:upq90 | l | Tsp_c:upq80 | 8.221 | 7.7 | 42 | True | `SET.up.q90 -l-> SET.up.q80` | — | hai |
| ra_t:peak | s | oa_t:peak | 8.21 | 3.849 | 43 | False | `MID.peak -s-> MID.peak` | — | tennessee_eastman, hai, fingrid |
| rf_spd:upq20 | m | sa_flow:downq20 | 8.158 | 4.572 | 259 | True | `SLOW.up.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| rf_spd:upq80 | s | sf_spd:downq80 | 8.153 | 7.111 | 95 | False | `SLOW.up.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| T:upq80 | m | fan:upq10 | 8.141 | 8.209 | 385 | True | `MID.up.q80 -m-> SET.up.q10` | — | tennessee_eastman, hai |
| hvac_kw_S:downq80 | s | sf_spd:downq80 | 8.116 | 4.543 | 140 | False | `MID-S.down.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_flow:upq80 | m | sf_spd:downq80 | 8.077 | 8.702 | 254 | True | `SLOW.up.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| fan:downq90 | l | Tsp_c:upq20 | 8.072 | 8.66 | 30 | True | `SET.down.q90 -l-> SET.up.q20` | — | hai |
| sa_flow:upq80 | s | rf_spd:upq80 | 7.982 | 7.584 | 134 | True | `SLOW.up.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| hw_valve:upq90 | s | Tsp_c:downq80 | 7.926 | 3.567 | 36 | True | `MID-S.up.q90 -s-> SET.down.q80` | — | hai |
| ra_t:peak | s | oa_flow:downq80 | 7.914 | 3.285 | 40 | False | `MID.peak -s-> MID.down.q80` | — | tennessee_eastman, hai |
| T:downq20 | s | T:upq20 | 7.877 | 7.78 | 1861 | True | `MID.down.q20 -s-> MID.up.q20 [same role]` | tennessee_eastman, hai | — |
| sa_flow:upq20 | s | plenum_p:upq20 | 7.86 | 3.204 | 145 | False | `SLOW.up.q20 -s-> MID.up.q20` | — | tennessee_eastman, hai |
| T_out:upq80 | m | oa_damper:downq90 | 7.855 | 7.135 | 85 | False | `MID.up.q80 -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| oa_damper:upq90 | s | sa_t:upq50 | 7.834 | 2.218 | 20 | True | `MID-S.up.q90 -s-> MID.up.q50` | — | tennessee_eastman, hai |
| hw_valve:upq90 | m | hw_valve:upq90 | 7.833 | 4.928 | 923 | True | `MID-S.up.q90 -m-> MID-S.up.q90 [same role]` | — | tennessee_eastman, hai, fingrid |
| sa_flow:upq50 | s | sf_spd:upq50 | 7.826 | 3.341 | 332 | True | `SLOW.up.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| sa_t:downq50 | s | oa_damper:upq10 | 7.818 | 14.023 | 15 | False | `MID.down.q50 -s-> MID-S.up.q10` | — | tennessee_eastman, hai |
| T_out:downq80 | s | oa_flow:downq80 | 7.784 | 8.259 | 38 | False | `MID.down.q80 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_flow:upq50 | s | oa_flow:upq80 | 7.751 | 23.848 | 71 | True | `MID.up.q50 -s-> MID.up.q80 [same role]` | tennessee_eastman, hai | — |
| oa_damper:upq90 | s | sa_t:downq20 | 7.725 | 11.439 | 30 | False | `MID-S.up.q90 -s-> MID.down.q20` | tennessee_eastman | hai |
| hw_valve:downq90 | m | hw_valve:downq90 | 7.697 | 5.853 | 905 | True | `MID-S.down.q90 -m-> MID-S.down.q90 [same role]` | — | tennessee_eastman, hai, fingrid |
| oa_damper:downq90 | s | oa_damper:upq10 | 7.676 | 8.433 | 12 | False | `MID-S.down.q90 -s-> MID-S.up.q10 [same role]` | — | tennessee_eastman, hai |
| fan:downq10 | s | T:downq80 | 7.657 | 3.755 | 125 | True | `SET.down.q10 -s-> MID.down.q80` | tennessee_eastman | hai |
| rf_spd:downq80 | s | sf_spd:downq80 | 7.643 | 6.703 | 87 | True | `SLOW.down.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| hw_valve:upq90 | s | T:upq20 | 7.642 | 7.844 | 1017 | True | `MID-S.up.q90 -s-> MID.up.q20` | — | tennessee_eastman, hai |
| sa_flow:downq80 | m | sf_spd:upq80 | 7.598 | 8.678 | 238 | True | `SLOW.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_flow:upq20 | m | rf_spd:downq20 | 7.579 | 4.631 | 247 | True | `SLOW.up.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| oa_flow:upq20 | s | oa_flow:upq50 | 7.484 | 13.904 | 61 | True | `MID.up.q20 -s-> MID.up.q50 [same role]` | tennessee_eastman | hai |
| oa_damper:downq90 | s | sa_t:upq20 | 7.47 | 11.858 | 34 | True | `MID-S.down.q90 -s-> MID.up.q20` | tennessee_eastman | hai |
| rf_spd:upq20 | m | sf_spd:downq20 | 7.461 | 4.63 | 250 | True | `SLOW.up.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| sf_spd:upq80 | m | sa_flow:downq80 | 7.459 | 6.331 | 248 | True | `SLOW.up.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| ma_t:peak | s | ra_t:peak | 7.452 | 8.793 | 49 | False | `MID.peak -s-> MID.peak` | hai | tennessee_eastman, fingrid |
| rf_spd:upq20 | s | plenum_p:upq20 | 7.4 | 2.313 | 144 | True | `SLOW.up.q20 -s-> MID.up.q20` | — | tennessee_eastman, hai |
| rf_spd:downq80 | m | rf_spd:upq80 | 7.368 | 6.83 | 492 | True | `SLOW.down.q80 -m-> SLOW.up.q80 [same role]` | — | tennessee_eastman, hai |
| oa_damper:downq90 | s | sa_t:upq50 | 7.363 | 3.861 | 22 | True | `MID-S.down.q90 -s-> MID.up.q50` | — | tennessee_eastman, hai |
| sa_t:upq20 | m | oa_damper:downq90 | 7.35 | 8.13 | 83 | True | `MID.up.q20 -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| ra_t:peak | m | oa_flow:downq80 | 7.349 | 4.673 | 159 | True | `MID.peak -m-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_flow:upq80 | m | oa_flow:downq80 | 7.329 | 7.065 | 210 | True | `MID.up.q80 -m-> MID.down.q80 [same role]` | tennessee_eastman, hai | — |
| sa_flow:downq80 | s | rf_spd:downq80 | 7.31 | 6.655 | 114 | True | `SLOW.down.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_flow:downq80 | s | sf_spd:upq80 | 7.265 | 11.44 | 67 | True | `SLOW.down.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sf_spd:upq80 | s | rf_spd:upq80 | 7.21 | 6.467 | 95 | True | `SLOW.up.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_flow:downq20 | s | plenum_p:downq20 | 7.177 | 3.796 | 114 | True | `SLOW.down.q20 -s-> MID.down.q20` | — | tennessee_eastman, hai |
| sf_spd:downq80 | m | sa_flow:downq80 | 7.152 | 6.227 | 247 | True | `SLOW.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| plenum_p:downq20 | s | sf_spd:upq20 | 7.15 | 3.478 | 109 | False | `MID.down.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_damper:downq90 | m | sa_t:upq20 | 7.133 | 11.296 | 103 | True | `MID-S.down.q90 -m-> MID.up.q20` | tennessee_eastman | hai |
| ma_t:peak | s | oa_damper:upq90 | 7.112 | 18.408 | 25 | True | `MID.peak -s-> MID-S.up.q90` | — | tennessee_eastman, hai |
| Tsp_h:downq20 | m | T:downq20 | 7.061 | 6.487 | 42 | True | `SET.down.q20 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| T_out:downq80 | m | fan:downq90 | 7.055 | 7.566 | 85 | False | `MID.down.q80 -m-> SET.down.q90` | — | tennessee_eastman, hai |
| sf_spd:downq20 | s | plenum_p:downq20 | 7.048 | 3.825 | 129 | True | `SLOW.down.q20 -s-> MID.down.q20` | — | tennessee_eastman, hai |
| hvac_kw_N:upq10 | s | sa_flow:upq20 | 7.043 | 7.528 | 137 | False | `SLOW-S.up.q10 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| ma_t:trough | s | sa_t:upq20 | 7.027 | 29.627 | 52 | True | `MID.trough -s-> MID.up.q20` | — | tennessee_eastman, hai |
| sf_spd:downq80 | s | rf_spd:downq80 | 6.998 | 4.826 | 101 | True | `SLOW.down.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_damper:downq90 | m | oa_flow:downq80 | 6.98 | 7.258 | 104 | False | `MID-S.down.q90 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_damper:downq90 | m | oa_damper:downq10 | 6.972 | 6.321 | 35 | False | `MID-S.down.q90 -m-> MID-S.down.q10 [same role]` | — | tennessee_eastman, hai |
| plenum_p:downq20 | s | sf_spd:downq20 | 6.953 | 2.504 | 106 | False | `MID.down.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| oa_damper:downq10 | s | oa_damper:upq90 | 6.953 | 15.489 | 10 | False | `MID-S.down.q10 -s-> MID-S.up.q90 [same role]` | — | tennessee_eastman, hai |
| sf_spd:upq20 | m | rf_spd:downq20 | 6.944 | 4.509 | 252 | True | `SLOW.up.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| plenum_p:downq20 | s | sa_flow:upq20 | 6.923 | 4.552 | 100 | False | `MID.down.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| sf_spd:downq80 | s | sa_flow:upq80 | 6.918 | 7.803 | 76 | True | `SLOW.down.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| plenum_p:downq20 | s | sa_flow:downq20 | 6.853 | 3.818 | 99 | False | `MID.down.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| plenum_p:downq20 | m | plenum_p:upq20 | 6.833 | 4.911 | 668 | True | `MID.down.q20 -m-> MID.up.q20 [same role]` | — | tennessee_eastman, hai |
| rf_spd:upq80 | s | sa_flow:upq80 | 6.82 | 4.919 | 102 | True | `SLOW.up.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sf_spd:downq20 | s | rf_spd:upq20 | 6.801 | 6.024 | 76 | True | `SLOW.down.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_t:peak | m | oa_damper:upq10 | 6.747 | 16.032 | 66 | True | `MID.peak -m-> MID-S.up.q10` | — | tennessee_eastman, hai |
| oa_damper:downq10 | s | oa_flow:downq20 | 6.745 | 8.574 | 18 | False | `MID-S.down.q10 -s-> MID.down.q20` | — | tennessee_eastman, hai |
| oa_flow:upq80 | s | oa_damper:downq90 | 6.733 | 8.871 | 21 | True | `MID.up.q80 -s-> MID-S.down.q90` | — | tennessee_eastman, hai |
| oa_damper:downq90 | m | sa_t:downq20 | 6.726 | 11.25 | 97 | True | `MID-S.down.q90 -m-> MID.down.q20` | tennessee_eastman | hai |
| oa_damper:downq10 | m | oa_damper:downq90 | 6.691 | 8.092 | 34 | False | `MID-S.down.q10 -m-> MID-S.down.q90 [same role]` | — | tennessee_eastman, hai |
| hvac_kw_N:upq10 | s | sf_spd:upq20 | 6.673 | 7.388 | 137 | False | `SLOW-S.up.q10 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_damper:downq10 | l | oa_damper:upq10 | 6.662 | 7.881 | 92 | True | `MID-S.down.q10 -l-> MID-S.up.q10 [same role]` | — | tennessee_eastman, hai |
| oa_flow:upq50 | s | oa_damper:upq90 | 6.594 | 22.139 | 27 | True | `MID.up.q50 -s-> MID-S.up.q90` | — | tennessee_eastman, hai |
| fan:upq10 | m | fan:downq90 | 6.587 | 5.492 | 21 | True | `SET.up.q10 -m-> SET.down.q90 [same role]` | — | tennessee_eastman, hai |
| T_out:downq80 | s | oa_damper:downq90 | 6.574 | 6.863 | 14 | False | `MID.down.q80 -s-> MID-S.down.q90` | — | tennessee_eastman, hai |
| T:upq80 | m | T:downq80 | 6.556 | 5.864 | 1253 | True | `MID.up.q80 -m-> MID.down.q80 [same role]` | tennessee_eastman, hai | — |
| sa_flow:upq80 | s | rf_spd:downq80 | 6.553 | 5.238 | 110 | True | `SLOW.up.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_t:upq50 | s | oa_damper:upq90 | 6.533 | 10.943 | 12 | False | `MID.up.q50 -s-> MID-S.up.q90` | — | tennessee_eastman, hai |
| sf_spd:downq80 | m | sa_flow:upq80 | 6.522 | 6.626 | 225 | True | `SLOW.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_t:downq20 | m | oa_damper:upq90 | 6.486 | 6.773 | 73 | False | `MID.down.q20 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| fan:upq10 | l | fan:downq90 | 6.482 | 6.594 | 114 | True | `SET.up.q10 -l-> SET.down.q90 [same role]` | — | tennessee_eastman, hai |
| T:upq50 | s | T:downq50 | 6.424 | 5.403 | 1904 | True | `MID.up.q50 -s-> MID.down.q50 [same role]` | hai | tennessee_eastman |
| rh_out:downq20 | s | oa_damper:downq10 | 6.41 | 6.08 | 17 | False | `SLOW.down.q20 -s-> MID-S.down.q10` | — | tennessee_eastman, hai |
| fan:upq90 | l | fan:downq10 | 6.404 | 6.643 | 154 | True | `SET.up.q90 -l-> SET.down.q10 [same role]` | — | tennessee_eastman, hai |
| sf_spd:upq50 | s | sa_flow:downq50 | 6.4 | 4.925 | 248 | True | `SLOW.up.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| Tsp_c:upq50 | m | T:downq20 | 6.4 | 9.432 | 13 | True | `SET.up.q50 -m-> MID.down.q20` | — | hai |
| sa_t:downq20 | s | oa_damper:upq90 | 6.397 | 10.004 | 24 | False | `MID.down.q20 -s-> MID-S.up.q90` | tennessee_eastman | hai |
| oa_damper:downq10 | s | oa_flow:downq80 | 6.369 | 4.018 | 21 | False | `MID-S.down.q10 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| rf_spd:upq80 | s | sf_spd:upq80 | 6.368 | 5.094 | 74 | False | `SLOW.up.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| ra_t:peak | s | oa_damper:downq90 | 6.35 | 13.446 | 14 | False | `MID.peak -s-> MID-S.down.q90` | — | tennessee_eastman, hai |
| oa_damper:upq90 | m | sa_t:upq20 | 6.334 | 9.96 | 93 | True | `MID-S.up.q90 -m-> MID.up.q20` | tennessee_eastman | hai |
| oa_flow:upq80 | m | oa_damper:downq90 | 6.321 | 13.578 | 79 | True | `MID.up.q80 -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| sa_flow:upq80 | m | rf_spd:downq80 | 6.279 | 6.217 | 333 | True | `SLOW.up.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| fan:upq10 | m | fan:upq90 | 6.273 | 2.746 | 20 | False | `SET.up.q10 -m-> SET.up.q90 [same role]` | tennessee_eastman | hai |
| sf_spd:downq50 | s | sa_flow:downq50 | 6.269 | 2.982 | 262 | True | `SLOW.down.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| ra_t:trough | s | oa_t:trough | 6.24 | 4.878 | 30 | False | `MID.trough -s-> MID.trough` | — | tennessee_eastman, hai, fingrid |
| Tsp_c:upq50 | m | T:downq50 | 6.232 | 2.449 | 15 | True | `SET.up.q50 -m-> MID.down.q50` | — | hai |
| ma_t:peak | s | oa_t:peak | 6.228 | 9.563 | 52 | False | `MID.peak -s-> MID.peak` | hai | tennessee_eastman, fingrid |
| rf_spd:upq80 | m | sa_flow:downq80 | 6.225 | 4.991 | 317 | True | `SLOW.up.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| T_out:upq80 | m | oa_damper:downq10 | 6.222 | 6.536 | 52 | False | `MID.up.q80 -m-> MID-S.down.q10` | — | tennessee_eastman, hai |
| sa_t:downq20 | m | oa_damper:downq90 | 6.219 | 7.232 | 70 | False | `MID.down.q20 -m-> MID-S.down.q90` | tennessee_eastman | hai |
| sf_spd:downq50 | s | sa_flow:upq50 | 6.207 | 5.169 | 260 | True | `SLOW.down.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| oa_damper:upq90 | m | oa_flow:downq80 | 6.205 | 6.899 | 94 | False | `MID-S.up.q90 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_damper:upq90 | m | sa_t:downq20 | 6.138 | 10.756 | 90 | True | `MID-S.up.q90 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| oa_damper:downq90 | m | sa_t:upq50 | 6.118 | 3.63 | 58 | True | `MID-S.down.q90 -m-> MID.up.q50` | — | tennessee_eastman, hai |
| plenum_p:upq20 | s | sf_spd:downq20 | 6.114 | 1.662 | 96 | False | `MID.up.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| sa_flow:upq80 | m | rf_spd:upq80 | 6.091 | 5.672 | 323 | True | `SLOW.up.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rf_spd:upq20 | s | sa_flow:downq20 | 6.068 | 5.057 | 57 | False | `SLOW.up.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| rf_spd:downq20 | m | sa_flow:downq20 | 6.064 | 2.997 | 188 | False | `SLOW.down.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| oa_flow:downq80 | s | oa_flow:downq50 | 6.061 | 7.876 | 68 | True | `MID.down.q80 -s-> MID.down.q50 [same role]` | tennessee_eastman | hai |
| sa_flow:downq20 | m | plenum_p:upq20 | 6.057 | 2.594 | 312 | True | `SLOW.down.q20 -m-> MID.up.q20` | — | tennessee_eastman, hai |
| sa_flow:downq80 | m | rf_spd:upq80 | 6.041 | 6.113 | 320 | True | `SLOW.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_t:upq20 | m | oa_damper:upq90 | 6.022 | 6.026 | 68 | False | `MID.up.q20 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| T_out:upq80 | m | oa_damper:upq90 | 6.007 | 5.728 | 65 | False | `MID.up.q80 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| sf_spd:upq20 | s | sa_flow:upq20 | 5.998 | 4.304 | 48 | False | `SLOW.up.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| plenum_p:upq20 | m | plenum_p:downq20 | 5.978 | 4.31 | 587 | True | `MID.up.q20 -m-> MID.down.q20 [same role]` | hai | tennessee_eastman |
| sa_flow:downq50 | s | sf_spd:upq50 | 5.964 | 4.967 | 234 | True | `SLOW.down.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| T:downq20 | m | hw_valve:downq90 | 5.936 | 4.197 | 1272 | True | `MID.down.q20 -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| fan:upq90 | l | Tsp_c:upq20 | 5.925 | 8.43 | 31 | True | `SET.up.q90 -l-> SET.up.q20` | — | hai |
| hw_valve:downq90 | s | hw_valve:downq10 | 5.902 | 4.789 | 294 | True | `MID-S.down.q90 -s-> MID-S.down.q10 [same role]` | — | tennessee_eastman, hai, fingrid |
| sa_flow:upq50 | s | sf_spd:downq50 | 5.894 | 4.432 | 248 | True | `SLOW.up.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| T:downq50 | s | hw_valve:upq10 | 5.88 | 3.03 | 428 | True | `MID.down.q50 -s-> MID-S.up.q10` | — | tennessee_eastman, hai |
| ra_t:peak | s | oa_damper:downq10 | 5.873 | 12.536 | 10 | True | `MID.peak -s-> MID-S.down.q10` | — | tennessee_eastman, hai |
| sf_spd:downq20 | m | plenum_p:upq20 | 5.857 | 2.655 | 326 | True | `SLOW.down.q20 -m-> MID.up.q20` | — | tennessee_eastman, hai |
| sf_spd:upq20 | m | rf_spd:upq20 | 5.854 | 4.384 | 212 | True | `SLOW.up.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_damper:downq10 | s | oa_t:peak | 5.854 | 4.582 | 20 | False | `MID-S.down.q10 -s-> MID.peak` | — | tennessee_eastman, hai |
| hw_valve:upq10 | s | hw_valve:upq90 | 5.852 | 6.029 | 253 | True | `MID-S.up.q10 -s-> MID-S.up.q90 [same role]` | fingrid | tennessee_eastman, hai |
| T:downq80 | s | T:upq80 | 5.851 | 4.824 | 286 | True | `MID.down.q80 -s-> MID.up.q80 [same role]` | hai | tennessee_eastman |
| rf_spd:downq20 | s | plenum_p:downq20 | 5.809 | 2.527 | 109 | False | `SLOW.down.q20 -s-> MID.down.q20` | — | tennessee_eastman, hai |
| sa_flow:downq20 | m | rf_spd:downq20 | 5.806 | 4.527 | 183 | True | `SLOW.down.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| Tsp_c:downq20 | s | T:upq20 | 5.789 | 5.925 | 27 | True | `SET.down.q20 -s-> MID.up.q20` | — | hai |
| oa_damper:upq10 | m | oa_flow:downq80 | 5.775 | 6.237 | 60 | False | `MID-S.up.q10 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| rf_spd:upq80 | m | sf_spd:downq80 | 5.753 | 5.797 | 228 | True | `SLOW.up.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| plenum_p:downq20 | s | rf_spd:downq20 | 5.734 | 2.433 | 105 | False | `MID.down.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| oa_flow:upq50 | m | oa_flow:upq80 | 5.723 | 5.944 | 196 | True | `MID.up.q50 -m-> MID.up.q80 [same role]` | tennessee_eastman | hai |
| sf_spd:upq80 | m | sa_flow:upq80 | 5.72 | 6.184 | 190 | True | `SLOW.up.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| ma_t:trough | s | oa_damper:upq90 | 5.704 | 7.719 | 19 | False | `MID.trough -s-> MID-S.up.q90` | — | tennessee_eastman, hai |
| Tsp_c:upq80 | s | hw_valve:downq10 | 5.682 | 2.075 | 40 | True | `SET.up.q80 -s-> MID-S.down.q10` | — | hai |
| oa_flow:downq20 | m | oa_damper:upq10 | 5.682 | 11.005 | 38 | True | `MID.down.q20 -m-> MID-S.up.q10` | tennessee_eastman | hai |
| hvac_kw_S:upq80 | s | oa_damper:downq90 | 5.678 | 5.796 | 39 | False | `MID-S.up.q80 -s-> MID-S.down.q90` | — | tennessee_eastman, hai |
| oa_flow:downq20 | s | sf_spd:upq20 | 5.667 | 2.015 | 32 | False | `MID.down.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_damper:downq90 | l | sa_t:downq20 | 5.65 | 10.286 | 206 | True | `MID-S.down.q90 -l-> MID.down.q20` | — | tennessee_eastman, hai |
| hvac_kw_N:downq10 | s | sa_flow:downq20 | 5.646 | 3.965 | 97 | False | `SLOW-S.down.q10 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| oa_flow:downq80 | s | sa_t:upq50 | 5.639 | 2.794 | 29 | False | `MID.down.q80 -s-> MID.up.q50` | — | tennessee_eastman, hai |
| oa_flow:upq20 | m | oa_damper:upq10 | 5.634 | 11.295 | 38 | True | `MID.up.q20 -m-> MID-S.up.q10` | tennessee_eastman | hai |
| oa_damper:upq10 | m | sa_t:upq50 | 5.597 | 3.727 | 37 | False | `MID-S.up.q10 -m-> MID.up.q50` | — | tennessee_eastman, hai |
| rf_spd:downq80 | m | sa_flow:upq80 | 5.587 | 4.702 | 284 | True | `SLOW.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| Tsp_c:downq80 | s | T:upq20 | 5.584 | 6.518 | 35 | True | `SET.down.q80 -s-> MID.up.q20` | — | hai |
| oa_damper:upq90 | l | sa_t:upq20 | 5.576 | 10.476 | 216 | False | `MID-S.up.q90 -l-> MID.up.q20` | tennessee_eastman | hai |
| oa_flow:downq20 | l | oa_damper:upq10 | 5.565 | 8.163 | 98 | True | `MID.down.q20 -l-> MID-S.up.q10` | — | tennessee_eastman, hai |
| sa_flow:downq20 | s | sf_spd:downq20 | 5.561 | 6.347 | 45 | False | `SLOW.down.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| plenum_p:downq20 | m | sf_spd:upq20 | 5.542 | 2.707 | 276 | False | `MID.down.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| plenum_p:upq20 | s | sf_spd:upq20 | 5.541 | 2.161 | 87 | False | `MID.up.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_t:peak | m | oa_damper:downq90 | 5.538 | 8.8 | 71 | True | `MID.peak -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| T:upq80 | l | fan:downq90 | 5.529 | 6.338 | 338 | True | `MID.up.q80 -l-> SET.down.q90` | — | tennessee_eastman, hai |
| sf_spd:upq80 | m | rf_spd:downq80 | 5.523 | 5.308 | 241 | True | `SLOW.up.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_flow:upq80 | m | sf_spd:upq80 | 5.516 | 3.917 | 173 | False | `SLOW.up.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sf_spd:downq80 | s | oa_damper:upq10 | 5.503 | 5.265 | 16 | True | `SLOW.down.q80 -s-> MID-S.up.q10` | — | tennessee_eastman, hai |
| sa_flow:downq50 | s | rf_spd:downq50 | 5.502 | 4.281 | 347 | True | `SLOW.down.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| oa_damper:downq90 | s | sa_t:downq20 | 5.5 | 8.067 | 25 | False | `MID-S.down.q90 -s-> MID.down.q20` | — | tennessee_eastman, hai |
| rf_spd:upq50 | s | sa_flow:upq50 | 5.485 | 4.56 | 319 | True | `SLOW.up.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| oa_damper:downq10 | s | oa_flow:downq50 | 5.463 | 5.263 | 25 | False | `MID-S.down.q10 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| plenum_p:upq20 | s | sa_flow:upq20 | 5.445 | 2.983 | 81 | False | `MID.up.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_flow:downq20 | s | sa_flow:upq20 | 5.42 | 2.127 | 29 | True | `MID.down.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| T:downq80 | m | fan:downq10 | 5.415 | 9.34 | 316 | True | `MID.down.q80 -m-> SET.down.q10` | — | tennessee_eastman, hai |
| oa_damper:downq10 | s | ma_t:peak | 5.409 | 2.961 | 22 | False | `MID-S.down.q10 -s-> MID.peak` | — | tennessee_eastman, hai |
| Tsp_c:downq50 | m | T:upq20 | 5.406 | 3.119 | 13 | True | `SET.down.q50 -m-> MID.up.q20` | — | hai |
| plenum_p:downq20 | m | sa_flow:upq20 | 5.404 | 2.556 | 255 | True | `MID.down.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| ma_t:trough | s | oa_damper:downq90 | 5.404 | 21.939 | 18 | False | `MID.trough -s-> MID-S.down.q90` | — | tennessee_eastman, hai |
| hvac_kw_N:upq90 | s | sf_spd:upq80 | 5.396 | 6.721 | 91 | False | `SLOW-S.up.q90 -s-> SLOW.up.q80` | — | tennessee_eastman |
| Tsp_c:upq20 | s | hw_valve:downq10 | 5.395 | 2.489 | 31 | True | `SET.up.q20 -s-> MID-S.down.q10` | hai | — |
| oa_damper:upq90 | l | sa_t:downq50 | 5.392 | 3.729 | 138 | True | `MID-S.up.q90 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| sa_t:downq50 | s | sa_t:downq20 | 5.378 | 17.009 | 30 | True | `MID.down.q50 -s-> MID.down.q20 [same role]` | tennessee_eastman | hai |
| oa_flow:downq80 | s | sa_t:upq20 | 5.362 | 10.821 | 42 | True | `MID.down.q80 -s-> MID.up.q20` | — | tennessee_eastman, hai |
| oa_damper:upq90 | l | sa_t:downq20 | 5.351 | 10.197 | 207 | False | `MID-S.up.q90 -l-> MID.down.q20` | — | tennessee_eastman, hai |
| sf_spd:upq80 | m | rf_spd:upq80 | 5.317 | 5.242 | 232 | True | `SLOW.up.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rf_spd:upq20 | m | sf_spd:upq20 | 5.313 | 3.51 | 178 | False | `SLOW.up.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| sf_spd:upq50 | m | sf_spd:downq50 | 5.297 | 3.983 | 711 | True | `SLOW.up.q50 -m-> SLOW.down.q50 [same role]` | hai | tennessee_eastman |
| oa_damper:upq10 | s | oa_flow:upq50 | 5.285 | 4.533 | 30 | False | `MID-S.up.q10 -s-> MID.up.q50` | — | tennessee_eastman, hai |
| Tsp_c:downq80 | s | hw_valve:downq90 | 5.275 | 5.041 | 9 | True | `SET.down.q80 -s-> MID-S.down.q90` | — | hai |
| rf_spd:upq50 | s | sf_spd:upq50 | 5.263 | 3.693 | 284 | True | `SLOW.up.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| sa_t:upq50 | m | oa_damper:downq90 | 5.247 | 9.215 | 40 | True | `MID.up.q50 -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| sa_flow:downq50 | m | sa_flow:upq50 | 5.245 | 4.426 | 742 | True | `SLOW.down.q50 -m-> SLOW.up.q50 [same role]` | hai | tennessee_eastman |
| plenum_p:upq20 | s | sa_flow:downq20 | 5.243 | 2.632 | 78 | False | `MID.up.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| rf_spd:downq80 | m | sf_spd:upq80 | 5.241 | 5.924 | 207 | True | `SLOW.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_damper:downq90 | m | sa_t:downq50 | 5.241 | 3.56 | 50 | True | `MID-S.down.q90 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| sa_t:downq20 | s | oa_flow:downq80 | 5.232 | 5.445 | 45 | False | `MID.down.q20 -s-> MID.down.q80` | hai | tennessee_eastman |
| oa_flow:downq50 | s | oa_flow:downq20 | 5.226 | 21.515 | 39 | True | `MID.down.q50 -s-> MID.down.q20 [same role]` | tennessee_eastman, hai | — |
| plenum_p:downq20 | m | sf_spd:downq20 | 5.221 | 2.042 | 260 | False | `MID.down.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| oa_flow:downq80 | m | sf_spd:downq80 | 5.203 | 4.627 | 149 | True | `MID.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| plenum_p:downq20 | s | rf_spd:upq20 | 5.199 | 2.554 | 95 | False | `MID.down.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| rf_spd:downq20 | m | sf_spd:downq20 | 5.195 | 3.496 | 170 | False | `SLOW.down.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| oa_damper:upq90 | l | sa_t:upq50 | 5.19 | 3.788 | 132 | True | `MID-S.up.q90 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| oa_damper:upq90 | m | sa_t:upq50 | 5.187 | 3.519 | 50 | True | `MID-S.up.q90 -m-> MID.up.q50` | — | tennessee_eastman, hai |
| sa_t:downq50 | m | oa_damper:upq90 | 5.178 | 10.95 | 39 | False | `MID.down.q50 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| oa_flow:downq80 | s | sf_spd:downq80 | 5.177 | 5.442 | 41 | True | `MID.down.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_t:downq50 | s | oa_damper:upq90 | 5.17 | 11.827 | 13 | False | `MID.down.q50 -s-> MID-S.up.q90` | tennessee_eastman | hai |
| sf_spd:downq50 | m | sf_spd:upq50 | 5.162 | 5.093 | 670 | True | `SLOW.down.q50 -m-> SLOW.up.q50 [same role]` | hai | tennessee_eastman |
| T:upq50 | s | hw_valve:downq10 | 5.16 | 6.701 | 677 | True | `MID.up.q50 -s-> MID-S.down.q10` | — | tennessee_eastman, hai |
| T_out:upq80 | s | oa_damper:downq90 | 5.159 | 5.651 | 13 | False | `MID.up.q80 -s-> MID-S.down.q90` | — | tennessee_eastman, hai |
| oa_damper:upq90 | m | oa_damper:upq10 | 5.155 | 8.363 | 26 | False | `MID-S.up.q90 -m-> MID-S.up.q10 [same role]` | — | tennessee_eastman, hai |
| sa_flow:upq20 | m | plenum_p:downq20 | 5.144 | 2.656 | 274 | True | `SLOW.up.q20 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| hvac_kw_N:downq90 | s | sf_spd:downq80 | 5.139 | 3.249 | 91 | False | `SLOW-S.down.q90 -s-> SLOW.down.q80` | — | tennessee_eastman |
| ma_t:peak | m | oa_damper:upq10 | 5.134 | 14.677 | 57 | True | `MID.peak -m-> MID-S.up.q10` | — | tennessee_eastman, hai |
| ma_t:trough | s | oa_flow:downq80 | 5.108 | 7.267 | 39 | False | `MID.trough -s-> MID.down.q80` | — | tennessee_eastman, hai |
| sa_flow:upq50 | s | rf_spd:upq50 | 5.107 | 3.951 | 349 | True | `SLOW.up.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| sf_spd:downq80 | m | rf_spd:upq80 | 5.096 | 5.143 | 231 | True | `SLOW.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_damper:downq10 | m | sf_spd:upq80 | 5.095 | 5.684 | 58 | False | `MID-S.down.q10 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_flow:downq50 | m | oa_flow:upq50 | 5.082 | 3.733 | 248 | True | `MID.down.q50 -m-> MID.up.q50 [same role]` | tennessee_eastman, hai | — |
| oa_flow:downq80 | m | sa_flow:downq80 | 5.082 | 3.431 | 187 | True | `MID.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_damper:upq10 | m | sa_t:upq20 | 5.065 | 13.298 | 51 | True | `MID-S.up.q10 -m-> MID.up.q20` | — | tennessee_eastman, hai |
| sa_flow:downq80 | m | rf_spd:downq80 | 5.06 | 5.493 | 268 | True | `SLOW.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_t:downq50 | m | oa_damper:downq90 | 5.045 | 10.429 | 38 | False | `MID.down.q50 -m-> MID-S.down.q90` | tennessee_eastman | hai |
| rf_spd:upq20 | s | sf_spd:downq20 | 5.044 | 4.539 | 50 | False | `SLOW.up.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| sa_flow:upq50 | m | sa_flow:downq50 | 5.043 | 4.137 | 737 | True | `SLOW.up.q50 -m-> SLOW.down.q50 [same role]` | hai | tennessee_eastman |
| oa_damper:upq10 | s | ra_t:peak | 5.039 | 3.269 | 17 | True | `MID-S.up.q10 -s-> MID.peak` | — | tennessee_eastman, hai |
| hw_valve:upq90 | l | hw_valve:upq90 | 5.037 | 3.332 | 613 | False | `MID-S.up.q90 -l-> MID-S.up.q90 [same role]` | — | tennessee_eastman, hai, fingrid |
| hw_valve:upq10 | s | T:downq20 | 5.031 | 5.355 | 797 | True | `MID-S.up.q10 -s-> MID.down.q20` | — | tennessee_eastman, hai |
| rf_spd:downq80 | s | sf_spd:upq80 | 5.021 | 4.987 | 57 | False | `SLOW.down.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| ma_t:trough | m | oa_flow:downq80 | 5.003 | 7.165 | 170 | True | `MID.trough -m-> MID.down.q80` | — | tennessee_eastman, hai |
| sf_spd:upq20 | m | plenum_p:downq20 | 4.991 | 2.594 | 296 | True | `SLOW.up.q20 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| sa_flow:downq50 | m | sf_spd:upq50 | 4.99 | 4.334 | 655 | True | `SLOW.down.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| sa_t:upq50 | m | rf_spd:downq80 | 4.987 | 3.751 | 144 | True | `MID.up.q50 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| ra_t:trough | l | ra_t:peak | 4.982 | 3.267 | 499 | True | `MID.trough -l-> MID.peak [same role]` | hai | tennessee_eastman, fingrid |
| plenum_p:upq20 | m | sa_flow:downq20 | 4.958 | 1.756 | 235 | False | `MID.up.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| rf_spd:downq50 | s | sa_flow:upq50 | 4.952 | 3.748 | 281 | True | `SLOW.down.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| oa_damper:downq10 | l | sf_spd:downq80 | 4.945 | 4.498 | 201 | True | `MID-S.down.q10 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rf_spd:downq20 | m | plenum_p:upq20 | 4.935 | 2.634 | 317 | False | `SLOW.down.q20 -m-> MID.up.q20` | — | tennessee_eastman, hai |
| plenum_p:upq80 | m | plenum_p:downq80 | 4.933 | 4.086 | 1153 | True | `MID.up.q80 -m-> MID.down.q80 [same role]` | — | tennessee_eastman, hai |
| oa_damper:upq10 | l | sf_spd:downq80 | 4.929 | 5.184 | 183 | False | `MID-S.up.q10 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| T:upq50 | s | hw_valve:downq90 | 4.927 | 4.229 | 337 | True | `MID.up.q50 -s-> MID-S.down.q90` | — | tennessee_eastman, hai |
| plenum_p:downq20 | m | sa_flow:downq20 | 4.916 | 2.005 | 232 | False | `MID.down.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| oa_damper:downq90 | l | sa_t:downq50 | 4.892 | 4.227 | 118 | True | `MID-S.down.q90 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| sf_spd:upq80 | s | oa_flow:downq80 | 4.891 | 3.533 | 39 | True | `SLOW.up.q80 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| sf_spd:upq80 | s | oa_damper:downq90 | 4.887 | 5.531 | 17 | False | `SLOW.up.q80 -s-> MID-S.down.q90` | — | tennessee_eastman, hai |
| oa_damper:downq10 | m | oa_flow:downq20 | 4.879 | 6.164 | 46 | False | `MID-S.down.q10 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| plenum_p:upq20 | m | sf_spd:downq20 | 4.878 | 2.139 | 244 | False | `MID.up.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| rf_spd:downq80 | m | sa_flow:downq80 | 4.874 | 4.234 | 248 | False | `SLOW.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rf_spd:downq80 | m | sf_spd:downq80 | 4.874 | 5.398 | 193 | False | `SLOW.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_flow:upq20 | m | plenum_p:upq20 | 4.863 | 2.391 | 259 | True | `SLOW.up.q20 -m-> MID.up.q20` | — | tennessee_eastman, hai |
| T_out:downq80 | s | sa_t:upq20 | 4.862 | 7.989 | 23 | False | `MID.down.q80 -s-> MID.up.q20` | — | tennessee_eastman, hai |
| oa_damper:upq90 | s | oa_flow:upq80 | 4.852 | 5.783 | 19 | False | `MID-S.up.q90 -s-> MID.up.q80` | — | tennessee_eastman, hai |
| sf_spd:upq80 | s | oa_damper:downq10 | 4.839 | 6.906 | 13 | False | `SLOW.up.q80 -s-> MID-S.down.q10` | — | tennessee_eastman, hai |
| hw_valve:downq90 | l | hw_valve:downq90 | 4.808 | 2.918 | 650 | False | `MID-S.down.q90 -l-> MID-S.down.q90 [same role]` | — | tennessee_eastman, hai, fingrid |
| ra_t:peak | s | ma_t:trough | 4.801 | 1.708 | 30 | False | `MID.peak -s-> MID.trough` | fingrid | tennessee_eastman, hai |
| sf_spd:downq80 | m | rf_spd:downq80 | 4.788 | 4.911 | 217 | True | `SLOW.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sf_spd:upq80 | s | sa_flow:upq80 | 4.786 | 6.372 | 48 | True | `SLOW.up.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sf_spd:upq80 | s | rf_spd:downq80 | 4.781 | 4.798 | 63 | True | `SLOW.up.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| T_out:upq50 | m | oa_flow:upq80 | 4.773 | 3.73 | 253 | False | `MID.up.q50 -m-> MID.up.q80` | — | tennessee_eastman |
| ra_t:trough | s | sa_flow:upq20 | 4.768 | 1.815 | 22 | False | `MID.trough -s-> SLOW.up.q20` | hai | tennessee_eastman |
| oa_damper:downq90 | l | sa_t:upq50 | 4.756 | 4.003 | 114 | True | `MID-S.down.q90 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| sf_spd:upq50 | m | sa_flow:downq50 | 4.748 | 3.811 | 691 | True | `SLOW.up.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| sa_flow:downq20 | m | sf_spd:downq20 | 4.725 | 3.365 | 124 | False | `SLOW.down.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| hvac_kw_N:downq90 | m | sf_spd:upq80 | 4.719 | 2.343 | 170 | False | `SLOW-S.down.q90 -m-> SLOW.up.q80` | — | tennessee_eastman |
| T:downq80 | s | T:downq50 | 4.717 | 2.778 | 416 | True | `MID.down.q80 -s-> MID.down.q50 [same role]` | tennessee_eastman, hai | — |
| hvac_kw_N:upq10 | s | rf_spd:upq20 | 4.714 | 3.401 | 116 | False | `SLOW-S.up.q10 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_t:trough | s | sa_t:upq50 | 4.709 | 3.343 | 17 | True | `MID.trough -s-> MID.up.q50` | — | tennessee_eastman, hai |
| plenum_p:downq20 | m | rf_spd:upq20 | 4.708 | 2.1 | 281 | False | `MID.down.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| sa_t:downq20 | s | ma_t:trough | 4.703 | 4.761 | 50 | True | `MID.down.q20 -s-> MID.trough` | — | tennessee_eastman, hai |
| ma_t:peak | m | ra_t:peak | 4.702 | 4.75 | 128 | True | `MID.peak -m-> MID.peak` | fingrid | tennessee_eastman, hai |
| oa_flow:downq80 | m | rf_spd:downq80 | 4.701 | 3.721 | 227 | True | `MID.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sf_spd:downq50 | m | sa_flow:upq50 | 4.696 | 4.401 | 657 | True | `SLOW.down.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| sa_flow:upq20 | s | rf_spd:downq20 | 4.696 | 3.684 | 53 | True | `SLOW.up.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| sa_t:downq50 | s | oa_flow:downq80 | 4.685 | 2.211 | 27 | False | `MID.down.q50 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| rf_spd:upq80 | m | sf_spd:upq80 | 4.681 | 4.514 | 185 | False | `SLOW.up.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_damper:upq10 | m | sa_t:downq20 | 4.674 | 13.21 | 47 | False | `MID-S.up.q10 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| oa_damper:upq90 | s | sa_t:downq50 | 4.671 | 2.034 | 12 | False | `MID-S.up.q90 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| sf_spd:upq80 | m | oa_damper:upq10 | 4.664 | 8.949 | 41 | True | `SLOW.up.q80 -m-> MID-S.up.q10` | hai | tennessee_eastman |
| ra_t:peak | m | oa_damper:downq90 | 4.662 | 11.262 | 44 | True | `MID.peak -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| oa_damper:upq10 | m | sa_t:downq50 | 4.66 | 2.496 | 31 | False | `MID-S.up.q10 -m-> MID.down.q50` | tennessee_eastman | hai |
| oa_damper:downq90 | s | sa_t:downq50 | 4.656 | 2.74 | 14 | False | `MID-S.down.q90 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| hvac_kw_N:upq90 | s | sa_flow:upq80 | 4.653 | 5.042 | 101 | False | `SLOW-S.up.q90 -s-> SLOW.up.q80` | — | tennessee_eastman |
| sa_flow:upq50 | m | sf_spd:downq50 | 4.643 | 3.724 | 626 | True | `SLOW.up.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| oa_damper:upq90 | m | sa_t:downq50 | 4.639 | 3.166 | 45 | False | `MID-S.up.q90 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| sf_spd:upq20 | s | rf_spd:downq20 | 4.633 | 4.15 | 47 | True | `SLOW.up.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| ma_t:trough | s | ra_t:trough | 4.631 | 1.513 | 29 | True | `MID.trough -s-> MID.trough` | hai | tennessee_eastman, fingrid |
| T_out:upq80 | s | oa_damper:downq10 | 4.625 | 2.71 | 9 | False | `MID.up.q80 -s-> MID-S.down.q10` | — | tennessee_eastman, hai |
| sa_t:downq80 | l | oa_flow:downq20 | 4.608 | 6.851 | 130 | False | `MID.down.q80 -l-> MID.down.q20` | tennessee_eastman | hai |
| ma_t:peak | m | oa_damper:downq90 | 4.605 | 7.219 | 67 | True | `MID.peak -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| sf_spd:downq50 | s | rf_spd:downq50 | 4.594 | 3.641 | 287 | True | `SLOW.down.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| oa_damper:downq10 | l | sf_spd:upq80 | 4.589 | 4.081 | 186 | True | `MID-S.down.q10 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_damper:downq10 | m | oa_flow:upq80 | 4.575 | 4.196 | 52 | False | `MID-S.down.q10 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| plenum_p:upq20 | s | rf_spd:upq20 | 4.57 | 2.636 | 86 | False | `MID.up.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| sa_t:downq80 | l | oa_flow:upq20 | 4.567 | 6.897 | 128 | True | `MID.down.q80 -l-> MID.up.q20` | — | tennessee_eastman, hai |
| sf_spd:upq20 | m | plenum_p:upq20 | 4.552 | 2.265 | 270 | True | `SLOW.up.q20 -m-> MID.up.q20` | — | tennessee_eastman, hai |
| oa_damper:downq90 | l | oa_damper:upq10 | 4.545 | 6.069 | 57 | False | `MID-S.down.q90 -l-> MID-S.up.q10 [same role]` | — | tennessee_eastman, hai |
| plenum_p:downq80 | m | plenum_p:upq80 | 4.544 | 3.621 | 1070 | True | `MID.down.q80 -m-> MID.up.q80 [same role]` | — | tennessee_eastman, hai |
| oa_flow:downq80 | s | oa_damper:downq90 | 4.538 | 7.945 | 16 | True | `MID.down.q80 -s-> MID-S.down.q90` | — | tennessee_eastman, hai |
| hvac_kw_S:upq80 | m | sf_spd:downq80 | 4.536 | 3.134 | 283 | False | `MID-S.up.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| T_out:downq80 | m | oa_flow:downq80 | 4.535 | 2.81 | 106 | False | `MID.down.q80 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| hvac_kw_N:downq90 | s | sa_flow:downq80 | 4.527 | 3.352 | 103 | False | `SLOW-S.down.q90 -s-> SLOW.down.q80` | — | tennessee_eastman |
| hvac_kw_S:downq80 | s | sa_flow:downq80 | 4.512 | 3.536 | 100 | False | `MID-S.down.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sf_spd:upq50 | s | rf_spd:upq50 | 4.495 | 3.382 | 261 | True | `SLOW.up.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| oa_damper:upq10 | l | rf_spd:downq80 | 4.488 | 5.136 | 281 | True | `MID-S.up.q10 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rf_spd:downq20 | s | plenum_p:upq20 | 4.477 | 1.769 | 84 | False | `SLOW.down.q20 -s-> MID.up.q20` | — | tennessee_eastman, hai |
| rf_spd:downq50 | s | sa_flow:downq50 | 4.469 | 3.304 | 253 | True | `SLOW.down.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| hvac_kw_N:downq10 | s | sf_spd:downq20 | 4.467 | 3.507 | 81 | False | `SLOW-S.down.q10 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| oa_damper:downq90 | l | rf_spd:downq80 | 4.466 | 3.513 | 278 | False | `MID-S.down.q90 -l-> SLOW.down.q80` | hai | tennessee_eastman |
| hw_valve:upq10 | m | hw_valve:downq90 | 4.456 | 4.203 | 591 | True | `MID-S.up.q10 -m-> MID-S.down.q90 [same role]` | — | tennessee_eastman, hai, fingrid |
| sa_flow:downq80 | s | oa_damper:upq10 | 4.456 | 5.733 | 14 | False | `SLOW.down.q80 -s-> MID-S.up.q10` | tennessee_eastman | hai |
| hvac_kw_N:downq10 | m | sa_flow:upq20 | 4.453 | 2.617 | 242 | False | `SLOW-S.down.q10 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| T:upq80 | l | fan:downq10 | 4.441 | 4.747 | 965 | True | `MID.up.q80 -l-> SET.down.q10` | — | tennessee_eastman, hai |
| sa_t:upq50 | m | rf_spd:upq80 | 4.433 | 3.92 | 128 | True | `MID.up.q50 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sf_spd:upq80 | m | oa_damper:downq90 | 4.427 | 8.283 | 51 | True | `SLOW.up.q80 -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| Tsp_h:upq20 | s | T:upq20 | 4.426 | 5.881 | 10 | True | `SET.up.q20 -s-> MID.up.q20` | — | tennessee_eastman, hai |
| sa_flow:downq80 | m | sf_spd:downq80 | 4.425 | 5.459 | 139 | False | `SLOW.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_flow:upq80 | s | ma_t:trough | 4.412 | 2.985 | 39 | True | `MID.up.q80 -s-> MID.trough` | — | tennessee_eastman, hai |
| T:downq80 | m | hw_valve:upq10 | 4.403 | 1.875 | 830 | True | `MID.down.q80 -m-> MID-S.up.q10` | — | tennessee_eastman, hai |
| oa_damper:downq90 | m | sf_spd:upq80 | 4.395 | 4.205 | 64 | False | `MID-S.down.q90 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| T_out:downq80 | s | sf_spd:downq80 | 4.39 | 2.529 | 21 | False | `MID.down.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_flow:upq80 | m | sa_t:upq50 | 4.389 | 2.991 | 80 | True | `MID.up.q80 -m-> MID.up.q50` | — | tennessee_eastman, hai |
| oa_t:peak | m | sf_spd:upq80 | 4.388 | 4.743 | 126 | True | `MID.peak -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sf_spd:upq80 | m | oa_damper:downq10 | 4.383 | 6.468 | 39 | True | `SLOW.up.q80 -m-> MID-S.down.q10` | — | tennessee_eastman, hai |
| sa_t:downq50 | m | rf_spd:upq80 | 4.382 | 4.061 | 125 | False | `MID.down.q50 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_flow:upq20 | l | oa_flow:downq20 | 4.364 | 1.603 | 190 | False | `SLOW.up.q20 -l-> MID.down.q20` | — | tennessee_eastman, hai |
| oa_damper:upq10 | m | ma_t:trough | 4.36 | 3.544 | 56 | True | `MID-S.up.q10 -m-> MID.trough` | — | tennessee_eastman, hai |
| sf_spd:upq80 | m | oa_flow:downq80 | 4.355 | 4.11 | 115 | True | `SLOW.up.q80 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_flow:upq80 | m | ma_t:trough | 4.348 | 2.675 | 154 | True | `MID.up.q80 -m-> MID.trough` | — | tennessee_eastman, hai |
| oa_damper:upq90 | l | rf_spd:downq80 | 4.345 | 3.351 | 287 | False | `MID-S.up.q90 -l-> SLOW.down.q80` | hai | tennessee_eastman |
| oa_flow:downq20 | l | sa_t:downq50 | 4.34 | 3.242 | 147 | True | `MID.down.q20 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| rf_spd:downq20 | s | oa_flow:downq20 | 4.336 | 1.606 | 32 | False | `SLOW.down.q20 -s-> MID.down.q20` | — | tennessee_eastman, hai |
| hvac_kw_S:upq80 | s | oa_damper:downq10 | 4.336 | 7.254 | 23 | False | `MID-S.up.q80 -s-> MID-S.down.q10` | — | tennessee_eastman, hai |
| T:downq20 | m | T:upq20 | 4.327 | 4.286 | 3406 | True | `MID.down.q20 -m-> MID.up.q20 [same role]` | tennessee_eastman, hai | — |
| ma_t:peak | s | oa_flow:upq80 | 4.324 | 5.253 | 34 | False | `MID.peak -s-> MID.up.q80` | — | tennessee_eastman, hai |
| oa_damper:upq10 | l | sf_spd:upq80 | 4.321 | 3.943 | 160 | False | `MID-S.up.q10 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rf_spd:downq80 | s | sa_flow:upq80 | 4.312 | 4.324 | 63 | False | `SLOW.down.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| plenum_p:downq20 | m | rf_spd:downq20 | 4.297 | 1.542 | 257 | False | `MID.down.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| sf_spd:downq20 | m | plenum_p:downq20 | 4.294 | 1.797 | 239 | True | `SLOW.down.q20 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| oa_damper:downq10 | m | sa_t:downq50 | 4.291 | 5.219 | 32 | False | `MID-S.down.q10 -m-> MID.down.q50` | tennessee_eastman | hai |
| oa_damper:upq90 | l | rf_spd:upq80 | 4.285 | 3.427 | 283 | True | `MID-S.up.q90 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rf_spd:downq50 | m | rf_spd:upq50 | 4.277 | 3.371 | 1232 | True | `SLOW.down.q50 -m-> SLOW.up.q50 [same role]` | hai | tennessee_eastman |
| sa_t:downq50 | m | rf_spd:downq80 | 4.277 | 3.476 | 122 | False | `MID.down.q50 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_damper:upq90 | s | ra_t:peak | 4.275 | 1.862 | 14 | False | `MID-S.up.q90 -s-> MID.peak` | — | tennessee_eastman, hai |
| oa_flow:upq20 | m | sa_t:upq50 | 4.266 | 2.826 | 55 | True | `MID.up.q20 -m-> MID.up.q50` | — | tennessee_eastman, hai |
| oa_flow:upq80 | l | oa_damper:downq90 | 4.259 | 6.205 | 220 | True | `MID.up.q80 -l-> MID-S.down.q90` | tennessee_eastman | hai |
| plenum_p:upq20 | m | sf_spd:upq20 | 4.258 | 2.471 | 213 | False | `MID.up.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| T:upq20 | m | hw_valve:upq90 | 4.253 | 2.644 | 979 | True | `MID.up.q20 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| oa_flow:upq80 | m | sa_t:downq50 | 4.252 | 2.935 | 78 | True | `MID.up.q80 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| oa_flow:downq20 | l | sa_t:upq50 | 4.249 | 3.051 | 143 | True | `MID.down.q20 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| oa_damper:upq10 | l | sa_flow:downq80 | 4.234 | 4.097 | 202 | False | `MID-S.up.q10 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_damper:downq10 | m | sa_flow:upq80 | 4.232 | 4.117 | 62 | False | `MID-S.down.q10 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_damper:downq90 | s | sa_flow:upq80 | 4.232 | 2.581 | 25 | False | `MID-S.down.q90 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_damper:upq10 | s | oa_flow:upq20 | 4.212 | 3.634 | 14 | False | `MID-S.up.q10 -s-> MID.up.q20` | — | tennessee_eastman, hai |
| hw_valve:downq10 | m | T:upq80 | 4.209 | 4.291 | 926 | True | `MID-S.down.q10 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| rf_spd:downq80 | s | sa_t:upq50 | 4.194 | 2.664 | 31 | False | `SLOW.down.q80 -s-> MID.up.q50` | — | tennessee_eastman, hai |
| rf_spd:upq50 | m | rf_spd:downq50 | 4.189 | 2.951 | 1228 | True | `SLOW.up.q50 -m-> SLOW.down.q50 [same role]` | hai | tennessee_eastman |
| sa_flow:downq50 | m | rf_spd:upq50 | 4.185 | 3.252 | 885 | True | `SLOW.down.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| ra_t:trough | s | plenum_p:upq20 | 4.185 | 1.752 | 40 | True | `MID.trough -s-> MID.up.q20` | — | tennessee_eastman, hai |
| oa_damper:downq10 | l | sa_t:downq50 | 4.179 | 3.465 | 111 | True | `MID-S.down.q10 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| rf_spd:upq50 | s | sa_flow:downq50 | 4.171 | 2.906 | 242 | True | `SLOW.up.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| oa_damper:downq10 | l | sa_t:upq50 | 4.168 | 3.275 | 110 | False | `MID-S.down.q10 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| oa_flow:downq80 | m | sa_t:upq20 | 4.166 | 10.998 | 118 | True | `MID.down.q80 -m-> MID.up.q20` | tennessee_eastman | hai |
| oa_damper:upq10 | l | oa_damper:downq10 | 4.152 | 2.883 | 53 | False | `MID-S.up.q10 -l-> MID-S.down.q10 [same role]` | tennessee_eastman | hai |
| oa_damper:downq90 | l | rf_spd:upq80 | 4.145 | 3.653 | 258 | True | `MID-S.down.q90 -l-> SLOW.up.q80` | hai | tennessee_eastman |
| hw_valve:upq10 | m | hw_valve:upq90 | 4.141 | 3.417 | 548 | True | `MID-S.up.q10 -m-> MID-S.up.q90 [same role]` | fingrid | tennessee_eastman, hai |
| oa_damper:downq10 | l | oa_flow:upq20 | 4.138 | 3.058 | 138 | False | `MID-S.down.q10 -l-> MID.up.q20` | — | tennessee_eastman, hai |
| rf_spd:downq50 | m | sa_flow:upq50 | 4.136 | 3.375 | 797 | True | `SLOW.down.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| sa_flow:upq50 | m | rf_spd:downq50 | 4.12 | 2.876 | 900 | True | `SLOW.up.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| Tsp_h:downq20 | m | T:downq50 | 4.114 | 2.053 | 29 | True | `SET.down.q20 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| T:upq20 | m | hw_valve:downq90 | 4.105 | 3.012 | 947 | True | `MID.up.q20 -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| rf_spd:upq50 | m | sa_flow:downq50 | 4.105 | 2.914 | 805 | True | `SLOW.up.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| oa_damper:upq10 | l | rf_spd:upq80 | 4.105 | 4.635 | 257 | True | `MID-S.up.q10 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| Tsp_c:downq80 | m | T:upq20 | 4.102 | 2.343 | 55 | True | `SET.down.q80 -m-> MID.up.q20` | — | hai |
| sf_spd:downq20 | s | plenum_p:upq20 | 4.098 | 1.618 | 75 | True | `SLOW.down.q20 -s-> MID.up.q20` | — | tennessee_eastman, hai |
| plenum_p:upq20 | m | sa_flow:upq20 | 4.093 | 2.207 | 194 | False | `MID.up.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| sa_t:downq50 | l | oa_flow:downq20 | 4.093 | 2.454 | 154 | False | `MID.down.q50 -l-> MID.down.q20` | tennessee_eastman | hai |
| T:downq50 | s | T:downq20 | 4.089 | 2.444 | 571 | True | `MID.down.q50 -s-> MID.down.q20 [same role]` | tennessee_eastman, hai | — |
| sf_spd:downq50 | m | sa_flow:downq50 | 4.084 | 3.447 | 570 | True | `SLOW.down.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| rf_spd:downq50 | s | sf_spd:downq50 | 4.079 | 3.437 | 213 | True | `SLOW.down.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| T:downq50 | s | Tsp_c:upq20 | 4.079 | 8.064 | 20 | False | `MID.down.q50 -s-> SET.up.q20` | — | hai |
| hw_valve:downq10 | l | fan:downq90 | 4.058 | 4.9 | 259 | True | `MID-S.down.q10 -l-> SET.down.q90` | — | tennessee_eastman, hai |
| oa_damper:downq10 | m | oa_flow:upq20 | 4.057 | 5.034 | 38 | False | `MID-S.down.q10 -m-> MID.up.q20` | — | tennessee_eastman, hai |
| Tsp_c:upq80 | m | T:downq50 | 4.047 | 4.299 | 48 | True | `SET.up.q80 -m-> MID.down.q50` | — | hai |
| hvac_kw_N:downq10 | m | sf_spd:upq20 | 4.045 | 2.907 | 232 | False | `SLOW-S.down.q10 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| Tsp_c:upq20 | m | T:downq50 | 4.04 | 3.573 | 50 | True | `SET.up.q20 -m-> MID.down.q50` | — | hai |
| oa_damper:upq10 | m | sf_spd:upq80 | 4.038 | 3.851 | 41 | False | `MID-S.up.q10 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_flow:downq50 | s | plenum_p:downq50 | 4.036 | 3.117 | 271 | True | `SLOW.down.q50 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| rf_spd:upq20 | m | plenum_p:downq20 | 4.029 | 2.511 | 265 | False | `SLOW.up.q20 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| sa_flow:downq20 | s | plenum_p:upq20 | 4.029 | 2.671 | 64 | False | `SLOW.down.q20 -s-> MID.up.q20` | — | tennessee_eastman, hai |
| rf_spd:downq50 | s | sf_spd:upq50 | 4.027 | 3.123 | 212 | True | `SLOW.down.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| Tsp_c:upq20 | s | T:downq20 | 4.017 | 2.467 | 44 | True | `SET.up.q20 -s-> MID.down.q20` | — | hai |
| oa_flow:upq20 | l | sa_t:downq50 | 4.016 | 3.025 | 135 | False | `MID.up.q20 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| oa_flow:downq20 | m | sa_flow:upq20 | 4.009 | 1.519 | 80 | False | `MID.down.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_flow:upq80 | m | sa_t:downq20 | 4.003 | 11.553 | 111 | True | `MID.up.q80 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| sa_t:downq50 | m | oa_damper:upq10 | 4.002 | 9.908 | 23 | False | `MID.down.q50 -m-> MID-S.up.q10` | — | tennessee_eastman, hai |
| sf_spd:downq20 | m | oa_flow:upq20 | 4.001 | 1.986 | 87 | True | `SLOW.down.q20 -m-> MID.up.q20` | — | tennessee_eastman, hai |
| hvac_kw_N:downq10 | s | rf_spd:downq20 | 3.995 | 2.92 | 87 | False | `SLOW-S.down.q10 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| oa_damper:upq90 | m | sf_spd:upq80 | 3.985 | 3.375 | 59 | False | `MID-S.up.q90 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_t:upq20 | m | oa_flow:downq80 | 3.979 | 4.742 | 103 | False | `MID.up.q20 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| ma_t:trough | m | sa_t:upq20 | 3.978 | 14.132 | 131 | True | `MID.trough -m-> MID.up.q20` | — | tennessee_eastman, hai |
| sa_flow:upq20 | l | oa_flow:upq20 | 3.977 | 1.561 | 172 | False | `SLOW.up.q20 -l-> MID.up.q20` | — | tennessee_eastman, hai |
| rh_out:upq20 | m | fan:downq90 | 3.977 | 3.979 | 67 | False | `SLOW.up.q20 -m-> SET.down.q90` | — | tennessee_eastman, hai |
| sa_flow:downq20 | m | oa_flow:upq20 | 3.974 | 2.363 | 80 | True | `SLOW.down.q20 -m-> MID.up.q20` | — | tennessee_eastman, hai |
| rf_spd:upq80 | m | sa_flow:upq80 | 3.971 | 3.573 | 202 | False | `SLOW.up.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_flow:upq20 | l | sa_t:upq50 | 3.952 | 3.097 | 132 | True | `MID.up.q20 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| Tsp_c:upq80 | s | T:downq20 | 3.949 | 2.721 | 53 | True | `SET.up.q80 -s-> MID.down.q20` | — | hai |
| Tsp_c:downq20 | m | T:upq20 | 3.945 | 2.643 | 46 | True | `SET.down.q20 -m-> MID.up.q20` | — | hai |
| plenum_p:downq50 | s | plenum_p:downq20 | 3.939 | 1.748 | 204 | True | `MID.down.q50 -s-> MID.down.q20 [same role]` | — | tennessee_eastman, hai |
| sa_flow:upq80 | m | oa_flow:downq80 | 3.926 | 4.221 | 126 | True | `SLOW.up.q80 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| hw_valve:upq10 | m | T:upq20 | 3.923 | 4.271 | 1911 | True | `MID-S.up.q10 -m-> MID.up.q20` | tennessee_eastman | hai |
| sa_t:downq20 | m | oa_flow:downq80 | 3.914 | 4.733 | 101 | False | `MID.down.q20 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_damper:downq10 | m | sa_t:upq50 | 3.913 | 5.179 | 29 | False | `MID-S.down.q10 -m-> MID.up.q50` | — | tennessee_eastman, hai |
| plenum_p:downq50 | m | plenum_p:upq50 | 3.91 | 3.063 | 1221 | True | `MID.down.q50 -m-> MID.up.q50 [same role]` | hai | tennessee_eastman |
| hvac_kw_N:upq90 | m | sf_spd:downq80 | 3.91 | 2.957 | 148 | False | `SLOW-S.up.q90 -m-> SLOW.down.q80` | — | tennessee_eastman |
| hvac_kw_S:downq80 | s | oa_damper:downq90 | 3.907 | 11.775 | 30 | False | `MID-S.down.q80 -s-> MID-S.down.q90` | — | tennessee_eastman, hai |
| oa_t:trough | l | oa_t:peak | 3.904 | 2.532 | 627 | True | `MID.trough -l-> MID.peak [same role]` | — | tennessee_eastman, hai, fingrid |
| oa_damper:downq90 | m | sf_spd:downq80 | 3.904 | 4.193 | 57 | False | `MID-S.down.q90 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sf_spd:upq80 | l | rf_spd:downq80 | 3.903 | 4.478 | 421 | True | `SLOW.up.q80 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_damper:upq10 | m | sa_flow:upq80 | 3.903 | 4.058 | 51 | False | `MID-S.up.q10 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_t:downq50 | s | sf_spd:downq80 | 3.896 | 4.012 | 22 | False | `MID.down.q50 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_flow:downq80 | s | oa_flow:downq50 | 3.894 | 1.506 | 51 | False | `SLOW.down.q80 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| oa_damper:downq10 | m | oa_t:peak | 3.894 | 3.452 | 47 | False | `MID-S.down.q10 -m-> MID.peak` | — | tennessee_eastman, hai |
| fan:downq10 | m | hw_valve:upq10 | 3.893 | 2.966 | 145 | True | `SET.down.q10 -m-> MID-S.up.q10` | — | tennessee_eastman, hai |
| oa_damper:downq10 | l | sa_flow:downq80 | 3.887 | 4.013 | 203 | True | `MID-S.down.q10 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| hvac_kw_S:downq80 | s | rf_spd:downq80 | 3.885 | 2.798 | 113 | False | `MID-S.down.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_damper:downq10 | l | rf_spd:downq80 | 3.881 | 4.636 | 266 | True | `MID-S.down.q10 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_t:downq50 | m | oa_flow:downq80 | 3.881 | 4.265 | 67 | False | `MID.down.q50 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_t:peak | m | sa_t:downq50 | 3.88 | 2.778 | 73 | True | `MID.peak -m-> MID.down.q50` | — | tennessee_eastman, hai |
| rf_spd:upq80 | m | sa_t:upq20 | 3.878 | 11.25 | 152 | True | `SLOW.up.q80 -m-> MID.up.q20` | tennessee_eastman | hai |
| oa_flow:downq50 | s | sa_flow:downq80 | 3.876 | 2.712 | 45 | True | `MID.down.q50 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| plenum_p:upq50 | m | plenum_p:downq50 | 3.861 | 3.064 | 1187 | True | `MID.up.q50 -m-> MID.down.q50 [same role]` | hai | tennessee_eastman |
| oa_flow:upq50 | m | oa_flow:downq50 | 3.859 | 2.916 | 188 | True | `MID.up.q50 -m-> MID.down.q50 [same role]` | tennessee_eastman, hai | — |
| fan:downq10 | s | T:downq20 | 3.858 | 3.092 | 96 | True | `SET.down.q10 -s-> MID.down.q20` | hai | tennessee_eastman |
| oa_damper:downq10 | l | rf_spd:upq80 | 3.852 | 4.6 | 264 | False | `MID-S.down.q10 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rh_out:downq50 | s | oa_flow:upq80 | 3.833 | 3.149 | 55 | False | `SLOW.down.q50 -s-> MID.up.q80` | — | tennessee_eastman, hai |
| rf_spd:upq20 | m | plenum_p:upq20 | 3.832 | 2.435 | 252 | False | `SLOW.up.q20 -m-> MID.up.q20` | — | tennessee_eastman, hai |
| oa_damper:upq90 | l | sf_spd:downq80 | 3.83 | 4.258 | 150 | False | `MID-S.up.q90 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| fan:downq10 | m | T:downq50 | 3.815 | 3.225 | 323 | True | `SET.down.q10 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| Tsp_c:downq80 | l | T:upq20 | 3.806 | 1.909 | 157 | True | `SET.down.q80 -l-> MID.up.q20` | — | hai |
| hw_valve:upq90 | s | Tsp_c:downq20 | 3.806 | 2.447 | 18 | True | `MID-S.up.q90 -s-> SET.down.q20` | — | hai |
| ma_t:trough | s | rf_spd:upq80 | 3.804 | 5.149 | 48 | True | `MID.trough -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_t:upq50 | m | oa_damper:upq90 | 3.804 | 9.855 | 29 | False | `MID.up.q50 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| oa_damper:upq90 | l | oa_flow:downq80 | 3.802 | 3.581 | 152 | False | `MID-S.up.q90 -l-> MID.down.q80` | tennessee_eastman | hai |
| sa_flow:downq20 | l | plenum_p:upq20 | 3.799 | 1.846 | 423 | False | `SLOW.down.q20 -l-> MID.up.q20` | — | tennessee_eastman, hai |
| ma_t:peak | s | oa_flow:upq50 | 3.796 | 3.982 | 42 | False | `MID.peak -s-> MID.up.q50` | — | tennessee_eastman, hai |
| oa_flow:downq80 | m | rf_spd:upq80 | 3.789 | 3.591 | 183 | True | `MID.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rf_spd:upq80 | s | oa_flow:downq80 | 3.784 | 3.84 | 45 | False | `SLOW.up.q80 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| ra_t:trough | l | oa_t:peak | 3.782 | 2.712 | 481 | True | `MID.trough -l-> MID.peak` | — | tennessee_eastman, hai, fingrid |
| sa_flow:downq20 | l | rf_spd:upq20 | 3.781 | 2.645 | 257 | False | `SLOW.down.q20 -l-> SLOW.up.q20` | — | tennessee_eastman, hai |
| T:upq20 | s | T:downq20 | 3.773 | 3.251 | 710 | True | `MID.up.q20 -s-> MID.down.q20 [same role]` | hai | tennessee_eastman |
| T:downq50 | s | Tsp_c:upq80 | 3.759 | 7.389 | 18 | True | `MID.down.q50 -s-> SET.up.q80` | — | hai |
| rf_spd:upq80 | m | oa_flow:downq80 | 3.758 | 4.182 | 152 | False | `SLOW.up.q80 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_t:trough | l | oa_flow:upq80 | 3.755 | 4.771 | 568 | True | `MID.trough -l-> MID.up.q80` | — | tennessee_eastman, hai |
| rf_spd:downq20 | m | plenum_p:downq20 | 3.752 | 2.374 | 241 | False | `SLOW.down.q20 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| oa_damper:upq10 | s | sa_t:downq20 | 3.749 | 9.057 | 15 | False | `MID-S.up.q10 -s-> MID.down.q20` | tennessee_eastman | hai |
| oa_damper:upq10 | m | oa_flow:upq80 | 3.748 | 3.275 | 38 | False | `MID-S.up.q10 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| sf_spd:downq80 | s | rf_spd:upq80 | 3.741 | 4.03 | 54 | True | `SLOW.down.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_damper:upq90 | s | oa_flow:downq80 | 3.738 | 4.884 | 15 | False | `MID-S.up.q90 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_damper:upq90 | l | sa_flow:downq80 | 3.735 | 3.215 | 188 | False | `MID-S.up.q90 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_t:peak | m | sa_flow:upq80 | 3.734 | 4.094 | 138 | True | `MID.peak -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rf_spd:downq80 | s | oa_flow:downq50 | 3.721 | 1.934 | 60 | False | `SLOW.down.q80 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| sa_flow:downq80 | s | rf_spd:upq80 | 3.719 | 4.785 | 58 | False | `SLOW.down.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sf_spd:downq20 | l | plenum_p:upq20 | 3.717 | 1.858 | 450 | False | `SLOW.down.q20 -l-> MID.up.q20` | — | tennessee_eastman, hai |
| ra_t:trough | l | oa_flow:upq80 | 3.707 | 4.945 | 444 | True | `MID.trough -l-> MID.up.q80` | — | tennessee_eastman, hai |
| sf_spd:downq20 | l | rf_spd:upq20 | 3.707 | 2.34 | 274 | False | `SLOW.down.q20 -l-> SLOW.up.q20` | — | tennessee_eastman, hai |
| sf_spd:upq50 | m | sa_flow:upq50 | 3.702 | 3.779 | 540 | True | `SLOW.up.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| oa_flow:downq80 | m | sa_flow:upq80 | 3.7 | 3.51 | 136 | True | `MID.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| T:upq80 | l | T:downq80 | 3.691 | 3.563 | 3260 | True | `MID.up.q80 -l-> MID.down.q80 [same role]` | — | tennessee_eastman, hai |
| hvac_kw_N:downq90 | m | sa_flow:upq80 | 3.688 | 2.456 | 171 | False | `SLOW-S.down.q90 -m-> SLOW.up.q80` | — | tennessee_eastman |
| T:upq80 | l | Tsp_c:upq80 | 3.683 | 3.15 | 170 | True | `MID.up.q80 -l-> SET.up.q80` | — | hai |
| oa_damper:downq90 | s | oa_flow:downq50 | 3.682 | 2.907 | 24 | False | `MID-S.down.q90 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| rf_spd:downq50 | m | sf_spd:upq50 | 3.68 | 3.103 | 658 | True | `SLOW.down.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| sa_flow:upq20 | m | oa_flow:downq20 | 3.675 | 1.688 | 77 | False | `SLOW.up.q20 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| oa_t:trough | l | ra_t:peak | 3.668 | 2.399 | 464 | True | `MID.trough -l-> MID.peak` | hai | tennessee_eastman, fingrid |
| hvac_kw_S:downq80 | m | sf_spd:downq80 | 3.668 | 3.008 | 224 | False | `MID-S.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_flow:downq80 | m | oa_flow:downq50 | 3.664 | 2.173 | 163 | True | `SLOW.down.q80 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| sa_t:upq50 | m | oa_flow:downq80 | 3.662 | 3.797 | 64 | False | `MID.up.q50 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_flow:downq80 | m | oa_damper:downq10 | 3.656 | 7.821 | 36 | True | `MID.down.q80 -m-> MID-S.down.q10` | tennessee_eastman | hai |
| rf_spd:upq80 | m | sa_t:downq20 | 3.653 | 11.566 | 143 | True | `SLOW.up.q80 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| oa_flow:upq50 | l | oa_flow:downq80 | 3.651 | 4.439 | 567 | True | `MID.up.q50 -l-> MID.down.q80 [same role]` | tennessee_eastman | hai |
| T_out:downq80 | s | ma_t:trough | 3.645 | 3.674 | 22 | False | `MID.down.q80 -s-> MID.trough` | — | tennessee_eastman, hai |
| rf_spd:upq50 | m | sf_spd:downq50 | 3.643 | 2.797 | 659 | True | `SLOW.up.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| rf_spd:downq50 | s | plenum_p:downq50 | 3.64 | 2.528 | 328 | True | `SLOW.down.q50 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| plenum_p:upq20 | s | plenum_p:upq50 | 3.64 | 3.278 | 200 | True | `MID.up.q20 -s-> MID.up.q50 [same role]` | — | tennessee_eastman, hai |
| T:downq50 | s | T:upq50 | 3.636 | 3.915 | 603 | True | `MID.down.q50 -s-> MID.up.q50 [same role]` | hai | tennessee_eastman |
| oa_flow:upq80 | l | rf_spd:downq80 | 3.634 | 3.798 | 711 | True | `MID.up.q80 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_damper:upq10 | s | oa_flow:downq80 | 3.628 | 4.446 | 15 | False | `MID-S.up.q10 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_damper:downq10 | m | oa_flow:upq50 | 3.626 | 2.674 | 58 | False | `MID-S.down.q10 -m-> MID.up.q50` | — | tennessee_eastman, hai |
| plenum_p:downq80 | s | plenum_p:downq50 | 3.621 | 2.923 | 293 | True | `MID.down.q80 -s-> MID.down.q50 [same role]` | hai | tennessee_eastman |
| plenum_p:upq20 | m | rf_spd:upq20 | 3.62 | 1.705 | 217 | False | `MID.up.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| rf_spd:upq80 | s | plenum_p:upq80 | 3.616 | 2.836 | 138 | True | `SLOW.up.q80 -s-> MID.up.q80` | — | tennessee_eastman, hai |
| rf_spd:downq80 | s | oa_flow:downq80 | 3.616 | 4.52 | 42 | False | `SLOW.down.q80 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_damper:downq10 | s | sa_flow:downq80 | 3.613 | 2.756 | 15 | False | `MID-S.down.q10 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_damper:upq10 | m | rf_spd:upq80 | 3.612 | 4.492 | 62 | False | `MID-S.up.q10 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_t:upq50 | m | oa_damper:upq10 | 3.61 | 10.064 | 21 | False | `MID.up.q50 -m-> MID-S.up.q10` | tennessee_eastman | hai |
| sa_t:upq80 | l | sf_spd:upq80 | 3.608 | 6.24 | 125 | False | `MID.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_damper:downq90 | l | sa_flow:downq80 | 3.605 | 3.209 | 171 | True | `MID-S.down.q90 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| Tsp_c:downq20 | l | T:upq20 | 3.601 | 1.938 | 164 | True | `SET.down.q20 -l-> MID.up.q20` | — | hai |
| sa_flow:downq20 | l | rf_spd:downq20 | 3.596 | 2.194 | 245 | False | `SLOW.down.q20 -l-> SLOW.down.q20` | — | tennessee_eastman, hai |
| rh_out:upq20 | s | oa_damper:downq90 | 3.588 | 3.471 | 12 | False | `SLOW.up.q20 -s-> MID-S.down.q90` | — | tennessee_eastman, hai |
| oa_flow:upq80 | l | sf_spd:downq80 | 3.585 | 4.333 | 416 | True | `MID.up.q80 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_t:downq50 | l | oa_flow:upq20 | 3.585 | 2.701 | 134 | False | `MID.down.q50 -l-> MID.up.q20` | — | tennessee_eastman, hai |
| oa_flow:upq80 | l | sa_t:upq20 | 3.581 | 9.826 | 411 | True | `MID.up.q80 -l-> MID.up.q20` | tennessee_eastman | hai |
| rh_out:upq20 | m | oa_flow:downq80 | 3.58 | 2.977 | 117 | False | `SLOW.up.q20 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| sf_spd:upq50 | s | sa_flow:upq50 | 3.579 | 3.217 | 139 | True | `SLOW.up.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| hw_valve:downq10 | m | hw_valve:upq10 | 3.562 | 1.979 | 622 | True | `MID-S.down.q10 -m-> MID-S.up.q10 [same role]` | fingrid | tennessee_eastman, hai |
| oa_flow:downq20 | m | sf_spd:upq20 | 3.561 | 1.542 | 75 | True | `MID.down.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| sf_spd:downq20 | s | ma_t:peak | 3.555 | 2.454 | 39 | True | `SLOW.down.q20 -s-> MID.peak` | — | tennessee_eastman, hai |
| ra_t:peak | m | rf_spd:upq80 | 3.553 | 3.844 | 127 | True | `MID.peak -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| plenum_p:upq80 | s | rf_spd:downq80 | 3.549 | 3.698 | 130 | True | `MID.up.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| T:downq80 | m | Tsp_c:upq80 | 3.549 | 6.401 | 44 | True | `MID.down.q80 -m-> SET.up.q80` | — | hai |
| sf_spd:upq80 | m | sa_t:downq50 | 3.548 | 3.36 | 60 | True | `SLOW.up.q80 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| oa_damper:downq10 | l | sa_flow:upq80 | 3.546 | 3.743 | 185 | False | `MID-S.down.q10 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_flow:downq50 | m | rf_spd:downq50 | 3.536 | 2.662 | 746 | True | `SLOW.down.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| sf_spd:downq50 | m | rf_spd:upq50 | 3.534 | 2.937 | 739 | True | `SLOW.down.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| oa_flow:upq50 | l | oa_damper:downq90 | 3.528 | 7.439 | 239 | True | `MID.up.q50 -l-> MID-S.down.q90` | — | tennessee_eastman, hai |
| oa_t:trough | m | sf_spd:downq50 | 3.526 | 2.885 | 195 | True | `MID.trough -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| oa_flow:downq50 | s | ma_t:peak | 3.517 | 1.661 | 40 | True | `MID.down.q50 -s-> MID.peak` | — | tennessee_eastman, hai |
| sa_flow:downq50 | s | rf_spd:upq50 | 3.512 | 3.106 | 222 | True | `SLOW.down.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| oa_flow:upq80 | l | rf_spd:upq80 | 3.511 | 3.803 | 687 | True | `MID.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_t:trough | m | sa_flow:downq50 | 3.503 | 3.087 | 210 | True | `MID.trough -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| oa_flow:downq80 | m | sf_spd:upq80 | 3.501 | 4.47 | 100 | True | `MID.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| hvac_kw_S:upq80 | m | oa_damper:downq10 | 3.496 | 5.939 | 75 | False | `MID-S.up.q80 -m-> MID-S.down.q10` | — | tennessee_eastman, hai |
| hvac_kw_N:downq90 | s | oa_damper:upq10 | 3.491 | 10.675 | 21 | False | `SLOW-S.down.q90 -s-> MID-S.up.q10` | — | tennessee_eastman |
| T_out:downq80 | m | sa_t:upq20 | 3.488 | 6.88 | 79 | False | `MID.down.q80 -m-> MID.up.q20` | — | tennessee_eastman, hai |
| oa_damper:downq90 | s | sf_spd:upq80 | 3.486 | 2.424 | 16 | False | `MID-S.down.q90 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_damper:downq10 | m | ma_t:peak | 3.48 | 2.556 | 50 | True | `MID-S.down.q10 -m-> MID.peak` | — | tennessee_eastman, hai |
| oa_damper:upq90 | l | oa_flow:downq50 | 3.479 | 2.326 | 193 | True | `MID-S.up.q90 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| rf_spd:upq50 | s | sf_spd:downq50 | 3.475 | 2.578 | 186 | True | `SLOW.up.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| T:upq50 | l | fan:downq90 | 3.474 | 4.83 | 300 | True | `MID.up.q50 -l-> SET.down.q90` | — | tennessee_eastman, hai |
| oa_flow:upq80 | l | sa_t:downq20 | 3.473 | 9.507 | 398 | True | `MID.up.q80 -l-> MID.down.q20` | — | tennessee_eastman, hai |
| sf_spd:downq80 | m | oa_flow:downq50 | 3.467 | 2.153 | 132 | True | `SLOW.down.q80 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| rf_spd:downq20 | s | ma_t:peak | 3.467 | 2.95 | 39 | False | `SLOW.down.q20 -s-> MID.peak` | — | tennessee_eastman, hai |
| sf_spd:upq50 | m | rf_spd:downq50 | 3.462 | 2.649 | 753 | True | `SLOW.up.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| oa_flow:upq80 | l | sa_flow:downq80 | 3.461 | 3.27 | 516 | True | `MID.up.q80 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_flow:upq80 | l | sf_spd:upq80 | 3.448 | 4.056 | 399 | True | `MID.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_flow:upq80 | l | oa_flow:downq80 | 3.446 | 2.989 | 408 | True | `MID.up.q80 -l-> MID.down.q80 [same role]` | — | tennessee_eastman, hai |
| oa_flow:downq80 | m | sa_t:upq50 | 3.442 | 3.022 | 64 | True | `MID.down.q80 -m-> MID.up.q50` | — | tennessee_eastman, hai |
| oa_flow:downq50 | s | sf_spd:upq80 | 3.441 | 1.631 | 31 | True | `MID.down.q50 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_t:downq50 | l | rf_spd:downq80 | 3.437 | 3.494 | 264 | False | `MID.down.q50 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| T_out:downq80 | m | oa_damper:downq90 | 3.433 | 3.268 | 35 | False | `MID.down.q80 -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| sf_spd:downq50 | s | plenum_p:downq50 | 3.428 | 2.951 | 228 | True | `SLOW.down.q50 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| oa_damper:upq90 | m | ma_t:trough | 3.417 | 2.252 | 64 | True | `MID-S.up.q90 -m-> MID.trough` | — | tennessee_eastman, hai |
| sa_t:upq50 | l | oa_flow:downq20 | 3.413 | 2.097 | 130 | False | `MID.up.q50 -l-> MID.down.q20` | — | tennessee_eastman, hai |
| sa_flow:upq20 | m | oa_flow:upq20 | 3.412 | 3.399 | 71 | False | `SLOW.up.q20 -m-> MID.up.q20` | — | tennessee_eastman, hai |
| fan:upq90 | l | T:downq80 | 3.406 | 4.024 | 333 | True | `SET.up.q90 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| sa_flow:downq80 | s | plenum_p:downq80 | 3.406 | 3.688 | 103 | True | `SLOW.down.q80 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_damper:upq90 | l | sf_spd:upq80 | 3.405 | 4.142 | 133 | False | `MID-S.up.q90 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| ra_t:peak | l | oa_flow:downq50 | 3.403 | 1.91 | 540 | True | `MID.peak -l-> MID.down.q50` | — | tennessee_eastman, hai |
| hvac_kw_N:upq90 | m | sf_spd:upq80 | 3.391 | 2.524 | 128 | False | `SLOW-S.up.q90 -m-> SLOW.up.q80` | — | tennessee_eastman |
| plenum_p:upq80 | s | sf_spd:downq50 | 3.38 | 2.526 | 159 | True | `MID.up.q80 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| hvac_kw_S:upq80 | s | sf_spd:upq80 | 3.38 | 4.916 | 52 | False | `MID-S.up.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_t:peak | m | rf_spd:upq80 | 3.378 | 3.343 | 164 | True | `MID.peak -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rf_spd:downq50 | s | oa_damper:downq10 | 3.377 | 5.277 | 28 | True | `SLOW.down.q50 -s-> MID-S.down.q10` | — | tennessee_eastman, hai |
| oa_damper:downq10 | l | oa_flow:downq80 | 3.375 | 3.748 | 140 | False | `MID-S.down.q10 -l-> MID.down.q80` | tennessee_eastman | hai |
| oa_flow:downq80 | s | rf_spd:downq80 | 3.369 | 2.797 | 45 | True | `MID.down.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_flow:upq80 | l | sa_flow:upq80 | 3.364 | 3.273 | 501 | True | `MID.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sf_spd:upq20 | l | rf_spd:upq20 | 3.36 | 1.905 | 245 | False | `SLOW.up.q20 -l-> SLOW.up.q20` | — | tennessee_eastman, hai |
| sa_t:downq50 | s | rf_spd:upq80 | 3.36 | 3.717 | 32 | False | `MID.down.q50 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_flow:upq50 | m | rf_spd:upq50 | 3.357 | 2.545 | 735 | True | `SLOW.up.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| sa_t:downq50 | l | rf_spd:upq80 | 3.346 | 3.078 | 257 | False | `MID.down.q50 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| ra_t:peak | l | rf_spd:downq80 | 3.34 | 4.855 | 631 | True | `MID.peak -l-> SLOW.down.q80` | hai | tennessee_eastman |
| oa_t:peak | l | rf_spd:downq80 | 3.337 | 4.798 | 790 | True | `MID.peak -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| ma_t:trough | m | sf_spd:downq80 | 3.334 | 4.813 | 111 | True | `MID.trough -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_t:peak | l | oa_flow:downq50 | 3.329 | 1.862 | 662 | True | `MID.peak -l-> MID.down.q50` | — | tennessee_eastman, hai |
| rf_spd:downq50 | l | rf_spd:downq80 | 3.328 | 4.163 | 656 | False | `SLOW.down.q50 -l-> SLOW.down.q80 [same role]` | hai | tennessee_eastman |
| sa_t:upq20 | m | oa_damper:downq10 | 3.325 | 5.264 | 29 | False | `MID.up.q20 -m-> MID-S.down.q10` | — | tennessee_eastman, hai |
| hw_valve:upq10 | l | hw_valve:downq90 | 3.324 | 2.288 | 1165 | True | `MID-S.up.q10 -l-> MID-S.down.q90 [same role]` | fingrid | tennessee_eastman, hai |
| T:downq20 | m | hw_valve:upq90 | 3.321 | 2.704 | 710 | True | `MID.down.q20 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| sa_t:downq50 | m | sf_spd:upq80 | 3.319 | 4.539 | 56 | False | `MID.down.q50 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| hvac_kw_S:upq80 | m | sa_flow:downq80 | 3.318 | 1.825 | 266 | False | `MID-S.up.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| T:upq50 | m | T:upq80 | 3.317 | 4.189 | 1740 | True | `MID.up.q50 -m-> MID.up.q80 [same role]` | hai | tennessee_eastman |
| sf_spd:upq20 | s | plenum_p:upq50 | 3.315 | 3.043 | 98 | True | `SLOW.up.q20 -s-> MID.up.q50` | — | tennessee_eastman, hai |
| rh_out:upq50 | s | fan:downq90 | 3.311 | 7.974 | 23 | False | `SLOW.up.q50 -s-> SET.down.q90` | — | tennessee_eastman, hai |
| oa_damper:downq90 | m | sa_flow:upq80 | 3.308 | 3.148 | 62 | False | `MID-S.down.q90 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_damper:upq90 | m | sa_flow:upq80 | 3.306 | 2.839 | 63 | False | `MID-S.up.q90 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_t:peak | s | plenum_p:downq20 | 3.304 | 2.069 | 47 | True | `MID.peak -s-> MID.down.q20` | — | tennessee_eastman, hai |
| sf_spd:upq50 | s | plenum_p:upq50 | 3.302 | 3.244 | 204 | True | `SLOW.up.q50 -s-> MID.up.q50` | — | tennessee_eastman, hai |
| oa_damper:upq90 | l | sa_flow:upq80 | 3.302 | 3.245 | 166 | True | `MID-S.up.q90 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rf_spd:upq50 | l | rf_spd:downq80 | 3.297 | 4.471 | 650 | False | `SLOW.up.q50 -l-> SLOW.down.q80 [same role]` | — | tennessee_eastman, hai |
| ma_t:peak | m | oa_flow:upq50 | 3.297 | 4.352 | 151 | True | `MID.peak -m-> MID.up.q50` | — | tennessee_eastman, hai |
| plenum_p:upq80 | s | sa_flow:downq80 | 3.297 | 4.427 | 92 | False | `MID.up.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| ma_t:trough | m | rf_spd:downq80 | 3.295 | 4.776 | 185 | True | `MID.trough -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_t:trough | l | oa_damper:downq10 | 3.294 | 8.033 | 172 | True | `MID.trough -l-> MID-S.down.q10` | — | tennessee_eastman, hai |
| rf_spd:downq50 | l | rf_spd:upq80 | 3.287 | 4.148 | 648 | False | `SLOW.down.q50 -l-> SLOW.up.q80 [same role]` | hai | tennessee_eastman |
| T:downq80 | m | T:downq50 | 3.286 | 3.502 | 1408 | True | `MID.down.q80 -m-> MID.down.q50 [same role]` | hai | tennessee_eastman |
| sa_flow:upq80 | l | rf_spd:upq80 | 3.282 | 4.149 | 410 | False | `SLOW.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_damper:downq90 | s | ma_t:peak | 3.28 | 2.133 | 19 | False | `MID-S.down.q90 -s-> MID.peak` | — | tennessee_eastman, hai |
| plenum_p:upq20 | s | sf_spd:upq50 | 3.277 | 2.607 | 105 | True | `MID.up.q20 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| sf_spd:downq20 | l | plenum_p:downq20 | 3.271 | 1.633 | 396 | True | `SLOW.down.q20 -l-> MID.down.q20` | — | tennessee_eastman, hai |
| plenum_p:upq80 | s | sf_spd:downq80 | 3.269 | 5.798 | 71 | True | `MID.up.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| hw_valve:downq10 | l | hw_valve:upq10 | 3.268 | 2.558 | 2395 | True | `MID-S.down.q10 -l-> MID-S.up.q10 [same role]` | hai | tennessee_eastman, fingrid |
| ra_t:peak | l | sf_spd:downq80 | 3.258 | 5.06 | 365 | True | `MID.peak -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rf_spd:upq20 | s | sa_flow:upq50 | 3.256 | 3.554 | 71 | False | `SLOW.up.q20 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| sf_spd:upq80 | l | rf_spd:upq80 | 3.254 | 4.03 | 351 | True | `SLOW.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_t:upq20 | m | oa_damper:upq10 | 3.25 | 4.27 | 28 | False | `MID.up.q20 -m-> MID-S.up.q10` | tennessee_eastman | hai |
| oa_t:peak | l | sa_flow:downq80 | 3.248 | 3.804 | 586 | True | `MID.peak -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| hvac_kw_S:downq50 | s | sf_spd:downq50 | 3.248 | 3.824 | 556 | False | `MID-S.down.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| T:upq80 | l | Tsp_c:upq50 | 3.246 | 2.943 | 31 | False | `MID.up.q80 -l-> SET.up.q50` | — | hai |
| rf_spd:downq80 | m | oa_flow:downq50 | 3.245 | 2.22 | 182 | False | `SLOW.down.q80 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| sa_t:upq50 | l | rf_spd:upq80 | 3.241 | 3.234 | 252 | False | `MID.up.q50 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_flow:downq50 | s | plenum_p:downq20 | 3.233 | 1.607 | 122 | True | `SLOW.down.q50 -s-> MID.down.q20` | — | tennessee_eastman, hai |
| sa_t:upq50 | l | rf_spd:downq80 | 3.228 | 3.503 | 251 | False | `MID.up.q50 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rf_spd:downq80 | s | plenum_p:downq80 | 3.224 | 2.865 | 120 | True | `SLOW.down.q80 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_t:peak | l | sf_spd:downq80 | 3.219 | 4.743 | 452 | True | `MID.peak -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sf_spd:downq80 | l | rf_spd:downq80 | 3.214 | 3.968 | 353 | True | `SLOW.down.q80 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_damper:downq90 | m | rf_spd:upq80 | 3.209 | 2.723 | 79 | False | `MID-S.down.q90 -m-> SLOW.up.q80` | hai | tennessee_eastman |
| rf_spd:downq20 | l | plenum_p:upq20 | 3.208 | 1.91 | 437 | False | `SLOW.down.q20 -l-> MID.up.q20` | — | tennessee_eastman, hai |
| oa_damper:downq90 | m | ma_t:trough | 3.203 | 2.062 | 59 | True | `MID-S.down.q90 -m-> MID.trough` | — | tennessee_eastman, hai |
| ma_t:peak | m | sa_t:downq20 | 3.191 | 11.807 | 103 | True | `MID.peak -m-> MID.down.q20` | — | tennessee_eastman, hai |
| oa_damper:upq90 | s | rf_spd:downq50 | 3.189 | 1.546 | 44 | True | `MID-S.up.q90 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| T:upq50 | l | fan:upq90 | 3.185 | 4.199 | 275 | True | `MID.up.q50 -l-> SET.up.q90` | — | tennessee_eastman, hai |
| sf_spd:downq20 | l | sa_flow:upq20 | 3.183 | 1.734 | 186 | False | `SLOW.down.q20 -l-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_flow:upq80 | l | oa_damper:downq10 | 3.183 | 5.094 | 127 | True | `MID.up.q80 -l-> MID-S.down.q10` | — | tennessee_eastman, hai |
| plenum_p:upq80 | l | plenum_p:upq50 | 3.182 | 2.843 | 1133 | False | `MID.up.q80 -l-> MID.up.q50 [same role]` | — | tennessee_eastman, hai |
| sf_spd:upq20 | l | plenum_p:upq20 | 3.182 | 1.687 | 380 | False | `SLOW.up.q20 -l-> MID.up.q20` | — | tennessee_eastman, hai |
| sf_spd:upq80 | l | sa_t:upq50 | 3.178 | 2.689 | 132 | False | `SLOW.up.q80 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| sf_spd:downq80 | l | oa_flow:upq50 | 3.177 | 2.506 | 290 | True | `SLOW.down.q80 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| rf_spd:upq50 | m | oa_damper:downq90 | 3.173 | 8.231 | 118 | False | `SLOW.up.q50 -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| rf_spd:upq80 | m | oa_flow:downq50 | 3.171 | 1.844 | 178 | False | `SLOW.up.q80 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| rf_spd:downq50 | s | ra_t:trough | 3.171 | 2.392 | 64 | True | `SLOW.down.q50 -s-> MID.trough` | — | tennessee_eastman, hai |
| rf_spd:downq50 | l | oa_flow:downq80 | 3.169 | 4.292 | 378 | False | `SLOW.down.q50 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_damper:downq90 | m | rf_spd:downq80 | 3.168 | 3.394 | 78 | False | `MID-S.down.q90 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| fan:downq90 | m | T:downq50 | 3.167 | 2.461 | 138 | True | `SET.down.q90 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| hvac_kw_N:upq90 | m | sa_flow:downq80 | 3.166 | 2.358 | 154 | False | `SLOW-S.up.q90 -m-> SLOW.down.q80` | — | tennessee_eastman |
| hvac_kw_N:downq10 | m | rf_spd:upq20 | 3.157 | 2.283 | 217 | False | `SLOW-S.down.q10 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| rf_spd:downq50 | m | oa_damper:downq90 | 3.155 | 7.315 | 115 | True | `SLOW.down.q50 -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| sa_flow:upq50 | s | rf_spd:downq50 | 3.153 | 2.275 | 215 | True | `SLOW.up.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| sf_spd:upq50 | s | plenum_p:upq80 | 3.145 | 2.438 | 170 | True | `SLOW.up.q50 -s-> MID.up.q80` | — | tennessee_eastman, hai |
| rf_spd:upq20 | s | plenum_p:upq50 | 3.142 | 3.315 | 109 | False | `SLOW.up.q20 -s-> MID.up.q50` | — | tennessee_eastman, hai |
| plenum_p:upq50 | s | sa_flow:downq50 | 3.141 | 2.674 | 192 | True | `MID.up.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| oa_damper:downq10 | s | sa_flow:upq80 | 3.135 | 3.194 | 13 | False | `MID-S.down.q10 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| T:downq50 | m | hw_valve:upq10 | 3.131 | 3.527 | 1461 | True | `MID.down.q50 -m-> MID-S.up.q10` | — | tennessee_eastman, hai |
| sa_flow:upq80 | s | plenum_p:upq80 | 3.128 | 3.174 | 102 | True | `SLOW.up.q80 -s-> MID.up.q80` | — | tennessee_eastman, hai |
| sf_spd:downq50 | m | rf_spd:downq50 | 3.125 | 2.4 | 652 | True | `SLOW.down.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| T:upq20 | m | T:downq20 | 3.12 | 2.585 | 2632 | True | `MID.up.q20 -m-> MID.down.q20 [same role]` | tennessee_eastman | hai |
| rf_spd:upq80 | m | plenum_p:downq80 | 3.117 | 2.507 | 404 | True | `SLOW.up.q80 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| T_out:downq80 | m | T:downq80 | 3.108 | 3.35 | 541 | False | `MID.down.q80 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| sa_flow:upq50 | s | plenum_p:upq50 | 3.107 | 3.487 | 226 | True | `SLOW.up.q50 -s-> MID.up.q50` | — | tennessee_eastman, hai |
| sf_spd:downq50 | s | plenum_p:downq20 | 3.103 | 1.959 | 116 | True | `SLOW.down.q50 -s-> MID.down.q20` | — | tennessee_eastman, hai |
| T_out:downq50 | s | fan:downq90 | 3.101 | 2.726 | 20 | False | `MID.down.q50 -s-> SET.down.q90` | — | tennessee_eastman |
| rf_spd:upq20 | l | plenum_p:downq20 | 3.095 | 1.641 | 422 | False | `SLOW.up.q20 -l-> MID.down.q20` | — | tennessee_eastman, hai |
| T_out:downq80 | m | sa_t:downq20 | 3.095 | 6.153 | 70 | False | `MID.down.q80 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| plenum_p:downq80 | m | oa_damper:upq90 | 3.093 | 6.911 | 99 | False | `MID.down.q80 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| oa_damper:downq90 | s | rf_spd:upq80 | 3.093 | 2.761 | 24 | False | `MID-S.down.q90 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sf_spd:downq80 | l | rf_spd:upq80 | 3.087 | 3.861 | 339 | False | `SLOW.down.q80 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_damper:downq90 | l | oa_flow:downq50 | 3.079 | 1.773 | 161 | False | `MID-S.down.q90 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| rf_spd:downq20 | l | plenum_p:downq20 | 3.075 | 1.699 | 419 | False | `SLOW.down.q20 -l-> MID.down.q20` | — | tennessee_eastman, hai |
| oa_damper:upq90 | m | ra_t:peak | 3.073 | 1.928 | 38 | False | `MID-S.up.q90 -m-> MID.peak` | — | tennessee_eastman, hai |
| fan:upq90 | l | hw_valve:upq10 | 3.064 | 2.517 | 238 | True | `SET.up.q90 -l-> MID-S.up.q10` | — | tennessee_eastman, hai |
| oa_flow:upq80 | l | oa_flow:downq50 | 3.061 | 2.13 | 503 | True | `MID.up.q80 -l-> MID.down.q50 [same role]` | tennessee_eastman | hai |
| hvac_kw_S:downq80 | m | sf_spd:upq80 | 3.054 | 2.018 | 186 | False | `MID-S.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_t:downq20 | m | rf_spd:upq80 | 3.049 | 3.834 | 130 | False | `MID.down.q20 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rf_spd:upq80 | m | oa_damper:upq10 | 3.045 | 8.063 | 41 | True | `SLOW.up.q80 -m-> MID-S.up.q10` | — | tennessee_eastman, hai |
| oa_flow:downq50 | l | ra_t:trough | 3.044 | 1.586 | 342 | True | `MID.down.q50 -l-> MID.trough` | — | tennessee_eastman, hai |
| oa_t:trough | l | oa_damper:upq10 | 3.043 | 6.382 | 157 | True | `MID.trough -l-> MID-S.up.q10` | — | tennessee_eastman, hai |
| plenum_p:downq50 | l | plenum_p:downq80 | 3.04 | 3.218 | 1211 | False | `MID.down.q50 -l-> MID.down.q80 [same role]` | — | tennessee_eastman, hai |
| rf_spd:downq50 | l | sa_flow:downq80 | 3.036 | 3.475 | 456 | False | `SLOW.down.q50 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rf_spd:upq20 | l | plenum_p:upq20 | 3.036 | 1.926 | 414 | False | `SLOW.up.q20 -l-> MID.up.q20` | — | tennessee_eastman, hai |
| oa_flow:downq50 | m | sf_spd:downq50 | 3.036 | 1.616 | 229 | True | `MID.down.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| hvac_kw_N:upq10 | m | sa_flow:downq20 | 3.033 | 1.531 | 162 | False | `SLOW-S.up.q10 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| fan:upq10 | l | T:downq80 | 3.026 | 3.156 | 769 | True | `SET.up.q10 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| hvac_kw_S:upq50 | s | Tsp_c:downq20 | 3.023 | 1.754 | 97 | False | `MID-S.up.q50 -s-> SET.down.q20` | — | hai |
| oa_damper:upq10 | s | sa_t:downq50 | 3.022 | 1.984 | 8 | False | `MID-S.up.q10 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| rf_spd:upq20 | l | oa_flow:downq20 | 3.02 | 1.533 | 162 | False | `SLOW.up.q20 -l-> MID.down.q20` | — | tennessee_eastman, hai |
| T_out:upq80 | m | T:upq80 | 3.017 | 1.908 | 558 | False | `MID.up.q80 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| plenum_p:downq50 | s | sa_flow:upq50 | 3.015 | 2.724 | 175 | True | `MID.down.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| rf_spd:upq50 | l | rf_spd:upq80 | 3.013 | 3.996 | 594 | False | `SLOW.up.q50 -l-> SLOW.up.q80 [same role]` | hai | tennessee_eastman |
| oa_flow:upq50 | l | sa_t:downq20 | 3.008 | 10.62 | 452 | True | `MID.up.q50 -l-> MID.down.q20` | — | tennessee_eastman, hai |
| hvac_kw_S:downq80 | m | sa_flow:downq80 | 3.007 | 2.18 | 236 | False | `MID-S.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| T:upq80 | l | hw_valve:upq10 | 3.002 | 2.283 | 2107 | True | `MID.up.q80 -l-> MID-S.up.q10` | — | tennessee_eastman, hai |
| plenum_p:upq50 | s | plenum_p:upq80 | 3.002 | 3.393 | 256 | True | `MID.up.q50 -s-> MID.up.q80 [same role]` | hai | tennessee_eastman |
| sa_t:downq20 | m | rf_spd:downq80 | 3.002 | 3.766 | 128 | False | `MID.down.q20 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| plenum_p:upq50 | l | plenum_p:upq20 | 3.0 | 1.501 | 777 | False | `MID.up.q50 -l-> MID.up.q20 [same role]` | — | tennessee_eastman, hai |
| sa_flow:downq80 | l | oa_flow:upq50 | 3.0 | 2.365 | 320 | False | `SLOW.down.q80 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| sa_t:upq50 | m | sa_flow:downq80 | 3.0 | 3.814 | 66 | False | `MID.up.q50 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_flow:downq50 | l | oa_t:trough | 2.998 | 1.543 | 425 | True | `MID.down.q50 -l-> MID.trough` | — | tennessee_eastman, hai |
| rf_spd:downq50 | l | oa_damper:upq10 | 2.997 | 6.088 | 119 | False | `SLOW.down.q50 -l-> MID-S.up.q10` | — | tennessee_eastman, hai |
| T:upq80 | m | T:upq80 | 2.995 | 2.703 | 573 | False | `MID.up.q80 -m-> MID.up.q80 [same role]` | — | tennessee_eastman, hai |
| plenum_p:downq50 | s | sf_spd:upq50 | 2.99 | 2.617 | 161 | True | `MID.down.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| hw_valve:upq10 | l | hw_valve:upq90 | 2.983 | 1.891 | 1043 | True | `MID-S.up.q10 -l-> MID-S.up.q90 [same role]` | — | tennessee_eastman, hai, fingrid |
| plenum_p:upq20 | s | sa_flow:upq50 | 2.982 | 2.796 | 103 | True | `MID.up.q20 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| rf_spd:downq50 | s | oa_damper:upq90 | 2.981 | 6.886 | 32 | False | `SLOW.down.q50 -s-> MID-S.up.q90` | tennessee_eastman | hai |
| sa_flow:upq20 | s | plenum_p:upq50 | 2.98 | 2.995 | 98 | True | `SLOW.up.q20 -s-> MID.up.q50` | — | tennessee_eastman, hai |
| rh_out:downq20 | m | oa_damper:upq10 | 2.978 | 4.173 | 36 | False | `SLOW.down.q20 -m-> MID-S.up.q10` | — | tennessee_eastman, hai |
| sf_spd:upq50 | s | sf_spd:upq80 | 2.977 | 5.088 | 49 | True | `SLOW.up.q50 -s-> SLOW.up.q80 [same role]` | hai | tennessee_eastman |
| hvac_kw_S:downq80 | s | fan:downq90 | 2.976 | 1.827 | 27 | False | `MID-S.down.q80 -s-> SET.down.q90` | — | tennessee_eastman, hai |
| sf_spd:upq80 | l | oa_flow:downq50 | 2.969 | 2.054 | 269 | True | `SLOW.up.q80 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| rf_spd:downq80 | l | rf_spd:downq50 | 2.968 | 2.027 | 845 | False | `SLOW.down.q80 -l-> SLOW.down.q50 [same role]` | hai | tennessee_eastman |
| rf_spd:upq20 | s | sf_spd:upq50 | 2.965 | 3.707 | 60 | False | `SLOW.up.q20 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| T_out:downq80 | s | sa_t:downq20 | 2.963 | 6.507 | 14 | False | `MID.down.q80 -s-> MID.down.q20` | — | tennessee_eastman, hai |
| rf_spd:upq50 | s | plenum_p:upq50 | 2.962 | 2.816 | 274 | False | `SLOW.up.q50 -s-> MID.up.q50` | — | tennessee_eastman, hai |
| sa_flow:upq50 | m | oa_damper:downq90 | 2.959 | 8.544 | 82 | True | `SLOW.up.q50 -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| rf_spd:upq50 | l | sa_flow:downq80 | 2.956 | 3.685 | 444 | False | `SLOW.up.q50 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rf_spd:downq50 | l | sa_flow:upq80 | 2.953 | 3.071 | 443 | False | `SLOW.down.q50 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_damper:downq90 | l | plenum_p:upq80 | 2.953 | 2.644 | 357 | True | `MID-S.down.q90 -l-> MID.up.q80` | — | tennessee_eastman, hai |
| sf_spd:upq80 | l | sa_t:downq50 | 2.943 | 2.561 | 123 | True | `SLOW.up.q80 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| rh_out:downq20 | m | oa_damper:downq10 | 2.943 | 2.783 | 36 | False | `SLOW.down.q20 -m-> MID-S.down.q10` | — | tennessee_eastman, hai |
| sa_flow:downq20 | s | ma_t:peak | 2.941 | 2.58 | 28 | False | `SLOW.down.q20 -s-> MID.peak` | — | tennessee_eastman, hai |
| rh_out:downq20 | m | fan:upq90 | 2.939 | 3.976 | 55 | False | `SLOW.down.q20 -m-> SET.up.q90` | — | tennessee_eastman, hai |
| rf_spd:upq20 | m | oa_flow:downq20 | 2.938 | 2.321 | 76 | False | `SLOW.up.q20 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| T:upq20 | s | T:upq50 | 2.935 | 2.88 | 656 | True | `MID.up.q20 -s-> MID.up.q50 [same role]` | tennessee_eastman, hai | — |
| rf_spd:upq50 | s | sa_flow:upq80 | 2.932 | 3.963 | 93 | False | `SLOW.up.q50 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| fan:downq10 | s | hw_valve:upq10 | 2.93 | 2.112 | 38 | True | `SET.down.q10 -s-> MID-S.up.q10` | — | tennessee_eastman, hai |
| plenum_p:upq80 | l | oa_damper:upq90 | 2.929 | 7.571 | 124 | False | `MID.up.q80 -l-> MID-S.up.q90` | — | tennessee_eastman, hai |
| oa_flow:upq80 | l | sa_t:downq50 | 2.928 | 2.705 | 222 | True | `MID.up.q80 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| rh_out:upq20 | s | sf_spd:downq80 | 2.928 | 3.09 | 22 | False | `SLOW.up.q20 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| ma_t:trough | l | ma_t:peak | 2.926 | 1.942 | 590 | True | `MID.trough -l-> MID.peak [same role]` | hai | tennessee_eastman, fingrid |
| fan:downq10 | m | T:downq20 | 2.925 | 3.413 | 209 | True | `SET.down.q10 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| rf_spd:upq80 | l | rf_spd:downq50 | 2.923 | 2.055 | 826 | False | `SLOW.up.q80 -l-> SLOW.down.q50 [same role]` | hai | tennessee_eastman |
| plenum_p:upq80 | s | sa_flow:downq50 | 2.922 | 2.516 | 149 | False | `MID.up.q80 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| plenum_p:upq50 | l | plenum_p:downq80 | 2.919 | 2.921 | 1177 | False | `MID.up.q50 -l-> MID.down.q80 [same role]` | — | tennessee_eastman, hai |
| rh_out:upq50 | m | fan:downq90 | 2.919 | 6.793 | 99 | False | `SLOW.up.q50 -m-> SET.down.q90` | tennessee_eastman | hai |
| oa_flow:upq50 | l | sa_t:upq20 | 2.917 | 10.951 | 439 | True | `MID.up.q50 -l-> MID.up.q20` | — | tennessee_eastman, hai |
| hvac_kw_S:upq80 | m | oa_damper:downq90 | 2.916 | 7.538 | 81 | False | `MID-S.up.q80 -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| plenum_p:downq80 | m | rf_spd:downq80 | 2.912 | 3.433 | 353 | True | `MID.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_flow:upq50 | l | sa_flow:downq80 | 2.911 | 3.648 | 405 | False | `SLOW.up.q50 -l-> SLOW.down.q80 [same role]` | hai | tennessee_eastman |
| rf_spd:downq20 | m | oa_flow:upq20 | 2.909 | 2.184 | 73 | False | `SLOW.down.q20 -m-> MID.up.q20` | — | tennessee_eastman, hai |
| oa_flow:downq80 | l | sf_spd:downq50 | 2.905 | 1.855 | 673 | True | `MID.down.q80 -l-> SLOW.down.q50` | — | tennessee_eastman, hai |
| plenum_p:upq80 | m | rf_spd:downq80 | 2.904 | 3.278 | 350 | False | `MID.up.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rf_spd:downq50 | l | sa_t:upq20 | 2.898 | 10.173 | 335 | False | `SLOW.down.q50 -l-> MID.up.q20` | — | tennessee_eastman, hai |
| ma_t:trough | m | sa_flow:downq80 | 2.898 | 4.25 | 124 | True | `MID.trough -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rf_spd:upq80 | l | oa_flow:upq80 | 2.893 | 3.856 | 232 | False | `SLOW.up.q80 -l-> MID.up.q80` | — | tennessee_eastman, hai |
| plenum_p:downq50 | l | plenum_p:upq80 | 2.892 | 2.998 | 1154 | False | `MID.down.q50 -l-> MID.up.q80 [same role]` | — | tennessee_eastman, hai |
| rh_out:upq20 | m | sa_flow:downq80 | 2.892 | 2.049 | 119 | False | `SLOW.up.q20 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_flow:upq80 | l | oa_flow:upq50 | 2.89 | 1.839 | 300 | False | `SLOW.up.q80 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| sa_flow:downq50 | l | sf_spd:upq20 | 2.889 | 1.601 | 330 | False | `SLOW.down.q50 -l-> SLOW.up.q20` | — | tennessee_eastman, hai |
| rf_spd:upq50 | s | oa_flow:upq50 | 2.888 | 2.036 | 100 | True | `SLOW.up.q50 -s-> MID.up.q50` | — | tennessee_eastman, hai |
| sf_spd:downq50 | s | rf_spd:downq20 | 2.886 | 1.839 | 66 | True | `SLOW.down.q50 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| oa_t:peak | s | plenum_p:downq50 | 2.884 | 2.491 | 73 | True | `MID.peak -s-> MID.down.q50` | — | tennessee_eastman, hai |
| T:upq50 | l | fan:downq10 | 2.883 | 3.469 | 885 | True | `MID.up.q50 -l-> SET.down.q10` | — | tennessee_eastman, hai |
| ma_t:trough | l | oa_flow:downq50 | 2.882 | 2.349 | 654 | True | `MID.trough -l-> MID.down.q50` | — | tennessee_eastman, hai |
| T:upq50 | m | hw_valve:downq10 | 2.881 | 2.24 | 1207 | True | `MID.up.q50 -m-> MID-S.down.q10` | — | tennessee_eastman, hai |
| oa_flow:upq80 | s | rf_spd:upq50 | 2.881 | 1.88 | 71 | True | `MID.up.q80 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| rf_spd:downq80 | l | rf_spd:upq50 | 2.88 | 2.053 | 822 | False | `SLOW.down.q80 -l-> SLOW.up.q50 [same role]` | hai | tennessee_eastman |
| sa_flow:upq80 | l | plenum_p:downq80 | 2.873 | 2.779 | 696 | False | `SLOW.up.q80 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| rf_spd:downq80 | m | plenum_p:downq80 | 2.873 | 2.385 | 372 | True | `SLOW.down.q80 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| rh_out:upq20 | m | sf_spd:downq80 | 2.873 | 2.431 | 92 | False | `SLOW.up.q20 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rf_spd:upq50 | l | sa_t:upq20 | 2.872 | 10.582 | 332 | False | `SLOW.up.q50 -l-> MID.up.q20` | — | tennessee_eastman, hai |
| rf_spd:downq50 | l | sa_t:downq20 | 2.867 | 10.581 | 331 | False | `SLOW.down.q50 -l-> MID.down.q20` | — | tennessee_eastman, hai |
| sa_t:upq50 | m | sa_flow:upq80 | 2.866 | 3.329 | 63 | False | `MID.up.q50 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| plenum_p:downq50 | s | sf_spd:downq50 | 2.865 | 1.995 | 153 | True | `MID.down.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| ma_t:peak | l | ma_t:trough | 2.858 | 2.724 | 576 | True | `MID.peak -l-> MID.trough [same role]` | — | tennessee_eastman, hai, fingrid |
| rf_spd:upq50 | l | oa_flow:downq80 | 2.858 | 3.843 | 341 | False | `SLOW.up.q50 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_damper:downq10 | m | rf_spd:upq80 | 2.858 | 3.105 | 55 | False | `MID-S.down.q10 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sf_spd:upq80 | s | plenum_p:upq80 | 2.852 | 2.954 | 73 | True | `SLOW.up.q80 -s-> MID.up.q80` | — | tennessee_eastman, hai |
| T_out:downq80 | s | rf_spd:upq80 | 2.851 | 2.687 | 23 | False | `MID.down.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| plenum_p:downq80 | l | plenum_p:upq50 | 2.85 | 2.622 | 999 | False | `MID.down.q80 -l-> MID.up.q50 [same role]` | — | tennessee_eastman, hai |
| sa_flow:upq80 | l | oa_flow:downq50 | 2.85 | 1.917 | 299 | False | `SLOW.up.q80 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| sf_spd:upq80 | l | plenum_p:downq80 | 2.849 | 2.563 | 596 | True | `SLOW.up.q80 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_flow:downq80 | s | rf_spd:upq80 | 2.845 | 2.904 | 38 | True | `MID.down.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rf_spd:downq50 | m | sa_flow:downq50 | 2.84 | 2.181 | 546 | False | `SLOW.down.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| T:downq50 | s | fan:downq10 | 2.84 | 7.018 | 64 | False | `MID.down.q50 -s-> SET.down.q10` | hai | tennessee_eastman |
| plenum_p:upq50 | s | sf_spd:downq50 | 2.838 | 2.661 | 160 | True | `MID.up.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| rf_spd:downq80 | m | plenum_p:upq80 | 2.837 | 2.504 | 368 | True | `SLOW.down.q80 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| rf_spd:upq50 | l | sa_t:downq20 | 2.832 | 10.08 | 327 | False | `SLOW.up.q50 -l-> MID.down.q20` | — | tennessee_eastman, hai |
| sa_flow:upq50 | s | plenum_p:upq80 | 2.829 | 2.251 | 180 | True | `SLOW.up.q50 -s-> MID.up.q80` | — | tennessee_eastman, hai |
| hvac_kw_S:upq80 | m | sf_spd:upq80 | 2.829 | 1.845 | 176 | False | `MID-S.up.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_flow:upq50 | l | oa_damper:downq10 | 2.829 | 4.889 | 148 | True | `MID.up.q50 -l-> MID-S.down.q10` | — | tennessee_eastman, hai |
| rf_spd:upq50 | m | oa_damper:upq90 | 2.824 | 7.517 | 105 | False | `SLOW.up.q50 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| rf_spd:upq80 | l | rf_spd:upq50 | 2.817 | 2.039 | 798 | False | `SLOW.up.q80 -l-> SLOW.up.q50 [same role]` | hai | tennessee_eastman |
| T:upq50 | l | T:downq80 | 2.811 | 3.134 | 3508 | True | `MID.up.q50 -l-> MID.down.q80 [same role]` | — | tennessee_eastman, hai |
| rf_spd:downq80 | m | oa_flow:upq50 | 2.811 | 1.865 | 156 | False | `SLOW.down.q80 -m-> MID.up.q50` | — | tennessee_eastman, hai |
| sa_t:upq20 | m | plenum_p:downq80 | 2.809 | 2.442 | 233 | False | `MID.up.q20 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| sf_spd:downq80 | l | plenum_p:downq80 | 2.803 | 2.373 | 597 | True | `SLOW.down.q80 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| hvac_kw_N:upq90 | m | oa_damper:upq10 | 2.799 | 6.402 | 36 | False | `SLOW-S.up.q90 -m-> MID-S.up.q10` | — | tennessee_eastman |
| ma_t:peak | l | sa_t:upq20 | 2.798 | 12.362 | 442 | True | `MID.peak -l-> MID.up.q20` | — | tennessee_eastman, hai |
| rh_out:upq20 | s | sa_flow:downq80 | 2.797 | 2.514 | 27 | False | `SLOW.up.q20 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rf_spd:downq20 | l | plenum_p:upq50 | 2.796 | 2.614 | 679 | False | `SLOW.down.q20 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| hvac_kw_S:upq80 | s | oa_flow:downq80 | 2.795 | 2.528 | 44 | False | `MID-S.up.q80 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| T:upq50 | m | T:downq50 | 2.791 | 2.336 | 2641 | True | `MID.up.q50 -m-> MID.down.q50 [same role]` | tennessee_eastman, hai | — |
| hw_valve:downq90 | s | T:downq50 | 2.791 | 2.846 | 314 | True | `MID-S.down.q90 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| plenum_p:upq80 | l | plenum_p:downq50 | 2.789 | 2.545 | 991 | False | `MID.up.q80 -l-> MID.down.q50 [same role]` | — | tennessee_eastman, hai |
| plenum_p:upq80 | m | sa_flow:downq80 | 2.787 | 2.982 | 256 | True | `MID.up.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_flow:upq50 | m | rf_spd:downq50 | 2.784 | 1.647 | 336 | True | `MID.up.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| plenum_p:downq20 | l | plenum_p:downq50 | 2.783 | 2.771 | 886 | False | `MID.down.q20 -l-> MID.down.q50 [same role]` | — | tennessee_eastman, hai |
| rf_spd:upq80 | l | sa_flow:downq50 | 2.782 | 2.174 | 526 | False | `SLOW.up.q80 -l-> SLOW.down.q50` | — | tennessee_eastman, hai |
| hvac_kw_S:downq50 | s | sa_flow:downq50 | 2.781 | 3.123 | 516 | False | `MID-S.down.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| T:downq50 | m | hw_valve:upq90 | 2.779 | 2.471 | 679 | True | `MID.down.q50 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| rf_spd:upq80 | m | plenum_p:upq80 | 2.773 | 2.347 | 360 | True | `SLOW.up.q80 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| hvac_kw_N:downq10 | l | Tsp_c:downq80 | 2.77 | 3.489 | 120 | False | `SLOW-S.down.q10 -l-> SET.down.q80` | — | hai |
| sf_spd:downq50 | s | plenum_p:downq80 | 2.766 | 3.158 | 161 | True | `SLOW.down.q50 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| rf_spd:upq80 | l | oa_t:trough | 2.763 | 1.835 | 235 | False | `SLOW.up.q80 -l-> MID.trough` | — | tennessee_eastman, hai |
| oa_t:trough | l | ma_t:peak | 2.762 | 2.074 | 528 | True | `MID.trough -l-> MID.peak` | hai | tennessee_eastman, fingrid |
| sa_t:downq50 | m | sa_flow:downq80 | 2.76 | 3.659 | 60 | False | `MID.down.q50 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rh_out:downq20 | m | sa_flow:upq80 | 2.759 | 2.347 | 126 | False | `SLOW.down.q20 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| hvac_kw_N:downq10 | l | Tsp_h:upq20 | 2.754 | 2.135 | 65 | False | `SLOW-S.down.q10 -l-> SET.up.q20` | — | tennessee_eastman, hai |
| hvac_kw_N:upq10 | m | sa_flow:upq20 | 2.752 | 2.252 | 147 | False | `SLOW-S.up.q10 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_flow:downq80 | l | plenum_p:upq80 | 2.749 | 2.629 | 963 | True | `MID.down.q80 -l-> MID.up.q80` | — | tennessee_eastman, hai |
| sf_spd:downq20 | l | sa_flow:upq50 | 2.749 | 1.53 | 373 | True | `SLOW.down.q20 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| rf_spd:downq80 | l | sa_flow:downq50 | 2.746 | 2.141 | 523 | False | `SLOW.down.q80 -l-> SLOW.down.q50` | — | tennessee_eastman, hai |
| T:upq20 | l | Tsp_c:downq80 | 2.746 | 2.627 | 140 | True | `MID.up.q20 -l-> SET.down.q80` | — | hai |
| sa_flow:upq80 | l | plenum_p:upq80 | 2.745 | 2.728 | 666 | False | `SLOW.up.q80 -l-> MID.up.q80` | — | tennessee_eastman, hai |
| sf_spd:upq80 | l | plenum_p:upq80 | 2.744 | 2.554 | 575 | True | `SLOW.up.q80 -l-> MID.up.q80` | — | tennessee_eastman, hai |
| rf_spd:downq20 | l | sa_flow:upq50 | 2.744 | 1.642 | 419 | False | `SLOW.down.q20 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| rf_spd:upq50 | s | plenum_p:upq80 | 2.743 | 2.197 | 222 | True | `SLOW.up.q50 -s-> MID.up.q80` | — | tennessee_eastman, hai |
| sa_flow:upq50 | m | oa_damper:upq90 | 2.742 | 8.203 | 76 | True | `SLOW.up.q50 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| sf_spd:downq20 | l | sf_spd:upq50 | 2.741 | 1.512 | 345 | True | `SLOW.down.q20 -l-> SLOW.up.q50 [same role]` | — | tennessee_eastman, hai |
| rf_spd:upq80 | l | plenum_p:downq80 | 2.738 | 2.47 | 721 | False | `SLOW.up.q80 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| sf_spd:upq50 | s | sa_flow:upq80 | 2.738 | 3.564 | 58 | True | `SLOW.up.q50 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rf_spd:downq80 | l | sa_flow:upq50 | 2.734 | 2.203 | 522 | False | `SLOW.down.q80 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| sf_spd:upq80 | m | ma_t:trough | 2.726 | 1.606 | 89 | True | `SLOW.up.q80 -m-> MID.trough` | — | tennessee_eastman, hai |
| sa_t:upq20 | l | rf_spd:downq50 | 2.725 | 1.775 | 362 | False | `MID.up.q20 -l-> SLOW.down.q50` | — | tennessee_eastman, hai |
| oa_flow:upq80 | m | rf_spd:upq80 | 2.725 | 3.239 | 129 | True | `MID.up.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sf_spd:upq50 | m | rf_spd:upq50 | 2.724 | 2.559 | 594 | True | `SLOW.up.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| sf_spd:downq80 | l | plenum_p:upq80 | 2.724 | 2.45 | 581 | True | `SLOW.down.q80 -l-> MID.up.q80` | — | tennessee_eastman, hai |
| T_out:downq80 | m | rf_spd:downq80 | 2.719 | 2.348 | 105 | False | `MID.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sf_spd:upq50 | m | oa_damper:downq90 | 2.718 | 8.329 | 75 | True | `SLOW.up.q50 -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| hvac_kw_S:downq80 | m | sa_flow:upq80 | 2.717 | 1.665 | 213 | False | `MID-S.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rf_spd:downq50 | s | plenum_p:downq80 | 2.714 | 3.023 | 214 | False | `SLOW.down.q50 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| hvac_kw_N:upq10 | m | sf_spd:downq20 | 2.714 | 1.792 | 153 | False | `SLOW-S.up.q10 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| sa_flow:upq50 | m | plenum_p:downq50 | 2.713 | 2.572 | 631 | True | `SLOW.up.q50 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| sf_spd:upq50 | l | sa_flow:downq80 | 2.712 | 3.552 | 396 | True | `SLOW.up.q50 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| T_out:downq80 | l | Tsp_c:upq50 | 2.712 | 1.865 | 24 | False | `MID.down.q80 -l-> SET.up.q50` | — | hai |
| hvac_kw_S:downq80 | m | fan:downq90 | 2.708 | 3.51 | 87 | False | `MID-S.down.q80 -m-> SET.down.q90` | — | tennessee_eastman, hai |
| T_out:upq80 | m | oa_flow:downq80 | 2.701 | 2.647 | 67 | False | `MID.up.q80 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| rf_spd:upq80 | l | plenum_p:upq80 | 2.7 | 2.407 | 712 | False | `SLOW.up.q80 -l-> MID.up.q80` | — | tennessee_eastman, hai |
| sa_flow:downq80 | l | plenum_p:downq80 | 2.7 | 2.615 | 672 | False | `SLOW.down.q80 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_flow:downq50 | l | plenum_p:downq80 | 2.691 | 2.574 | 1181 | True | `MID.down.q50 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| hw_valve:downq10 | s | T:downq20 | 2.69 | 2.354 | 185 | True | `MID-S.down.q10 -s-> MID.down.q20` | tennessee_eastman | hai |
| T:downq50 | m | T:upq50 | 2.684 | 2.186 | 2854 | True | `MID.down.q50 -m-> MID.up.q50 [same role]` | tennessee_eastman, hai | — |
| hw_valve:downq10 | l | T:downq80 | 2.682 | 2.847 | 2474 | True | `MID-S.down.q10 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_flow:upq50 | l | rf_spd:upq80 | 2.678 | 3.767 | 687 | True | `MID.up.q50 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sf_spd:downq50 | l | sa_flow:downq80 | 2.678 | 2.944 | 378 | True | `SLOW.down.q50 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| plenum_p:downq80 | s | rf_spd:upq50 | 2.678 | 1.808 | 204 | False | `MID.down.q80 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| rh_out:upq20 | m | sa_flow:upq80 | 2.676 | 2.236 | 110 | False | `SLOW.up.q20 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rf_spd:downq80 | l | oa_flow:upq50 | 2.674 | 2.159 | 304 | False | `SLOW.down.q80 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| plenum_p:downq50 | s | rf_spd:upq50 | 2.674 | 1.928 | 232 | False | `MID.down.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| plenum_p:upq50 | s | sf_spd:upq50 | 2.674 | 1.579 | 152 | True | `MID.up.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| sa_t:downq20 | l | rf_spd:downq50 | 2.668 | 1.902 | 341 | False | `MID.down.q20 -l-> SLOW.down.q50` | — | tennessee_eastman, hai |
| oa_flow:downq50 | l | rf_spd:downq50 | 2.666 | 1.703 | 1256 | True | `MID.down.q50 -l-> SLOW.down.q50` | — | tennessee_eastman, hai |
| sa_flow:upq80 | m | plenum_p:downq80 | 2.664 | 2.486 | 274 | True | `SLOW.up.q80 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| T_out:upq80 | m | oa_damper:upq10 | 2.664 | 2.544 | 22 | False | `MID.up.q80 -m-> MID-S.up.q10` | — | tennessee_eastman, hai |
| sa_flow:downq50 | l | oa_flow:downq80 | 2.661 | 4.063 | 290 | False | `SLOW.down.q50 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| plenum_p:downq80 | l | oa_flow:downq80 | 2.659 | 3.713 | 254 | False | `MID.down.q80 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| sf_spd:upq50 | s | rf_spd:upq80 | 2.659 | 3.305 | 74 | True | `SLOW.up.q50 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_damper:downq10 | m | sa_flow:downq80 | 2.659 | 3.065 | 39 | False | `MID-S.down.q10 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| plenum_p:upq50 | l | plenum_p:upq80 | 2.656 | 2.592 | 1073 | False | `MID.up.q50 -l-> MID.up.q80 [same role]` | — | tennessee_eastman, hai |
| oa_flow:upq50 | l | sa_t:downq50 | 2.655 | 2.989 | 264 | True | `MID.up.q50 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| rf_spd:downq50 | l | sf_spd:downq80 | 2.643 | 4.222 | 309 | False | `SLOW.down.q50 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_flow:downq50 | l | sa_flow:upq80 | 2.641 | 3.051 | 362 | False | `SLOW.down.q50 -l-> SLOW.up.q80 [same role]` | — | tennessee_eastman, hai |
| rf_spd:downq80 | l | plenum_p:downq80 | 2.639 | 2.31 | 700 | False | `SLOW.down.q80 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| rf_spd:upq80 | l | sa_flow:upq50 | 2.638 | 2.215 | 500 | False | `SLOW.up.q80 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| sf_spd:downq50 | s | rf_spd:upq50 | 2.635 | 2.562 | 165 | True | `SLOW.down.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| hvac_kw_N:upq90 | m | sa_flow:upq80 | 2.634 | 2.494 | 128 | False | `SLOW-S.up.q90 -m-> SLOW.up.q80` | — | tennessee_eastman |
| sa_t:upq50 | l | oa_flow:downq50 | 2.633 | 1.945 | 172 | False | `MID.up.q50 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| T:downq20 | l | hw_valve:downq10 | 2.63 | 2.311 | 1622 | False | `MID.down.q20 -l-> MID-S.down.q10` | — | tennessee_eastman, hai |
| rh_out:upq20 | m | sf_spd:upq80 | 2.63 | 2.539 | 84 | False | `SLOW.up.q20 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sf_spd:downq80 | s | plenum_p:downq50 | 2.626 | 2.489 | 84 | True | `SLOW.down.q80 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| T:downq50 | l | hw_valve:downq90 | 2.625 | 1.505 | 1275 | True | `MID.down.q50 -l-> MID-S.down.q90` | — | tennessee_eastman, hai |
| sf_spd:upq50 | s | rf_spd:downq50 | 2.624 | 2.299 | 152 | True | `SLOW.up.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| oa_flow:upq50 | l | rf_spd:downq80 | 2.619 | 3.993 | 672 | True | `MID.up.q50 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sa_flow:downq50 | m | plenum_p:upq50 | 2.617 | 2.645 | 589 | True | `SLOW.down.q50 -m-> MID.up.q50` | — | tennessee_eastman, hai |
| sa_t:upq20 | l | rf_spd:upq50 | 2.614 | 1.785 | 348 | False | `MID.up.q20 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| sa_flow:downq80 | l | sa_flow:downq50 | 2.613 | 2.196 | 467 | True | `SLOW.down.q80 -l-> SLOW.down.q50 [same role]` | — | tennessee_eastman, hai |
| rf_spd:downq50 | m | sf_spd:downq50 | 2.611 | 2.164 | 463 | False | `SLOW.down.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| T:upq20 | l | fan:upq10 | 2.61 | 3.189 | 630 | True | `MID.up.q20 -l-> SET.up.q10` | — | tennessee_eastman, hai |
| oa_flow:downq50 | m | rf_spd:downq50 | 2.61 | 1.56 | 319 | True | `MID.down.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| oa_flow:downq50 | l | rf_spd:upq50 | 2.609 | 1.653 | 1232 | True | `MID.down.q50 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| rf_spd:upq50 | m | plenum_p:downq50 | 2.608 | 2.286 | 814 | True | `SLOW.up.q50 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| sf_spd:downq80 | s | plenum_p:downq80 | 2.608 | 3.391 | 73 | True | `SLOW.down.q80 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| oa_flow:upq50 | l | sa_flow:upq80 | 2.606 | 2.815 | 509 | True | `MID.up.q50 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sa_flow:downq50 | s | plenum_p:downq80 | 2.604 | 2.801 | 153 | True | `SLOW.down.q50 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| sa_flow:upq50 | l | oa_flow:downq50 | 2.602 | 2.012 | 399 | False | `SLOW.up.q50 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| plenum_p:downq50 | m | sa_flow:upq50 | 2.598 | 2.086 | 510 | False | `MID.down.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| plenum_p:upq50 | s | rf_spd:downq50 | 2.594 | 2.023 | 237 | False | `MID.up.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| hvac_kw_S:downq80 | m | Tsp_c:upq50 | 2.59 | 2.272 | 13 | False | `MID-S.down.q80 -m-> SET.up.q50` | — | hai |
| plenum_p:upq80 | l | plenum_p:upq20 | 2.589 | 1.54 | 517 | False | `MID.up.q80 -l-> MID.up.q20 [same role]` | — | tennessee_eastman, hai |
| hw_valve:upq10 | m | Tsp_c:upq20 | 2.584 | 2.162 | 44 | True | `MID-S.up.q10 -m-> SET.up.q20` | — | hai |
| plenum_p:upq80 | l | plenum_p:downq20 | 2.574 | 1.551 | 514 | False | `MID.up.q80 -l-> MID.down.q20 [same role]` | — | tennessee_eastman, hai |
| hvac_kw_S:downq80 | m | oa_damper:downq90 | 2.574 | 4.147 | 70 | False | `MID-S.down.q80 -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| rh_out:upq80 | m | Tsp_c:upq20 | 2.574 | 1.785 | 52 | False | `SLOW.up.q80 -m-> SET.up.q20` | — | hai |
| hw_valve:downq90 | m | T:upq20 | 2.57 | 2.012 | 1110 | True | `MID-S.down.q90 -m-> MID.up.q20` | — | tennessee_eastman, hai |
| sa_flow:upq50 | l | plenum_p:downq50 | 2.57 | 2.195 | 1040 | False | `SLOW.up.q50 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| sa_flow:upq50 | m | oa_damper:downq10 | 2.57 | 5.753 | 55 | True | `SLOW.up.q50 -m-> MID-S.down.q10` | — | tennessee_eastman, hai |
| oa_flow:downq50 | l | sa_flow:upq50 | 2.567 | 1.756 | 811 | True | `MID.down.q50 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| rf_spd:downq80 | l | sf_spd:upq50 | 2.557 | 1.989 | 453 | False | `SLOW.down.q80 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| plenum_p:upq50 | l | oa_flow:downq50 | 2.553 | 2.086 | 446 | False | `MID.up.q50 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| hvac_kw_N:downq10 | l | Tsp_c:downq50 | 2.55 | 4.015 | 24 | False | `SLOW-S.down.q10 -l-> SET.down.q50` | — | hai |
| plenum_p:upq50 | l | rf_spd:downq80 | 2.549 | 3.789 | 530 | False | `MID.up.q50 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| hvac_kw_N:downq10 | l | Tsp_c:downq20 | 2.549 | 3.816 | 115 | False | `SLOW-S.down.q10 -l-> SET.down.q20` | — | hai |
| sa_flow:downq80 | m | plenum_p:upq80 | 2.547 | 2.545 | 262 | True | `SLOW.down.q80 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| hvac_kw_N:downq90 | s | rf_spd:downq80 | 2.545 | 2.195 | 76 | False | `SLOW-S.down.q90 -s-> SLOW.down.q80` | — | tennessee_eastman |
| sf_spd:downq80 | m | plenum_p:upq80 | 2.544 | 2.366 | 224 | True | `SLOW.down.q80 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| oa_flow:upq50 | l | sf_spd:downq80 | 2.543 | 3.755 | 387 | True | `MID.up.q50 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| T_out:upq80 | l | oa_damper:upq10 | 2.543 | 3.498 | 97 | False | `MID.up.q80 -l-> MID-S.up.q10` | — | tennessee_eastman, hai |
| T_out:upq80 | l | fan:downq90 | 2.54 | 2.38 | 150 | False | `MID.up.q80 -l-> SET.down.q90` | — | tennessee_eastman, hai |
| sa_t:downq20 | l | rf_spd:upq50 | 2.537 | 1.766 | 325 | False | `MID.down.q20 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| oa_flow:upq80 | l | plenum_p:upq80 | 2.531 | 2.478 | 962 | True | `MID.up.q80 -l-> MID.up.q80` | — | tennessee_eastman, hai |
| plenum_p:downq50 | l | sf_spd:downq50 | 2.528 | 1.813 | 667 | False | `MID.down.q50 -l-> SLOW.down.q50` | — | tennessee_eastman, hai |
| plenum_p:downq50 | m | oa_t:peak | 2.528 | 1.891 | 223 | False | `MID.down.q50 -m-> MID.peak` | — | tennessee_eastman, hai |
| plenum_p:downq50 | m | sf_spd:upq50 | 2.525 | 1.922 | 460 | False | `MID.down.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| rf_spd:upq50 | l | plenum_p:downq50 | 2.523 | 2.404 | 1102 | False | `SLOW.up.q50 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| T_out:downq50 | m | fan:downq10 | 2.521 | 2.111 | 269 | False | `MID.down.q50 -m-> SET.down.q10` | — | tennessee_eastman |
| rh_out:upq50 | s | T:downq80 | 2.521 | 3.645 | 253 | False | `SLOW.up.q50 -s-> MID.down.q80` | hai | tennessee_eastman |
| sa_flow:downq50 | l | plenum_p:upq50 | 2.519 | 2.397 | 1007 | False | `SLOW.down.q50 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| oa_flow:upq50 | l | sf_spd:upq50 | 2.519 | 1.692 | 837 | True | `MID.up.q50 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| plenum_p:downq50 | m | ra_t:peak | 2.519 | 1.764 | 175 | False | `MID.down.q50 -m-> MID.peak` | — | tennessee_eastman, hai |
| plenum_p:downq80 | m | sf_spd:downq50 | 2.518 | 1.78 | 392 | False | `MID.down.q80 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| plenum_p:downq50 | l | rf_spd:downq80 | 2.516 | 3.899 | 517 | False | `MID.down.q50 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| sf_spd:upq50 | l | oa_flow:downq50 | 2.516 | 1.973 | 405 | False | `SLOW.up.q50 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| T_out:downq80 | s | sf_spd:upq80 | 2.516 | 2.852 | 12 | False | `MID.down.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| plenum_p:downq80 | l | plenum_p:upq20 | 2.513 | 1.52 | 494 | False | `MID.down.q80 -l-> MID.up.q20 [same role]` | — | tennessee_eastman, hai |
| T_out:downq80 | l | Tsp_c:upq20 | 2.512 | 2.135 | 110 | False | `MID.down.q80 -l-> SET.up.q20` | — | hai |
| T_out:downq80 | m | rf_spd:upq80 | 2.512 | 1.637 | 97 | False | `MID.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| hw_valve:upq90 | m | T:downq20 | 2.506 | 1.82 | 1082 | True | `MID-S.up.q90 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| rf_spd:downq50 | m | plenum_p:upq50 | 2.505 | 2.353 | 768 | True | `SLOW.down.q50 -m-> MID.up.q50` | — | tennessee_eastman, hai |
| T:upq20 | l | Tsp_c:downq20 | 2.505 | 2.911 | 133 | True | `MID.up.q20 -l-> SET.down.q20` | — | hai |
| sf_spd:upq50 | m | plenum_p:downq50 | 2.5 | 2.164 | 579 | True | `SLOW.up.q50 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| sa_t:upq20 | m | ma_t:trough | 2.5 | 1.964 | 80 | True | `MID.up.q20 -m-> MID.trough` | — | tennessee_eastman, hai |
| plenum_p:upq50 | m | sf_spd:downq50 | 2.497 | 1.69 | 445 | False | `MID.up.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| sa_t:upq50 | m | plenum_p:upq80 | 2.496 | 1.914 | 140 | False | `MID.up.q50 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| sa_flow:upq80 | s | plenum_p:upq50 | 2.495 | 2.654 | 93 | True | `SLOW.up.q80 -s-> MID.up.q50` | — | tennessee_eastman, hai |
| T:upq50 | l | hw_valve:upq10 | 2.494 | 1.921 | 2473 | True | `MID.up.q50 -l-> MID-S.up.q10` | — | tennessee_eastman, hai |
| plenum_p:upq50 | m | sf_spd:upq50 | 2.494 | 1.795 | 448 | False | `MID.up.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| plenum_p:downq80 | m | sa_flow:downq50 | 2.494 | 1.783 | 421 | False | `MID.down.q80 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| rf_spd:downq80 | l | sf_spd:downq50 | 2.493 | 1.893 | 438 | False | `SLOW.down.q80 -l-> SLOW.down.q50` | — | tennessee_eastman, hai |
| T:upq20 | s | hw_valve:downq10 | 2.492 | 2.677 | 246 | True | `MID.up.q20 -s-> MID-S.down.q10` | — | tennessee_eastman, hai |
| plenum_p:downq80 | l | plenum_p:downq50 | 2.49 | 2.298 | 871 | False | `MID.down.q80 -l-> MID.down.q50 [same role]` | — | tennessee_eastman, hai |
| plenum_p:downq50 | l | sa_flow:downq50 | 2.489 | 1.728 | 712 | False | `MID.down.q50 -l-> SLOW.down.q50` | — | tennessee_eastman, hai |
| oa_damper:downq90 | m | plenum_p:upq80 | 2.488 | 2.028 | 119 | False | `MID-S.down.q90 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| sf_spd:downq50 | l | plenum_p:upq50 | 2.487 | 2.371 | 1023 | True | `SLOW.down.q50 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| plenum_p:downq80 | m | rf_spd:downq50 | 2.485 | 1.65 | 627 | False | `MID.down.q80 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| plenum_p:upq80 | l | sf_spd:upq50 | 2.485 | 1.715 | 516 | False | `MID.up.q80 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| rf_spd:downq50 | l | plenum_p:upq50 | 2.482 | 2.405 | 1086 | False | `SLOW.down.q50 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| plenum_p:upq50 | l | rf_spd:downq50 | 2.481 | 1.657 | 1074 | False | `MID.up.q50 -l-> SLOW.down.q50` | — | tennessee_eastman, hai |
| rh_out:downq20 | l | fan:downq90 | 2.48 | 2.595 | 159 | False | `SLOW.down.q20 -l-> SET.down.q90` | — | tennessee_eastman, hai |
| sf_spd:upq50 | l | plenum_p:downq50 | 2.477 | 2.24 | 1052 | True | `SLOW.up.q50 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| plenum_p:upq50 | l | sa_flow:downq50 | 2.476 | 1.724 | 717 | False | `MID.up.q50 -l-> SLOW.down.q50` | — | tennessee_eastman, hai |
| sa_flow:upq80 | m | plenum_p:upq80 | 2.476 | 2.096 | 255 | True | `SLOW.up.q80 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| sa_flow:downq50 | m | oa_flow:upq80 | 2.472 | 3.478 | 148 | True | `SLOW.down.q50 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| oa_flow:upq80 | l | sf_spd:upq50 | 2.467 | 1.826 | 625 | True | `MID.up.q80 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| plenum_p:upq80 | m | oa_flow:upq50 | 2.466 | 1.875 | 247 | False | `MID.up.q80 -m-> MID.up.q50` | — | tennessee_eastman, hai |
| hvac_kw_N:upq10 | m | sf_spd:upq20 | 2.466 | 2.134 | 139 | False | `SLOW-S.up.q10 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| rf_spd:upq50 | l | plenum_p:downq80 | 2.464 | 2.462 | 942 | False | `SLOW.up.q50 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| plenum_p:upq80 | l | ra_t:peak | 2.462 | 1.976 | 195 | False | `MID.up.q80 -l-> MID.peak` | — | tennessee_eastman, hai |
| rh_out:downq20 | m | oa_damper:upq90 | 2.462 | 3.822 | 39 | False | `SLOW.down.q20 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| plenum_p:downq50 | m | rf_spd:downq50 | 2.459 | 1.645 | 720 | False | `MID.down.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| hw_valve:downq10 | l | fan:downq10 | 2.459 | 2.425 | 558 | True | `MID-S.down.q10 -l-> SET.down.q10` | — | tennessee_eastman, hai |
| plenum_p:upq50 | m | sa_flow:upq50 | 2.458 | 2.065 | 476 | False | `MID.up.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| hvac_kw_S:upq80 | m | oa_flow:downq80 | 2.45 | 3.942 | 156 | False | `MID-S.up.q80 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| plenum_p:upq50 | m | sa_flow:downq50 | 2.448 | 1.857 | 473 | False | `MID.up.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| plenum_p:upq50 | l | oa_flow:upq50 | 2.448 | 2.138 | 423 | False | `MID.up.q50 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| plenum_p:upq80 | l | rf_spd:upq80 | 2.445 | 3.728 | 392 | False | `MID.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| sf_spd:upq50 | l | rf_spd:upq50 | 2.441 | 1.77 | 976 | False | `SLOW.up.q50 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| oa_damper:upq10 | s | oa_flow:downq50 | 2.44 | 1.831 | 14 | False | `MID-S.up.q10 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| rf_spd:downq50 | m | plenum_p:upq80 | 2.435 | 2.161 | 653 | True | `SLOW.down.q50 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| plenum_p:upq50 | l | sf_spd:downq50 | 2.43 | 1.821 | 649 | False | `MID.up.q50 -l-> SLOW.down.q50` | — | tennessee_eastman, hai |
| sf_spd:upq50 | m | oa_damper:upq90 | 2.428 | 7.665 | 67 | True | `SLOW.up.q50 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| sa_flow:upq50 | s | oa_damper:upq90 | 2.428 | 7.761 | 21 | False | `SLOW.up.q50 -s-> MID-S.up.q90` | — | tennessee_eastman, hai |
| plenum_p:upq50 | m | rf_spd:upq50 | 2.425 | 1.736 | 702 | False | `MID.up.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| plenum_p:downq80 | l | sf_spd:upq50 | 2.422 | 1.588 | 495 | False | `MID.down.q80 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| plenum_p:upq80 | m | sf_spd:downq50 | 2.422 | 1.574 | 375 | False | `MID.up.q80 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| T:downq20 | l | T:upq50 | 2.414 | 2.13 | 3371 | False | `MID.down.q20 -l-> MID.up.q50 [same role]` | — | tennessee_eastman, hai |
| oa_flow:upq50 | l | rf_spd:upq50 | 2.414 | 1.614 | 1292 | True | `MID.up.q50 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| plenum_p:downq80 | m | sa_flow:downq80 | 2.414 | 3.244 | 223 | False | `MID.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| oa_damper:upq90 | m | rf_spd:upq50 | 2.413 | 1.606 | 126 | True | `MID-S.up.q90 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| plenum_p:downq50 | m | rf_spd:upq50 | 2.409 | 1.74 | 707 | False | `MID.down.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| T:downq20 | m | T:downq20 | 2.408 | 1.747 | 1887 | True | `MID.down.q20 -m-> MID.down.q20 [same role]` | — | tennessee_eastman, hai |
| oa_flow:upq80 | l | plenum_p:downq80 | 2.406 | 2.449 | 913 | True | `MID.up.q80 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| plenum_p:upq80 | m | sa_flow:downq50 | 2.401 | 1.553 | 403 | False | `MID.up.q80 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| plenum_p:downq80 | l | oa_flow:upq50 | 2.401 | 2.106 | 315 | False | `MID.down.q80 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| hvac_kw_S:downq80 | m | fan:downq10 | 2.399 | 2.241 | 274 | False | `MID-S.down.q80 -m-> SET.down.q10` | — | tennessee_eastman, hai |
| T_out:downq50 | s | fan:downq10 | 2.399 | 4.907 | 55 | False | `MID.down.q50 -s-> SET.down.q10` | — | tennessee_eastman |
| T:downq50 | m | T:downq20 | 2.397 | 2.574 | 2146 | True | `MID.down.q50 -m-> MID.down.q20 [same role]` | hai | tennessee_eastman |
| T:upq80 | l | T:downq50 | 2.395 | 2.25 | 3821 | True | `MID.up.q80 -l-> MID.down.q50 [same role]` | — | tennessee_eastman, hai |
| sf_spd:upq50 | l | plenum_p:downq80 | 2.395 | 2.474 | 890 | True | `SLOW.up.q50 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| plenum_p:downq80 | l | rf_spd:downq80 | 2.394 | 3.718 | 378 | False | `MID.down.q80 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rf_spd:upq50 | m | plenum_p:downq80 | 2.391 | 2.167 | 653 | False | `SLOW.up.q50 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| rf_spd:upq50 | m | sf_spd:upq50 | 2.391 | 2.141 | 436 | False | `SLOW.up.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| plenum_p:downq50 | m | sa_flow:downq50 | 2.39 | 1.903 | 468 | False | `MID.down.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| hvac_kw_N:downq10 | s | sa_flow:upq20 | 2.386 | 2.908 | 41 | False | `SLOW-S.down.q10 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| oa_damper:upq90 | s | rf_spd:upq50 | 2.386 | 1.952 | 33 | False | `MID-S.up.q90 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| hvac_kw_S:downq80 | m | Tsp_c:upq20 | 2.374 | 3.008 | 59 | False | `MID-S.down.q80 -m-> SET.up.q20` | — | hai |
| sf_spd:downq50 | m | plenum_p:upq50 | 2.373 | 2.495 | 528 | True | `SLOW.down.q50 -m-> MID.up.q50` | — | tennessee_eastman, hai |
| rh_out:upq20 | m | rf_spd:downq80 | 2.37 | 2.062 | 128 | False | `SLOW.up.q20 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rh_out:downq20 | m | sf_spd:upq80 | 2.367 | 2.31 | 84 | False | `SLOW.down.q20 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| oa_flow:upq50 | l | plenum_p:upq50 | 2.363 | 2.277 | 1346 | True | `MID.up.q50 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| Tsp_c:downq20 | s | hw_valve:downq90 | 2.363 | 4.583 | 3 | True | `SET.down.q20 -s-> MID-S.down.q90` | — | hai |
| hvac_kw_N:upq90 | l | oa_damper:upq10 | 2.361 | 2.926 | 48 | False | `SLOW-S.up.q90 -l-> MID-S.up.q10` | — | tennessee_eastman |
| sf_spd:upq50 | m | sa_flow:upq80 | 2.351 | 1.675 | 187 | True | `SLOW.up.q50 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| hvac_kw_S:downq80 | m | rf_spd:downq80 | 2.35 | 1.821 | 242 | False | `MID-S.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| hvac_kw_N:upq10 | m | rf_spd:downq20 | 2.349 | 1.919 | 159 | False | `SLOW-S.up.q10 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| plenum_p:upq80 | l | rf_spd:upq50 | 2.344 | 1.626 | 784 | False | `MID.up.q80 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| oa_damper:upq10 | s | rf_spd:upq80 | 2.342 | 2.153 | 16 | False | `MID-S.up.q10 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| T_out:downq80 | m | fan:downq10 | 2.335 | 3.49 | 100 | False | `MID.down.q80 -m-> SET.down.q10` | — | tennessee_eastman, hai |
| hvac_kw_S:downq50 | s | Tsp_c:upq20 | 2.332 | 1.802 | 75 | False | `MID-S.down.q50 -s-> SET.up.q20` | — | hai |
| rh_out:downq20 | m | fan:upq10 | 2.331 | 2.469 | 156 | False | `SLOW.down.q20 -m-> SET.up.q10` | tennessee_eastman | hai |
| oa_flow:upq50 | l | rf_spd:downq50 | 2.328 | 1.589 | 1243 | True | `MID.up.q50 -l-> SLOW.down.q50` | — | tennessee_eastman, hai |
| plenum_p:upq50 | m | rf_spd:downq50 | 2.327 | 1.627 | 672 | False | `MID.up.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| T_out:upq50 | m | hw_valve:downq10 | 2.325 | 1.969 | 752 | True | `MID.up.q50 -m-> MID-S.down.q10` | — | tennessee_eastman |
| hvac_kw_S:upq80 | m | Tsp_c:upq20 | 2.324 | 2.336 | 59 | False | `MID-S.up.q80 -m-> SET.up.q20` | — | hai |
| hvac_kw_S:downq80 | m | rf_spd:upq80 | 2.321 | 1.722 | 239 | False | `MID-S.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rh_out:upq20 | s | ma_t:trough | 2.321 | 1.559 | 22 | False | `SLOW.up.q20 -s-> MID.trough` | — | tennessee_eastman, hai |
| sa_flow:upq80 | m | ma_t:trough | 2.319 | 1.958 | 92 | True | `SLOW.up.q80 -m-> MID.trough` | — | tennessee_eastman, hai |
| sa_flow:upq50 | m | plenum_p:upq50 | 2.317 | 2.337 | 540 | True | `SLOW.up.q50 -m-> MID.up.q50` | — | tennessee_eastman, hai |
| plenum_p:upq80 | m | oa_flow:downq50 | 2.311 | 1.903 | 234 | False | `MID.up.q80 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| sa_flow:upq50 | m | plenum_p:downq80 | 2.309 | 1.947 | 470 | True | `SLOW.up.q50 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| plenum_p:downq80 | l | sf_spd:downq50 | 2.308 | 1.665 | 468 | False | `MID.down.q80 -l-> SLOW.down.q50` | — | tennessee_eastman, hai |
| plenum_p:upq80 | m | rf_spd:downq50 | 2.304 | 1.536 | 578 | False | `MID.up.q80 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| T:upq20 | m | hw_valve:downq10 | 2.303 | 2.194 | 1019 | True | `MID.up.q20 -m-> MID-S.down.q10` | — | tennessee_eastman, hai |
| Tsp_c:upq50 | s | T:downq20 | 2.298 | 4.595 | 6 | False | `SET.up.q50 -s-> MID.down.q20` | — | hai |
| T:upq20 | m | T:upq20 | 2.294 | 1.869 | 1944 | True | `MID.up.q20 -m-> MID.up.q20 [same role]` | — | tennessee_eastman, hai |
| plenum_p:downq80 | l | rf_spd:upq50 | 2.293 | 1.577 | 755 | False | `MID.down.q80 -l-> SLOW.up.q50` | — | tennessee_eastman, hai |
| hvac_kw_N:downq90 | l | sf_spd:downq80 | 2.292 | 1.896 | 145 | False | `SLOW-S.down.q90 -l-> SLOW.down.q80` | — | tennessee_eastman |
| hw_valve:downq90 | m | T:downq20 | 2.277 | 2.121 | 979 | True | `MID-S.down.q90 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| hvac_kw_S:upq80 | s | sa_flow:upq80 | 2.273 | 2.68 | 45 | False | `MID-S.up.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| T_out:upq80 | s | hw_valve:downq10 | 2.267 | 2.744 | 78 | False | `MID.up.q80 -s-> MID-S.down.q10` | — | tennessee_eastman, hai |
| hvac_kw_N:downq90 | m | rf_spd:upq80 | 2.266 | 2.286 | 138 | False | `SLOW-S.down.q90 -m-> SLOW.up.q80` | — | tennessee_eastman |
| T:upq20 | l | Tsp_c:downq50 | 2.258 | 1.994 | 25 | True | `MID.up.q20 -l-> SET.down.q50` | — | hai |
| T_out:downq80 | s | T:downq80 | 2.255 | 2.606 | 82 | False | `MID.down.q80 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| plenum_p:downq80 | l | ma_t:trough | 2.252 | 1.611 | 266 | False | `MID.down.q80 -l-> MID.trough` | — | tennessee_eastman, hai |
| plenum_p:upq80 | m | sf_spd:upq50 | 2.249 | 1.646 | 351 | False | `MID.up.q80 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| T:upq50 | s | T:upq80 | 2.246 | 2.146 | 369 | True | `MID.up.q50 -s-> MID.up.q80 [same role]` | tennessee_eastman, hai | — |
| T_out:downq80 | l | Tsp_c:upq80 | 2.245 | 1.543 | 96 | False | `MID.down.q80 -l-> SET.up.q80` | — | hai |
| rh_out:upq20 | s | sa_t:downq50 | 2.241 | 1.505 | 11 | False | `SLOW.up.q20 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| hvac_kw_N:downq10 | m | sa_flow:downq20 | 2.227 | 1.624 | 121 | False | `SLOW-S.down.q10 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| sa_flow:downq50 | m | plenum_p:downq50 | 2.217 | 2.33 | 498 | True | `SLOW.down.q50 -m-> MID.down.q50` | — | tennessee_eastman, hai |
| sf_spd:upq50 | m | plenum_p:upq50 | 2.211 | 2.132 | 513 | True | `SLOW.up.q50 -m-> MID.up.q50` | — | tennessee_eastman, hai |
| rh_out:upq20 | s | rf_spd:downq80 | 2.21 | 1.583 | 28 | False | `SLOW.up.q20 -s-> SLOW.down.q80` | — | tennessee_eastman, hai |
| T_out:upq80 | m | sa_t:downq20 | 2.208 | 3.632 | 53 | False | `MID.up.q80 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| hw_valve:upq10 | m | hw_valve:downq10 | 2.193 | 2.184 | 558 | True | `MID-S.up.q10 -m-> MID-S.down.q10 [same role]` | — | tennessee_eastman, hai, fingrid |
| rh_out:downq50 | s | oa_damper:upq90 | 2.183 | 5.87 | 14 | False | `SLOW.down.q50 -s-> MID-S.up.q90` | — | tennessee_eastman, hai |
| sf_spd:upq50 | m | plenum_p:downq80 | 2.181 | 2.022 | 442 | True | `SLOW.up.q50 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| rh_out:downq20 | l | oa_damper:upq10 | 2.174 | 3.003 | 90 | False | `SLOW.down.q20 -l-> MID-S.up.q10` | — | tennessee_eastman, hai |
| T:downq50 | l | T:upq20 | 2.168 | 1.909 | 3869 | True | `MID.down.q50 -l-> MID.up.q20 [same role]` | — | tennessee_eastman, hai |
| sf_spd:downq50 | m | plenum_p:upq80 | 2.168 | 2.067 | 422 | True | `SLOW.down.q50 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| T:downq50 | l | T:downq20 | 2.167 | 1.661 | 3849 | True | `MID.down.q50 -l-> MID.down.q20 [same role]` | — | tennessee_eastman, hai |
| T:downq80 | l | T:downq20 | 2.166 | 1.976 | 2799 | True | `MID.down.q80 -l-> MID.down.q20 [same role]` | — | tennessee_eastman, hai |
| T_out:upq80 | l | fan:upq90 | 2.15 | 2.388 | 127 | False | `MID.up.q80 -l-> SET.up.q90` | — | tennessee_eastman, hai |
| T_out:upq80 | m | hw_valve:downq10 | 2.146 | 2.307 | 317 | False | `MID.up.q80 -m-> MID-S.down.q10` | — | tennessee_eastman, hai |
| fan:upq90 | l | T:downq50 | 2.141 | 2.302 | 378 | True | `SET.up.q90 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| T_out:downq80 | m | sa_flow:downq80 | 2.141 | 1.982 | 63 | False | `MID.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| T_out:upq80 | l | oa_damper:upq90 | 2.14 | 2.771 | 107 | False | `MID.up.q80 -l-> MID-S.up.q90` | — | tennessee_eastman, hai |
| T_out:downq80 | m | sf_spd:downq80 | 2.139 | 1.862 | 49 | False | `MID.down.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rh_out:upq20 | m | T:downq80 | 2.136 | 2.123 | 520 | True | `SLOW.up.q20 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| rh_out:downq50 | m | oa_damper:upq90 | 2.136 | 6.421 | 59 | False | `SLOW.down.q50 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| hw_valve:downq10 | s | T:downq50 | 2.135 | 2.067 | 174 | True | `MID-S.down.q10 -s-> MID.down.q50` | tennessee_eastman | hai |
| T:upq50 | m | hw_valve:upq90 | 2.134 | 1.98 | 465 | True | `MID.up.q50 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| hvac_kw_S:downq80 | m | oa_flow:downq80 | 2.134 | 4.126 | 133 | False | `MID-S.down.q80 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| T_out:upq80 | l | oa_flow:downq80 | 2.129 | 2.187 | 244 | False | `MID.up.q80 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| hw_valve:upq90 | l | T:upq50 | 2.128 | 2.241 | 1127 | False | `MID-S.up.q90 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| T_out:upq80 | l | rf_spd:upq80 | 2.128 | 1.688 | 403 | False | `MID.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rh_out:downq20 | m | oa_t:peak | 2.126 | 2.045 | 80 | False | `SLOW.down.q20 -m-> MID.peak` | — | tennessee_eastman, hai |
| hvac_kw_S:upq80 | m | oa_damper:upq90 | 2.124 | 3.769 | 59 | False | `MID-S.up.q80 -m-> MID-S.up.q90` | — | tennessee_eastman, hai |
| hvac_kw_S:upq80 | m | oa_damper:upq10 | 2.123 | 2.738 | 45 | False | `MID-S.up.q80 -m-> MID-S.up.q10` | — | tennessee_eastman, hai |
| T:upq20 | m | T:upq50 | 2.116 | 2.392 | 2120 | True | `MID.up.q20 -m-> MID.up.q50 [same role]` | — | tennessee_eastman, hai |
| T:downq50 | m | hw_valve:downq90 | 2.112 | 2.017 | 517 | True | `MID.down.q50 -m-> MID-S.down.q90` | — | tennessee_eastman, hai |
| hvac_kw_S:upq50 | s | sf_spd:upq50 | 2.108 | 2.913 | 357 | False | `MID-S.up.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| hvac_kw_S:downq20 | s | rf_spd:upq20 | 2.107 | 1.555 | 161 | False | `MID-S.down.q20 -s-> SLOW.up.q20` | — | tennessee_eastman, hai |
| rh_out:downq20 | l | sa_flow:downq80 | 2.088 | 1.696 | 327 | False | `SLOW.down.q20 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| Tsp_h:downq20 | s | T:downq20 | 2.085 | 1.969 | 18 | True | `SET.down.q20 -s-> MID.down.q20` | — | tennessee_eastman, hai |
| T_out:upq80 | l | fan:downq10 | 2.072 | 1.697 | 435 | False | `MID.up.q80 -l-> SET.down.q10` | — | tennessee_eastman, hai |
| T_out:upq80 | l | sa_t:downq20 | 2.065 | 4.749 | 229 | False | `MID.up.q80 -l-> MID.down.q20` | — | tennessee_eastman, hai |
| sf_spd:upq50 | m | plenum_p:upq80 | 2.064 | 1.936 | 419 | True | `SLOW.up.q50 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| hvac_kw_N:upq10 | s | plenum_p:upq20 | 2.06 | 1.947 | 83 | False | `SLOW-S.up.q10 -s-> MID.up.q20` | — | tennessee_eastman, hai |
| rh_out:downq20 | m | oa_flow:upq80 | 2.06 | 2.064 | 73 | False | `SLOW.down.q20 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| rh_out:downq20 | s | ma_t:peak | 2.06 | 2.546 | 20 | False | `SLOW.down.q20 -s-> MID.peak` | — | tennessee_eastman, hai |
| T_out:upq80 | l | rf_spd:downq80 | 2.054 | 1.527 | 389 | False | `MID.up.q80 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| Tsp_h:downq20 | s | T:downq50 | 2.053 | 2.77 | 21 | True | `SET.down.q20 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| hvac_kw_S:downq80 | m | T:downq80 | 2.046 | 1.839 | 950 | True | `MID-S.down.q80 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| hvac_kw_S:downq50 | s | rf_spd:downq50 | 2.041 | 1.782 | 566 | False | `MID-S.down.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, hai |
| hvac_kw_N:upq10 | m | rf_spd:upq20 | 2.028 | 2.279 | 137 | False | `SLOW-S.up.q10 -m-> SLOW.up.q20` | — | tennessee_eastman, hai |
| T:upq50 | m | T:upq50 | 2.023 | 1.619 | 1919 | True | `MID.up.q50 -m-> MID.up.q50 [same role]` | — | tennessee_eastman, hai |
| rh_out:downq20 | m | rf_spd:upq80 | 2.017 | 2.375 | 121 | False | `SLOW.down.q20 -m-> SLOW.up.q80` | — | tennessee_eastman, hai |
| Tsp_c:upq80 | s | T:downq50 | 2.012 | 3.368 | 32 | True | `SET.up.q80 -s-> MID.down.q50` | — | hai |
| hw_valve:downq10 | l | T:downq50 | 2.01 | 1.809 | 3348 | True | `MID-S.down.q10 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| rh_out:downq20 | l | sf_spd:downq80 | 2.01 | 1.937 | 245 | False | `SLOW.down.q20 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| hw_valve:upq90 | l | hw_valve:downq10 | 2.009 | 2.398 | 470 | False | `MID-S.up.q90 -l-> MID-S.down.q10 [same role]` | fingrid | tennessee_eastman, hai |
| rh_out:upq50 | m | T:downq80 | 2.008 | 3.048 | 984 | True | `SLOW.up.q50 -m-> MID.down.q80` | — | tennessee_eastman, hai |
| fan:downq10 | s | T:downq50 | 2.001 | 4.247 | 59 | False | `SET.down.q10 -s-> MID.down.q50` | — | tennessee_eastman, hai |
| rh_out:downq20 | l | rf_spd:downq80 | 2.0 | 1.889 | 411 | False | `SLOW.down.q20 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rh_out:upq50 | s | sa_t:upq20 | 1.991 | 7.924 | 26 | False | `SLOW.up.q50 -s-> MID.up.q20` | — | tennessee_eastman, hai |
| fan:upq10 | l | T:downq50 | 1.972 | 1.901 | 905 | True | `SET.up.q10 -l-> MID.down.q50` | — | tennessee_eastman, hai |
| fan:upq10 | l | T:downq20 | 1.972 | 1.729 | 764 | True | `SET.up.q10 -l-> MID.down.q20` | — | tennessee_eastman, hai |
| T_out:upq50 | m | T:upq50 | 1.969 | 1.864 | 1442 | True | `MID.up.q50 -m-> MID.up.q50` | — | tennessee_eastman |
| T:downq20 | s | hw_valve:upq10 | 1.966 | 2.589 | 241 | True | `MID.down.q20 -s-> MID-S.up.q10` | — | tennessee_eastman, hai |
| T_out:upq50 | l | oa_damper:downq90 | 1.958 | 4.564 | 218 | False | `MID.up.q50 -l-> MID-S.down.q90` | — | tennessee_eastman |
| hw_valve:downq90 | l | T:upq50 | 1.948 | 2.125 | 1144 | False | `MID-S.down.q90 -l-> MID.up.q50` | — | tennessee_eastman, hai |
| rh_out:upq20 | l | rf_spd:downq80 | 1.936 | 1.946 | 383 | False | `SLOW.up.q20 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| T_out:upq80 | l | sf_spd:upq80 | 1.929 | 1.899 | 216 | False | `MID.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| T_out:upq80 | l | T:downq80 | 1.928 | 1.625 | 1646 | True | `MID.up.q80 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| rh_out:downq20 | s | T:upq80 | 1.925 | 2.125 | 113 | False | `SLOW.down.q20 -s-> MID.up.q80` | hai | tennessee_eastman |
| hvac_kw_S:upq50 | s | sa_flow:upq50 | 1.923 | 2.594 | 351 | False | `MID-S.up.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, hai |
| rh_out:upq50 | m | fan:downq10 | 1.916 | 3.323 | 231 | False | `SLOW.up.q50 -m-> SET.down.q10` | — | tennessee_eastman, hai |
| T_out:upq80 | s | T:upq50 | 1.913 | 1.686 | 149 | False | `MID.up.q80 -s-> MID.up.q50` | — | tennessee_eastman, hai |
| hvac_kw_N:upq90 | m | rf_spd:downq80 | 1.911 | 1.927 | 122 | False | `SLOW-S.up.q90 -m-> SLOW.down.q80` | — | tennessee_eastman |
| rh_out:downq20 | m | sa_flow:downq80 | 1.903 | 1.986 | 87 | False | `SLOW.down.q20 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rh_out:upq20 | l | sa_flow:downq80 | 1.898 | 1.626 | 286 | False | `SLOW.up.q20 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rh_out:downq50 | s | T:upq50 | 1.891 | 1.587 | 375 | False | `SLOW.down.q50 -s-> MID.up.q50` | hai | tennessee_eastman |
| T_out:upq50 | l | oa_damper:upq90 | 1.878 | 4.535 | 209 | False | `MID.up.q50 -l-> MID-S.up.q90` | — | tennessee_eastman |
| hvac_kw_S:upq80 | l | oa_damper:upq10 | 1.861 | 3.394 | 104 | False | `MID-S.up.q80 -l-> MID-S.up.q10` | — | tennessee_eastman, hai |
| hvac_kw_S:downq80 | s | rf_spd:upq80 | 1.856 | 1.658 | 54 | False | `MID-S.down.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, hai |
| T_out:upq80 | l | sa_flow:upq80 | 1.853 | 1.602 | 267 | False | `MID.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| T_out:upq50 | l | oa_flow:downq80 | 1.846 | 2.103 | 471 | False | `MID.up.q50 -l-> MID.down.q80` | — | tennessee_eastman |
| T_out:upq80 | l | sf_spd:downq80 | 1.835 | 1.826 | 206 | False | `MID.up.q80 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rh_out:downq20 | m | T:upq80 | 1.828 | 2.418 | 495 | True | `SLOW.down.q20 -m-> MID.up.q80` | — | tennessee_eastman, hai |
| T:upq50 | m | fan:upq10 | 1.82 | 3.263 | 236 | True | `MID.up.q50 -m-> SET.up.q10` | — | tennessee_eastman, hai |
| rh_out:downq50 | l | Tsp_c:downq50 | 1.813 | 1.748 | 46 | False | `SLOW.down.q50 -l-> SET.down.q50` | — | hai |
| T_out:downq50 | m | hw_valve:upq10 | 1.805 | 1.618 | 622 | True | `MID.down.q50 -m-> MID-S.up.q10` | — | tennessee_eastman |
| hvac_kw_N:downq10 | m | rf_spd:downq20 | 1.8 | 1.78 | 124 | False | `SLOW-S.down.q10 -m-> SLOW.down.q20` | — | tennessee_eastman, hai |
| rh_out:downq20 | m | sf_spd:downq80 | 1.799 | 1.737 | 64 | False | `SLOW.down.q20 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| T:upq20 | l | T:upq80 | 1.786 | 2.178 | 1744 | True | `MID.up.q20 -l-> MID.up.q80 [same role]` | — | tennessee_eastman, hai |
| T:downq50 | m | Tsp_c:upq20 | 1.781 | 1.957 | 56 | False | `MID.down.q50 -m-> SET.up.q20` | — | hai |
| rh_out:downq20 | l | sf_spd:upq80 | 1.777 | 1.729 | 216 | False | `SLOW.down.q20 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| Tsp_c:upq20 | s | T:downq50 | 1.772 | 3.674 | 23 | True | `SET.up.q20 -s-> MID.down.q50` | — | hai |
| hvac_kw_S:upq20 | s | rf_spd:downq20 | 1.757 | 1.91 | 143 | False | `MID-S.up.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| rh_out:downq20 | l | oa_flow:downq80 | 1.753 | 1.769 | 218 | False | `SLOW.down.q20 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| T_out:upq50 | l | fan:upq90 | 1.749 | 1.907 | 230 | False | `MID.up.q50 -l-> SET.up.q90` | — | tennessee_eastman |
| rh_out:downq50 | l | Tsp_c:downq20 | 1.743 | 1.883 | 212 | False | `SLOW.down.q50 -l-> SET.down.q20` | — | hai |
| hvac_kw_S:upq80 | l | rf_spd:downq80 | 1.716 | 1.673 | 476 | False | `MID-S.up.q80 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rh_out:downq20 | l | fan:downq10 | 1.716 | 1.923 | 391 | False | `SLOW.down.q20 -l-> SET.down.q10` | — | tennessee_eastman, hai |
| hvac_kw_S:upq80 | l | rf_spd:upq80 | 1.712 | 1.815 | 475 | False | `MID-S.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rh_out:upq20 | m | ma_t:trough | 1.708 | 1.846 | 69 | False | `SLOW.up.q20 -m-> MID.trough` | — | tennessee_eastman, hai |
| hvac_kw_S:upq20 | s | sf_spd:downq20 | 1.697 | 1.514 | 115 | False | `MID-S.up.q20 -s-> SLOW.down.q20` | — | tennessee_eastman, hai |
| rh_out:downq80 | m | hw_valve:downq10 | 1.685 | 2.525 | 517 | True | `SLOW.down.q80 -m-> MID-S.down.q10` | — | tennessee_eastman, hai |
| T:downq20 | m | Tsp_c:downq20 | 1.68 | 1.706 | 47 | True | `MID.down.q20 -m-> SET.down.q20` | — | hai |
| hw_valve:downq90 | l | T:upq80 | 1.663 | 2.239 | 540 | False | `MID-S.down.q90 -l-> MID.up.q80` | — | tennessee_eastman, hai |
| hvac_kw_S:downq50 | m | sa_flow:upq50 | 1.657 | 1.798 | 1111 | False | `MID-S.down.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| hvac_kw_S:downq50 | m | sf_spd:upq50 | 1.656 | 2.075 | 1030 | False | `MID-S.down.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, hai |
| hvac_kw_S:upq80 | l | sa_flow:upq80 | 1.639 | 1.619 | 346 | False | `MID-S.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rh_out:downq20 | l | T:downq80 | 1.634 | 1.604 | 1514 | True | `SLOW.down.q20 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| rh_out:downq20 | m | rf_spd:downq80 | 1.633 | 1.829 | 98 | False | `SLOW.down.q20 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| rh_out:upq50 | l | Tsp_c:upq80 | 1.625 | 1.782 | 168 | False | `SLOW.up.q50 -l-> SET.up.q80` | — | hai |
| hvac_kw_N:upq90 | m | oa_t:peak | 1.599 | 1.641 | 64 | False | `SLOW-S.up.q90 -m-> MID.peak` | — | tennessee_eastman |
| hvac_kw_S:upq50 | m | sa_flow:downq50 | 1.594 | 1.817 | 1060 | False | `MID-S.up.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| hvac_kw_S:upq50 | m | sf_spd:downq50 | 1.592 | 2.092 | 976 | False | `MID-S.up.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, hai |
| hvac_kw_S:downq80 | s | T:downq80 | 1.579 | 1.805 | 207 | False | `MID-S.down.q80 -s-> MID.down.q80` | — | tennessee_eastman, hai |
| T:downq20 | m | hw_valve:upq10 | 1.577 | 1.887 | 644 | True | `MID.down.q20 -m-> MID-S.up.q10` | — | tennessee_eastman, hai |
| hvac_kw_N:downq90 | l | rf_spd:upq80 | 1.575 | 1.953 | 168 | False | `SLOW-S.down.q90 -l-> SLOW.up.q80` | — | tennessee_eastman |
| T:downq50 | m | Tsp_c:upq50 | 1.575 | 1.571 | 10 | False | `MID.down.q50 -m-> SET.up.q50` | — | hai |
| hvac_kw_S:upq80 | l | sf_spd:upq80 | 1.555 | 1.878 | 255 | False | `MID-S.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman, hai |
| rh_out:downq20 | m | ra_t:peak | 1.552 | 1.915 | 46 | False | `SLOW.down.q20 -m-> MID.peak` | — | tennessee_eastman, hai |
| hvac_kw_S:downq50 | l | oa_damper:downq90 | 1.543 | 3.54 | 178 | False | `MID-S.down.q50 -l-> MID-S.down.q90` | — | tennessee_eastman, hai |
| rh_out:downq50 | l | oa_flow:downq80 | 1.533 | 2.223 | 460 | False | `SLOW.down.q50 -l-> MID.down.q80` | — | tennessee_eastman, hai |
| T_out:downq20 | m | T:downq20 | 1.525 | 1.677 | 756 | True | `MID.down.q20 -m-> MID.down.q20` | — | tennessee_eastman, hai |
| rh_out:upq50 | m | rf_spd:downq80 | 1.517 | 2.024 | 165 | False | `SLOW.up.q50 -m-> SLOW.down.q80` | — | tennessee_eastman, hai |
| hvac_kw_S:downq80 | l | rf_spd:downq80 | 1.511 | 1.653 | 401 | False | `MID-S.down.q80 -l-> SLOW.down.q80` | — | tennessee_eastman, hai |
| hvac_kw_S:upq80 | l | fan:downq90 | 1.502 | 2.292 | 130 | False | `MID-S.up.q80 -l-> SET.down.q90` | — | tennessee_eastman, hai |

## Loops (returns; verdicts recorded, not promoted)

| X | l1 | Y | l2 | X′ | n | cond. lift | timing (g1 / g2) | determinism (p1 / p2) | used |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| oa_damper:downq90 | s | ma_t:peak | s | oa_damper:upq90 | 13 | 12.143 | unresolved (10.0 / 10.0) | X reacts (0.017 / 0.051) | False |
| oa_damper:downq90 | s | sa_t:upq50 | s | oa_damper:upq90 | 6 | 11.768 | unresolved (10.0 / 12.5) | X reacts (0.016 / 0.031) | False |
| oa_damper:upq90 | s | rf_spd:upq50 | m | oa_damper:downq90 | 21 | 10.505 | Y reacts (15.0 / 65.0) | Y reacts (0.043 / 0.023) | False |
| sf_spd:upq80 | s | plenum_p:upq80 | s | sf_spd:downq80 | 31 | 10.234 | Y reacts (10.0 / 15.0) | Y reacts (0.061 / 0.036) | False |
| oa_damper:upq90 | s | rf_spd:downq50 | m | oa_damper:downq90 | 28 | 10.108 | Y reacts (10.0 / 75.0) | Y reacts (0.034 / 0.020) | False |
| sa_t:downq50 | s | oa_damper:downq90 | s | sa_t:upq50 | 14 | 9.744 | unresolved (20.0 / 15.0) | unresolved (0.020 / 0.016) | False |
| oa_damper:downq10 | m | sa_flow:downq80 | s | oa_damper:upq10 | 7 | 9.468 | X reacts (67.5 / 15.0) | Y reacts (0.025 / 0.012) | False |
| oa_damper:upq90 | s | ra_t:peak | m | oa_damper:downq90 | 13 | 8.478 | Y reacts (10.0 / 90.0) | X reacts (0.010 / 0.031) | False |
| fan:upq10 | l | T:downq50 | s | fan:downq10 | 34 | 8.181 | X reacts (375.0 / 20.0) | Y reacts (0.163 / 0.082) | False |
| oa_damper:upq90 | s | ra_t:peak | s | oa_damper:downq90 | 4 | 8.071 | X reacts (10.0 / 5.0) | X reacts (0.010 / 0.037) | False |
| oa_damper:upq90 | m | ma_t:trough | s | oa_damper:downq90 | 13 | 7.775 | X reacts (80.0 / 5.0) | X reacts (0.018 / 0.061) | False |
| fan:upq90 | l | T:downq80 | s | fan:downq90 | 62 | 7.657 | X reacts (305.0 / 15.0) | unresolved (0.192 / 0.133) | False |
| sa_t:downq50 | s | oa_flow:downq80 | m | sa_t:upq50 | 16 | 7.523 | Y reacts (15.0 / 65.0) | unresolved (0.014 / 0.012) | False |
| sa_t:upq50 | s | oa_damper:upq90 | s | sa_t:downq50 | 3 | 7.476 | X reacts (10.0 / 5.0) | Y reacts (0.031 / 0.008) | False |
| hw_valve:downq10 | s | T:downq20 | s | hw_valve:upq10 | 22 | 7.218 | unresolved (15.0 / 15.0) | Y reacts (0.171 / 0.098) | False |
| oa_damper:upq90 | s | oa_flow:downq80 | s | oa_damper:downq90 | 3 | 7.188 | X reacts (10.0 / 5.0) | unresolved (0.031 / 0.022) | False |
| oa_damper:upq90 | s | sa_t:upq50 | m | oa_damper:downq90 | 13 | 6.944 | Y reacts (22.5 / 85.0) | X reacts (0.009 / 0.026) | False |
| rf_spd:upq80 | s | plenum_p:upq80 | s | rf_spd:downq80 | 55 | 6.641 | X reacts (15.0 / 10.0) | unresolved (0.058 / 0.039) | False |
| oa_flow:downq20 | s | sa_flow:upq20 | m | oa_flow:upq20 | 19 | 6.491 | unresolved (25.0 / 35.0) | unresolved (0.013 / 0.017) | False |
| oa_damper:upq10 | s | oa_flow:upq80 | s | oa_damper:downq90 | 9 | 6.481 | Y reacts (5.0 / 15.0) | Y reacts (0.062 / 0.025) | False |
| sa_t:downq20 | s | oa_flow:downq80 | s | sa_t:upq20 | 20 | 6.477 | unresolved (10.0 / 10.0) | X reacts (0.035 / 0.067) | False |
| sa_flow:upq80 | s | plenum_p:upq80 | s | sa_flow:downq80 | 31 | 6.458 | X reacts (15.0 / 10.0) | Y reacts (0.065 / 0.036) | False |
| oa_damper:upq90 | s | sa_t:downq50 | s | oa_damper:downq90 | 5 | 5.966 | Y reacts (5.0 / 20.0) | X reacts (0.008 / 0.020) | False |
| oa_damper:upq90 | m | ra_t:peak | s | oa_damper:downq90 | 8 | 5.947 | X reacts (97.5 / 20.0) | X reacts (0.010 / 0.037) | False |
| oa_damper:downq10 | s | oa_t:peak | m | oa_damper:upq10 | 19 | 5.884 | Y reacts (10.0 / 55.0) | unresolved (0.030 / 0.034) | False |
| oa_damper:upq90 | m | rf_spd:upq50 | m | oa_damper:downq90 | 44 | 5.777 | unresolved (85.0 / 70.0) | Y reacts (0.035 / 0.023) | False |
| oa_damper:upq90 | m | sf_spd:upq80 | m | oa_damper:downq90 | 25 | 5.346 | unresolved (75.0 / 70.0) | unresolved (0.021 / 0.023) | False |
| fan:upq10 | l | T:downq80 | m | fan:downq10 | 225 | 5.212 | X reacts (285.0 / 65.0) | unresolved (0.150 / 0.109) | False |
| sa_t:downq20 | s | oa_damper:upq90 | s | sa_t:upq20 | 16 | 5.185 | Y reacts (5.0 / 15.0) | X reacts (0.028 / 0.087) | False |
| rf_spd:upq80 | s | oa_flow:downq80 | s | rf_spd:downq80 | 14 | 5.178 | Y reacts (10.0 / 15.0) | unresolved (0.025 / 0.030) | False |
| oa_damper:downq10 | m | rf_spd:upq80 | m | oa_damper:upq10 | 9 | 4.858 | unresolved (80.0 / 65.0) | Y reacts (0.033 / 0.017) | False |
| sf_spd:upq80 | s | oa_flow:downq80 | s | sf_spd:downq80 | 14 | 4.747 | unresolved (10.0 / 10.0) | X reacts (0.023 / 0.034) | False |
| plenum_p:upq80 | s | sa_flow:downq50 | s | plenum_p:downq80 | 71 | 4.706 | Y reacts (10.0 / 15.0) | X reacts (0.037 / 0.057) | False |
| rf_spd:downq20 | s | plenum_p:downq20 | s | rf_spd:upq20 | 41 | 4.655 | X reacts (15.0 / 10.0) | Y reacts (0.033 / 0.021) | False |
| oa_damper:downq10 | m | ma_t:peak | m | oa_damper:upq10 | 23 | 4.639 | unresolved (85.0 / 75.0) | X reacts (0.020 / 0.031) | False |
| oa_damper:downq10 | s | ma_t:peak | s | oa_damper:upq10 | 12 | 4.613 | X reacts (15.0 / 5.0) | X reacts (0.023 / 0.046) | False |
| sf_spd:upq80 | m | ma_t:trough | m | sf_spd:downq80 | 53 | 4.575 | unresolved (65.0 / 75.0) | X reacts (0.013 / 0.030) | False |
| hw_valve:upq90 | s | Tsp_c:downq20 | s | hw_valve:downq90 | 3 | 4.571 | Y reacts (5.0 / 10.0) | X reacts (0.006 / 0.091) | False |
| oa_damper:upq90 | s | oa_flow:upq80 | s | oa_damper:downq90 | 3 | 4.567 | Y reacts (10.0 / 20.0) | unresolved (0.036 / 0.025) | False |
| oa_damper:upq90 | s | sa_t:upq20 | m | oa_damper:downq10 | 8 | 4.47 | Y reacts (15.0 / 75.0) | Y reacts (0.087 / 0.011) | False |
| sa_t:downq50 | s | oa_damper:upq90 | m | sa_t:upq50 | 9 | 4.355 | Y reacts (5.0 / 65.0) | Y reacts (0.033 / 0.014) | False |
| sa_t:downq50 | m | rf_spd:downq80 | s | sa_t:upq50 | 14 | 4.344 | X reacts (85.0 / 12.5) | Y reacts (0.037 / 0.011) | False |
| fan:upq10 | l | T:downq80 | s | fan:downq10 | 97 | 4.313 | X reacts (250.0 / 15.0) | X reacts (0.150 / 0.239) | False |
| oa_damper:downq10 | m | ma_t:peak | s | oa_damper:upq10 | 18 | 4.292 | X reacts (50.0 / 10.0) | X reacts (0.020 / 0.046) | False |
| sa_flow:downq20 | s | plenum_p:upq20 | s | sa_flow:upq20 | 21 | 4.28 | X reacts (20.0 / 5.0) | Y reacts (0.035 / 0.019) | False |
| oa_damper:downq10 | m | oa_t:peak | m | oa_damper:upq10 | 27 | 4.266 | unresolved (85.0 / 105.0) | unresolved (0.023 / 0.034) | False |
| plenum_p:upq80 | s | sf_spd:downq80 | s | plenum_p:downq80 | 28 | 4.263 | unresolved (10.0 / 10.0) | X reacts (0.036 / 0.069) | False |
| oa_damper:upq90 | m | ra_t:peak | s | oa_damper:downq10 | 4 | 4.163 | X reacts (105.0 / 15.0) | X reacts (0.010 / 0.027) | False |
| sa_flow:upq80 | s | plenum_p:upq80 | m | sa_flow:downq80 | 51 | 4.135 | Y reacts (15.0 / 70.0) | Y reacts (0.065 / 0.024) | False |
| sa_t:downq20 | s | oa_damper:downq90 | s | sa_t:upq20 | 17 | 4.083 | X reacts (15.0 / 10.0) | X reacts (0.041 / 0.073) | False |
| sa_flow:upq50 | s | plenum_p:upq80 | s | sa_flow:downq50 | 62 | 4.043 | X reacts (15.0 / 10.0) | unresolved (0.046 / 0.037) | False |
| sa_t:downq50 | s | oa_damper:downq90 | m | sa_t:upq50 | 17 | 3.997 | Y reacts (17.5 / 97.5) | unresolved (0.020 / 0.015) | False |
| sa_flow:downq20 | s | plenum_p:downq20 | s | sa_flow:upq20 | 41 | 3.971 | X reacts (12.5 / 5.0) | Y reacts (0.050 / 0.029) | False |
| plenum_p:upq80 | s | sf_spd:downq50 | s | plenum_p:downq80 | 76 | 3.924 | unresolved (10.0 / 10.0) | X reacts (0.034 / 0.065) | False |
| sa_t:downq50 | m | oa_flow:downq80 | s | sa_t:upq50 | 12 | 3.906 | X reacts (65.0 / 10.0) | Y reacts (0.027 / 0.011) | False |
| oa_flow:downq50 | s | ma_t:peak | s | oa_flow:upq50 | 13 | 3.903 | Y reacts (10.0 / 15.0) | X reacts (0.013 / 0.035) | False |
| sa_flow:downq50 | s | plenum_p:downq50 | s | sa_flow:upq50 | 78 | 3.876 | unresolved (10.0 / 10.0) | Y reacts (0.073 / 0.040) | False |
| sf_spd:upq50 | s | plenum_p:upq50 | s | sf_spd:downq50 | 61 | 3.848 | unresolved (10.0 / 10.0) | Y reacts (0.076 / 0.036) | False |
| oa_damper:upq90 | s | sa_t:downq20 | s | oa_damper:downq90 | 8 | 3.818 | unresolved (10.0 / 10.0) | Y reacts (0.071 / 0.041) | False |
| plenum_p:downq80 | s | rf_spd:upq50 | s | plenum_p:upq80 | 72 | 3.754 | X reacts (15.0 / 10.0) | unresolved (0.040 / 0.045) | False |
| sf_spd:downq50 | s | plenum_p:downq50 | s | sf_spd:upq50 | 62 | 3.736 | unresolved (10.0 / 10.0) | Y reacts (0.069 / 0.036) | False |
| rf_spd:downq20 | s | plenum_p:upq20 | s | rf_spd:upq20 | 24 | 3.717 | Y reacts (12.5 / 20.0) | unresolved (0.023 / 0.021) | False |
| sf_spd:upq80 | s | rf_spd:upq80 | s | sf_spd:downq80 | 27 | 3.699 | Y reacts (10.0 / 15.0) | Y reacts (0.068 / 0.045) | False |
| sf_spd:downq20 | s | plenum_p:downq20 | s | sf_spd:upq20 | 46 | 3.694 | X reacts (15.0 / 5.0) | Y reacts (0.050 / 0.023) | False |
| sa_t:downq50 | m | oa_damper:upq10 | m | sa_t:upq50 | 13 | 3.662 | unresolved (55.0 / 77.5) | unresolved (0.021 / 0.015) | False |
| sa_t:downq50 | m | oa_flow:downq80 | m | sa_t:upq50 | 21 | 3.661 | unresolved (62.5 / 80.0) | Y reacts (0.027 / 0.012) | False |
| rf_spd:downq80 | s | oa_flow:downq80 | s | rf_spd:upq80 | 8 | 3.648 | Y reacts (10.0 / 15.0) | unresolved (0.029 / 0.031) | False |
| sa_flow:upq50 | s | plenum_p:upq50 | s | sa_flow:downq50 | 74 | 3.609 | unresolved (10.0 / 10.0) | Y reacts (0.082 / 0.039) | False |
| oa_damper:upq10 | m | ma_t:trough | s | oa_damper:downq90 | 5 | 3.608 | X reacts (90.0 / 5.0) | X reacts (0.028 / 0.061) | False |
| sa_t:upq50 | m | oa_damper:downq90 | m | sa_t:downq50 | 22 | 3.575 | unresolved (70.0 / 95.0) | Y reacts (0.026 / 0.015) | False |
| sf_spd:upq50 | s | plenum_p:upq80 | s | sf_spd:downq50 | 52 | 3.568 | unresolved (10.0 / 10.0) | unresolved (0.050 / 0.034) | False |
| sf_spd:upq80 | s | rf_spd:downq80 | s | sf_spd:downq80 | 18 | 3.548 | X reacts (20.0 / 10.0) | unresolved (0.051 / 0.042) | False |
| oa_damper:upq10 | s | ra_t:peak | m | oa_damper:downq90 | 6 | 3.525 | Y reacts (5.0 / 100.0) | X reacts (0.017 / 0.031) | False |
| oa_damper:upq90 | s | sa_t:upq20 | m | oa_damper:downq90 | 18 | 3.514 | Y reacts (15.0 / 75.0) | Y reacts (0.087 / 0.023) | False |
| plenum_p:downq20 | s | rf_spd:downq20 | s | plenum_p:upq20 | 37 | 3.512 | unresolved (10.0 / 10.0) | unresolved (0.020 / 0.023) | False |
| oa_damper:upq90 | m | sa_t:downq20 | s | oa_damper:downq90 | 26 | 3.512 | X reacts (70.0 / 15.0) | Y reacts (0.067 / 0.041) | False |
| sa_flow:upq80 | m | ma_t:trough | m | sa_flow:downq80 | 43 | 3.506 | unresolved (80.0 / 65.0) | X reacts (0.015 / 0.034) | False |
| oa_damper:downq10 | m | sa_t:downq50 | s | oa_damper:upq10 | 4 | 3.486 | X reacts (62.5 / 5.0) | unresolved (0.021 / 0.030) | False |
| sa_flow:downq80 | s | oa_damper:upq10 | m | sa_flow:upq80 | 12 | 3.478 | Y reacts (10.0 / 65.0) | X reacts (0.012 / 0.033) | False |
| oa_damper:upq90 | s | oa_flow:upq80 | m | oa_damper:downq90 | 6 | 3.475 | Y reacts (10.0 / 75.0) | unresolved (0.036 / 0.038) | False |
| sa_t:downq50 | m | oa_damper:upq90 | s | sa_t:upq50 | 10 | 3.451 | X reacts (40.0 / 15.0) | Y reacts (0.031 / 0.009) | False |
| rf_spd:downq50 | s | plenum_p:downq50 | s | rf_spd:upq50 | 100 | 3.444 | unresolved (10.0 / 10.0) | unresolved (0.059 / 0.042) | False |
| plenum_p:upq80 | s | rf_spd:downq80 | s | plenum_p:downq80 | 48 | 3.43 | Y reacts (10.0 / 15.0) | X reacts (0.039 / 0.059) | False |
| rf_spd:upq80 | s | plenum_p:upq80 | m | rf_spd:downq80 | 74 | 3.4 | Y reacts (15.0 / 85.0) | Y reacts (0.058 / 0.035) | False |
| oa_damper:upq90 | m | ra_t:peak | m | oa_damper:downq90 | 13 | 3.391 | unresolved (100.0 / 85.0) | X reacts (0.010 / 0.031) | False |
| rf_spd:downq50 | s | plenum_p:downq80 | s | rf_spd:upq50 | 75 | 3.381 | X reacts (15.0 / 10.0) | Y reacts (0.062 / 0.040) | False |
| oa_damper:upq90 | m | oa_flow:downq80 | s | oa_damper:downq90 | 9 | 3.341 | X reacts (95.0 / 10.0) | Y reacts (0.044 / 0.022) | False |
| oa_damper:upq90 | s | sa_t:downq20 | m | oa_damper:downq90 | 11 | 3.34 | Y reacts (10.0 / 62.5) | Y reacts (0.071 / 0.020) | False |
| oa_damper:upq90 | s | sa_t:downq50 | m | oa_damper:downq90 | 3 | 3.333 | Y reacts (5.0 / 85.0) | X reacts (0.008 / 0.029) | False |
| oa_damper:upq90 | s | oa_flow:downq80 | s | oa_damper:downq10 | 3 | 3.286 | X reacts (15.0 / 5.0) | unresolved (0.031 / 0.040) | False |
| oa_damper:upq90 | m | sf_spd:upq80 | s | oa_damper:downq90 | 5 | 3.277 | X reacts (62.5 / 15.0) | unresolved (0.021 / 0.015) | False |
| rf_spd:upq80 | s | sa_flow:upq80 | s | rf_spd:downq80 | 42 | 3.212 | Y reacts (5.0 / 15.0) | unresolved (0.040 / 0.055) | False |
| oa_damper:upq90 | m | sa_t:downq50 | m | oa_damper:downq90 | 13 | 3.187 | unresolved (60.0 / 75.0) | X reacts (0.013 / 0.029) | False |
| plenum_p:upq80 | s | sa_flow:downq80 | s | plenum_p:downq80 | 33 | 3.176 | unresolved (10.0 / 10.0) | X reacts (0.036 / 0.075) | False |
| sa_t:downq50 | m | oa_damper:upq90 | m | sa_t:upq50 | 20 | 3.172 | unresolved (62.5 / 80.0) | Y reacts (0.031 / 0.014) | False |
| sa_flow:upq80 | m | plenum_p:upq80 | s | sa_flow:downq80 | 32 | 3.167 | X reacts (55.0 / 15.0) | unresolved (0.043 / 0.036) | False |
| oa_damper:downq90 | s | sa_t:downq20 | s | oa_damper:upq90 | 3 | 3.116 | X reacts (10.0 / 5.0) | Y reacts (0.050 / 0.028) | False |
| sf_spd:downq80 | s | oa_damper:upq10 | m | sf_spd:upq80 | 9 | 3.104 | Y reacts (15.0 / 50.0) | X reacts (0.011 / 0.024) | False |
| sf_spd:upq50 | s | rf_spd:upq50 | s | sf_spd:downq50 | 57 | 3.094 | Y reacts (10.0 / 17.5) | Y reacts (0.074 / 0.035) | False |
| sa_flow:upq20 | s | plenum_p:upq20 | s | sa_flow:downq20 | 23 | 3.086 | unresolved (17.5 / 12.5) | Y reacts (0.042 / 0.017) | False |
| sa_t:upq50 | m | oa_damper:upq90 | m | sa_t:downq50 | 11 | 3.067 | unresolved (72.5 / 70.0) | Y reacts (0.027 / 0.013) | False |
| sf_spd:upq80 | m | oa_flow:downq80 | m | sf_spd:downq80 | 69 | 3.061 | unresolved (80.0 / 90.0) | unresolved (0.026 / 0.029) | False |
| sf_spd:upq80 | s | oa_flow:downq80 | m | sf_spd:downq80 | 25 | 2.998 | Y reacts (10.0 / 90.0) | unresolved (0.023 / 0.029) | False |
| plenum_p:downq50 | s | rf_spd:upq50 | s | plenum_p:upq50 | 86 | 2.985 | unresolved (10.0 / 10.0) | X reacts (0.042 / 0.066) | False |
| plenum_p:downq50 | s | sa_flow:upq50 | s | plenum_p:upq50 | 72 | 2.942 | unresolved (10.0 / 10.0) | X reacts (0.040 / 0.082) | False |
| sf_spd:downq80 | s | rf_spd:upq80 | s | sf_spd:upq80 | 9 | 2.939 | X reacts (15.0 / 5.0) | unresolved (0.043 / 0.032) | False |
| plenum_p:downq20 | s | sa_flow:downq20 | s | plenum_p:upq20 | 24 | 2.923 | Y reacts (5.0 / 20.0) | unresolved (0.024 / 0.035) | False |
| oa_damper:upq10 | m | oa_flow:upq80 | s | oa_damper:downq90 | 4 | 2.92 | X reacts (80.0 / 20.0) | unresolved (0.020 / 0.025) | False |
| plenum_p:upq50 | s | rf_spd:downq50 | s | plenum_p:downq50 | 103 | 2.914 | Y reacts (10.0 / 15.0) | unresolved (0.044 / 0.059) | False |
| hw_valve:downq90 | s | T:downq50 | m | hw_valve:upq90 | 142 | 2.913 | Y reacts (25.0 / 45.0) | Y reacts (0.245 / 0.049) | False |
| rf_spd:upq50 | s | plenum_p:upq50 | s | rf_spd:downq50 | 83 | 2.907 | unresolved (10.0 / 10.0) | unresolved (0.066 / 0.044) | False |
| rf_spd:downq50 | s | oa_damper:upq90 | s | rf_spd:upq50 | 7 | 2.896 | unresolved (10.0 / 10.0) | X reacts (0.019 / 0.043) | False |
| oa_damper:upq90 | m | sa_t:upq20 | m | oa_damper:downq90 | 37 | 2.871 | unresolved (65.0 / 80.0) | Y reacts (0.062 / 0.023) | False |
| rf_spd:upq80 | s | sf_spd:upq80 | s | rf_spd:downq80 | 17 | 2.854 | Y reacts (10.0 / 15.0) | X reacts (0.032 / 0.051) | False |
| sf_spd:downq20 | s | plenum_p:downq20 | m | sf_spd:upq20 | 75 | 2.791 | Y reacts (5.0 / 75.0) | Y reacts (0.050 / 0.018) | False |
| sf_spd:downq50 | s | rf_spd:upq50 | s | sf_spd:upq50 | 55 | 2.79 | X reacts (15.0 / 10.0) | unresolved (0.056 / 0.050) | False |
| oa_damper:upq90 | m | sa_t:downq20 | m | oa_damper:downq90 | 29 | 2.788 | unresolved (65.0 / 70.0) | Y reacts (0.067 / 0.020) | False |
| oa_damper:upq10 | s | oa_flow:downq80 | s | oa_damper:downq10 | 3 | 2.78 | X reacts (15.0 / 5.0) | unresolved (0.028 / 0.040) | False |
| sa_flow:downq80 | s | rf_spd:downq80 | s | sa_flow:upq80 | 15 | 2.775 | Y reacts (5.0 / 20.0) | Y reacts (0.070 / 0.035) | False |
| rf_spd:downq80 | s | sf_spd:upq80 | s | rf_spd:upq80 | 16 | 2.766 | X reacts (20.0 / 10.0) | X reacts (0.031 / 0.068) | False |
| T:upq50 | s | hw_valve:downq90 | s | T:downq50 | 168 | 2.757 | Y reacts (5.0 / 20.0) | X reacts (0.084 / 0.245) | False |
| sf_spd:upq20 | s | plenum_p:upq20 | s | sf_spd:downq20 | 30 | 2.754 | X reacts (15.0 / 10.0) | Y reacts (0.041 / 0.011) | False |
| sa_flow:upq80 | m | plenum_p:upq80 | m | sa_flow:downq80 | 72 | 2.728 | unresolved (70.0 / 70.0) | Y reacts (0.043 / 0.024) | False |
| oa_damper:upq10 | m | sf_spd:upq80 | s | oa_damper:downq90 | 3 | 2.719 | X reacts (55.0 / 15.0) | Y reacts (0.024 / 0.015) | False |
| sa_flow:downq20 | s | plenum_p:downq20 | m | sa_flow:upq20 | 61 | 2.715 | Y reacts (5.0 / 80.0) | Y reacts (0.050 / 0.016) | False |
| sa_flow:downq20 | s | plenum_p:upq20 | m | sa_flow:upq20 | 23 | 2.699 | Y reacts (25.0 / 55.0) | Y reacts (0.035 / 0.014) | False |
| sf_spd:downq80 | s | rf_spd:downq80 | s | sf_spd:upq80 | 12 | 2.695 | Y reacts (10.0 / 15.0) | Y reacts (0.051 / 0.031) | False |
| plenum_p:downq20 | s | sf_spd:downq20 | s | plenum_p:upq20 | 29 | 2.691 | Y reacts (5.0 / 17.5) | unresolved (0.017 / 0.021) | False |
| rf_spd:upq80 | m | plenum_p:upq80 | m | rf_spd:downq80 | 143 | 2.689 | unresolved (85.0 / 75.0) | unresolved (0.048 / 0.035) | False |
| oa_damper:upq10 | s | sa_t:downq20 | m | oa_damper:downq90 | 5 | 2.671 | Y reacts (15.0 / 65.0) | Y reacts (0.056 / 0.020) | False |
| oa_damper:upq90 | m | sa_t:upq20 | m | oa_damper:downq10 | 12 | 2.665 | unresolved (65.0 / 90.0) | Y reacts (0.062 / 0.011) | False |
| oa_damper:upq10 | m | sa_t:upq20 | m | oa_damper:downq10 | 6 | 2.661 | unresolved (60.0 / 75.0) | Y reacts (0.082 / 0.011) | False |
| rf_spd:downq80 | s | oa_flow:downq80 | m | rf_spd:upq80 | 27 | 2.646 | Y reacts (15.0 / 70.0) | unresolved (0.029 / 0.038) | False |
| oa_damper:upq90 | m | sa_t:upq50 | m | oa_damper:downq90 | 12 | 2.638 | Y reacts (55.0 / 90.0) | X reacts (0.014 / 0.026) | False |
| sa_t:downq50 | m | oa_damper:upq90 | l | sa_t:upq50 | 49 | 2.633 | Y reacts (70.0 / 370.0) | Y reacts (0.031 / 0.015) | False |
| plenum_p:downq50 | s | sf_spd:upq50 | s | plenum_p:upq50 | 65 | 2.625 | unresolved (10.0 / 10.0) | X reacts (0.036 / 0.076) | False |
| plenum_p:downq20 | s | rf_spd:upq20 | s | plenum_p:upq20 | 48 | 2.624 | X reacts (15.0 / 10.0) | unresolved (0.021 / 0.030) | False |
| sf_spd:upq50 | s | rf_spd:downq50 | s | sf_spd:downq50 | 40 | 2.62 | X reacts (15.0 / 10.0) | unresolved (0.051 / 0.047) | False |
| oa_flow:downq20 | m | sa_flow:upq20 | m | oa_flow:upq20 | 23 | 2.614 | unresolved (65.0 / 60.0) | X reacts (0.010 / 0.017) | False |
| oa_flow:downq50 | s | ma_t:peak | s | oa_flow:upq80 | 7 | 2.596 | Y reacts (7.5 / 12.5) | X reacts (0.013 / 0.033) | False |
| oa_damper:upq90 | m | sf_spd:upq80 | s | oa_damper:downq10 | 3 | 2.571 | X reacts (105.0 / 12.5) | unresolved (0.021 / 0.015) | False |
| hw_valve:upq90 | s | T:upq20 | s | hw_valve:downq90 | 462 | 2.569 | Y reacts (5.0 / 20.0) | Y reacts (0.572 / 0.228) | False |
| oa_flow:upq50 | s | oa_damper:upq90 | s | oa_flow:downq80 | 4 | 2.537 | Y reacts (5.0 / 20.0) | Y reacts (0.062 / 0.031) | False |
| hw_valve:downq10 | s | T:downq20 | m | hw_valve:upq90 | 73 | 2.524 | Y reacts (15.0 / 50.0) | Y reacts (0.171 / 0.054) | False |
| oa_damper:downq10 | s | ma_t:peak | s | oa_damper:upq90 | 4 | 2.522 | unresolved (12.5 / 10.0) | X reacts (0.023 / 0.051) | False |
| oa_damper:upq90 | m | sf_spd:upq80 | m | oa_damper:downq10 | 9 | 2.517 | unresolved (70.0 / 80.0) | Y reacts (0.021 / 0.014) | False |
| oa_damper:downq10 | m | sf_spd:upq80 | m | oa_damper:upq10 | 9 | 2.513 | unresolved (80.0 / 75.0) | Y reacts (0.035 / 0.019) | False |
| rf_spd:upq80 | s | oa_flow:downq80 | m | rf_spd:downq80 | 36 | 2.501 | Y reacts (15.0 / 90.0) | X reacts (0.025 / 0.039) | False |
| plenum_p:upq20 | s | sf_spd:downq20 | s | plenum_p:downq20 | 41 | 2.5 | unresolved (10.0 / 12.5) | X reacts (0.011 / 0.050) | False |
| sf_spd:upq80 | s | rf_spd:upq80 | m | sf_spd:downq80 | 48 | 2.491 | Y reacts (15.0 / 60.0) | Y reacts (0.068 / 0.036) | False |
| rf_spd:upq80 | m | plenum_p:downq80 | m | rf_spd:downq80 | 154 | 2.488 | unresolved (80.0 / 80.0) | unresolved (0.051 / 0.036) | False |
| oa_damper:upq10 | m | sa_t:upq20 | m | oa_damper:downq90 | 16 | 2.479 | unresolved (57.5 / 62.5) | Y reacts (0.082 / 0.023) | False |
| oa_flow:upq80 | m | sa_t:downq50 | s | oa_flow:downq80 | 10 | 2.475 | X reacts (90.0 / 15.0) | unresolved (0.012 / 0.014) | False |
| rf_spd:downq80 | s | sf_spd:downq80 | s | rf_spd:upq80 | 14 | 2.461 | Y reacts (5.0 / 15.0) | unresolved (0.042 / 0.043) | False |
| oa_damper:downq90 | m | sf_spd:downq80 | s | oa_damper:upq10 | 4 | 2.459 | X reacts (80.0 / 10.0) | Y reacts (0.026 / 0.011) | False |
| T:upq50 | s | hw_valve:downq10 | s | T:downq50 | 74 | 2.458 | Y reacts (10.0 / 15.0) | unresolved (0.255 / 0.178) | False |
| sa_flow:upq80 | m | oa_flow:downq80 | m | sa_flow:downq80 | 81 | 2.452 | unresolved (75.0 / 60.0) | unresolved (0.027 / 0.028) | False |
| sa_t:upq50 | m | oa_damper:upq10 | m | sa_t:downq50 | 8 | 2.44 | unresolved (85.0 / 90.0) | Y reacts (0.021 / 0.010) | False |
| plenum_p:upq50 | s | sa_flow:downq50 | s | plenum_p:downq50 | 79 | 2.411 | unresolved (10.0 / 12.5) | X reacts (0.039 / 0.073) | False |
| sf_spd:upq80 | s | oa_damper:downq90 | m | sf_spd:downq80 | 7 | 2.407 | Y reacts (12.5 / 55.0) | X reacts (0.015 / 0.026) | False |
| fan:upq90 | l | Tsp_c:upq50 | s | fan:downq10 | 6 | 2.4 | X reacts (495.0 / 5.0) | X reacts (0.007 / 0.200) | False |
| rf_spd:upq20 | s | sf_spd:upq20 | s | rf_spd:downq20 | 13 | 2.389 | Y reacts (7.5 / 20.0) | unresolved (0.049 / 0.033) | False |
| rf_spd:upq80 | s | sa_flow:downq80 | s | rf_spd:downq80 | 42 | 2.387 | X reacts (15.0 / 10.0) | unresolved (0.051 / 0.070) | False |
| rf_spd:downq20 | s | plenum_p:downq20 | m | rf_spd:upq20 | 54 | 2.366 | Y reacts (15.0 / 85.0) | Y reacts (0.033 / 0.017) | False |
| plenum_p:upq20 | s | sa_flow:downq20 | s | plenum_p:downq20 | 30 | 2.355 | unresolved (17.5 / 15.0) | X reacts (0.017 / 0.050) | False |
| sf_spd:upq50 | s | plenum_p:upq80 | m | sf_spd:downq50 | 78 | 2.354 | Y reacts (10.0 / 85.0) | Y reacts (0.050 / 0.021) | False |
| sa_flow:upq20 | s | rf_spd:upq20 | s | sa_flow:downq20 | 20 | 2.35 | Y reacts (10.0 / 15.0) | Y reacts (0.059 / 0.032) | False |
| rf_spd:upq80 | m | sa_t:downq20 | m | rf_spd:downq80 | 56 | 2.334 | unresolved (70.0 / 80.0) | Y reacts (0.072 / 0.040) | False |
| oa_flow:downq20 | s | oa_damper:downq10 | m | oa_flow:upq20 | 7 | 2.316 | Y reacts (5.0 / 80.0) | Y reacts (0.055 / 0.026) | False |
| rf_spd:downq20 | m | plenum_p:upq20 | s | rf_spd:upq20 | 44 | 2.315 | X reacts (75.0 / 15.0) | Y reacts (0.035 / 0.021) | False |
| ma_t:peak | s | oa_damper:upq90 | m | ma_t:trough | 11 | 2.315 | Y reacts (10.0 / 102.5) | Y reacts (0.051 / 0.018) | False |
| hw_valve:upq90 | m | T:downq20 | m | hw_valve:downq90 | 732 | 2.313 | X reacts (100.0 / 60.0) | Y reacts (0.132 / 0.083) | False |
| sa_t:downq50 | m | oa_damper:downq90 | m | sa_t:upq50 | 14 | 2.307 | unresolved (90.0 / 82.5) | Y reacts (0.029 / 0.015) | False |
| sa_flow:downq50 | s | rf_spd:upq50 | s | sa_flow:upq50 | 68 | 2.286 | X reacts (15.0 / 10.0) | unresolved (0.068 / 0.067) | False |
| rf_spd:downq80 | s | sa_t:upq50 | m | rf_spd:upq80 | 21 | 2.278 | Y reacts (10.0 / 95.0) | X reacts (0.011 / 0.041) | False |
| hw_valve:upq90 | s | T:upq20 | m | hw_valve:downq90 | 588 | 2.269 | Y reacts (10.0 / 40.0) | Y reacts (0.572 / 0.060) | False |
| rf_spd:downq50 | s | sf_spd:upq50 | s | rf_spd:upq50 | 78 | 2.264 | X reacts (15.0 / 10.0) | X reacts (0.043 / 0.074) | False |
| hw_valve:upq90 | s | Tsp_c:downq80 | s | hw_valve:downq90 | 9 | 2.263 | Y reacts (5.0 / 10.0) | X reacts (0.009 / 0.100) | False |
| oa_damper:downq90 | s | sa_t:downq20 | m | oa_damper:upq90 | 7 | 2.251 | Y reacts (10.0 / 62.5) | Y reacts (0.050 / 0.019) | False |
| rf_spd:downq20 | s | plenum_p:upq20 | m | rf_spd:upq20 | 28 | 2.236 | Y reacts (20.0 / 55.0) | Y reacts (0.023 / 0.014) | False |
| sa_flow:downq20 | s | rf_spd:downq20 | s | sa_flow:upq20 | 25 | 2.235 | Y reacts (7.5 / 15.0) | unresolved (0.061 / 0.068) | False |
| sa_t:upq50 | m | oa_damper:upq90 | l | sa_t:downq50 | 31 | 2.234 | Y reacts (90.0 / 400.0) | Y reacts (0.027 / 0.015) | False |
| sa_flow:upq80 | s | rf_spd:downq80 | s | sa_flow:downq80 | 26 | 2.233 | X reacts (15.0 / 10.0) | unresolved (0.055 / 0.048) | False |
| oa_flow:upq80 | m | rf_spd:upq80 | s | oa_flow:downq80 | 12 | 2.225 | X reacts (70.0 / 15.0) | unresolved (0.034 / 0.025) | False |
| rf_spd:downq50 | s | sf_spd:downq50 | s | rf_spd:upq50 | 53 | 2.222 | Y reacts (10.0 / 17.5) | unresolved (0.047 / 0.056) | False |
| sa_flow:upq50 | s | rf_spd:downq50 | s | sa_flow:downq50 | 51 | 2.218 | X reacts (15.0 / 5.0) | unresolved (0.050 / 0.049) | False |
| sa_flow:upq80 | m | plenum_p:downq80 | m | sa_flow:downq80 | 56 | 2.183 | unresolved (70.0 / 75.0) | Y reacts (0.051 / 0.026) | False |
| sa_flow:upq80 | s | rf_spd:upq80 | s | sa_flow:downq80 | 36 | 2.183 | Y reacts (10.0 / 15.0) | Y reacts (0.080 / 0.051) | False |
| hw_valve:downq90 | m | T:upq20 | m | hw_valve:upq90 | 587 | 2.179 | unresolved (85.0 / 105.0) | Y reacts (0.147 / 0.052) | False |
| sf_spd:downq20 | s | rf_spd:downq20 | s | sf_spd:upq20 | 24 | 2.174 | Y reacts (5.0 / 20.0) | unresolved (0.070 / 0.055) | False |
| sa_flow:upq50 | s | plenum_p:upq80 | m | sa_flow:downq50 | 80 | 2.161 | Y reacts (12.5 / 77.5) | Y reacts (0.046 / 0.023) | False |
| T:upq50 | m | hw_valve:downq10 | s | T:downq50 | 71 | 2.161 | X reacts (47.5 / 15.0) | X reacts (0.085 / 0.178) | False |
| ma_t:peak | m | oa_damper:downq90 | m | ma_t:trough | 24 | 2.161 | unresolved (107.5 / 80.0) | unresolved (0.020 / 0.016) | False |
| rf_spd:upq80 | m | oa_flow:downq80 | m | rf_spd:downq80 | 99 | 2.159 | unresolved (70.0 / 82.5) | unresolved (0.027 / 0.039) | False |
| rf_spd:upq80 | s | sf_spd:downq80 | s | rf_spd:downq80 | 29 | 2.157 | X reacts (20.0 / 12.5) | unresolved (0.045 / 0.051) | False |
| sa_flow:downq20 | m | plenum_p:upq20 | s | sa_flow:upq20 | 42 | 2.147 | X reacts (55.0 / 10.0) | Y reacts (0.034 / 0.019) | False |
| rf_spd:upq80 | m | plenum_p:upq80 | s | rf_spd:downq80 | 40 | 2.143 | X reacts (57.5 / 10.0) | unresolved (0.048 / 0.039) | False |
| sf_spd:downq20 | s | plenum_p:upq20 | m | sf_spd:upq20 | 23 | 2.139 | Y reacts (25.0 / 87.5) | unresolved (0.021 / 0.017) | False |
| plenum_p:upq50 | s | sf_spd:downq50 | s | plenum_p:downq50 | 58 | 2.127 | X reacts (15.0 / 10.0) | X reacts (0.036 / 0.069) | False |
| oa_flow:upq80 | m | sa_t:upq50 | m | oa_flow:downq80 | 22 | 2.127 | X reacts (90.0 / 57.5) | X reacts (0.012 / 0.024) | False |
| oa_damper:downq10 | l | oa_flow:upq20 | s | oa_damper:upq10 | 20 | 2.119 | X reacts (350.0 / 15.0) | X reacts (0.016 / 0.053) | False |
| oa_flow:upq80 | m | ma_t:trough | s | oa_flow:downq80 | 16 | 2.113 | X reacts (80.0 / 15.0) | X reacts (0.021 / 0.046) | False |
| sa_flow:downq50 | s | plenum_p:downq50 | m | sa_flow:upq50 | 121 | 2.102 | Y reacts (10.0 / 50.0) | Y reacts (0.073 / 0.031) | False |
| sf_spd:downq50 | s | rf_spd:downq50 | s | sf_spd:upq50 | 48 | 2.101 | Y reacts (10.0 / 15.0) | Y reacts (0.080 / 0.043) | False |
| sa_flow:downq80 | s | rf_spd:upq80 | s | sa_flow:upq80 | 11 | 2.091 | X reacts (20.0 / 7.5) | unresolved (0.051 / 0.040) | False |
| sa_flow:upq20 | s | plenum_p:upq20 | m | sa_flow:downq20 | 57 | 2.068 | Y reacts (10.0 / 80.0) | Y reacts (0.042 / 0.011) | False |
| oa_damper:upq10 | m | sa_t:downq20 | s | oa_damper:downq90 | 7 | 2.067 | X reacts (75.0 / 15.0) | Y reacts (0.082 / 0.041) | False |
| sf_spd:upq50 | m | plenum_p:upq80 | s | sf_spd:downq50 | 68 | 2.066 | X reacts (65.0 / 15.0) | unresolved (0.040 / 0.034) | False |
| sf_spd:downq80 | m | rf_spd:upq80 | m | sf_spd:upq80 | 72 | 2.044 | unresolved (75.0 / 75.0) | Y reacts (0.054 / 0.028) | False |
| sa_flow:downq50 | s | rf_spd:downq50 | s | sa_flow:upq50 | 75 | 2.015 | Y reacts (5.0 / 20.0) | Y reacts (0.094 / 0.055) | False |
| sa_t:downq50 | l | oa_flow:downq20 | l | sa_t:upq50 | 69 | 2.0 | Y reacts (260.0 / 465.0) | unresolved (0.013 / 0.012) | False |
| sf_spd:downq50 | s | plenum_p:downq50 | m | sf_spd:upq50 | 90 | 1.984 | Y reacts (12.5 / 70.0) | Y reacts (0.069 / 0.026) | False |
| sa_flow:upq50 | s | rf_spd:upq50 | s | sa_flow:downq50 | 65 | 1.982 | Y reacts (10.0 / 15.0) | Y reacts (0.087 / 0.043) | False |
| rf_spd:upq80 | m | oa_flow:downq80 | s | rf_spd:downq80 | 16 | 1.981 | X reacts (47.5 / 15.0) | unresolved (0.027 / 0.030) | False |
| rf_spd:downq50 | s | sa_flow:downq50 | s | rf_spd:upq50 | 64 | 1.975 | Y reacts (5.0 / 15.0) | unresolved (0.049 / 0.068) | False |
| oa_damper:downq10 | m | sa_t:downq50 | m | oa_damper:upq10 | 3 | 1.969 | unresolved (85.0 / 80.0) | unresolved (0.021 / 0.021) | False |
| oa_damper:upq10 | s | oa_flow:upq80 | m | oa_damper:downq90 | 8 | 1.949 | Y reacts (10.0 / 70.0) | Y reacts (0.062 / 0.038) | False |
| oa_damper:downq90 | s | sa_t:upq20 | m | oa_damper:upq90 | 8 | 1.937 | Y reacts (17.5 / 60.0) | Y reacts (0.073 / 0.017) | False |
| rf_spd:downq50 | s | sa_flow:upq50 | s | rf_spd:upq50 | 109 | 1.931 | X reacts (15.0 / 10.0) | X reacts (0.055 / 0.087) | False |
| sf_spd:upq80 | m | oa_damper:downq90 | m | sf_spd:downq80 | 16 | 1.931 | unresolved (70.0 / 72.5) | unresolved (0.023 / 0.026) | False |
| plenum_p:downq20 | s | sa_flow:upq20 | s | plenum_p:upq20 | 39 | 1.925 | X reacts (15.0 / 10.0) | unresolved (0.029 / 0.042) | False |
| rf_spd:downq80 | s | sa_flow:downq80 | s | rf_spd:upq80 | 13 | 1.914 | Y reacts (10.0 / 15.0) | unresolved (0.048 / 0.051) | False |
| sf_spd:downq20 | m | plenum_p:upq20 | s | sf_spd:upq20 | 40 | 1.894 | X reacts (82.5 / 10.0) | Y reacts (0.035 / 0.014) | False |
| sa_t:upq50 | l | oa_flow:downq20 | l | sa_t:downq50 | 55 | 1.88 | Y reacts (270.0 / 430.0) | unresolved (0.011 / 0.013) | False |
| oa_flow:upq80 | m | sa_t:downq50 | m | oa_flow:downq80 | 24 | 1.879 | unresolved (87.5 / 65.0) | X reacts (0.012 / 0.027) | False |
| sa_t:upq50 | m | oa_damper:downq90 | l | sa_t:downq50 | 34 | 1.877 | Y reacts (85.0 / 405.0) | unresolved (0.026 / 0.017) | False |
| oa_flow:upq80 | m | rf_spd:upq80 | m | oa_flow:downq80 | 29 | 1.847 | unresolved (80.0 / 70.0) | unresolved (0.034 / 0.027) | False |
| plenum_p:upq80 | s | rf_spd:downq80 | m | plenum_p:downq80 | 71 | 1.835 | Y reacts (10.0 / 80.0) | unresolved (0.039 / 0.049) | False |
| sf_spd:downq80 | s | rf_spd:downq80 | m | sf_spd:upq80 | 34 | 1.835 | Y reacts (10.0 / 70.0) | unresolved (0.051 / 0.037) | False |
| rf_spd:downq20 | s | sf_spd:upq20 | s | rf_spd:upq20 | 26 | 1.816 | X reacts (20.0 / 5.0) | unresolved (0.055 / 0.071) | False |
| rf_spd:upq50 | s | sf_spd:downq50 | s | rf_spd:downq50 | 61 | 1.809 | X reacts (20.0 / 10.0) | X reacts (0.035 / 0.080) | False |
| sa_flow:upq50 | m | plenum_p:downq80 | m | sa_flow:downq50 | 175 | 1.807 | unresolved (70.0 / 70.0) | Y reacts (0.040 / 0.026) | False |
| hw_valve:downq10 | l | T:downq50 | s | hw_valve:upq10 | 302 | 1.799 | X reacts (462.5 / 20.0) | unresolved (0.155 / 0.115) | False |
| sf_spd:downq50 | m | plenum_p:upq80 | m | sf_spd:upq50 | 135 | 1.799 | unresolved (75.0 / 70.0) | Y reacts (0.042 / 0.023) | False |
| sf_spd:upq20 | m | plenum_p:downq20 | m | sf_spd:downq20 | 94 | 1.798 | Y reacts (35.0 / 70.0) | Y reacts (0.034 / 0.014) | False |
| sa_flow:downq20 | m | plenum_p:upq20 | m | sa_flow:upq20 | 76 | 1.798 | Y reacts (50.0 / 75.0) | Y reacts (0.034 / 0.014) | False |
| sf_spd:downq20 | m | plenum_p:downq20 | s | sf_spd:upq20 | 34 | 1.797 | X reacts (77.5 / 15.0) | unresolved (0.024 / 0.023) | False |
| rf_spd:upq20 | s | sa_flow:upq20 | s | rf_spd:downq20 | 10 | 1.789 | Y reacts (7.5 / 17.5) | unresolved (0.041 / 0.030) | False |
| rf_spd:upq50 | s | sa_flow:upq50 | s | rf_spd:downq50 | 73 | 1.786 | Y reacts (7.5 / 17.5) | unresolved (0.067 / 0.050) | False |
| rf_spd:downq20 | s | sa_flow:upq20 | s | rf_spd:upq20 | 36 | 1.786 | X reacts (20.0 / 5.0) | unresolved (0.068 / 0.059) | False |
| sf_spd:upq20 | m | plenum_p:upq20 | s | sf_spd:downq20 | 35 | 1.784 | X reacts (95.0 / 10.0) | Y reacts (0.030 / 0.011) | False |
| rf_spd:upq20 | s | sa_flow:downq20 | s | rf_spd:downq20 | 20 | 1.78 | unresolved (17.5 / 12.5) | X reacts (0.032 / 0.061) | False |
| sf_spd:downq20 | s | rf_spd:downq20 | m | sf_spd:upq20 | 70 | 1.779 | Y reacts (5.0 / 55.0) | Y reacts (0.070 / 0.045) | False |
| ma_t:peak | m | oa_damper:upq10 | m | ma_t:trough | 22 | 1.779 | unresolved (95.0 / 85.0) | unresolved (0.031 / 0.028) | False |
| hw_valve:upq10 | m | Tsp_c:upq20 | s | hw_valve:downq10 | 12 | 1.771 | X reacts (85.0 / 5.0) | X reacts (0.006 / 0.095) | False |
| sa_flow:downq50 | m | plenum_p:upq50 | m | sa_flow:upq50 | 203 | 1.767 | unresolved (65.0 / 70.0) | Y reacts (0.062 / 0.030) | False |
| rf_spd:upq50 | s | sf_spd:upq50 | s | rf_spd:downq50 | 46 | 1.765 | Y reacts (10.0 / 20.0) | unresolved (0.050 / 0.051) | False |
| sf_spd:downq50 | s | rf_spd:upq50 | m | sf_spd:upq50 | 54 | 1.743 | Y reacts (20.0 / 50.0) | Y reacts (0.056 / 0.029) | False |
| rf_spd:downq20 | m | plenum_p:downq20 | s | rf_spd:upq20 | 29 | 1.741 | X reacts (50.0 / 15.0) | Y reacts (0.031 / 0.021) | False |
| rf_spd:downq20 | m | plenum_p:downq20 | m | rf_spd:upq20 | 79 | 1.74 | Y reacts (52.5 / 80.0) | Y reacts (0.031 / 0.017) | False |
| rf_spd:upq20 | s | sf_spd:downq20 | s | rf_spd:downq20 | 17 | 1.737 | X reacts (20.0 / 5.0) | X reacts (0.030 / 0.070) | False |
| sa_t:downq50 | s | oa_damper:upq90 | l | sa_t:upq50 | 9 | 1.734 | Y reacts (5.0 / 605.0) | Y reacts (0.033 / 0.015) | False |
| sf_spd:downq20 | m | plenum_p:downq20 | m | sf_spd:upq20 | 73 | 1.727 | X reacts (100.0 / 60.0) | unresolved (0.024 / 0.018) | False |
| T:upq20 | m | hw_valve:downq10 | s | T:downq20 | 105 | 1.725 | X reacts (40.0 / 15.0) | X reacts (0.084 / 0.171) | False |
| sa_flow:upq50 | m | plenum_p:downq50 | m | sa_flow:downq50 | 213 | 1.719 | unresolved (65.0 / 65.0) | Y reacts (0.060 / 0.028) | False |
| rf_spd:downq20 | s | sa_flow:downq20 | s | rf_spd:upq20 | 20 | 1.716 | Y reacts (5.0 / 20.0) | unresolved (0.061 / 0.059) | False |
| hw_valve:downq90 | m | T:downq20 | s | hw_valve:upq90 | 536 | 1.713 | X reacts (60.0 / 15.0) | unresolved (0.154 / 0.203) | False |
| hw_valve:downq10 | l | T:downq50 | m | hw_valve:upq10 | 1041 | 1.712 | X reacts (590.0 / 70.0) | unresolved (0.155 / 0.133) | False |
| sf_spd:downq20 | m | plenum_p:upq20 | m | sf_spd:upq20 | 81 | 1.711 | Y reacts (40.0 / 75.0) | Y reacts (0.035 / 0.017) | False |
| rf_spd:upq50 | s | plenum_p:upq80 | m | rf_spd:downq50 | 106 | 1.709 | Y reacts (10.0 / 62.5) | unresolved (0.045 / 0.034) | False |
| sa_t:downq50 | m | oa_damper:downq90 | s | sa_t:upq50 | 5 | 1.705 | X reacts (80.0 / 10.0) | Y reacts (0.029 / 0.016) | False |
| rf_spd:downq50 | s | oa_damper:upq90 | m | rf_spd:upq50 | 20 | 1.703 | Y reacts (10.0 / 90.0) | X reacts (0.019 / 0.035) | False |
| oa_flow:upq80 | s | oa_damper:downq90 | s | oa_flow:downq50 | 3 | 1.701 | unresolved (20.0 / 20.0) | unresolved (0.025 / 0.026) | False |
| sa_flow:upq50 | s | plenum_p:upq50 | m | sa_flow:downq50 | 78 | 1.686 | Y reacts (10.0 / 80.0) | Y reacts (0.082 / 0.027) | False |
| sf_spd:upq20 | s | plenum_p:upq20 | m | sf_spd:downq20 | 53 | 1.686 | Y reacts (10.0 / 85.0) | Y reacts (0.041 / 0.014) | False |
| sf_spd:upq20 | s | rf_spd:upq20 | s | sf_spd:downq20 | 11 | 1.661 | Y reacts (10.0 / 20.0) | Y reacts (0.071 / 0.030) | False |
| sf_spd:downq50 | m | plenum_p:upq50 | s | sf_spd:upq50 | 59 | 1.66 | X reacts (55.0 / 10.0) | Y reacts (0.058 / 0.022) | False |
| rf_spd:downq80 | m | oa_flow:upq50 | l | rf_spd:upq80 | 133 | 1.649 | Y reacts (95.0 / 470.0) | X reacts (0.016 / 0.040) | False |
| oa_flow:upq80 | m | sa_t:downq20 | m | oa_flow:downq80 | 31 | 1.646 | unresolved (70.0 / 70.0) | Y reacts (0.071 / 0.030) | False |
| sf_spd:upq80 | m | oa_flow:downq80 | s | sf_spd:downq80 | 8 | 1.646 | X reacts (45.0 / 20.0) | unresolved (0.026 / 0.034) | False |
| plenum_p:downq20 | s | rf_spd:downq20 | m | plenum_p:upq20 | 60 | 1.628 | Y reacts (17.5 / 82.5) | X reacts (0.020 / 0.035) | False |
| oa_flow:upq80 | m | ma_t:trough | m | oa_flow:downq80 | 59 | 1.626 | unresolved (65.0 / 72.5) | X reacts (0.021 / 0.046) | False |
| rf_spd:upq20 | m | plenum_p:downq20 | s | rf_spd:downq20 | 34 | 1.623 | X reacts (100.0 / 12.5) | Y reacts (0.033 / 0.020) | False |
| sa_t:downq50 | l | oa_flow:upq20 | l | sa_t:upq50 | 42 | 1.62 | Y reacts (245.0 / 450.0) | unresolved (0.014 / 0.013) | False |
| oa_flow:upq20 | m | sa_t:upq50 | l | oa_flow:downq20 | 27 | 1.617 | Y reacts (130.0 / 260.0) | unresolved (0.011 / 0.011) | False |
| plenum_p:upq20 | s | rf_spd:upq20 | m | plenum_p:downq20 | 40 | 1.613 | Y reacts (15.0 / 90.0) | X reacts (0.021 / 0.033) | False |
| sa_flow:upq20 | m | plenum_p:downq20 | m | sa_flow:downq20 | 72 | 1.611 | X reacts (105.0 / 62.5) | Y reacts (0.035 / 0.013) | False |
| sf_spd:upq50 | m | plenum_p:downq80 | m | sf_spd:downq50 | 140 | 1.606 | unresolved (75.0 / 85.0) | Y reacts (0.041 / 0.024) | False |
| plenum_p:downq20 | s | sf_spd:upq20 | s | plenum_p:upq20 | 47 | 1.605 | unresolved (10.0 / 10.0) | X reacts (0.023 / 0.041) | False |
| sa_flow:upq50 | m | plenum_p:upq50 | m | sa_flow:downq50 | 168 | 1.604 | unresolved (80.0 / 70.0) | Y reacts (0.055 / 0.027) | False |
| rf_spd:downq50 | s | plenum_p:downq50 | m | rf_spd:upq50 | 139 | 1.599 | Y reacts (15.0 / 70.0) | Y reacts (0.059 / 0.038) | False |
| rf_spd:downq20 | m | plenum_p:upq20 | m | rf_spd:upq20 | 77 | 1.582 | unresolved (70.0 / 75.0) | Y reacts (0.035 / 0.014) | False |
| plenum_p:downq50 | s | sf_spd:downq50 | m | plenum_p:upq50 | 85 | 1.581 | Y reacts (15.0 / 55.0) | X reacts (0.027 / 0.058) | False |
| rf_spd:upq20 | m | plenum_p:downq20 | m | rf_spd:downq20 | 80 | 1.578 | Y reacts (55.0 / 85.0) | Y reacts (0.033 / 0.012) | False |
| sa_flow:downq50 | m | plenum_p:downq50 | m | sa_flow:upq50 | 158 | 1.571 | unresolved (80.0 / 75.0) | Y reacts (0.055 / 0.031) | False |
| hw_valve:downq10 | l | fan:downq10 | m | hw_valve:upq10 | 127 | 1.569 | X reacts (600.0 / 67.5) | X reacts (0.028 / 0.112) | False |
| oa_flow:downq20 | l | oa_damper:upq10 | s | oa_flow:upq50 | 18 | 1.565 | X reacts (417.5 / 5.0) | X reacts (0.017 / 0.040) | False |
| hw_valve:downq10 | l | T:downq80 | m | hw_valve:upq10 | 696 | 1.563 | X reacts (420.0 / 115.0) | Y reacts (0.136 / 0.071) | False |
| plenum_p:downq20 | m | rf_spd:upq20 | m | plenum_p:upq20 | 130 | 1.561 | unresolved (55.0 / 60.0) | X reacts (0.017 / 0.032) | False |
| T:upq20 | m | hw_valve:downq90 | s | T:downq50 | 178 | 1.543 | X reacts (40.0 / 25.0) | X reacts (0.060 / 0.245) | False |
| sf_spd:downq50 | m | plenum_p:upq50 | m | sf_spd:upq50 | 151 | 1.543 | unresolved (65.0 / 70.0) | Y reacts (0.058 / 0.025) | False |
| sf_spd:downq50 | s | rf_spd:downq50 | m | sf_spd:upq50 | 119 | 1.542 | Y reacts (10.0 / 55.0) | Y reacts (0.080 / 0.042) | False |
| sa_flow:downq20 | m | rf_spd:upq20 | s | sa_flow:upq20 | 50 | 1.541 | X reacts (62.5 / 5.0) | unresolved (0.049 / 0.041) | False |
| sa_flow:upq20 | m | plenum_p:upq20 | s | sa_flow:downq20 | 25 | 1.54 | X reacts (85.0 / 25.0) | Y reacts (0.031 / 0.017) | False |
| sf_spd:upq20 | m | plenum_p:downq20 | s | sf_spd:downq20 | 37 | 1.522 | X reacts (55.0 / 5.0) | Y reacts (0.034 / 0.017) | False |
| sf_spd:upq50 | m | plenum_p:upq80 | m | sf_spd:downq50 | 115 | 1.519 | unresolved (75.0 / 75.0) | Y reacts (0.040 / 0.021) | False |
| sa_flow:upq20 | m | plenum_p:downq20 | s | sa_flow:downq20 | 33 | 1.517 | X reacts (40.0 / 5.0) | unresolved (0.035 / 0.024) | False |
| sa_t:downq50 | m | oa_damper:downq90 | l | sa_t:upq50 | 24 | 1.506 | Y reacts (80.0 / 427.5) | Y reacts (0.029 / 0.016) | False |
| ra_t:peak | l | oa_flow:downq50 | l | ra_t:trough | 274 | 1.504 | unresolved (370.0 / 410.0) | Y reacts (0.017 / 0.008) | False |

Chains (non-return): 745.

## Absences

- silent roles: ['solar']
- roles never a target: ['T_out', 'co2', 'econ_sp', 'hvac_kw_N', 'hvac_kw_S', 'rh_out', 'sat_sp', 'static_sp']
- keyed pairs not found: static_sp → sf_spd; sat_sp → sa_t
- signal floor: 68 (absence is informative only for pairs whose support would exceed the signal floor)

## Regimes

none recorded

## Matrix row

Cells in (this system as receiver):

| source | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| building_59_stretch (diagonal) | 116.75 | 151.49 | 569.00 | 452.25 | 417.51 | marginal | — | 74/89 |  |
| building_a | -0.93 | 0.68 | 118.64 | 119.56 | 117.96 | marginal | -0.01 | 22/89 |  |
| building_b | -4.51 | -1.33 | 119.17 | 123.69 | 120.51 | marginal | -0.04 | 26/89 |  |
| tennessee_eastman | 11.16 | 25.00 | 143.65 | 132.49 | 118.65 | marginal | 0.10 | 89/89 |  |
| hai | 4.37 | 8.01 | 129.67 | 125.30 | 121.65 | marginal | 0.04 | 85/89 | damage |
| fingrid | -1.89 | 0.20 | 108.18 | 110.07 | 107.98 | marginal | -0.02 | 10/89 |  |
| alibaba_2018 | 4.29 | 4.29 | 117.26 | 112.45 | 112.98 | derangement | 0.04 | 16/89 |  |

Cells out (this system as source):

| receiver | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| building_a | -1.93 | 4.59 | 20.85 | 22.78 | 16.26 | marginal | -0.01 | 12/20 | damage |
| building_b | -1.11 | 0.34 | 11.28 | 12.39 | 10.94 | marginal | -0.01 | 22/22 |  |
| tennessee_eastman | 13.39 | 71.08 | 103.96 | 90.57 | 32.87 | marginal | 0.08 | 32/40 | damage |
| hai | 17.27 | 26.26 | 49.52 | 32.25 | 23.26 | marginal | — | 95/168 | short, damage |
| fingrid | 3.98 | 7.08 | 15.24 | 11.26 | 8.16 | marginal | 0.03 | 10/16 | damage |
| alibaba_2018 | 2.64 | 4.03 | 2.64 | 0.00 | -1.39 | marginal | — | 27/27 |  |

Nearest taxa by distance: shape_jaccard: tennessee_eastman 0.832, hai 0.886, nasa_battery 0.966; shape_bray_curtis: tennessee_eastman 0.775, hai 0.841, nasa_battery 0.963; transfer_net: tennessee_eastman 0.075, hai 0.085, fingrid 0.489
