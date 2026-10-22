# Brief — tennessee_eastman (method v8, a view)

*Lifts are odds ratios on the proposal split (3.6-3.8), confirmed on the confirmation split; absence is informative only above the signal floor (3.5); `no gain` means found but already carried by the trivial alternation model (3.11); loop-rule verdicts are recorded, not promoted (3.16); cells are bit-horizons net of the larger of two controls, with share of the receiver's ceiling where a diagonal exists (3.12).*

## Identity

- kind: simulated plant (Tennessee Eastman); standing: admitted
- entity: vessel (3 units); H = 143.2 min; lag edges [10.88, 39.49, 143.25] min
- periods: slow —, fast —; admission: {'days': 120.0, 'slow_periods': None, 'horizons': 1206.2, 'test_horizons': 301.6, 'admitted': True, 'by': 'days'}
- claim: **beats baselines** — library 3.033 bits, triviality 3.171, best baseline 3.410; gain over triviality 0.138
- events 280002, types 40, signal floor 138

## Vocabulary

| role | full tag | quantity | scheme | loop tags (timing / determinism) |
| --- | --- | --- | --- | --- |
| AC_feed | SLOW·LEAD ⟨L³ T⁻¹⟩ | volume_flow | q20_50_80 | — / — |
| AC_valve | SLOW·LEAD | — | q20_50_80 | — / — |
| A_feed | SLOW·LEAD ⟨L³ T⁻¹⟩ | volume_flow | q20_50_80 | — / — |
| A_valve | SLOW·LEAD | — | q20_50_80 | — / — |
| D_feed | SLOW·ISOLATED ⟨M T⁻¹⟩ | mass_flow | dsign | — / — |
| D_valve | MID·ISOLATED | — | q20_50_80 | — / — |
| E_feed | SLOW·ISOLATED ⟨M T⁻¹⟩ | mass_flow | dsign | — / — |
| E_valve | MID·ISOLATED | — | q20_50_80 | — / — |
| L | MID·LEAD | — | dsign | — / — |
| P | MID·COMMON·FOLLOW ⟨M L⁻¹ T⁻²⟩ | pressure | q20_50_80 | REACTS / REACTS |
| T | MID·COMMON·FOLLOW ⟨Θ⟩ | temperature | q20_50_80 | REACTS / REACTS |
| compressor | MID·LEAD ⟨M L² T⁻³⟩ | power | q20_50_80 | — / — |
| cw_flow | SLOW·LOCAL·RELAY | — | q20_50_80 | RESPONDS / RESPONDS |
| cw_out | MID·LOCAL·RELAY ⟨Θ⟩ | temperature | q20_50_80 | RESPONDS / RESPONDS |
| feed | MID·COMMON·RELAY ⟨L³ T⁻¹⟩ | volume_flow | q20_50_80 | REACTS / RESPONDS |
| feed_A | MID·ISOLATED | — | q20_50_80 | — / — |
| feed_B | SLOW·ISOLATED | — | q20_50_80 | — / — |
| feed_C | MID·ISOLATED | — | q20_50_80 | — / — |
| feed_D | MID·ISOLATED | — | dsign | — / — |
| feed_E | MID·ISOLATED | — | q20_50_80 | — / — |
| feed_F | SLOW·LEAD | — | q20_50_80 | — / — |
| prod_D | FAST·ISOLATED | — | dsign | — / — |
| prod_E | MID·ISOLATED | — | q20_50_80 | — / — |
| prod_F | MID·ISOLATED | — | dsign | — / — |
| prod_G | FAST·ISOLATED | — | dsign | — / — |
| prod_H | FAST·ISOLATED | — | dsign | — / — |
| purge | MID·LEAD ⟨L³ T⁻¹⟩ | volume_flow | dsign | — / — |
| purge_A | MID·ISOLATED | — | q20_50_80 | — / — |
| purge_B | SLOW·ISOLATED | — | q20_50_80 | — / — |
| purge_C | MID·LEAD | — | q20_50_80 | — / — |
| purge_D | MID·ISOLATED | — | dsign | — / — |
| purge_E | MID·ISOLATED | — | q20_50_80 | — / — |
| purge_F | SLOW·ISOLATED | — | q20_50_80 | — / — |
| purge_G | MID·LEAD | — | q20_50_80 | — / — |
| purge_H | MID·ISOLATED | — | q20_50_80 | — / — |
| purge_valve | MID·LEAD | — | dsign | — / — |
| recycle | MID·LEAD ⟨L³ T⁻¹⟩ | volume_flow | q20_50_80 | — / — |
| steam | TEX·ISOLATED ⟨M T⁻¹⟩ | mass_flow | silent | — / — |
| underflow | MID·LOCAL·RELAY ⟨L³ T⁻¹⟩ | volume_flow | dsign | RESPONDS / — |
| underflow_valve | MID·LOCAL·RELAY | — | q20_50_80 | REACTS / RESPONDS |

## Couplings (validated fragments)

| prior | lag | target | lift | conf. lift | n | binding | shape | confirmed in | failed in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| underflow_valve:downq20 | s | underflow_valve:upq20 | 18.946 | 12.487 | 135 | True | `MID.down.q20 -s-> MID.up.q20 [same role]` | hai | nasa_battery, building_59 |
| cw_flow:upq80 | s | cw_flow:downq80 | 17.24 | 18.676 | 71 | True | `SLOW.up.q80 -s-> SLOW.down.q80 [same role]` | hai, nasa_battery, building_59 | — |
| feed:downq50 | s | feed:downq20 | 12.445 | 11.397 | 134 | False | `MID.down.q50 -s-> MID.down.q20 [same role]` | building_59 | hai |
| feed:downq80 | s | feed:downq50 | 11.421 | 10.871 | 130 | False | `MID.down.q80 -s-> MID.down.q50 [same role]` | hai, building_59 | — |
| feed:downq20 | m | feed:upq20 | 11.162 | 11.277 | 248 | False | `MID.down.q20 -m-> MID.up.q20 [same role]` | hai, building_59 | — |
| feed:upq80 | m | feed:downq80 | 10.892 | 10.535 | 235 | False | `MID.up.q80 -m-> MID.down.q80 [same role]` | hai, building_59 | — |
| feed:upq50 | s | feed:upq80 | 10.858 | 11.946 | 113 | False | `MID.up.q50 -s-> MID.up.q80 [same role]` | hai, building_59 | — |
| underflow_valve:upq80 | s | underflow_valve:downq80 | 9.845 | 8.071 | 161 | True | `MID.up.q80 -s-> MID.down.q80 [same role]` | hai, nasa_battery | building_59 |
| cw_flow:upq80 | m | cw_flow:downq80 | 9.662 | 9.344 | 155 | True | `SLOW.up.q80 -m-> SLOW.down.q80 [same role]` | hai, nasa_battery, building_59 | — |
| feed:downq20 | s | feed:upq20 | 9.517 | 7.495 | 49 | False | `MID.down.q20 -s-> MID.up.q20 [same role]` | hai, building_59 | — |
| feed:upq20 | s | feed:upq50 | 8.556 | 9.416 | 103 | False | `MID.up.q20 -s-> MID.up.q50 [same role]` | building_59 | hai |
| underflow_valve:downq20 | m | underflow_valve:upq20 | 8.361 | 8.113 | 179 | True | `MID.down.q20 -m-> MID.up.q20 [same role]` | hai | nasa_battery, building_59 |
| cw_out:downq80 | s | cw_out:downq20 | 8.274 | 8.312 | 121 | True | `MID.down.q80 -s-> MID.down.q20 [same role]` | — | hai, building_59 |
| cw_flow:downq20 | s | cw_flow:upq20 | 8.18 | 7.216 | 128 | True | `SLOW.down.q20 -s-> SLOW.up.q20 [same role]` | nasa_battery, building_59 | hai |
| cw_flow:upq50 | s | cw_flow:upq80 | 7.656 | 9.381 | 106 | True | `SLOW.up.q50 -s-> SLOW.up.q80 [same role]` | hai | — |
| cw_flow:downq50 | s | cw_flow:downq20 | 7.578 | 8.88 | 216 | True | `SLOW.down.q50 -s-> SLOW.down.q20 [same role]` | hai | — |
| cw_flow:upq20 | s | cw_flow:upq80 | 7.289 | 9.548 | 69 | True | `SLOW.up.q20 -s-> SLOW.up.q80 [same role]` | hai, building_59 | nasa_battery |
| feed:upq80 | s | feed:downq80 | 7.239 | 6.885 | 38 | False | `MID.up.q80 -s-> MID.down.q80 [same role]` | hai, building_59 | — |
| cw_out:downq20 | m | cw_out:upq20 | 6.977 | 7.266 | 244 | True | `MID.down.q20 -m-> MID.up.q20 [same role]` | hai, building_59 | — |
| cw_flow:downq20 | m | cw_flow:upq20 | 6.941 | 7.105 | 378 | True | `SLOW.down.q20 -m-> SLOW.up.q20 [same role]` | hai, nasa_battery, building_59 | — |
| underflow_valve:downq50 | s | underflow_valve:downq20 | 6.766 | 7.979 | 145 | True | `MID.down.q50 -s-> MID.down.q20 [same role]` | — | nasa_battery, building_59 |
| underflow_valve:upq80 | m | underflow_valve:downq80 | 6.758 | 6.362 | 376 | True | `MID.up.q80 -m-> MID.down.q80 [same role]` | hai, nasa_battery | building_59 |
| cw_out:downq20 | s | cw_out:upq20 | 6.717 | 5.663 | 64 | True | `MID.down.q20 -s-> MID.up.q20 [same role]` | hai, building_59 | — |
| T:upq80 | s | T:downq80 | 6.605 | 5.336 | 108 | True | `MID.up.q80 -s-> MID.down.q80 [same role]` | hai | building_59 |
| cw_flow:upq20 | s | cw_flow:upq50 | 6.48 | 6.815 | 221 | True | `SLOW.up.q20 -s-> SLOW.up.q50 [same role]` | hai | — |
| feed:upq20 | s | feed:upq80 | 6.13 | 4.92 | 41 | False | `MID.up.q20 -s-> MID.up.q80 [same role]` | building_59 | hai |
| cw_flow:downq80 | m | cw_flow:upq80 | 6.059 | 3.823 | 96 | True | `SLOW.down.q80 -m-> SLOW.up.q80 [same role]` | building_59 | hai, nasa_battery |
| cw_out:upq80 | m | cw_out:downq80 | 5.917 | 6.496 | 304 | True | `MID.up.q80 -m-> MID.down.q80 [same role]` | hai | building_59 |
| T:upq20 | s | T:upq80 | 5.889 | 6.216 | 159 | True | `MID.up.q20 -s-> MID.up.q80 [same role]` | building_59 | hai |
| cw_out:upq80 | s | cw_out:downq80 | 5.889 | 3.756 | 87 | True | `MID.up.q80 -s-> MID.down.q80 [same role]` | hai | building_59 |
| T:downq80 | s | T:downq20 | 5.862 | 4.687 | 180 | True | `MID.down.q80 -s-> MID.down.q20 [same role]` | building_59 | hai |
| cw_flow:downq80 | s | cw_flow:downq20 | 5.557 | 5.26 | 60 | True | `SLOW.down.q80 -s-> SLOW.down.q20 [same role]` | building_59 | hai, nasa_battery |
| underflow_valve:upq20 | s | underflow_valve:upq80 | 5.321 | 6.263 | 60 | True | `MID.up.q20 -s-> MID.up.q80 [same role]` | — | hai, nasa_battery, building_59 |
| cw_out:downq50 | s | cw_out:downq20 | 5.188 | 7.712 | 136 | True | `MID.down.q50 -s-> MID.down.q20 [same role]` | hai, building_59 | — |
| T:upq80 | m | T:downq80 | 5.157 | 6.043 | 336 | True | `MID.up.q80 -m-> MID.down.q80 [same role]` | hai, building_59 | — |
| compressor:upq80 | s | cw_out:upq80 | 4.99 | 2.998 | 59 | False | `MID.up.q80 -s-> MID.up.q80` | — | building_59 |
| cw_flow:upq80 | s | cw_out:downq20 | 4.933 | 6.485 | 30 | True | `SLOW.up.q80 -s-> MID.down.q20` | building_59 | hai |
| cw_flow:downq80 | s | cw_flow:downq50 | 4.905 | 6.155 | 103 | True | `SLOW.down.q80 -s-> SLOW.down.q50 [same role]` | hai | — |
| underflow_valve:upq50 | s | underflow_valve:upq80 | 4.804 | 5.064 | 163 | True | `MID.up.q50 -s-> MID.up.q80 [same role]` | nasa_battery | building_59 |
| P:upq50 | s | P:upq80 | 4.794 | 4.586 | 724 | True | `MID.up.q50 -s-> MID.up.q80 [same role]` | — | — |
| feed:upq50 | m | feed:upq80 | 4.773 | 4.235 | 178 | False | `MID.up.q50 -m-> MID.up.q80 [same role]` | hai, building_59 | — |
| feed:downq80 | m | feed:downq20 | 4.75 | 5.053 | 102 | False | `MID.down.q80 -m-> MID.down.q20 [same role]` | — | hai, building_59 |
| A_feed:downq80 | s | T:upq80 | 4.732 | 2.981 | 92 | False | `SLOW.down.q80 -s-> MID.up.q80` | — | hai, building_59 |
| cw_out:upq50 | s | cw_out:upq80 | 4.72 | 5.832 | 150 | True | `MID.up.q50 -s-> MID.up.q80 [same role]` | — | hai, building_59 |
| feed:downq50 | m | feed:downq20 | 4.684 | 4.103 | 175 | False | `MID.down.q50 -m-> MID.down.q20 [same role]` | hai | building_59 |
| underflow_valve:upq20 | s | underflow_valve:upq50 | 4.63 | 3.776 | 127 | True | `MID.up.q20 -s-> MID.up.q50 [same role]` | — | nasa_battery, building_59 |
| AC_valve:upq80 | s | P:upq80 | 4.591 | 4.353 | 372 | False | `SLOW.up.q80 -s-> MID.up.q80` | — | building_59 |
| AC_valve:downq80 | s | P:downq80 | 4.55 | 4.647 | 372 | False | `SLOW.down.q80 -s-> MID.down.q80` | — | building_59 |
| compressor:upq80 | s | cw_out:upq20 | 4.541 | 3.5 | 46 | False | `MID.up.q80 -s-> MID.up.q20` | — | building_59 |
| AC_valve:upq20 | s | P:upq20 | 4.514 | 3.528 | 375 | False | `SLOW.up.q20 -s-> MID.up.q20` | — | building_59 |
| underflow_valve:downq80 | s | underflow_valve:downq20 | 4.491 | 6.375 | 48 | True | `MID.down.q80 -s-> MID.down.q20 [same role]` | hai | nasa_battery, building_59 |
| T:downq20 | m | T:upq20 | 4.423 | 4.438 | 491 | True | `MID.down.q20 -m-> MID.up.q20 [same role]` | hai | building_59 |
| feed:upq20 | m | feed:upq50 | 4.397 | 4.24 | 175 | False | `MID.up.q20 -m-> MID.up.q50 [same role]` | hai | building_59 |
| T:upq50 | s | T:upq80 | 4.365 | 5.979 | 173 | True | `MID.up.q50 -s-> MID.up.q80 [same role]` | hai | — |
| feed:downq80 | m | feed:downq50 | 4.345 | 4.138 | 165 | False | `MID.down.q80 -m-> MID.down.q50 [same role]` | hai | building_59 |
| cw_out:upq80 | s | T:upq80 | 4.339 | 3.909 | 78 | True | `MID.up.q80 -s-> MID.up.q80` | — | hai, building_59 |
| compressor:upq20 | s | cw_out:upq20 | 4.339 | 2.616 | 58 | False | `MID.up.q20 -s-> MID.up.q20` | — | hai, building_59 |
| compressor:upq80 | s | feed:upq80 | 4.301 | 3.176 | 36 | False | `MID.up.q80 -s-> MID.up.q80` | — | building_59 |
| feed:downq50 | m | feed:upq20 | 4.298 | 3.523 | 161 | False | `MID.down.q50 -m-> MID.up.q20 [same role]` | — | hai, building_59 |
| P:downq50 | s | P:downq20 | 4.269 | 4.146 | 608 | True | `MID.down.q50 -s-> MID.down.q20 [same role]` | — | — |
| cw_flow:upq20 | s | cw_out:downq80 | 4.206 | 3.935 | 69 | True | `SLOW.up.q20 -s-> MID.down.q80` | — | hai, building_59 |
| purge_C:downq20 | s | P:upq80 | 4.184 | 3.693 | 459 | False | `MID.down.q20 -s-> MID.up.q80` | — | building_59 |
| cw_flow:upq50 | m | cw_flow:downq50 | 4.144 | 4.25 | 730 | True | `SLOW.up.q50 -m-> SLOW.down.q50 [same role]` | hai | — |
| T:downq50 | s | T:downq20 | 4.138 | 4.09 | 227 | True | `MID.down.q50 -s-> MID.down.q20 [same role]` | hai | — |
| purge_valve:trough | s | P:upq50 | 4.121 | 3.857 | 1195 | False | `MID.trough -s-> MID.up.q50` | — | — |
| AC_valve:downq20 | s | P:downq20 | 4.119 | 4.443 | 314 | False | `SLOW.down.q20 -s-> MID.down.q20` | — | building_59 |
| purge_C:downq80 | s | P:upq20 | 4.095 | 3.413 | 467 | False | `MID.down.q80 -s-> MID.up.q20` | — | building_59 |
| purge_C:upq20 | s | P:downq80 | 4.084 | 4.139 | 493 | False | `MID.up.q20 -s-> MID.down.q80` | — | building_59 |
| underflow_valve:downq80 | s | underflow_valve:downq50 | 4.056 | 4.114 | 166 | True | `MID.down.q80 -s-> MID.down.q50 [same role]` | nasa_battery | building_59 |
| cw_flow:upq50 | s | cw_out:downq20 | 3.998 | 2.949 | 82 | True | `SLOW.up.q50 -s-> MID.down.q20` | — | hai |
| cw_out:downq80 | s | cw_out:downq50 | 3.946 | 4.212 | 162 | True | `MID.down.q80 -s-> MID.down.q50 [same role]` | — | hai, building_59 |
| purge_valve:peak | s | P:downq50 | 3.943 | 4.015 | 1184 | False | `MID.peak -s-> MID.down.q50` | — | — |
| A_feed:downq80 | s | T:upq20 | 3.936 | 3.198 | 103 | False | `SLOW.down.q80 -s-> MID.up.q20` | — | hai, building_59 |
| cw_out:downq20 | s | cw_flow:upq80 | 3.895 | 4.483 | 25 | False | `MID.down.q20 -s-> SLOW.up.q80` | building_59 | hai |
| feed:downq50 | m | feed:upq50 | 3.889 | 3.788 | 257 | False | `MID.down.q50 -m-> MID.up.q50 [same role]` | hai, building_59 | — |
| feed:upq20 | m | feed:upq80 | 3.889 | 4.21 | 86 | False | `MID.up.q20 -m-> MID.up.q80 [same role]` | — | hai, building_59 |
| feed:upq50 | m | feed:downq50 | 3.888 | 4.0 | 261 | False | `MID.up.q50 -m-> MID.down.q50 [same role]` | hai, building_59 | — |
| cw_flow:downq20 | s | feed:upq20 | 3.888 | 3.686 | 41 | False | `SLOW.down.q20 -s-> MID.up.q20` | — | hai, building_59 |
| feed:upq20 | m | cw_flow:upq80 | 3.883 | 3.766 | 70 | True | `MID.up.q20 -m-> SLOW.up.q80` | — | hai, building_59 |
| cw_flow:downq50 | m | cw_flow:upq50 | 3.87 | 3.623 | 684 | True | `SLOW.down.q50 -m-> SLOW.up.q50 [same role]` | hai | — |
| T:downq20 | s | T:upq20 | 3.865 | 4.296 | 115 | True | `MID.down.q20 -s-> MID.up.q20 [same role]` | hai | building_59 |
| purge_C:upq80 | s | P:downq20 | 3.854 | 3.48 | 387 | False | `MID.up.q80 -s-> MID.down.q20` | building_59 | — |
| purge:trough | s | P:upq50 | 3.799 | 3.681 | 1138 | False | `MID.trough -s-> MID.up.q50` | — | — |
| P:downq20 | s | P:upq20 | 3.746 | 3.075 | 258 | True | `MID.down.q20 -s-> MID.up.q20 [same role]` | — | building_59 |
| cw_flow:downq50 | m | cw_flow:upq20 | 3.732 | 4.039 | 340 | True | `SLOW.down.q50 -m-> SLOW.up.q20 [same role]` | hai | — |
| A_valve:downq80 | s | T:upq80 | 3.721 | 2.48 | 103 | False | `SLOW.down.q80 -s-> MID.up.q80` | — | hai, building_59 |
| compressor:downq80 | s | cw_out:downq20 | 3.701 | 2.123 | 38 | False | `MID.down.q80 -s-> MID.down.q20` | — | building_59 |
| cw_flow:downq80 | s | cw_out:upq20 | 3.701 | 3.851 | 32 | True | `SLOW.down.q80 -s-> MID.up.q20` | building_59 | hai |
| P:upq80 | m | P:downq80 | 3.696 | 3.632 | 1133 | True | `MID.up.q80 -m-> MID.down.q80 [same role]` | building_59 | — |
| cw_flow:downq20 | s | feed:upq80 | 3.676 | 2.507 | 38 | False | `SLOW.down.q20 -s-> MID.up.q80` | — | hai, building_59 |
| T:downq80 | s | T:downq50 | 3.671 | 3.06 | 203 | True | `MID.down.q80 -s-> MID.down.q50 [same role]` | — | hai |
| cw_out:downq80 | s | cw_flow:upq80 | 3.647 | 3.815 | 36 | True | `MID.down.q80 -s-> SLOW.up.q80` | — | hai, building_59 |
| P:downq20 | m | P:upq20 | 3.604 | 3.723 | 999 | True | `MID.down.q20 -m-> MID.up.q20 [same role]` | building_59 | — |
| purge:peak | s | P:downq50 | 3.59 | 3.492 | 1066 | False | `MID.peak -s-> MID.down.q50` | — | — |
| feed:downq20 | m | feed:upq50 | 3.546 | 3.245 | 139 | False | `MID.down.q20 -m-> MID.up.q50 [same role]` | — | hai, building_59 |
| T:upq80 | s | underflow_valve:downq20 | 3.504 | 4.968 | 36 | True | `MID.up.q80 -s-> MID.down.q20` | — | hai, building_59 |
| A_valve:downq20 | s | T:upq80 | 3.479 | 2.915 | 122 | False | `SLOW.down.q20 -s-> MID.up.q80` | — | hai, building_59 |
| cw_out:upq20 | s | T:upq20 | 3.461 | 3.51 | 87 | True | `MID.up.q20 -s-> MID.up.q20` | — | hai, building_59 |
| A_feed:downq20 | s | T:upq80 | 3.454 | 3.465 | 113 | False | `SLOW.down.q20 -s-> MID.up.q80` | — | hai, building_59 |
| cw_out:upq20 | s | cw_out:upq50 | 3.444 | 4.017 | 127 | True | `MID.up.q20 -s-> MID.up.q50 [same role]` | hai | building_59 |
| compressor:upq20 | s | feed:upq80 | 3.44 | 3.518 | 38 | False | `MID.up.q20 -s-> MID.up.q80` | — | hai, building_59 |
| feed:upq50 | m | feed:downq80 | 3.432 | 3.653 | 128 | False | `MID.up.q50 -m-> MID.down.q80 [same role]` | — | hai, building_59 |
| P:upq80 | s | P:downq80 | 3.429 | 3.059 | 231 | True | `MID.up.q80 -s-> MID.down.q80 [same role]` | building_59 | — |
| cw_out:downq20 | s | feed:upq80 | 3.429 | 1.599 | 27 | False | `MID.down.q20 -s-> MID.up.q80` | — | hai, building_59 |
| A_valve:downq80 | s | T:upq20 | 3.382 | 2.764 | 126 | False | `SLOW.down.q80 -s-> MID.up.q20` | — | hai, building_59 |
| cw_out:downq80 | s | T:downq80 | 3.368 | 3.542 | 70 | True | `MID.down.q80 -s-> MID.down.q80` | — | hai, building_59 |
| feed:upq80 | m | cw_flow:upq80 | 3.355 | 2.262 | 59 | True | `MID.up.q80 -m-> SLOW.up.q80` | building_59 | hai |
| cw_flow:upq20 | s | cw_out:downq20 | 3.351 | 3.568 | 47 | True | `SLOW.up.q20 -s-> MID.down.q20` | building_59 | hai |
| cw_flow:downq20 | s | feed:upq50 | 3.332 | 2.985 | 62 | False | `SLOW.down.q20 -s-> MID.up.q50` | — | hai, building_59 |
| feed:upq20 | l | feed:downq80 | 3.331 | 3.021 | 183 | False | `MID.up.q20 -l-> MID.down.q80 [same role]` | — | hai, building_59 |
| feed:downq50 | l | feed:upq80 | 3.304 | 3.125 | 265 | False | `MID.down.q50 -l-> MID.up.q80 [same role]` | hai | building_59 |
| feed:upq50 | l | feed:upq20 | 3.291 | 3.237 | 264 | False | `MID.up.q50 -l-> MID.up.q20 [same role]` | hai | building_59 |
| cw_flow:downq80 | l | cw_flow:upq80 | 3.265 | 3.495 | 97 | False | `SLOW.down.q80 -l-> SLOW.up.q80 [same role]` | — | hai, nasa_battery, building_59 |
| underflow_valve:downq20 | s | T:downq80 | 3.263 | 4.058 | 37 | False | `MID.down.q20 -s-> MID.down.q80` | — | hai, building_59 |
| feed:upq50 | l | feed:downq20 | 3.261 | 3.419 | 261 | False | `MID.up.q50 -l-> MID.down.q20 [same role]` | hai | building_59 |
| feed:upq20 | l | feed:downq50 | 3.256 | 2.6 | 322 | False | `MID.up.q20 -l-> MID.down.q50 [same role]` | — | hai, building_59 |
| feed:downq50 | l | feed:downq80 | 3.229 | 3.445 | 259 | False | `MID.down.q50 -l-> MID.down.q80 [same role]` | hai | building_59 |
| cw_flow:upq50 | l | cw_flow:upq20 | 3.221 | 3.778 | 320 | True | `SLOW.up.q50 -l-> SLOW.up.q20 [same role]` | hai | — |
| cw_flow:downq20 | m | cw_flow:upq80 | 3.205 | 3.93 | 94 | True | `SLOW.down.q20 -m-> SLOW.up.q80 [same role]` | building_59 | hai, nasa_battery |
| compressor:upq20 | s | cw_out:upq80 | 3.204 | 2.241 | 50 | False | `MID.up.q20 -s-> MID.up.q80` | — | hai, building_59 |
| compressor:downq20 | s | T:downq20 | 3.185 | 1.952 | 77 | False | `MID.down.q20 -s-> MID.down.q20` | — | hai, building_59 |
| cw_flow:downq20 | m | cw_flow:upq50 | 3.18 | 3.257 | 336 | True | `SLOW.down.q20 -m-> SLOW.up.q50 [same role]` | hai | — |
| P:upq20 | s | P:upq50 | 3.176 | 3.081 | 639 | True | `MID.up.q20 -s-> MID.up.q50 [same role]` | — | — |
| compressor:upq80 | m | T:upq80 | 3.176 | 3.295 | 145 | False | `MID.up.q80 -m-> MID.up.q80` | — | building_59 |
| feed:upq80 | l | feed:downq20 | 3.17 | 2.765 | 178 | False | `MID.up.q80 -l-> MID.down.q20 [same role]` | hai | building_59 |
| compressor:downq20 | s | cw_out:downq20 | 3.167 | 2.599 | 40 | False | `MID.down.q20 -s-> MID.down.q20` | — | hai, building_59 |
| feed:upq20 | l | feed:downq20 | 3.166 | 2.837 | 177 | False | `MID.up.q20 -l-> MID.down.q20 [same role]` | — | hai, building_59 |
| A_feed:downq80 | s | cw_flow:upq80 | 3.146 | 2.794 | 29 | False | `SLOW.down.q80 -s-> SLOW.up.q80` | — | hai, building_59 |
| feed:downq80 | l | feed:upq80 | 3.143 | 2.813 | 175 | False | `MID.down.q80 -l-> MID.up.q80 [same role]` | — | hai, building_59 |
| P:downq80 | s | P:downq50 | 3.136 | 2.881 | 644 | True | `MID.down.q80 -s-> MID.down.q50 [same role]` | — | — |
| T:upq20 | s | T:upq50 | 3.134 | 3.546 | 205 | True | `MID.up.q20 -s-> MID.up.q50 [same role]` | — | hai |
| feed:upq80 | m | feed:downq50 | 3.116 | 3.463 | 121 | False | `MID.up.q80 -m-> MID.down.q50 [same role]` | — | hai, building_59 |
| cw_flow:upq20 | m | cw_flow:downq20 | 3.096 | 3.222 | 155 | True | `SLOW.up.q20 -m-> SLOW.down.q20 [same role]` | building_59 | hai, nasa_battery |
| compressor:downq80 | s | T:downq80 | 3.084 | 3.285 | 45 | False | `MID.down.q80 -s-> MID.down.q80` | building_59 | — |
| feed:upq50 | l | feed:downq80 | 3.065 | 2.845 | 241 | False | `MID.up.q50 -l-> MID.down.q80 [same role]` | building_59 | hai |
| underflow_valve:upq20 | m | underflow_valve:downq20 | 3.026 | 2.839 | 63 | True | `MID.up.q20 -m-> MID.down.q20 [same role]` | — | hai, nasa_battery, building_59 |
| A_feed:upq80 | s | T:downq20 | 3.024 | 2.17 | 69 | False | `SLOW.up.q80 -s-> MID.down.q20` | — | hai, building_59 |
| underflow_valve:downq20 | s | cw_out:downq80 | 3.0 | 2.465 | 28 | True | `MID.down.q20 -s-> MID.down.q80` | — | hai, building_59 |
| feed:downq20 | l | feed:upq80 | 2.977 | 3.015 | 171 | False | `MID.down.q20 -l-> MID.up.q80 [same role]` | — | hai, building_59 |
| feed:upq80 | l | feed:downq50 | 2.92 | 2.547 | 290 | False | `MID.up.q80 -l-> MID.down.q50 [same role]` | hai, building_59 | — |
| feed:downq80 | l | feed:upq50 | 2.913 | 2.63 | 292 | False | `MID.down.q80 -l-> MID.up.q50 [same role]` | hai | building_59 |
| cw_flow:downq20 | m | cw_out:downq80 | 2.912 | 2.981 | 148 | True | `SLOW.down.q20 -m-> MID.down.q80` | — | hai, building_59 |
| cw_out:upq80 | s | cw_flow:downq20 | 2.91 | 3.744 | 46 | True | `MID.up.q80 -s-> SLOW.down.q20` | — | hai, building_59 |
| feed:downq20 | l | feed:upq50 | 2.902 | 2.637 | 300 | False | `MID.down.q20 -l-> MID.up.q50 [same role]` | — | hai, building_59 |
| cw_flow:downq80 | m | cw_out:upq20 | 2.891 | 3.902 | 68 | False | `SLOW.down.q80 -m-> MID.up.q20` | building_59 | hai |
| cw_flow:upq50 | m | cw_flow:downq20 | 2.87 | 2.853 | 260 | True | `SLOW.up.q50 -m-> SLOW.down.q20 [same role]` | — | hai |
| underflow:trough | l | underflow:peak | 2.867 | 2.76 | 291 | True | `MID.trough -l-> MID.peak [same role]` | — | hai |
| T:downq80 | s | underflow_valve:upq20 | 2.862 | 3.937 | 41 | True | `MID.down.q80 -s-> MID.up.q20` | — | hai, building_59 |
| underflow_valve:downq50 | m | underflow_valve:upq50 | 2.859 | 2.655 | 809 | True | `MID.down.q50 -m-> MID.up.q50 [same role]` | — | nasa_battery, building_59 |
| cw_out:downq20 | m | cw_flow:downq80 | 2.835 | 3.444 | 67 | True | `MID.down.q20 -m-> SLOW.down.q80` | building_59 | hai |
| T:downq20 | s | cw_out:downq20 | 2.833 | 1.937 | 44 | True | `MID.down.q20 -s-> MID.down.q20` | — | hai, building_59 |
| feed:upq50 | m | cw_flow:upq80 | 2.796 | 2.987 | 85 | False | `MID.up.q50 -m-> SLOW.up.q80` | — | hai, building_59 |
| underflow_valve:upq80 | s | T:upq20 | 2.783 | 3.508 | 62 | False | `MID.up.q80 -s-> MID.up.q20` | — | hai, building_59 |
| T:upq80 | s | underflow_valve:downq80 | 2.781 | 3.764 | 45 | True | `MID.up.q80 -s-> MID.down.q80` | — | hai, building_59 |
| cw_out:upq80 | m | cw_flow:upq20 | 2.779 | 3.318 | 153 | True | `MID.up.q80 -m-> SLOW.up.q20` | — | hai, building_59 |
| A_feed:downq20 | s | cw_flow:upq80 | 2.772 | 2.267 | 43 | False | `SLOW.down.q20 -s-> SLOW.up.q80` | — | hai, building_59 |
| cw_out:upq20 | m | cw_out:downq20 | 2.771 | 2.202 | 100 | False | `MID.up.q20 -m-> MID.down.q20 [same role]` | hai, building_59 | — |
| cw_out:downq20 | s | T:downq20 | 2.747 | 2.174 | 50 | False | `MID.down.q20 -s-> MID.down.q20` | — | hai, building_59 |
| cw_flow:downq20 | s | cw_out:upq80 | 2.739 | 3.043 | 40 | False | `SLOW.down.q20 -s-> MID.up.q80` | — | hai, building_59 |
| underflow:peak | l | underflow:trough | 2.731 | 3.01 | 281 | True | `MID.peak -l-> MID.trough [same role]` | — | hai |
| P:upq20 | s | P:upq80 | 2.717 | 2.648 | 270 | True | `MID.up.q20 -s-> MID.up.q80 [same role]` | building_59 | — |
| P:upq80 | s | T:downq20 | 2.699 | 2.212 | 110 | True | `MID.up.q80 -s-> MID.down.q20` | — | building_59 |
| T:downq80 | m | T:upq80 | 2.695 | 2.902 | 168 | True | `MID.down.q80 -m-> MID.up.q80 [same role]` | hai | building_59 |
| feed:upq20 | l | cw_flow:downq80 | 2.671 | 2.76 | 120 | False | `MID.up.q20 -l-> SLOW.down.q80` | — | hai, building_59 |
| underflow_valve:upq50 | m | underflow_valve:downq50 | 2.662 | 2.48 | 754 | True | `MID.up.q50 -m-> MID.down.q50 [same role]` | — | nasa_battery, building_59 |
| underflow_valve:upq80 | s | cw_out:upq20 | 2.661 | 5.218 | 31 | True | `MID.up.q80 -s-> MID.up.q20` | — | hai, building_59 |
| cw_out:downq50 | s | cw_flow:upq80 | 2.656 | 2.885 | 47 | True | `MID.down.q50 -s-> SLOW.up.q80` | building_59 | hai |
| purge_valve:trough | s | P:upq80 | 2.653 | 2.932 | 380 | False | `MID.trough -s-> MID.up.q80` | — | — |
| A_valve:upq80 | s | T:downq20 | 2.639 | 2.402 | 95 | False | `SLOW.up.q80 -s-> MID.down.q20` | hai | building_59 |
| T:downq20 | s | cw_out:upq20 | 2.635 | 2.658 | 41 | False | `MID.down.q20 -s-> MID.up.q20` | — | hai, building_59 |
| feed:upq20 | m | cw_flow:upq20 | 2.629 | 3.013 | 88 | False | `MID.up.q20 -m-> SLOW.up.q20` | building_59 | hai |
| AC_feed:upq20 | s | P:upq20 | 2.625 | 2.464 | 246 | False | `SLOW.up.q20 -s-> MID.up.q20` | — | building_59 |
| cw_out:upq20 | s | T:upq80 | 2.624 | 3.387 | 49 | True | `MID.up.q20 -s-> MID.up.q80` | — | hai, building_59 |
| AC_valve:downq50 | s | P:downq50 | 2.619 | 2.534 | 1248 | False | `SLOW.down.q50 -s-> MID.down.q50` | — | — |
| T:upq80 | m | underflow_valve:downq20 | 2.614 | 2.384 | 107 | True | `MID.up.q80 -m-> MID.down.q20` | — | hai, building_59 |
| T:downq20 | s | underflow_valve:upq80 | 2.613 | 4.223 | 57 | True | `MID.down.q20 -s-> MID.up.q80` | — | hai, building_59 |
| underflow_valve:downq50 | s | underflow_valve:upq50 | 2.61 | 1.977 | 214 | False | `MID.down.q50 -s-> MID.up.q50 [same role]` | nasa_battery | building_59 |
| feed:downq50 | s | cw_out:upq80 | 2.61 | 1.768 | 39 | True | `MID.down.q50 -s-> MID.up.q80` | — | hai, building_59 |
| feed:downq20 | m | cw_flow:upq20 | 2.609 | 3.391 | 86 | True | `MID.down.q20 -m-> SLOW.up.q20` | building_59 | hai |
| AC_valve:downq20 | m | P:upq20 | 2.604 | 2.452 | 599 | False | `SLOW.down.q20 -m-> MID.up.q20` | — | building_59 |
| T:upq80 | s | cw_out:downq80 | 2.601 | 2.324 | 35 | False | `MID.up.q80 -s-> MID.down.q80` | — | hai, building_59 |
| AC_valve:upq80 | m | P:downq80 | 2.6 | 2.551 | 616 | False | `SLOW.up.q80 -m-> MID.down.q80` | — | building_59 |
| AC_valve:upq50 | s | P:upq50 | 2.588 | 2.292 | 1211 | False | `SLOW.up.q50 -s-> MID.up.q50` | — | — |
| compressor:upq80 | m | cw_flow:upq80 | 2.586 | 2.417 | 56 | False | `MID.up.q80 -m-> SLOW.up.q80` | building_59 | — |
| feed:upq20 | m | cw_out:downq20 | 2.584 | 2.47 | 69 | True | `MID.up.q20 -m-> MID.down.q20` | — | hai, building_59 |
| cw_flow:downq80 | m | cw_flow:upq20 | 2.583 | 2.682 | 76 | False | `SLOW.down.q80 -m-> SLOW.up.q20 [same role]` | building_59 | hai, nasa_battery |
| purge:trough | s | P:upq80 | 2.575 | 2.889 | 381 | False | `MID.trough -s-> MID.up.q80` | — | — |
| compressor:upq20 | s | feed:upq20 | 2.573 | 1.724 | 29 | False | `MID.up.q20 -s-> MID.up.q20` | — | hai, building_59 |
| feed:downq80 | m | cw_flow:downq20 | 2.572 | 2.405 | 82 | False | `MID.down.q80 -m-> SLOW.down.q20` | building_59 | hai |
| cw_flow:upq50 | m | cw_flow:downq80 | 2.571 | 3.637 | 126 | True | `SLOW.up.q50 -m-> SLOW.down.q80 [same role]` | hai | — |
| cw_flow:downq50 | m | cw_flow:upq80 | 2.568 | 2.738 | 126 | True | `SLOW.down.q50 -m-> SLOW.up.q80 [same role]` | hai | — |
| feed:downq80 | m | cw_flow:upq50 | 2.566 | 2.083 | 159 | False | `MID.down.q80 -m-> SLOW.up.q50` | — | hai |
| cw_flow:downq20 | l | cw_flow:downq50 | 2.557 | 2.721 | 459 | True | `SLOW.down.q20 -l-> SLOW.down.q50 [same role]` | hai | — |
| feed:upq20 | m | cw_flow:upq50 | 2.541 | 2.449 | 165 | False | `MID.up.q20 -m-> SLOW.up.q50` | — | hai |
| AC_valve:upq50 | s | P:upq80 | 2.536 | 2.848 | 586 | False | `SLOW.up.q50 -s-> MID.up.q80` | — | — |
| cw_flow:upq20 | l | cw_flow:downq20 | 2.532 | 2.834 | 240 | False | `SLOW.up.q20 -l-> SLOW.down.q20 [same role]` | hai, building_59 | nasa_battery |
| A_feed:downq50 | s | T:upq20 | 2.51 | 2.326 | 175 | False | `SLOW.down.q50 -s-> MID.up.q20` | — | building_59 |
| cw_flow:upq20 | m | cw_flow:downq50 | 2.496 | 2.668 | 243 | True | `SLOW.up.q20 -m-> SLOW.down.q50 [same role]` | — | hai |
| purge_C:upq50 | s | P:downq50 | 2.494 | 2.264 | 1356 | False | `MID.up.q50 -s-> MID.down.q50` | — | — |
| P:downq20 | s | underflow_valve:upq80 | 2.491 | 1.904 | 81 | True | `MID.down.q20 -s-> MID.up.q80` | — | building_59 |
| purge_C:downq50 | s | P:upq50 | 2.481 | 2.153 | 1363 | False | `MID.down.q50 -s-> MID.up.q50` | — | — |
| cw_flow:downq80 | m | cw_out:upq80 | 2.477 | 2.674 | 68 | False | `SLOW.down.q80 -m-> MID.up.q80` | — | hai, building_59 |
| feed:downq80 | m | cw_flow:upq20 | 2.473 | 2.694 | 79 | False | `MID.down.q80 -m-> SLOW.up.q20` | — | hai, building_59 |
| cw_flow:upq20 | m | cw_flow:downq80 | 2.473 | 4.138 | 67 | False | `SLOW.up.q20 -m-> SLOW.down.q80 [same role]` | hai, building_59 | nasa_battery |
| compressor:upq20 | m | cw_flow:upq80 | 2.464 | 2.109 | 68 | False | `MID.up.q20 -m-> SLOW.up.q80` | — | hai, building_59 |
| feed:upq80 | m | cw_flow:upq50 | 2.462 | 2.123 | 156 | True | `MID.up.q80 -m-> SLOW.up.q50` | — | hai |
| purge_C:downq20 | m | P:downq80 | 2.456 | 2.339 | 814 | False | `MID.down.q20 -m-> MID.down.q80` | — | building_59 |
| cw_out:downq80 | s | cw_flow:upq20 | 2.455 | 2.802 | 45 | True | `MID.down.q80 -s-> SLOW.up.q20` | — | hai, building_59 |
| T:downq20 | s | underflow_valve:upq20 | 2.452 | 5.287 | 34 | False | `MID.down.q20 -s-> MID.up.q20` | — | hai, building_59 |
| A_valve:upq20 | s | T:downq80 | 2.449 | 2.27 | 72 | False | `SLOW.up.q20 -s-> MID.down.q80` | — | hai, building_59 |
| cw_flow:downq50 | l | feed:downq80 | 2.444 | 2.033 | 157 | False | `SLOW.down.q50 -l-> MID.down.q80` | — | hai |
| feed:upq50 | m | cw_flow:upq50 | 2.438 | 2.145 | 267 | False | `MID.up.q50 -m-> SLOW.up.q50` | — | hai |
| cw_out:downq80 | m | cw_out:upq80 | 2.429 | 2.223 | 111 | True | `MID.down.q80 -m-> MID.up.q80 [same role]` | — | hai, building_59 |
| cw_flow:downq20 | l | feed:downq80 | 2.423 | 2.666 | 148 | False | `SLOW.down.q20 -l-> MID.down.q80` | hai, building_59 | — |
| T:downq50 | s | underflow_valve:upq20 | 2.422 | 3.691 | 62 | True | `MID.down.q50 -s-> MID.up.q20` | — | hai |
| feed:upq80 | m | cw_flow:downq50 | 2.413 | 2.36 | 153 | False | `MID.up.q80 -m-> SLOW.down.q50` | hai | — |
| feed:downq20 | l | cw_flow:upq80 | 2.413 | 2.872 | 113 | False | `MID.down.q20 -l-> SLOW.up.q80` | — | hai, building_59 |
| A_feed:upq20 | s | T:downq80 | 2.411 | 2.289 | 69 | False | `SLOW.up.q20 -s-> MID.down.q80` | — | hai, building_59 |
| A_feed:downq20 | s | T:upq20 | 2.407 | 2.973 | 106 | False | `SLOW.down.q20 -s-> MID.up.q20` | — | hai, building_59 |
| compressor:upq20 | m | T:upq20 | 2.4 | 1.752 | 188 | False | `MID.up.q20 -m-> MID.up.q20` | — | hai, building_59 |
| T:downq80 | s | cw_out:downq80 | 2.398 | 1.969 | 45 | True | `MID.down.q80 -s-> MID.down.q80` | — | hai, building_59 |
| underflow_valve:downq80 | m | underflow_valve:downq20 | 2.395 | 2.357 | 79 | True | `MID.down.q80 -m-> MID.down.q20 [same role]` | — | hai, nasa_battery, building_59 |
| purge_C:upq80 | m | P:upq20 | 2.389 | 2.243 | 713 | False | `MID.up.q80 -m-> MID.up.q20` | — | building_59 |
| cw_flow:upq80 | l | feed:downq80 | 2.387 | 1.673 | 86 | False | `SLOW.up.q80 -l-> MID.down.q80` | building_59 | hai |
| cw_out:upq50 | s | cw_flow:downq20 | 2.382 | 2.029 | 81 | True | `MID.up.q50 -s-> SLOW.down.q20` | — | hai, building_59 |
| cw_flow:downq80 | m | feed:downq20 | 2.376 | 2.041 | 47 | True | `SLOW.down.q80 -m-> MID.down.q20` | hai | building_59 |
| A_valve:downq50 | s | T:upq20 | 2.373 | 2.309 | 177 | False | `SLOW.down.q50 -s-> MID.up.q20` | — | hai, building_59 |
| feed:downq20 | m | cw_flow:downq20 | 2.37 | 2.928 | 78 | False | `MID.down.q20 -m-> SLOW.down.q20` | hai | building_59 |
| cw_out:upq20 | s | cw_flow:downq80 | 2.364 | 2.061 | 21 | False | `MID.up.q20 -s-> SLOW.down.q80` | — | hai, building_59 |
| underflow:trough | m | underflow_valve:upq20 | 2.358 | 2.42 | 59 | True | `MID.trough -m-> MID.up.q20` | — | hai |
| purge_valve:peak | s | P:downq20 | 2.352 | 2.108 | 328 | False | `MID.peak -s-> MID.down.q20` | — | — |
| A_valve:downq20 | s | T:upq20 | 2.352 | 3.491 | 111 | False | `SLOW.down.q20 -s-> MID.up.q20` | — | hai, building_59 |
| A_valve:downq20 | s | cw_flow:upq80 | 2.345 | 2.885 | 39 | False | `SLOW.down.q20 -s-> SLOW.up.q80` | — | hai, building_59 |
| purge:peak | s | P:downq20 | 2.342 | 1.806 | 323 | False | `MID.peak -s-> MID.down.q20` | — | — |
| cw_flow:upq20 | l | cw_flow:downq50 | 2.338 | 2.48 | 431 | False | `SLOW.up.q20 -l-> SLOW.down.q50 [same role]` | — | hai |
| AC_feed:downq80 | s | P:downq80 | 2.326 | 2.587 | 269 | False | `SLOW.down.q80 -s-> MID.down.q80` | — | building_59 |
| cw_flow:upq80 | m | cw_flow:downq50 | 2.324 | 2.725 | 134 | True | `SLOW.up.q80 -m-> SLOW.down.q50 [same role]` | hai | — |
| AC_feed:downq20 | s | P:downq20 | 2.318 | 2.296 | 202 | False | `SLOW.down.q20 -s-> MID.down.q20` | — | building_59 |
| AC_feed:upq80 | s | P:upq80 | 2.306 | 2.744 | 251 | False | `SLOW.up.q80 -s-> MID.up.q80` | — | building_59 |
| feed:upq80 | l | cw_flow:downq80 | 2.305 | 2.336 | 104 | False | `MID.up.q80 -l-> SLOW.down.q80` | building_59 | hai |
| compressor:upq80 | m | underflow_valve:upq20 | 2.304 | 1.599 | 66 | False | `MID.up.q80 -m-> MID.up.q20` | — | building_59 |
| P:upq80 | s | cw_flow:upq80 | 2.296 | 3.024 | 33 | True | `MID.up.q80 -s-> SLOW.up.q80` | — | building_59 |
| cw_flow:upq80 | l | cw_out:upq20 | 2.294 | 1.928 | 100 | False | `SLOW.up.q80 -l-> MID.up.q20` | building_59 | hai |
| cw_flow:downq50 | s | cw_out:upq80 | 2.29 | 2.585 | 61 | True | `SLOW.down.q50 -s-> MID.up.q80` | — | hai |
| cw_out:downq50 | m | cw_out:upq50 | 2.287 | 2.167 | 529 | True | `MID.down.q50 -m-> MID.up.q50 [same role]` | hai, building_59 | — |
| underflow_valve:upq20 | s | T:upq20 | 2.275 | 1.734 | 35 | False | `MID.up.q20 -s-> MID.up.q20` | — | hai, building_59 |
| underflow_valve:upq50 | m | underflow_valve:downq80 | 2.265 | 2.316 | 264 | True | `MID.up.q50 -m-> MID.down.q80 [same role]` | — | nasa_battery, building_59 |
| AC_valve:upq20 | s | P:upq50 | 2.264 | 1.998 | 405 | False | `SLOW.up.q20 -s-> MID.up.q50` | — | — |
| cw_out:upq20 | l | cw_out:downq20 | 2.262 | 2.489 | 166 | True | `MID.up.q20 -l-> MID.down.q20 [same role]` | — | hai, building_59 |
| cw_flow:upq80 | m | cw_flow:downq20 | 2.26 | 2.68 | 67 | True | `SLOW.up.q80 -m-> SLOW.down.q20 [same role]` | building_59 | hai, nasa_battery |
| L:peak | s | underflow:peak | 2.258 | 1.772 | 42 | True | `MID.peak -s-> MID.peak` | — | hai |
| cw_flow:downq50 | l | cw_flow:downq80 | 2.247 | 2.688 | 118 | False | `SLOW.down.q50 -l-> SLOW.down.q80 [same role]` | hai | — |
| purge_C:downq50 | s | P:upq80 | 2.244 | 2.592 | 609 | False | `MID.down.q50 -s-> MID.up.q80` | — | building_59 |
| cw_out:upq80 | s | T:upq20 | 2.232 | 1.529 | 54 | False | `MID.up.q80 -s-> MID.up.q20` | — | hai, building_59 |
| A_valve:downq50 | s | T:upq80 | 2.22 | 2.235 | 123 | False | `SLOW.down.q50 -s-> MID.up.q80` | — | hai, building_59 |
| T:downq20 | s | P:upq80 | 2.219 | 2.411 | 109 | False | `MID.down.q20 -s-> MID.up.q80` | — | building_59 |
| underflow_valve:upq20 | l | underflow_valve:downq20 | 2.218 | 2.365 | 123 | False | `MID.up.q20 -l-> MID.down.q20 [same role]` | — | hai, nasa_battery, building_59 |
| cw_out:upq50 | m | cw_out:downq50 | 2.217 | 1.976 | 548 | True | `MID.up.q50 -m-> MID.down.q50 [same role]` | building_59 | hai |
| compressor:upq20 | m | T:upq80 | 2.217 | 2.143 | 129 | False | `MID.up.q20 -m-> MID.up.q80` | — | hai, building_59 |
| T:upq20 | m | underflow_valve:downq80 | 2.216 | 2.418 | 173 | True | `MID.up.q20 -m-> MID.down.q80` | — | hai, building_59 |
| T:upq20 | s | P:downq80 | 2.216 | 2.074 | 133 | False | `MID.up.q20 -s-> MID.down.q80` | — | building_59 |
| A_valve:downq80 | s | cw_flow:upq80 | 2.209 | 2.769 | 29 | False | `SLOW.down.q80 -s-> SLOW.up.q80` | — | hai, building_59 |
| A_feed:downq80 | s | T:upq50 | 2.208 | 1.732 | 104 | False | `SLOW.down.q80 -s-> MID.up.q50` | — | hai |
| compressor:upq20 | m | cw_out:downq20 | 2.201 | 1.526 | 90 | False | `MID.up.q20 -m-> MID.down.q20` | — | hai, building_59 |
| underflow_valve:downq80 | m | underflow_valve:upq80 | 2.198 | 2.135 | 114 | True | `MID.down.q80 -m-> MID.up.q80 [same role]` | — | hai, nasa_battery, building_59 |
| compressor:downq20 | m | cw_out:upq20 | 2.197 | 1.71 | 86 | False | `MID.down.q20 -m-> MID.up.q20` | — | hai, building_59 |
| A_feed:downq20 | s | T:upq50 | 2.195 | 1.973 | 174 | False | `SLOW.down.q20 -s-> MID.up.q50` | — | hai |
| purge_C:upq20 | s | P:downq50 | 2.189 | 1.823 | 535 | False | `MID.up.q20 -s-> MID.down.q50` | — | — |
| AC_feed:upq50 | s | P:upq80 | 2.189 | 1.924 | 414 | False | `SLOW.up.q50 -s-> MID.up.q80` | — | building_59 |
| cw_flow:upq50 | l | cw_flow:downq20 | 2.188 | 2.585 | 217 | False | `SLOW.up.q50 -l-> SLOW.down.q20 [same role]` | — | hai |
| compressor:upq50 | s | cw_out:upq20 | 2.185 | 2.323 | 83 | False | `MID.up.q50 -s-> MID.up.q20` | — | building_59 |
| P:downq80 | s | P:downq20 | 2.181 | 2.333 | 208 | True | `MID.down.q80 -s-> MID.down.q20 [same role]` | building_59 | — |
| A_valve:upq20 | s | cw_out:downq20 | 2.176 | 3.019 | 45 | False | `SLOW.up.q20 -s-> MID.down.q20` | — | hai, building_59 |
| purge_C:downq80 | s | P:upq50 | 2.175 | 1.951 | 534 | False | `MID.down.q80 -s-> MID.up.q50` | — | — |
| compressor:downq80 | m | cw_out:upq80 | 2.173 | 1.647 | 72 | False | `MID.down.q80 -m-> MID.up.q80` | — | building_59 |
| cw_out:downq20 | s | underflow_valve:upq80 | 2.171 | 2.155 | 29 | True | `MID.down.q20 -s-> MID.up.q80` | — | hai, building_59 |
| cw_out:upq80 | m | cw_flow:upq80 | 2.159 | 2.704 | 64 | False | `MID.up.q80 -m-> SLOW.up.q80` | — | hai, building_59 |
| P:upq80 | s | underflow_valve:downq20 | 2.156 | 2.285 | 41 | False | `MID.up.q80 -s-> MID.down.q20` | — | building_59 |
| cw_out:downq80 | m | cw_flow:downq80 | 2.155 | 3.329 | 57 | False | `MID.down.q80 -m-> SLOW.down.q80` | — | hai, building_59 |
| T:downq80 | m | underflow_valve:upq20 | 2.148 | 2.313 | 84 | True | `MID.down.q80 -m-> MID.up.q20` | — | hai, building_59 |
| cw_out:upq50 | s | T:upq80 | 2.146 | 2.09 | 83 | True | `MID.up.q50 -s-> MID.up.q80` | — | hai, building_59 |
| feed:upq20 | m | cw_out:downq80 | 2.145 | 1.863 | 67 | True | `MID.up.q20 -m-> MID.down.q80` | — | hai, building_59 |
| L:trough | s | underflow:trough | 2.14 | 3.414 | 40 | True | `MID.trough -s-> MID.trough` | — | hai |
| AC_valve:downq80 | s | P:downq50 | 2.139 | 1.845 | 354 | False | `SLOW.down.q80 -s-> MID.down.q50` | — | — |
| cw_flow:downq80 | m | cw_flow:upq50 | 2.137 | 1.961 | 122 | False | `SLOW.down.q80 -m-> SLOW.up.q50 [same role]` | hai | — |
| A_valve:upq80 | s | T:downq80 | 2.132 | 2.494 | 57 | False | `SLOW.up.q80 -s-> MID.down.q80` | hai | building_59 |
| A_feed:downq50 | s | T:upq80 | 2.124 | 2.088 | 110 | False | `SLOW.down.q50 -s-> MID.up.q80` | — | building_59 |
| cw_out:downq80 | m | cw_out:upq20 | 2.12 | 2.25 | 83 | False | `MID.down.q80 -m-> MID.up.q20 [same role]` | — | hai, building_59 |
| AC_valve:upq20 | m | P:upq80 | 2.119 | 1.955 | 487 | False | `SLOW.up.q20 -m-> MID.up.q80` | — | building_59 |
| T:downq50 | s | P:upq80 | 2.118 | 2.258 | 192 | True | `MID.down.q50 -s-> MID.up.q80` | — | — |
| compressor:downq20 | s | T:downq80 | 2.117 | 1.714 | 38 | False | `MID.down.q20 -s-> MID.down.q80` | — | hai, building_59 |
| A_feed:upq80 | m | cw_flow:downq80 | 2.111 | 1.718 | 51 | False | `SLOW.up.q80 -m-> SLOW.down.q80` | — | hai, building_59 |
| cw_flow:upq80 | l | cw_flow:upq50 | 2.108 | 1.993 | 223 | False | `SLOW.up.q80 -l-> SLOW.up.q50 [same role]` | hai | — |
| compressor:upq50 | s | feed:upq80 | 2.103 | 2.4 | 66 | False | `MID.up.q50 -s-> MID.up.q80` | — | building_59 |
| A_feed:downq80 | s | cw_flow:upq20 | 2.103 | 2.256 | 36 | False | `SLOW.down.q80 -s-> SLOW.up.q20` | — | hai, building_59 |
| A_feed:upq80 | s | cw_out:downq20 | 2.097 | 2.225 | 25 | False | `SLOW.up.q80 -s-> MID.down.q20` | — | hai, building_59 |
| T:upq50 | m | T:downq50 | 2.092 | 2.134 | 660 | True | `MID.up.q50 -m-> MID.down.q50 [same role]` | hai | — |
| cw_flow:upq80 | m | feed:upq80 | 2.09 | 1.565 | 41 | False | `SLOW.up.q80 -m-> MID.up.q80` | — | hai, building_59 |
| purge_valve:trough | m | P:upq80 | 2.082 | 2.233 | 685 | False | `MID.trough -m-> MID.up.q80` | — | — |
| underflow_valve:downq50 | m | underflow_valve:upq20 | 2.082 | 2.849 | 154 | True | `MID.down.q50 -m-> MID.up.q20 [same role]` | — | nasa_battery, building_59 |
| T:upq80 | s | cw_out:upq80 | 2.081 | 1.835 | 28 | True | `MID.up.q80 -s-> MID.up.q80` | — | hai, building_59 |
| AC_valve:downq50 | s | P:downq80 | 2.078 | 2.153 | 489 | False | `SLOW.down.q50 -s-> MID.down.q80` | — | — |
| underflow_valve:upq80 | m | underflow:peak | 2.075 | 2.179 | 90 | True | `MID.up.q80 -m-> MID.peak` | — | hai |
| purge_valve:peak | m | P:downq20 | 2.072 | 1.952 | 663 | False | `MID.peak -m-> MID.down.q20` | — | — |
| cw_out:downq80 | l | cw_out:upq80 | 2.062 | 2.31 | 202 | True | `MID.down.q80 -l-> MID.up.q80 [same role]` | — | hai, building_59 |
| compressor:upq20 | s | feed:upq50 | 2.062 | 1.661 | 41 | False | `MID.up.q20 -s-> MID.up.q50` | — | hai, building_59 |
| underflow_valve:downq20 | s | P:downq80 | 2.06 | 2.37 | 52 | False | `MID.down.q20 -s-> MID.down.q80` | — | building_59 |
| purge:trough | m | P:upq80 | 2.055 | 2.145 | 738 | False | `MID.trough -m-> MID.up.q80` | — | — |
| underflow_valve:upq80 | s | T:upq80 | 2.055 | 2.099 | 34 | False | `MID.up.q80 -s-> MID.up.q80` | — | hai, building_59 |
| underflow_valve:upq80 | s | P:upq20 | 2.053 | 1.657 | 71 | False | `MID.up.q80 -s-> MID.up.q20` | — | building_59 |
| purge_C:upq20 | m | P:downq20 | 2.051 | 1.799 | 616 | False | `MID.up.q20 -m-> MID.down.q20` | — | building_59 |
| underflow_valve:downq20 | m | underflow_valve:upq50 | 2.051 | 1.825 | 168 | True | `MID.down.q20 -m-> MID.up.q50 [same role]` | — | nasa_battery, building_59 |
| cw_flow:downq20 | s | P:downq20 | 2.047 | 2.592 | 76 | True | `SLOW.down.q20 -s-> MID.down.q20` | — | building_59 |
| underflow_valve:upq80 | l | underflow_valve:downq20 | 2.037 | 2.681 | 157 | True | `MID.up.q80 -l-> MID.down.q20 [same role]` | — | hai, nasa_battery, building_59 |
| P:downq50 | s | underflow_valve:upq20 | 2.035 | 1.783 | 87 | True | `MID.down.q50 -s-> MID.up.q20` | — | — |
| P:downq20 | s | T:upq80 | 2.033 | 2.0 | 67 | True | `MID.down.q20 -s-> MID.up.q80` | — | building_59 |
| cw_flow:upq20 | m | cw_out:downq80 | 2.03 | 1.996 | 95 | True | `SLOW.up.q20 -m-> MID.down.q80` | — | hai, building_59 |
| cw_out:upq50 | s | T:upq50 | 2.028 | 1.999 | 190 | True | `MID.up.q50 -s-> MID.up.q50` | — | hai |
| cw_out:downq80 | s | cw_flow:upq50 | 2.025 | 1.829 | 72 | True | `MID.down.q80 -s-> SLOW.up.q50` | — | hai |
| AC_valve:downq50 | s | P:downq20 | 2.024 | 2.018 | 448 | False | `SLOW.down.q50 -s-> MID.down.q20` | — | — |
| purge_valve:peak | m | T:upq80 | 2.018 | 2.098 | 309 | False | `MID.peak -m-> MID.up.q80` | — | hai |
| T:upq50 | s | P:downq20 | 2.016 | 1.833 | 167 | False | `MID.up.q50 -s-> MID.down.q20` | — | — |
| A_valve:downq20 | s | T:upq50 | 2.013 | 2.161 | 171 | False | `SLOW.down.q20 -s-> MID.up.q50` | hai | — |
| A_feed:upq80 | m | cw_out:upq20 | 2.013 | 1.9 | 72 | False | `SLOW.up.q80 -m-> MID.up.q20` | — | hai, building_59 |
| L:peak | s | underflow_valve:downq80 | 2.012 | 1.813 | 48 | True | `MID.peak -s-> MID.down.q80` | hai | building_59 |
| compressor:downq50 | s | T:downq80 | 2.011 | 2.112 | 111 | False | `MID.down.q50 -s-> MID.down.q80` | — | building_59 |
| underflow_valve:downq20 | s | cw_out:downq20 | 2.005 | 1.538 | 16 | True | `MID.down.q20 -s-> MID.down.q20` | — | hai, building_59 |
| A_valve:upq50 | s | T:downq80 | 2.004 | 2.67 | 108 | False | `SLOW.up.q50 -s-> MID.down.q80` | hai | building_59 |
| cw_out:upq50 | m | cw_flow:upq20 | 2.002 | 2.277 | 221 | True | `MID.up.q50 -m-> SLOW.up.q20` | building_59 | hai |
| underflow_valve:downq80 | s | T:downq80 | 1.999 | 2.474 | 34 | True | `MID.down.q80 -s-> MID.down.q80` | — | hai, building_59 |
| underflow:peak | m | underflow_valve:downq80 | 1.995 | 2.345 | 79 | True | `MID.peak -m-> MID.down.q80` | — | hai |
| cw_out:upq80 | m | feed:upq20 | 1.994 | 1.708 | 74 | True | `MID.up.q80 -m-> MID.up.q20` | — | hai, building_59 |
| AC_feed:upq50 | s | P:upq50 | 1.99 | 1.7 | 762 | False | `SLOW.up.q50 -s-> MID.up.q50` | — | — |
| purge:peak | m | T:upq80 | 1.985 | 2.057 | 332 | False | `MID.peak -m-> MID.up.q80` | — | hai |
| P:downq20 | s | underflow_valve:upq20 | 1.983 | 2.416 | 41 | True | `MID.down.q20 -s-> MID.up.q20` | — | building_59 |
| cw_flow:upq80 | m | cw_out:upq20 | 1.98 | 3.727 | 47 | False | `SLOW.up.q80 -m-> MID.up.q20` | building_59 | hai |
| purge:peak | m | P:downq20 | 1.979 | 1.853 | 692 | False | `MID.peak -m-> MID.down.q20` | — | — |
| AC_valve:upq80 | s | T:downq20 | 1.979 | 2.044 | 97 | False | `SLOW.up.q80 -s-> MID.down.q20` | — | hai, building_59 |
| cw_flow:downq80 | s | P:downq80 | 1.979 | 1.866 | 54 | True | `SLOW.down.q80 -s-> MID.down.q80` | — | building_59 |
| AC_valve:downq80 | m | P:downq20 | 1.974 | 1.71 | 426 | False | `SLOW.down.q80 -m-> MID.down.q20` | — | building_59 |
| cw_flow:downq80 | m | feed:downq50 | 1.972 | 1.994 | 69 | False | `SLOW.down.q80 -m-> MID.down.q50` | hai | building_59 |
| cw_out:downq80 | l | feed:downq20 | 1.97 | 1.732 | 139 | True | `MID.down.q80 -l-> MID.down.q20` | building_59 | hai |
| purge_C:downq80 | m | P:upq80 | 1.969 | 1.895 | 586 | False | `MID.down.q80 -m-> MID.up.q80` | — | building_59 |
| P:downq80 | s | cw_flow:downq20 | 1.969 | 1.939 | 79 | True | `MID.down.q80 -s-> SLOW.down.q20` | — | building_59 |
| cw_out:upq20 | l | cw_out:downq80 | 1.968 | 2.031 | 169 | True | `MID.up.q20 -l-> MID.down.q80 [same role]` | — | hai, building_59 |
| recycle:upq20 | s | cw_out:upq20 | 1.957 | 1.633 | 46 | False | `MID.up.q20 -s-> MID.up.q20` | — | hai |
| A_valve:upq80 | s | P:upq20 | 1.948 | 1.546 | 109 | False | `SLOW.up.q80 -s-> MID.up.q20` | — | building_59 |
| feed:downq80 | m | cw_out:upq80 | 1.946 | 1.757 | 58 | False | `MID.down.q80 -m-> MID.up.q80` | — | hai, building_59 |
| cw_out:upq50 | m | cw_out:downq80 | 1.942 | 2.282 | 200 | True | `MID.up.q50 -m-> MID.down.q80 [same role]` | — | hai, building_59 |
| P:downq20 | m | cw_flow:upq80 | 1.94 | 2.106 | 122 | True | `MID.down.q20 -m-> SLOW.up.q80` | — | building_59 |
| AC_valve:downq80 | s | T:upq20 | 1.938 | 1.88 | 96 | False | `SLOW.down.q80 -s-> MID.up.q20` | — | hai, building_59 |
| cw_out:upq80 | m | cw_out:downq20 | 1.935 | 1.953 | 85 | False | `MID.up.q80 -m-> MID.down.q20 [same role]` | — | hai, building_59 |
| cw_flow:downq20 | m | cw_out:downq20 | 1.934 | 2.881 | 84 | True | `SLOW.down.q20 -m-> MID.down.q20` | — | hai, building_59 |
| underflow_valve:upq80 | m | underflow_valve:downq50 | 1.93 | 1.699 | 261 | True | `MID.up.q80 -m-> MID.down.q50 [same role]` | nasa_battery | building_59 |
| underflow_valve:upq20 | m | T:upq80 | 1.929 | 2.651 | 64 | False | `MID.up.q20 -m-> MID.up.q80` | — | hai, building_59 |
| underflow_valve:downq80 | m | underflow_valve:downq50 | 1.924 | 1.754 | 243 | True | `MID.down.q80 -m-> MID.down.q50 [same role]` | — | nasa_battery, building_59 |
| P:upq50 | m | P:downq80 | 1.923 | 1.999 | 983 | True | `MID.up.q50 -m-> MID.down.q80 [same role]` | — | — |
| AC_feed:upq20 | s | P:upq50 | 1.923 | 1.826 | 388 | False | `SLOW.up.q20 -s-> MID.up.q50` | — | — |
| compressor:upq20 | s | cw_out:upq50 | 1.92 | 1.503 | 72 | False | `MID.up.q20 -s-> MID.up.q50` | — | hai, building_59 |
| T:downq50 | m | T:upq50 | 1.914 | 1.91 | 602 | True | `MID.down.q50 -m-> MID.up.q50 [same role]` | hai | — |
| underflow_valve:downq20 | m | T:downq80 | 1.908 | 2.216 | 65 | False | `MID.down.q20 -m-> MID.down.q80` | — | hai, building_59 |
| AC_feed:downq80 | s | P:downq50 | 1.905 | 1.639 | 446 | False | `SLOW.down.q80 -s-> MID.down.q50` | — | — |
| AC_valve:downq20 | s | P:downq50 | 1.901 | 2.043 | 312 | False | `SLOW.down.q20 -s-> MID.down.q50` | — | — |
| T:upq80 | s | P:downq20 | 1.899 | 1.732 | 65 | False | `MID.up.q80 -s-> MID.down.q20` | — | building_59 |
| cw_out:downq80 | l | cw_flow:upq20 | 1.896 | 2.121 | 199 | True | `MID.down.q80 -l-> SLOW.up.q20` | — | hai, building_59 |
| P:upq50 | s | cw_flow:upq80 | 1.893 | 2.945 | 61 | True | `MID.up.q50 -s-> SLOW.up.q80` | — | — |
| compressor:upq80 | m | cw_out:downq80 | 1.892 | 2.034 | 71 | False | `MID.up.q80 -m-> MID.down.q80` | — | building_59 |
| underflow:trough | m | underflow_valve:upq50 | 1.891 | 1.53 | 181 | True | `MID.trough -m-> MID.up.q50` | — | — |
| P:downq20 | s | T:downq80 | 1.884 | 1.943 | 62 | True | `MID.down.q20 -s-> MID.down.q80` | — | building_59 |
| feed:downq80 | m | cw_out:upq20 | 1.88 | 1.905 | 48 | False | `MID.down.q80 -m-> MID.up.q20` | building_59 | hai |
| purge_C:upq50 | s | P:downq20 | 1.877 | 2.044 | 474 | False | `MID.up.q50 -s-> MID.down.q20` | — | building_59 |
| AC_valve:downq20 | s | cw_flow:downq20 | 1.871 | 1.769 | 60 | False | `SLOW.down.q20 -s-> SLOW.down.q20` | — | hai, building_59 |
| cw_out:downq80 | m | T:upq80 | 1.87 | 1.553 | 104 | True | `MID.down.q80 -m-> MID.up.q80` | — | hai, building_59 |
| T:upq80 | m | cw_out:downq80 | 1.865 | 1.916 | 100 | True | `MID.up.q80 -m-> MID.down.q80` | — | hai, building_59 |
| P:downq20 | s | cw_flow:downq20 | 1.863 | 2.482 | 54 | True | `MID.down.q20 -s-> SLOW.down.q20` | — | building_59 |
| cw_out:downq50 | s | T:downq50 | 1.86 | 1.56 | 168 | True | `MID.down.q50 -s-> MID.down.q50` | — | hai |
| compressor:downq80 | m | T:upq80 | 1.86 | 1.874 | 75 | False | `MID.down.q80 -m-> MID.up.q80` | — | building_59 |
| T:downq20 | m | underflow_valve:upq80 | 1.856 | 1.69 | 151 | True | `MID.down.q20 -m-> MID.up.q80` | — | hai, building_59 |
| purge_C:downq50 | l | P:downq20 | 1.849 | 1.736 | 754 | False | `MID.down.q50 -l-> MID.down.q20` | — | building_59 |
| cw_out:upq80 | l | cw_flow:downq80 | 1.846 | 2.614 | 102 | False | `MID.up.q80 -l-> SLOW.down.q80` | — | hai, building_59 |
| T:downq20 | m | P:downq80 | 1.844 | 1.761 | 338 | True | `MID.down.q20 -m-> MID.down.q80` | — | building_59 |
| feed:upq50 | m | cw_out:downq20 | 1.843 | 2.06 | 83 | True | `MID.up.q50 -m-> MID.down.q20` | — | hai, building_59 |
| AC_feed:downq50 | s | P:downq20 | 1.842 | 2.019 | 324 | False | `SLOW.down.q50 -s-> MID.down.q20` | — | building_59 |
| AC_valve:downq20 | m | P:upq50 | 1.84 | 1.609 | 911 | False | `SLOW.down.q20 -m-> MID.up.q50` | — | — |
| purge_C:upq80 | m | P:upq50 | 1.837 | 1.566 | 1180 | False | `MID.up.q80 -m-> MID.up.q50` | — | — |
| T:upq80 | s | underflow_valve:downq50 | 1.831 | 1.716 | 72 | True | `MID.up.q80 -s-> MID.down.q50` | — | building_59 |
| cw_out:upq80 | m | T:downq80 | 1.826 | 1.732 | 114 | True | `MID.up.q80 -m-> MID.down.q80` | — | hai, building_59 |
| P:downq50 | m | P:upq20 | 1.825 | 1.808 | 888 | True | `MID.down.q50 -m-> MID.up.q20 [same role]` | — | — |
| cw_out:downq80 | s | T:downq20 | 1.822 | 1.713 | 51 | True | `MID.down.q80 -s-> MID.down.q20` | — | hai, building_59 |
| P:downq80 | s | underflow_valve:upq20 | 1.816 | 1.833 | 52 | True | `MID.down.q80 -s-> MID.up.q20` | — | building_59 |
| T:upq80 | l | underflow_valve:upq20 | 1.813 | 2.053 | 147 | True | `MID.up.q80 -l-> MID.up.q20` | — | hai, building_59 |
| P:upq20 | m | cw_flow:downq80 | 1.811 | 2.068 | 102 | True | `MID.up.q20 -m-> SLOW.down.q80` | — | building_59 |
| T:upq20 | m | T:downq20 | 1.808 | 1.777 | 192 | True | `MID.up.q20 -m-> MID.down.q20 [same role]` | hai, building_59 | — |
| purge_C:downq20 | s | T:downq20 | 1.808 | 1.77 | 120 | False | `MID.down.q20 -s-> MID.down.q20` | — | hai, building_59 |
| A_valve:upq80 | s | cw_out:downq20 | 1.808 | 2.203 | 34 | False | `SLOW.up.q80 -s-> MID.down.q20` | — | hai, building_59 |
| A_valve:downq80 | s | cw_flow:upq20 | 1.805 | 1.822 | 44 | False | `SLOW.down.q80 -s-> SLOW.up.q20` | — | hai, building_59 |
| AC_valve:upq50 | s | P:upq20 | 1.804 | 1.528 | 392 | False | `SLOW.up.q50 -s-> MID.up.q20` | — | — |
| feed:upq50 | m | cw_out:downq80 | 1.803 | 1.649 | 95 | True | `MID.up.q50 -m-> MID.down.q80` | — | hai, building_59 |
| purge_C:downq20 | s | P:upq50 | 1.801 | 1.623 | 400 | False | `MID.down.q20 -s-> MID.up.q50` | — | — |
| cw_flow:downq50 | s | P:downq20 | 1.801 | 1.84 | 122 | True | `SLOW.down.q50 -s-> MID.down.q20` | — | — |
| cw_out:upq80 | m | cw_flow:downq20 | 1.801 | 2.442 | 99 | False | `MID.up.q80 -m-> SLOW.down.q20` | — | hai, building_59 |
| purge_C:upq50 | s | P:downq80 | 1.799 | 1.668 | 483 | False | `MID.up.q50 -s-> MID.down.q80` | — | building_59 |
| underflow_valve:upq50 | l | underflow_valve:downq20 | 1.799 | 2.21 | 211 | True | `MID.up.q50 -l-> MID.down.q20 [same role]` | — | nasa_battery, building_59 |
| AC_valve:upq80 | s | P:upq50 | 1.798 | 1.668 | 295 | False | `SLOW.up.q80 -s-> MID.up.q50` | — | — |
| AC_feed:downq20 | m | P:upq20 | 1.797 | 1.95 | 503 | False | `SLOW.down.q20 -m-> MID.up.q20` | — | building_59 |
| recycle:upq20 | m | cw_flow:upq80 | 1.795 | 1.711 | 90 | False | `MID.up.q20 -m-> SLOW.up.q80` | — | hai |
| A_valve:upq80 | m | cw_out:upq20 | 1.794 | 1.726 | 97 | False | `SLOW.up.q80 -m-> MID.up.q20` | hai | building_59 |
| cw_out:downq50 | s | T:downq20 | 1.794 | 1.506 | 90 | False | `MID.down.q50 -s-> MID.down.q20` | — | hai, building_59 |
| P:downq20 | s | feed:downq20 | 1.794 | 2.15 | 35 | True | `MID.down.q20 -s-> MID.down.q20` | — | building_59 |
| compressor:upq80 | l | T:downq80 | 1.791 | 1.666 | 184 | False | `MID.up.q80 -l-> MID.down.q80` | building_59 | — |
| A_feed:upq20 | s | cw_out:downq20 | 1.788 | 2.563 | 36 | False | `SLOW.up.q20 -s-> MID.down.q20` | — | hai, building_59 |
| AC_feed:upq80 | m | P:downq80 | 1.787 | 2.051 | 613 | False | `SLOW.up.q80 -m-> MID.down.q80` | — | building_59 |
| cw_out:upq80 | l | cw_out:upq20 | 1.786 | 2.416 | 146 | False | `MID.up.q80 -l-> MID.up.q20 [same role]` | — | hai, building_59 |
| purge_C:upq50 | l | P:upq80 | 1.781 | 1.813 | 776 | False | `MID.up.q50 -l-> MID.up.q80` | — | building_59 |
| cw_flow:downq50 | s | cw_out:upq50 | 1.781 | 2.18 | 114 | True | `SLOW.down.q50 -s-> MID.up.q50` | — | hai |
| cw_out:upq20 | m | cw_out:downq80 | 1.777 | 2.133 | 75 | False | `MID.up.q20 -m-> MID.down.q80 [same role]` | — | hai, building_59 |
| A_valve:upq20 | s | cw_out:downq80 | 1.777 | 2.225 | 43 | False | `SLOW.up.q20 -s-> MID.down.q80` | — | hai, building_59 |
| cw_out:upq80 | s | underflow_valve:downq20 | 1.773 | 1.968 | 20 | True | `MID.up.q80 -s-> MID.down.q20` | — | hai, building_59 |
| underflow_valve:downq50 | l | underflow_valve:upq80 | 1.771 | 1.981 | 317 | True | `MID.down.q50 -l-> MID.up.q80 [same role]` | — | nasa_battery, building_59 |
| cw_out:downq20 | l | cw_flow:upq80 | 1.765 | 1.619 | 91 | False | `MID.down.q20 -l-> SLOW.up.q80` | — | hai, building_59 |
| P:upq80 | s | T:upq20 | 1.765 | 2.643 | 72 | True | `MID.up.q80 -s-> MID.up.q20` | — | building_59 |
| AC_feed:upq80 | s | cw_flow:upq80 | 1.765 | 1.825 | 41 | False | `SLOW.up.q80 -s-> SLOW.up.q80` | — | hai, building_59 |
| AC_valve:upq50 | m | P:downq80 | 1.761 | 1.888 | 1016 | False | `SLOW.up.q50 -m-> MID.down.q80` | — | — |
| T:downq50 | s | P:upq50 | 1.76 | 1.64 | 323 | False | `MID.down.q50 -s-> MID.up.q50` | — | — |
| cw_out:downq80 | l | cw_flow:downq20 | 1.756 | 2.246 | 184 | True | `MID.down.q80 -l-> SLOW.down.q20` | — | hai, building_59 |
| underflow:peak | m | underflow_valve:downq50 | 1.756 | 1.829 | 169 | True | `MID.peak -m-> MID.down.q50` | — | — |
| T:upq50 | s | P:downq50 | 1.755 | 1.516 | 313 | True | `MID.up.q50 -s-> MID.down.q50` | — | — |
| feed:downq80 | l | cw_out:downq20 | 1.755 | 1.846 | 118 | True | `MID.down.q80 -l-> MID.down.q20` | — | hai, building_59 |
| compressor:upq20 | s | P:upq80 | 1.754 | 1.888 | 74 | False | `MID.up.q20 -s-> MID.up.q80` | — | building_59 |
| cw_out:upq20 | s | cw_flow:downq50 | 1.754 | 2.085 | 56 | True | `MID.up.q20 -s-> SLOW.down.q50` | — | hai |
| cw_flow:upq20 | l | cw_out:upq20 | 1.753 | 1.852 | 133 | False | `SLOW.up.q20 -l-> MID.up.q20` | — | hai, building_59 |
| P:downq80 | m | T:upq80 | 1.751 | 1.954 | 222 | True | `MID.down.q80 -m-> MID.up.q80` | — | building_59 |
| A_feed:upq50 | s | P:upq20 | 1.749 | 1.617 | 182 | False | `SLOW.up.q50 -s-> MID.up.q20` | — | building_59 |
| P:downq20 | m | cw_out:downq20 | 1.749 | 1.528 | 163 | True | `MID.down.q20 -m-> MID.down.q20` | — | building_59 |
| cw_flow:upq80 | l | cw_out:upq80 | 1.749 | 1.589 | 89 | False | `SLOW.up.q80 -l-> MID.up.q80` | — | hai, building_59 |
| cw_flow:downq80 | m | cw_out:downq20 | 1.747 | 1.564 | 41 | False | `SLOW.down.q80 -m-> MID.down.q20` | building_59 | hai |
| cw_out:upq20 | m | cw_flow:upq20 | 1.746 | 2.069 | 79 | False | `MID.up.q20 -m-> SLOW.up.q20` | building_59 | hai |
| compressor:upq80 | m | cw_out:downq20 | 1.746 | 1.564 | 56 | False | `MID.up.q80 -m-> MID.down.q20` | — | building_59 |
| feed:upq20 | l | cw_out:upq20 | 1.745 | 1.838 | 116 | False | `MID.up.q20 -l-> MID.up.q20` | — | hai, building_59 |
| P:upq20 | s | cw_flow:upq80 | 1.745 | 2.941 | 37 | True | `MID.up.q20 -s-> SLOW.up.q80` | — | building_59 |
| purge_C:downq20 | m | P:downq50 | 1.741 | 1.582 | 1168 | False | `MID.down.q20 -m-> MID.down.q50` | — | — |
| cw_out:downq50 | m | cw_out:downq20 | 1.738 | 1.938 | 143 | True | `MID.down.q50 -m-> MID.down.q20 [same role]` | hai | building_59 |
| compressor:downq80 | m | T:downq80 | 1.738 | 1.981 | 70 | False | `MID.down.q80 -m-> MID.down.q80` | building_59 | — |
| T:downq80 | m | underflow_valve:downq20 | 1.738 | 1.892 | 68 | True | `MID.down.q80 -m-> MID.down.q20` | — | hai, building_59 |
| T:downq80 | m | cw_out:upq80 | 1.737 | 1.573 | 89 | True | `MID.down.q80 -m-> MID.up.q80` | — | hai, building_59 |
| underflow_valve:upq20 | l | T:downq20 | 1.733 | 1.517 | 206 | True | `MID.up.q20 -l-> MID.down.q20` | — | hai, building_59 |
| underflow_valve:downq20 | l | T:downq80 | 1.733 | 2.155 | 147 | False | `MID.down.q20 -l-> MID.down.q80` | — | hai, building_59 |
| A_feed:downq80 | m | cw_out:downq20 | 1.729 | 1.772 | 60 | False | `SLOW.down.q80 -m-> MID.down.q20` | hai | building_59 |
| purge_C:upq80 | s | T:upq80 | 1.728 | 1.535 | 83 | False | `MID.up.q80 -s-> MID.up.q80` | — | hai, building_59 |
| P:downq80 | m | P:downq20 | 1.725 | 1.547 | 457 | True | `MID.down.q80 -m-> MID.down.q20 [same role]` | — | building_59 |
| compressor:downq50 | s | cw_out:downq20 | 1.725 | 1.982 | 67 | False | `MID.down.q50 -s-> MID.down.q20` | — | building_59 |
| T:downq20 | m | cw_out:upq20 | 1.723 | 1.941 | 100 | True | `MID.down.q20 -m-> MID.up.q20` | — | hai, building_59 |
| underflow_valve:upq50 | l | underflow:peak | 1.722 | 1.594 | 248 | True | `MID.up.q50 -l-> MID.peak` | — | — |
| A_valve:downq20 | s | P:downq80 | 1.72 | 1.767 | 134 | False | `SLOW.down.q20 -s-> MID.down.q80` | — | building_59 |
| AC_valve:upq20 | m | T:downq20 | 1.718 | 1.75 | 239 | False | `SLOW.up.q20 -m-> MID.down.q20` | — | hai, building_59 |
| cw_out:upq50 | l | cw_out:upq20 | 1.717 | 2.16 | 257 | True | `MID.up.q50 -l-> MID.up.q20 [same role]` | hai | building_59 |
| feed:downq20 | l | cw_out:downq20 | 1.716 | 1.965 | 119 | True | `MID.down.q20 -l-> MID.down.q20` | — | hai, building_59 |
| cw_flow:downq80 | s | P:downq20 | 1.714 | 1.831 | 44 | False | `SLOW.down.q80 -s-> MID.down.q20` | — | building_59 |
| feed_F:upq20 | m | cw_out:upq20 | 1.711 | 1.72 | 40 | False | `SLOW.up.q20 -m-> MID.up.q20` | — | hai, building_59 |
| cw_out:downq50 | m | cw_out:upq20 | 1.71 | 2.349 | 141 | False | `MID.down.q50 -m-> MID.up.q20 [same role]` | hai | building_59 |
| purge:trough | m | P:downq80 | 1.707 | 1.969 | 613 | False | `MID.trough -m-> MID.down.q80` | — | — |
| purge_valve:peak | m | cw_flow:upq20 | 1.706 | 1.815 | 230 | False | `MID.peak -m-> SLOW.up.q20` | — | hai |
| feed:upq80 | m | cw_out:downq80 | 1.706 | 1.616 | 52 | False | `MID.up.q80 -m-> MID.down.q80` | — | hai, building_59 |
| underflow_valve:downq20 | m | T:upq80 | 1.7 | 1.77 | 58 | False | `MID.down.q20 -m-> MID.up.q80` | — | hai, building_59 |
| purge_valve:trough | m | P:downq80 | 1.696 | 1.956 | 558 | False | `MID.trough -m-> MID.down.q80` | — | — |
| P:downq20 | m | cw_flow:upq20 | 1.695 | 1.693 | 198 | True | `MID.down.q20 -m-> SLOW.up.q20` | — | building_59 |
| cw_out:downq20 | m | feed:upq80 | 1.695 | 1.724 | 49 | True | `MID.down.q20 -m-> MID.up.q80` | — | hai, building_59 |
| T:upq50 | m | underflow_valve:downq50 | 1.694 | 1.509 | 530 | True | `MID.up.q50 -m-> MID.down.q50` | — | — |
| feed:upq80 | l | cw_out:upq20 | 1.693 | 1.78 | 113 | True | `MID.up.q80 -l-> MID.up.q20` | building_59 | hai |
| A_feed:upq50 | s | T:downq80 | 1.689 | 2.268 | 84 | False | `SLOW.up.q50 -s-> MID.down.q80` | building_59 | — |
| T:upq50 | m | underflow_valve:downq80 | 1.685 | 1.619 | 217 | True | `MID.up.q50 -m-> MID.down.q80` | hai | — |
| compressor:downq20 | s | T:downq50 | 1.677 | 1.744 | 73 | False | `MID.down.q20 -s-> MID.down.q50` | — | hai |
| AC_valve:upq80 | m | P:downq50 | 1.674 | 1.571 | 803 | False | `SLOW.up.q80 -m-> MID.down.q50` | — | — |
| compressor:downq80 | l | underflow_valve:upq20 | 1.674 | 1.712 | 112 | False | `MID.down.q80 -l-> MID.up.q20` | — | building_59 |
| A_valve:downq50 | s | cw_flow:upq80 | 1.674 | 2.062 | 44 | False | `SLOW.down.q50 -s-> SLOW.up.q80` | — | hai, building_59 |
| underflow_valve:upq50 | m | underflow:peak | 1.673 | 1.814 | 152 | True | `MID.up.q50 -m-> MID.peak` | — | — |
| compressor:upq80 | l | underflow_valve:downq20 | 1.673 | 1.716 | 108 | False | `MID.up.q80 -l-> MID.down.q20` | — | building_59 |
| P:upq50 | s | T:downq50 | 1.671 | 1.522 | 275 | True | `MID.up.q50 -s-> MID.down.q50` | — | — |
| recycle:upq20 | s | underflow_valve:upq20 | 1.671 | 1.639 | 35 | False | `MID.up.q20 -s-> MID.up.q20` | — | hai |
| AC_valve:downq50 | m | P:upq20 | 1.669 | 1.533 | 894 | False | `SLOW.down.q50 -m-> MID.up.q20` | — | — |
| A_feed:downq50 | s | cw_flow:upq80 | 1.669 | 1.981 | 41 | False | `SLOW.down.q50 -s-> SLOW.up.q80` | building_59 | — |
| cw_out:downq50 | l | feed:downq20 | 1.668 | 1.589 | 217 | True | `MID.down.q50 -l-> MID.down.q20` | building_59 | hai |
| P:upq50 | l | P:upq20 | 1.667 | 1.643 | 1123 | True | `MID.up.q50 -l-> MID.up.q20 [same role]` | — | — |
| P:upq50 | s | underflow_valve:downq20 | 1.665 | 1.942 | 71 | True | `MID.up.q50 -s-> MID.down.q20` | — | — |
| AC_feed:downq20 | s | feed:downq20 | 1.661 | 1.97 | 41 | False | `SLOW.down.q20 -s-> MID.down.q20` | — | hai, building_59 |
| cw_out:upq50 | l | cw_out:downq20 | 1.66 | 2.027 | 248 | True | `MID.up.q50 -l-> MID.down.q20 [same role]` | — | hai, building_59 |
| feed_F:upq20 | m | T:downq80 | 1.659 | 1.698 | 55 | False | `SLOW.up.q20 -m-> MID.down.q80` | — | hai, building_59 |
| purge_C:upq20 | s | cw_flow:downq50 | 1.658 | 1.944 | 154 | False | `MID.up.q20 -s-> SLOW.down.q50` | — | hai |
| A_feed:upq50 | s | T:downq20 | 1.658 | 1.795 | 111 | False | `SLOW.up.q50 -s-> MID.down.q20` | — | building_59 |
| cw_out:downq80 | l | cw_out:upq20 | 1.657 | 2.24 | 139 | False | `MID.down.q80 -l-> MID.up.q20 [same role]` | — | hai, building_59 |
| purge_C:downq80 | m | T:downq20 | 1.655 | 1.63 | 298 | False | `MID.down.q80 -m-> MID.down.q20` | building_59 | hai |
| AC_valve:downq50 | l | P:upq80 | 1.654 | 1.742 | 880 | False | `SLOW.down.q50 -l-> MID.up.q80` | — | — |
| underflow:trough | m | underflow_valve:upq80 | 1.652 | 1.737 | 65 | True | `MID.trough -m-> MID.up.q80` | — | hai |
| T:downq20 | m | T:upq80 | 1.649 | 2.362 | 136 | True | `MID.down.q20 -m-> MID.up.q80 [same role]` | — | hai, building_59 |
| P:upq80 | m | cw_flow:downq80 | 1.646 | 2.051 | 108 | True | `MID.up.q80 -m-> SLOW.down.q80` | — | building_59 |
| cw_flow:upq20 | m | cw_out:downq50 | 1.639 | 1.573 | 184 | True | `SLOW.up.q20 -m-> MID.down.q50` | building_59 | hai |
| P:downq80 | m | cw_flow:upq20 | 1.639 | 1.647 | 183 | True | `MID.down.q80 -m-> SLOW.up.q20` | — | building_59 |
| AC_valve:upq80 | m | T:upq20 | 1.638 | 1.658 | 235 | False | `SLOW.up.q80 -m-> MID.up.q20` | — | hai, building_59 |
| P:downq50 | s | T:upq50 | 1.635 | 1.61 | 270 | True | `MID.down.q50 -s-> MID.up.q50` | — | — |
| purge_C:upq80 | s | P:downq50 | 1.633 | 1.652 | 353 | False | `MID.up.q80 -s-> MID.down.q50` | — | — |
| cw_flow:downq20 | m | cw_out:downq50 | 1.632 | 1.661 | 199 | True | `SLOW.down.q20 -m-> MID.down.q50` | building_59 | hai |
| cw_flow:downq80 | l | cw_out:downq80 | 1.632 | 2.048 | 84 | False | `SLOW.down.q80 -l-> MID.down.q80` | — | hai, building_59 |
| purge_C:upq20 | s | T:upq20 | 1.628 | 1.756 | 119 | False | `MID.up.q20 -s-> MID.up.q20` | — | hai, building_59 |
| L:trough | m | underflow_valve:upq20 | 1.628 | 1.978 | 84 | True | `MID.trough -m-> MID.up.q20` | — | hai, building_59 |
| AC_valve:upq50 | l | P:downq20 | 1.621 | 1.523 | 815 | False | `SLOW.up.q50 -l-> MID.down.q20` | — | — |
| A_valve:upq80 | s | T:downq50 | 1.62 | 1.696 | 105 | False | `SLOW.up.q80 -s-> MID.down.q50` | hai | — |
| AC_valve:upq80 | s | cw_flow:upq80 | 1.619 | 2.006 | 28 | False | `SLOW.up.q80 -s-> SLOW.up.q80` | — | hai, building_59 |
| P:downq80 | m | T:upq50 | 1.618 | 1.554 | 497 | True | `MID.down.q80 -m-> MID.up.q50` | — | — |
| recycle:upq20 | m | T:upq80 | 1.618 | 1.584 | 171 | False | `MID.up.q20 -m-> MID.up.q80` | — | hai |
| underflow_valve:upq20 | s | cw_out:upq20 | 1.616 | 1.756 | 13 | True | `MID.up.q20 -s-> MID.up.q20` | — | hai, building_59 |
| purge:peak | m | cw_flow:upq20 | 1.615 | 1.8 | 238 | False | `MID.peak -m-> SLOW.up.q20` | — | hai |
| A_feed:downq80 | l | T:downq80 | 1.614 | 1.697 | 194 | False | `SLOW.down.q80 -l-> MID.down.q80` | — | hai, building_59 |
| cw_out:downq50 | l | cw_flow:upq20 | 1.612 | 1.937 | 312 | True | `MID.down.q50 -l-> SLOW.up.q20` | — | hai, building_59 |
| cw_out:downq20 | l | cw_out:downq80 | 1.612 | 2.021 | 144 | False | `MID.down.q20 -l-> MID.down.q80 [same role]` | — | hai, building_59 |
| compressor:downq50 | s | P:downq20 | 1.61 | 1.504 | 186 | False | `MID.down.q50 -s-> MID.down.q20` | — | building_59 |
| underflow_valve:upq20 | l | T:downq80 | 1.609 | 2.378 | 142 | False | `MID.up.q20 -l-> MID.down.q80` | — | hai, building_59 |
| AC_valve:downq20 | m | P:upq80 | 1.607 | 1.731 | 393 | False | `SLOW.down.q20 -m-> MID.up.q80` | — | building_59 |
| T:upq50 | m | T:downq80 | 1.607 | 2.278 | 209 | True | `MID.up.q50 -m-> MID.down.q80 [same role]` | — | hai |
| cw_out:downq50 | l | feed:downq80 | 1.604 | 1.663 | 205 | True | `MID.down.q50 -l-> MID.down.q80` | — | hai, building_59 |
| cw_out:downq20 | m | cw_flow:downq50 | 1.601 | 1.721 | 136 | True | `MID.down.q20 -m-> SLOW.down.q50` | — | hai |
| A_valve:downq50 | s | P:downq80 | 1.6 | 1.964 | 197 | False | `SLOW.down.q50 -s-> MID.down.q80` | — | building_59 |
| AC_feed:downq80 | s | T:upq20 | 1.599 | 1.826 | 112 | False | `SLOW.down.q80 -s-> MID.up.q20` | — | hai, building_59 |
| cw_out:upq50 | m | cw_flow:downq20 | 1.597 | 2.114 | 176 | True | `MID.up.q50 -m-> SLOW.down.q20` | — | hai, building_59 |
| underflow_valve:upq80 | m | T:upq20 | 1.597 | 1.761 | 121 | False | `MID.up.q80 -m-> MID.up.q20` | — | hai, building_59 |
| cw_out:upq20 | s | T:upq50 | 1.591 | 1.693 | 72 | True | `MID.up.q20 -s-> MID.up.q50` | — | hai |
| cw_out:downq50 | l | cw_out:upq80 | 1.589 | 1.883 | 287 | True | `MID.down.q50 -l-> MID.up.q80 [same role]` | — | hai, building_59 |
| cw_flow:downq50 | m | cw_out:downq80 | 1.588 | 1.688 | 135 | True | `SLOW.down.q50 -m-> MID.down.q80` | — | hai |
| purge_C:downq50 | m | P:downq80 | 1.583 | 1.732 | 1025 | False | `MID.down.q50 -m-> MID.down.q80` | — | building_59 |
| cw_out:downq50 | m | cw_flow:downq80 | 1.58 | 2.249 | 88 | False | `MID.down.q50 -m-> SLOW.down.q80` | building_59 | hai |
| compressor:downq80 | m | cw_flow:downq20 | 1.579 | 1.657 | 56 | False | `MID.down.q80 -m-> SLOW.down.q20` | — | building_59 |
| T:downq80 | m | T:upq20 | 1.573 | 1.509 | 132 | True | `MID.down.q80 -m-> MID.up.q20 [same role]` | — | hai, building_59 |
| compressor:downq80 | s | P:downq20 | 1.572 | 1.57 | 48 | False | `MID.down.q80 -s-> MID.down.q20` | — | building_59 |
| feed:downq50 | l | cw_out:downq80 | 1.571 | 1.568 | 178 | True | `MID.down.q50 -l-> MID.down.q80` | — | hai, building_59 |
| purge_G:downq20 | s | T:upq20 | 1.571 | 2.069 | 122 | False | `MID.down.q20 -s-> MID.up.q20` | — | hai, building_59 |
| AC_valve:upq20 | s | cw_flow:upq20 | 1.571 | 1.62 | 55 | False | `SLOW.up.q20 -s-> SLOW.up.q20` | — | hai, building_59 |
| cw_flow:downq50 | m | cw_out:downq20 | 1.569 | 1.595 | 114 | True | `SLOW.down.q50 -m-> MID.down.q20` | — | hai |
| A_valve:downq80 | m | P:downq80 | 1.567 | 1.581 | 264 | False | `SLOW.down.q80 -m-> MID.down.q80` | — | building_59 |
| recycle:upq20 | s | cw_out:upq80 | 1.567 | 1.84 | 43 | False | `MID.up.q20 -s-> MID.up.q80` | — | hai |
| cw_out:downq80 | m | cw_out:downq20 | 1.562 | 2.818 | 61 | False | `MID.down.q80 -m-> MID.down.q20 [same role]` | — | hai, building_59 |
| T:upq20 | m | underflow:peak | 1.561 | 1.713 | 95 | True | `MID.up.q20 -m-> MID.peak` | — | hai |
| cw_out:downq50 | m | feed:upq80 | 1.556 | 1.839 | 106 | True | `MID.down.q50 -m-> MID.up.q80` | — | hai, building_59 |
| A_feed:downq20 | s | P:downq80 | 1.554 | 1.532 | 113 | False | `SLOW.down.q20 -s-> MID.down.q80` | — | building_59 |
| A_valve:downq20 | s | cw_flow:upq20 | 1.554 | 2.161 | 48 | False | `SLOW.down.q20 -s-> SLOW.up.q20` | — | hai, building_59 |
| compressor:upq80 | s | underflow_valve:downq20 | 1.551 | 1.571 | 14 | False | `MID.up.q80 -s-> MID.down.q20` | — | building_59 |
| purge_C:upq80 | s | feed:downq20 | 1.547 | 1.706 | 44 | False | `MID.up.q80 -s-> MID.down.q20` | — | hai, building_59 |
| P:upq20 | m | P:upq80 | 1.543 | 1.749 | 406 | True | `MID.up.q20 -m-> MID.up.q80 [same role]` | building_59 | — |
| cw_out:downq50 | l | feed:downq50 | 1.543 | 1.545 | 355 | True | `MID.down.q50 -l-> MID.down.q50` | — | hai, building_59 |
| cw_flow:downq50 | m | cw_out:upq80 | 1.541 | 1.536 | 131 | False | `SLOW.down.q50 -m-> MID.up.q80` | — | hai |
| purge_C:downq80 | s | cw_out:downq20 | 1.539 | 1.673 | 59 | False | `MID.down.q80 -s-> MID.down.q20` | building_59 | hai |
| feed:downq50 | l | cw_out:downq20 | 1.538 | 1.671 | 149 | True | `MID.down.q50 -l-> MID.down.q20` | — | hai, building_59 |
| T:upq20 | s | underflow_valve:downq80 | 1.537 | 2.12 | 41 | False | `MID.up.q20 -s-> MID.down.q80` | — | hai, building_59 |
| AC_feed:upq50 | m | P:downq80 | 1.536 | 1.507 | 833 | False | `SLOW.up.q50 -m-> MID.down.q80` | — | building_59 |
| cw_out:downq50 | l | cw_out:upq20 | 1.532 | 1.549 | 237 | True | `MID.down.q50 -l-> MID.up.q20 [same role]` | — | hai, building_59 |
| purge_valve:peak | m | T:upq50 | 1.531 | 1.531 | 568 | False | `MID.peak -m-> MID.up.q50` | — | hai |
| AC_valve:downq80 | m | T:upq80 | 1.53 | 2.056 | 158 | False | `SLOW.down.q80 -m-> MID.up.q80` | — | hai, building_59 |
| purge:peak | l | P:upq80 | 1.529 | 1.522 | 1259 | False | `MID.peak -l-> MID.up.q80` | — | — |
| AC_feed:upq20 | m | P:upq80 | 1.527 | 1.667 | 446 | False | `SLOW.up.q20 -m-> MID.up.q80` | — | building_59 |
| A_feed:downq20 | s | cw_flow:upq20 | 1.527 | 1.831 | 44 | False | `SLOW.down.q20 -s-> SLOW.up.q20` | — | hai, building_59 |
| A_feed:upq80 | l | T:upq80 | 1.525 | 1.616 | 194 | False | `SLOW.up.q80 -l-> MID.up.q80` | — | hai, building_59 |
| A_feed:downq80 | m | cw_out:upq20 | 1.524 | 1.56 | 53 | False | `SLOW.down.q80 -m-> MID.up.q20` | — | hai, building_59 |
| P:downq20 | m | P:upq50 | 1.523 | 1.527 | 909 | True | `MID.down.q20 -m-> MID.up.q50 [same role]` | — | — |
| T:upq20 | m | T:downq80 | 1.521 | 2.169 | 120 | True | `MID.up.q20 -m-> MID.down.q80 [same role]` | building_59 | hai |
| compressor:upq50 | s | P:upq80 | 1.518 | 1.526 | 182 | False | `MID.up.q50 -s-> MID.up.q80` | — | building_59 |
| T:downq80 | l | underflow_valve:upq20 | 1.518 | 1.653 | 123 | True | `MID.down.q80 -l-> MID.up.q20` | — | hai, building_59 |
| P:downq50 | l | P:downq80 | 1.517 | 1.628 | 1063 | True | `MID.down.q50 -l-> MID.down.q80 [same role]` | — | — |
| compressor:upq80 | l | cw_flow:downq80 | 1.512 | 1.564 | 74 | False | `MID.up.q80 -l-> SLOW.down.q80` | — | building_59 |
| purge_C:upq20 | m | T:upq80 | 1.503 | 2.007 | 216 | False | `MID.up.q20 -m-> MID.up.q80` | — | hai, building_59 |

## Loops (returns; verdicts recorded, not promoted)

| X | l1 | Y | l2 | X′ | n | cond. lift | timing (g1 / g2) | determinism (p1 / p2) | used |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| underflow_valve:downq20 | s | P:downq80 | s | underflow_valve:upq20 | 29 | 8.349 | unresolved (6.0 / 6.0) | Y reacts (0.092 / 0.020) | False |
| underflow_valve:downq20 | s | T:downq80 | s | underflow_valve:upq20 | 21 | 6.995 | X reacts (9.0 / 6.0) | Y reacts (0.071 / 0.043) | False |
| T:upq80 | s | P:downq20 | s | T:downq80 | 25 | 6.465 | X reacts (6.0 / 3.0) | Y reacts (0.063 / 0.034) | False |
| cw_out:downq20 | s | underflow_valve:upq80 | s | cw_out:upq20 | 20 | 6.191 | unresolved (6.0 / 6.0) | X reacts (0.037 / 0.064) | False |
| underflow_valve:upq80 | s | T:upq20 | s | underflow_valve:downq80 | 19 | 6.087 | unresolved (6.0 / 6.0) | Y reacts (0.082 / 0.036) | False |
| underflow_valve:upq80 | s | T:upq80 | s | underflow_valve:downq80 | 10 | 5.356 | unresolved (6.0 / 6.0) | X reacts (0.037 / 0.065) | False |
| cw_out:downq20 | s | T:downq20 | s | cw_out:upq20 | 16 | 5.268 | Y reacts (4.5 / 7.5) | Y reacts (0.051 / 0.033) | False |
| cw_flow:downq80 | s | P:downq20 | m | cw_flow:upq80 | 29 | 5.186 | Y reacts (3.0 / 25.5) | Y reacts (0.067 / 0.017) | False |
| cw_out:upq80 | s | T:upq80 | s | cw_out:downq80 | 25 | 4.663 | Y reacts (3.0 / 6.0) | Y reacts (0.068 / 0.033) | False |
| T:downq20 | s | P:upq80 | s | T:upq20 | 20 | 4.131 | unresolved (6.0 / 6.0) | Y reacts (0.093 / 0.062) | False |
| cw_flow:downq20 | s | P:downq20 | m | cw_flow:upq80 | 31 | 3.846 | Y reacts (3.0 / 21.0) | Y reacts (0.094 / 0.017) | False |
| T:upq80 | s | underflow_valve:downq80 | s | T:downq80 | 16 | 3.742 | unresolved (6.0 / 6.0) | Y reacts (0.065 / 0.043) | False |
| cw_flow:downq20 | s | P:downq20 | m | cw_flow:upq20 | 46 | 3.517 | Y reacts (3.0 / 18.0) | Y reacts (0.094 / 0.026) | False |
| cw_flow:downq20 | s | feed:upq50 | m | cw_flow:upq80 | 33 | 3.426 | Y reacts (6.0 / 18.0) | Y reacts (0.054 / 0.025) | False |
| cw_flow:downq50 | s | P:downq20 | m | cw_flow:upq80 | 44 | 3.361 | Y reacts (3.0 / 21.0) | Y reacts (0.067 / 0.017) | False |
| cw_flow:downq80 | s | P:downq20 | m | cw_flow:upq20 | 30 | 3.306 | Y reacts (3.0 / 21.0) | Y reacts (0.067 / 0.026) | False |
| cw_out:upq80 | s | underflow_valve:downq20 | s | cw_out:downq80 | 11 | 3.242 | unresolved (7.5 / 7.5) | X reacts (0.022 / 0.035) | False |
| cw_flow:downq20 | s | feed:upq80 | m | cw_flow:upq80 | 25 | 3.122 | Y reacts (6.0 / 15.0) | unresolved (0.025 / 0.019) | False |
| P:downq20 | s | underflow_valve:upq80 | s | P:upq20 | 38 | 3.119 | unresolved (6.0 / 6.0) | X reacts (0.033 / 0.060) | False |
| cw_flow:downq20 | s | feed:upq20 | m | cw_flow:upq80 | 28 | 3.02 | Y reacts (7.5 / 19.5) | unresolved (0.038 / 0.031) | False |
| underflow_valve:upq20 | m | T:upq80 | s | underflow_valve:downq80 | 13 | 3.017 | X reacts (24.0 / 6.0) | unresolved (0.046 / 0.065) | False |
| T:upq80 | s | cw_out:downq80 | s | T:downq80 | 24 | 3.013 | X reacts (6.0 / 3.0) | X reacts (0.033 / 0.062) | False |
| underflow:trough | m | underflow_valve:upq80 | m | underflow:peak | 28 | 2.993 | unresolved (30.0 / 24.0) | unresolved (0.030 / 0.029) | False |
| cw_flow:downq80 | s | P:downq80 | m | cw_flow:upq20 | 26 | 2.963 | Y reacts (3.0 / 24.0) | Y reacts (0.072 / 0.025) | False |
| underflow_valve:downq20 | s | cw_out:downq20 | s | underflow_valve:upq80 | 6 | 2.82 | Y reacts (6.0 / 9.0) | X reacts (0.019 / 0.037) | False |
| cw_flow:downq20 | m | cw_out:downq50 | s | cw_flow:upq80 | 23 | 2.81 | X reacts (21.0 / 6.0) | Y reacts (0.057 / 0.024) | False |
| cw_flow:downq50 | s | P:downq20 | m | cw_flow:upq20 | 59 | 2.777 | Y reacts (3.0 / 18.0) | Y reacts (0.067 / 0.026) | False |
| cw_out:upq50 | s | T:upq80 | s | cw_out:downq80 | 18 | 2.747 | Y reacts (3.0 / 6.0) | unresolved (0.036 / 0.033) | False |
| cw_flow:downq20 | s | feed:upq20 | m | cw_flow:upq20 | 32 | 2.746 | Y reacts (6.0 / 15.0) | unresolved (0.038 / 0.046) | False |
| cw_out:upq20 | s | T:upq80 | s | cw_out:downq80 | 11 | 2.735 | Y reacts (3.0 / 6.0) | Y reacts (0.059 / 0.033) | False |
| cw_flow:downq80 | m | cw_out:upq80 | m | cw_flow:upq80 | 25 | 2.665 | Y reacts (18.0 / 30.0) | Y reacts (0.038 / 0.022) | False |
| P:upq80 | s | T:upq20 | s | P:downq80 | 27 | 2.601 | unresolved (6.0 / 6.0) | unresolved (0.062 / 0.080) | False |
| cw_flow:upq20 | m | cw_out:downq50 | m | cw_flow:downq80 | 39 | 2.582 | Y reacts (16.5 / 27.0) | Y reacts (0.054 / 0.019) | False |
| T:downq20 | s | underflow_valve:upq80 | s | T:upq20 | 20 | 2.554 | unresolved (4.5 / 6.0) | unresolved (0.073 / 0.082) | False |
| underflow_valve:downq20 | m | T:downq80 | s | underflow_valve:upq20 | 13 | 2.535 | X reacts (19.5 / 6.0) | unresolved (0.039 / 0.043) | False |
| cw_flow:downq20 | m | cw_out:downq20 | s | cw_flow:upq80 | 10 | 2.527 | X reacts (28.5 / 6.0) | unresolved (0.035 / 0.037) | False |
| feed:downq50 | s | cw_out:upq80 | m | feed:upq20 | 14 | 2.496 | Y reacts (6.0 / 34.5) | unresolved (0.025 / 0.018) | False |
| cw_flow:downq80 | l | cw_out:downq80 | s | cw_flow:upq80 | 16 | 2.459 | X reacts (105.0 / 3.0) | unresolved (0.029 / 0.032) | False |
| P:upq80 | s | underflow_valve:downq20 | s | P:downq80 | 18 | 2.453 | unresolved (6.0 / 6.0) | X reacts (0.025 / 0.092) | False |
| T:upq80 | s | cw_out:upq80 | m | T:downq80 | 14 | 2.449 | Y reacts (4.5 / 22.5) | unresolved (0.026 / 0.030) | False |
| underflow_valve:upq80 | s | T:upq20 | m | underflow_valve:downq80 | 37 | 2.443 | Y reacts (6.0 / 24.0) | Y reacts (0.082 / 0.042) | False |
| T:upq80 | s | cw_out:downq80 | s | T:downq20 | 14 | 2.412 | X reacts (7.5 / 4.5) | unresolved (0.033 / 0.040) | False |
| cw_out:downq20 | s | T:downq20 | m | cw_out:upq20 | 22 | 2.4 | Y reacts (3.0 / 19.5) | Y reacts (0.051 / 0.024) | False |
| cw_flow:downq50 | m | cw_out:downq80 | s | cw_flow:upq80 | 23 | 2.393 | X reacts (27.0 / 6.0) | unresolved (0.024 / 0.032) | False |
| feed:downq20 | l | cw_out:downq20 | s | feed:upq80 | 13 | 2.368 | X reacts (87.0 / 6.0) | unresolved (0.024 / 0.016) | False |
| cw_flow:downq20 | m | cw_out:downq80 | s | cw_flow:upq80 | 25 | 2.344 | X reacts (24.0 / 6.0) | unresolved (0.043 / 0.032) | False |
| underflow_valve:upq80 | s | T:upq80 | s | underflow_valve:downq50 | 7 | 2.343 | Y reacts (6.0 / 9.0) | X reacts (0.037 / 0.072) | False |
| T:upq80 | m | cw_out:downq80 | s | T:downq80 | 36 | 2.285 | X reacts (18.0 / 3.0) | X reacts (0.027 / 0.062) | False |
| underflow_valve:upq20 | s | T:upq20 | m | underflow_valve:downq80 | 19 | 2.285 | Y reacts (7.5 / 25.5) | unresolved (0.041 / 0.042) | False |
| underflow_valve:upq80 | m | T:upq20 | s | underflow_valve:downq80 | 12 | 2.268 | X reacts (16.5 / 6.0) | unresolved (0.041 / 0.036) | False |
| T:downq80 | m | cw_out:upq80 | s | T:upq80 | 37 | 2.266 | X reacts (24.0 / 3.0) | X reacts (0.023 / 0.068) | False |
| T:upq80 | s | underflow_valve:downq20 | m | T:downq80 | 18 | 2.26 | Y reacts (9.0 / 21.0) | unresolved (0.054 / 0.039) | False |
| T:downq20 | s | cw_out:upq20 | s | T:upq80 | 13 | 2.239 | unresolved (7.5 / 9.0) | X reacts (0.033 / 0.059) | False |
| cw_out:upq80 | m | cw_flow:downq20 | m | cw_out:downq20 | 39 | 2.236 | Y reacts (15.0 / 30.0) | unresolved (0.037 / 0.035) | False |
| cw_flow:upq80 | l | cw_out:upq80 | s | cw_flow:downq20 | 17 | 2.131 | X reacts (79.5 / 6.0) | X reacts (0.023 / 0.057) | False |
| P:upq80 | s | T:downq20 | m | P:downq80 | 81 | 2.124 | Y reacts (6.0 / 21.0) | unresolved (0.052 / 0.068) | False |
| cw_flow:downq20 | s | cw_out:upq80 | m | cw_flow:upq20 | 23 | 2.124 | Y reacts (6.0 / 27.0) | unresolved (0.044 / 0.051) | False |
| cw_flow:upq80 | l | cw_out:upq80 | l | cw_flow:downq80 | 38 | 2.119 | unresolved (72.0 / 69.0) | unresolved (0.023 / 0.022) | False |
| underflow_valve:upq80 | m | T:upq20 | m | underflow_valve:downq80 | 50 | 2.09 | unresolved (15.0 / 21.0) | unresolved (0.041 / 0.042) | False |
| cw_out:downq50 | s | T:downq20 | m | cw_out:upq20 | 37 | 2.08 | Y reacts (3.0 / 19.5) | unresolved (0.035 / 0.024) | False |
| cw_out:downq80 | s | T:downq20 | m | cw_out:upq20 | 23 | 2.078 | Y reacts (6.0 / 18.0) | Y reacts (0.040 / 0.024) | False |
| cw_flow:downq80 | s | cw_out:upq20 | m | cw_flow:upq20 | 11 | 2.074 | Y reacts (9.0 / 33.0) | unresolved (0.047 / 0.032) | False |
| T:upq80 | m | underflow_valve:downq20 | s | T:downq80 | 25 | 2.068 | X reacts (21.0 / 6.0) | X reacts (0.026 / 0.071) | False |
| T:downq20 | m | cw_out:upq20 | s | T:upq20 | 45 | 2.046 | X reacts (19.5 / 3.0) | X reacts (0.024 / 0.082) | False |
| feed:upq80 | m | cw_out:downq80 | l | feed:downq20 | 33 | 2.038 | Y reacts (18.0 / 70.5) | unresolved (0.023 / 0.018) | False |
| cw_out:upq80 | s | cw_flow:downq20 | m | cw_out:downq80 | 21 | 2.031 | Y reacts (6.0 / 25.5) | unresolved (0.057 / 0.043) | False |
| underflow_valve:downq20 | m | T:downq80 | m | underflow_valve:upq20 | 17 | 2.018 | unresolved (18.0 / 18.0) | Y reacts (0.039 / 0.025) | False |
| cw_flow:upq80 | s | cw_out:downq20 | m | cw_flow:downq80 | 8 | 2.015 | Y reacts (6.0 / 15.0) | Y reacts (0.079 / 0.029) | False |
| T:upq80 | m | cw_out:downq80 | s | T:downq20 | 23 | 2.003 | X reacts (18.0 / 6.0) | unresolved (0.027 / 0.040) | False |
| cw_out:upq80 | m | cw_flow:upq80 | s | cw_out:downq20 | 14 | 1.999 | X reacts (36.0 / 6.0) | X reacts (0.022 / 0.079) | False |
| cw_flow:downq50 | s | cw_out:upq80 | m | cw_flow:upq20 | 31 | 1.992 | Y reacts (6.0 / 27.0) | unresolved (0.037 / 0.051) | False |
| cw_out:upq80 | m | feed:upq20 | m | cw_out:downq80 | 31 | 1.976 | unresolved (21.0 / 18.0) | X reacts (0.018 / 0.027) | False |
| cw_out:downq80 | s | T:downq80 | m | cw_out:upq80 | 28 | 1.938 | Y reacts (3.0 / 21.0) | Y reacts (0.062 / 0.023) | False |
| T:downq20 | m | cw_out:upq20 | s | T:upq80 | 24 | 1.937 | X reacts (18.0 / 6.0) | X reacts (0.024 / 0.059) | False |
| cw_flow:downq50 | m | cw_out:downq20 | s | cw_flow:upq80 | 11 | 1.921 | X reacts (30.0 / 6.0) | X reacts (0.020 / 0.037) | False |
| T:upq20 | m | underflow_valve:downq80 | s | T:downq80 | 18 | 1.897 | X reacts (19.5 / 6.0) | unresolved (0.042 / 0.043) | False |
| cw_flow:downq50 | s | cw_out:upq50 | m | cw_flow:upq20 | 35 | 1.896 | Y reacts (6.0 / 27.0) | Y reacts (0.075 / 0.035) | False |
| T:downq20 | s | cw_out:upq20 | s | T:upq50 | 16 | 1.876 | Y reacts (6.0 / 9.0) | X reacts (0.033 / 0.071) | False |
| cw_out:upq80 | m | T:downq80 | s | cw_out:downq80 | 19 | 1.87 | X reacts (24.0 / 6.0) | unresolved (0.030 / 0.028) | False |
| cw_flow:downq80 | m | cw_out:upq20 | m | cw_flow:upq20 | 24 | 1.863 | Y reacts (18.0 / 33.0) | Y reacts (0.048 / 0.032) | False |
| cw_out:upq80 | m | feed:upq20 | m | cw_out:downq20 | 30 | 1.857 | unresolved (21.0 / 24.0) | X reacts (0.018 / 0.030) | False |
| cw_flow:downq20 | m | cw_out:downq80 | s | cw_flow:upq50 | 39 | 1.829 | X reacts (21.0 / 6.0) | unresolved (0.043 / 0.054) | False |
| cw_flow:downq80 | m | feed:downq20 | l | cw_flow:upq80 | 30 | 1.828 | Y reacts (27.0 / 81.0) | unresolved (0.021 / 0.024) | False |
| cw_flow:downq50 | m | cw_out:downq80 | s | cw_flow:upq50 | 35 | 1.821 | X reacts (25.5 / 6.0) | X reacts (0.024 / 0.054) | False |
| T:downq20 | s | underflow_valve:upq20 | m | T:upq80 | 21 | 1.807 | Y reacts (6.0 / 24.0) | unresolved (0.058 / 0.046) | False |
| feed:upq20 | m | cw_out:downq80 | l | feed:downq20 | 35 | 1.793 | Y reacts (21.0 / 67.5) | unresolved (0.027 / 0.018) | False |
| cw_out:upq80 | s | T:upq80 | m | cw_out:downq80 | 29 | 1.793 | Y reacts (3.0 / 19.5) | Y reacts (0.068 / 0.027) | False |
| T:downq80 | l | underflow_valve:upq20 | s | T:upq20 | 18 | 1.776 | X reacts (120.0 / 6.0) | X reacts (0.018 / 0.041) | False |
| cw_out:upq80 | m | cw_flow:upq20 | s | cw_out:downq80 | 40 | 1.73 | X reacts (28.5 / 6.0) | unresolved (0.051 / 0.056) | False |
| cw_flow:downq20 | m | cw_out:downq50 | l | cw_flow:upq20 | 109 | 1.729 | Y reacts (27.0 / 75.0) | Y reacts (0.057 / 0.030) | False |
| underflow_valve:downq20 | l | T:downq80 | l | underflow_valve:upq20 | 38 | 1.707 | unresolved (72.0 / 87.0) | Y reacts (0.037 / 0.018) | False |
| cw_out:upq20 | s | cw_flow:downq50 | m | cw_out:downq80 | 13 | 1.697 | Y reacts (6.0 / 33.0) | Y reacts (0.062 / 0.024) | False |
| T:downq80 | s | underflow_valve:upq20 | m | T:upq80 | 20 | 1.696 | Y reacts (6.0 / 24.0) | unresolved (0.043 / 0.046) | False |
| cw_out:upq50 | s | T:upq80 | m | cw_out:downq80 | 35 | 1.664 | Y reacts (3.0 / 18.0) | unresolved (0.036 / 0.027) | False |
| feed:upq80 | m | cw_flow:upq80 | l | feed:downq80 | 32 | 1.653 | Y reacts (18.0 / 72.0) | unresolved (0.019 / 0.017) | False |
| cw_flow:downq20 | m | cw_out:downq20 | l | cw_flow:upq80 | 34 | 1.635 | Y reacts (27.0 / 73.5) | Y reacts (0.035 / 0.013) | False |
| cw_flow:downq80 | m | cw_out:upq80 | m | cw_flow:upq20 | 36 | 1.605 | Y reacts (18.0 / 30.0) | unresolved (0.038 / 0.051) | False |
| T:downq80 | s | cw_out:downq80 | m | T:upq80 | 12 | 1.581 | Y reacts (4.5 / 28.5) | unresolved (0.028 / 0.027) | False |
| feed:downq50 | l | cw_out:downq20 | m | feed:upq80 | 25 | 1.575 | X reacts (72.0 / 27.0) | unresolved (0.020 / 0.017) | False |
| underflow_valve:upq80 | m | underflow:peak | m | underflow_valve:downq80 | 27 | 1.566 | X reacts (27.0 / 18.0) | unresolved (0.029 / 0.040) | False |
| cw_flow:upq20 | l | cw_out:upq20 | s | cw_flow:downq50 | 28 | 1.554 | X reacts (57.0 / 6.0) | X reacts (0.023 / 0.062) | False |
| T:downq20 | s | cw_out:upq20 | s | T:upq20 | 16 | 1.552 | X reacts (9.0 / 3.0) | X reacts (0.033 / 0.082) | False |
| T:downq20 | m | cw_out:upq20 | s | T:upq50 | 28 | 1.538 | X reacts (18.0 / 3.0) | X reacts (0.024 / 0.071) | False |
| cw_flow:upq80 | l | cw_out:upq80 | m | cw_flow:downq20 | 26 | 1.511 | X reacts (84.0 / 15.0) | X reacts (0.023 / 0.037) | False |
| T:upq80 | s | underflow_valve:downq20 | s | T:downq80 | 7 | 1.504 | Y reacts (6.0 / 9.0) | unresolved (0.054 / 0.071) | False |
| cw_flow:downq20 | m | cw_out:downq80 | s | cw_flow:upq20 | 20 | 1.5 | X reacts (16.5 / 6.0) | unresolved (0.043 / 0.043) | False |

Chains (non-return): 419.

## Absences

- silent roles: ['steam']
- roles never a target: ['AC_feed', 'AC_valve', 'A_feed', 'A_valve', 'D_feed', 'D_valve', 'E_feed', 'E_valve', 'L', 'compressor', 'feed_A', 'feed_B', 'feed_C', 'feed_D', 'feed_E', 'feed_F', 'prod_D', 'prod_E', 'prod_F', 'prod_G', 'prod_H', 'purge', 'purge_A', 'purge_B', 'purge_C', 'purge_D', 'purge_E', 'purge_F', 'purge_G', 'purge_H', 'purge_valve', 'recycle']
- keyed pairs not found: D_valve → D_feed; E_valve → E_feed; A_valve → A_feed; AC_valve → AC_feed; purge_valve → purge; cw_flow → T; steam → T; underflow → L
- signal floor: 138 (absence is informative only for pairs whose support would exceed the signal floor)

## Regimes

82 annotations

## Matrix row

Cells in (this system as receiver):

| source | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tennessee_eastman_stretch (diagonal) | 177.62 | 349.04 | 291.41 | 113.79 | -57.63 | marginal | — | 40/40 |  |
| hai | -21.37 | 48.61 | 89.49 | 110.86 | 40.88 | marginal | -0.12 | 34/40 | damage |
| nasa_battery | -6.68 | 8.46 | 26.82 | 33.50 | 18.36 | marginal | -0.04 | 6/40 | damage |
| physionet_slp | 62.39 | 62.39 | 81.83 | 7.13 | 19.44 | derangement | 0.35 | 4/40 | damage |
| building_59 | 13.39 | 71.08 | 103.96 | 90.57 | 32.87 | marginal | 0.08 | 32/40 | damage |
| fingrid | -8.10 | 3.20 | 35.27 | 43.36 | 32.06 | marginal | -0.05 | 10/40 | damage |
| alibaba_2018 | 51.23 | 80.61 | 124.43 | 73.19 | 43.81 | marginal | 0.29 | 30/40 | damage |

Cells out (this system as source):

| receiver | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hai | 8.74 | 13.73 | 39.92 | 31.18 | 26.19 | marginal | — | 142/168 | short, damage |
| nasa_battery | 0.41 | 0.50 | 0.15 | -0.26 | -0.35 | marginal | 0.16 | 12/12 | short |
| physionet_slp | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | marginal | — | 10/10 |  |
| building_59 | 11.16 | 25.00 | 143.65 | 132.49 | 118.65 | marginal | 0.10 | 89/89 |  |
| fingrid | 0.35 | 0.35 | 18.35 | 10.89 | 18.00 | derangement | 0.00 | 16/16 |  |
| alibaba_2018 | 4.56 | 6.63 | 5.41 | 0.85 | -1.23 | marginal | — | 27/27 |  |

Nearest taxa by distance: shape_jaccard: building_59 0.832, hai 0.89, nasa_battery 0.979; shape_bray_curtis: building_59 0.775, hai 0.849, nasa_battery 0.977; transfer_net: physionet_slp 0.031, building_59 0.075, hai 1.0
