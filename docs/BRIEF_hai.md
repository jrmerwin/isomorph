# Brief — hai (method v8, a view)

*Lifts are odds ratios on the proposal split (3.6-3.8), confirmed on the confirmation split; absence is informative only above the signal floor (3.5); `no gain` means found but already carried by the trivial alternation model (3.11); loop-rule verdicts are recorded, not promoted (3.16); cells are bit-horizons net of the larger of two controls, with share of the receiver's ceiling where a diagonal exists (3.12).*

## Identity

- kind: real ICS testbed (HAI 21.03); standing: admitted (provisional: 15.3 days, 178 H; standing decision, section 6)
- entity: process (3 units); H = 124.0 min; lag edges [4.99, 24.87, 124.0] min
- periods: slow —, fast —; admission: {'days': 15.32, 'slow_periods': None, 'horizons': 178.0, 'test_horizons': 44.5, 'admitted': False, 'by': None}
- claim: **no gain** — library 3.714 bits, triviality 3.675, best baseline 3.892; gain over triviality -0.039
- events 34298, types 168, signal floor 12

## Vocabulary

| role | full tag | quantity | scheme | loop tags (timing / determinism) |
| --- | --- | --- | --- | --- |
| 24Vdc | SLOW·LEAD ⟨M L² T⁻³ N⁻¹⟩ | voltage | dsign | — / — |
| B2004 | SET·COMMON·RELAY ⟨M L⁻¹ T⁻²⟩ | pressure | q20_50_80 | RESPONDS / RESPONDS |
| B2016 | MID·LOCAL·RELAY ⟨M L⁻¹ T⁻²⟩ | pressure | dsign | REACTS / — |
| B3004 | SET·COMMON·LEAD ⟨L⟩ | length | q20_50_80 | REACTS / REACTS |
| B3005 | SET·COMMON·RELAY ⟨L³ T⁻¹⟩ | volume_flow | q10_90 | — / — |
| B4002 | SET·LEAD ⟨Θ⟩ | temperature | q10_90 | — / — |
| B4005 | MID-S·LOCAL·RELAY | — | q20_50_80 | RESPONDS / RESPONDS |
| B400B | MID-S·LOCAL·RELAY ⟨L³ T⁻¹⟩ | volume_flow | q20_50_80 | RESPONDS / RESPONDS |
| B4022 | SLOW·LOCAL·RELAY ⟨Θ⟩ | temperature | q20_50_80 | RESPONDS / REACTS |
| CO_rpm | MID·LOCAL·RELAY | — | dsign | REACTS / REACTS |
| Emerg | SET·ISOLATED | — | silent | — / — |
| FCV01D | MID-S·LOCAL·RELAY | — | q10_90 | REACTS / RESPONDS |
| FCV01Z | MID-S·LOCAL·RELAY | — | dsign | — / RESPONDS |
| FCV02D | MID-S·ISOLATED | — | silent | — / — |
| FCV02Z | MID-S·LOCAL·RELAY | — | q20_50_80 | REACTS / RESPONDS |
| FCV03D | MID·COMMON·RELAY | — | dsign | — / — |
| FCV03Z | MID·LOCAL·RELAY | — | dsign | — / — |
| FIT01 | TEX·ISOLATED ⟨L³ T⁻¹⟩ | volume_flow | silent | — / — |
| FT01 | MID·LOCAL·RELAY ⟨M L⁻¹ T⁻²⟩ | pressure | q20_50_80 | — / RESPONDS |
| FT01Z | MID·LOCAL·RELAY ⟨L³ T⁻¹⟩ | volume_flow | dsign | REACTS / REACTS |
| FT02 | MID-S·LOCAL·RELAY ⟨M L⁻¹ T⁻²⟩ | pressure | q20_50_80 | RESPONDS / RESPONDS |
| FT02Z | MID-S·LOCAL·RELAY ⟨L³ T⁻¹⟩ | volume_flow | q20_50_80 | — / RESPONDS |
| FT03 | MID·LOCAL·RELAY ⟨M L⁻¹ T⁻²⟩ | pressure | dsign | — / — |
| FT03Z | MID·COMMON·RELAY ⟨L³ T⁻¹⟩ | volume_flow | dsign | — / — |
| HILout | SLOW·LOCAL·RELAY | — | q20_50_80 | RESPONDS / RESPONDS |
| HT_FD | TEX·ISOLATED ⟨T⁻¹⟩ | frequency | silent | — / — |
| HT_LD | MID-S·LEAD ⟨M L² T⁻³⟩ | power | dsign | — / — |
| HT_PO | MID-S·LEAD ⟨M L² T⁻³⟩ | power | dsign | — / — |
| HT_PS | SET·LEAD ⟨M L² T⁻³⟩ | power | q20_50_80 | — / — |
| LCP01D | MID-S·LOCAL·RELAY | — | q20_50_80 | RESPONDS / RESPONDS |
| LCV01D | MID·LOCAL·RELAY | — | q20_50_80 | RESPONDS / REACTS |
| LCV01Z | MID·LOCAL·RELAY | — | q20_50_80 | REACTS / RESPONDS |
| LD | MID·LEAD ⟨M L² T⁻³⟩ | power | dsign | — / — |
| LIT01 | MID·LOCAL·RELAY ⟨L⟩ | length | q20_50_80 | REACTS / REACTS |
| OnOff | SET·ISOLATED | — | silent | — / — |
| PCV01D | MID-S·LOCAL·RELAY | — | dsign | — / RESPONDS |
| PCV01Z | MID-S·LOCAL·RELAY | — | dsign | — / RESPONDS |
| PCV02D | SET·ISOLATED | — | silent | — / — |
| PCV02Z | SLOW-S·LEAD | — | dsign | — / — |
| PIT01 | MID·LOCAL·RELAY ⟨M L⁻¹ T⁻²⟩ | pressure | dsign | RESPONDS / REACTS |
| PIT02 | MID·LOCAL·RELAY ⟨M L⁻¹ T⁻²⟩ | pressure | q10_90 | REACTS / REACTS |
| SIT01 | MID·LOCAL·RELAY ⟨T⁻¹⟩ | frequency | dsign | REACTS / REACTS |
| SIT02 | MID·LOCAL·RELAY ⟨T⁻¹⟩ | frequency | dsign | REACTS / — |
| ST_FD | TEX·ISOLATED ⟨T⁻¹⟩ | frequency | silent | — / — |
| ST_GOV | MID·LEAD | — | dsign | — / — |
| ST_LD | MID·LEAD ⟨M L² T⁻³⟩ | power | dsign | — / — |
| ST_PO | MID·LEAD ⟨M L² T⁻³⟩ | power | dsign | — / — |
| ST_PS | SET·LEAD ⟨M L² T⁻³⟩ | power | q20_50_80 | — / — |
| ST_PT01 | MID·LEAD ⟨M L⁻¹ T⁻²⟩ | pressure | dsign | — / — |
| ST_TT01 | MID·LEAD ⟨Θ⟩ | temperature | q10_90 | — / — |
| TIT01 | MID·LOCAL·LEAD ⟨Θ⟩ | temperature | dsign | REACTS / REACTS |
| TIT02 | MID·LOCAL·RELAY ⟨Θ⟩ | temperature | q20_50_80 | RESPONDS / RESPONDS |
| VT01 | MID-S·LOCAL·LEAD ⟨T⁻¹⟩ | frequency | q20_50_80 | — / — |
| VXT02 | SLOW·LOCAL·RELAY ⟨L⟩ | length | q20_50_80 | REACTS / REACTS |
| VXT03 | SLOW·COMMON·RELAY ⟨L⟩ | length | q20_50_80 | REACTS / RESPONDS |
| VYT02 | SLOW·COMMON·RELAY ⟨L⟩ | length | q20_50_80 | REACTS / — |
| VYT03 | SLOW·COMMON·RELAY ⟨L⟩ | length | q20_50_80 | RESPONDS / RESPONDS |

## Couplings (validated fragments)

| prior | lag | target | lift | conf. lift | n | binding | shape | confirmed in | failed in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VYT02:upq80 | s | VYT02:downq80 | 641.636 | 222.609 | 5 | False | `SLOW.up.q80 -s-> SLOW.down.q80 [same role]` | — | tennessee_eastman |
| VYT02:downq80 | s | VYT02:upq80 | 256.655 | 340.692 | 3 | False | `SLOW.down.q80 -s-> SLOW.up.q80 [same role]` | — | tennessee_eastman |
| VYT03:downq80 | m | VYT02:upq80 | 202.622 | 100.649 | 3 | False | `SLOW.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman |
| VYT03:upq80 | l | VYT02:downq80 | 92.991 | 65.809 | 5 | False | `SLOW.up.q80 -l-> SLOW.down.q80` | — | tennessee_eastman |
| VYT03:downq80 | l | VT01:downq80 | 90.487 | 70.986 | 3 | False | `SLOW.down.q80 -l-> MID-S.down.q80` | — | tennessee_eastman |
| TIT02:upq50 | s | TIT02:upq80 | 86.704 | 94.877 | 57 | True | `MID.up.q50 -s-> MID.up.q80 [same role]` | building_59 | tennessee_eastman |
| B400B:downq20 | s | FCV02Z:upq80 | 83.236 | 21.518 | 22 | True | `MID-S.down.q20 -s-> MID-S.up.q80` | — | tennessee_eastman |
| FT02Z:downq20 | s | FCV02Z:upq80 | 83.236 | 28.691 | 22 | True | `MID-S.down.q20 -s-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| FT02:downq20 | s | FCV02Z:upq80 | 83.236 | 28.691 | 22 | True | `MID-S.down.q20 -s-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| VT01:upq80 | l | VT01:downq80 | 79.007 | 48.342 | 3 | False | `MID-S.up.q80 -l-> MID-S.down.q80 [same role]` | — | tennessee_eastman |
| VYT02:upq80 | m | VYT02:downq80 | 78.568 | 108.446 | 3 | False | `SLOW.up.q80 -m-> SLOW.down.q80 [same role]` | — | tennessee_eastman |
| TIT02:upq20 | s | TIT02:upq50 | 70.58 | 63.288 | 57 | True | `MID.up.q20 -s-> MID.up.q50 [same role]` | building_59 | tennessee_eastman |
| VT01:upq80 | l | VYT02:upq80 | 67.037 | 87.895 | 7 | False | `MID-S.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman |
| VYT03:downq80 | l | VYT02:downq80 | 65.809 | 70.064 | 6 | False | `SLOW.down.q80 -l-> SLOW.down.q80` | — | tennessee_eastman |
| FT02:upq20 | s | FCV02Z:downq80 | 64.11 | 54.513 | 27 | True | `MID-S.up.q20 -s-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| VT01:upq80 | l | VYT03:upq80 | 63.206 | 164.364 | 3 | False | `MID-S.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman |
| VT01:upq80 | l | VYT03:downq80 | 63.206 | 164.364 | 3 | False | `MID-S.up.q80 -l-> SLOW.down.q80` | — | tennessee_eastman |
| FT02Z:upq20 | s | FCV02Z:downq80 | 61.481 | 51.644 | 25 | True | `MID-S.up.q20 -s-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| B400B:upq20 | s | FCV02Z:downq80 | 61.481 | 49.578 | 25 | True | `MID-S.up.q20 -s-> MID-S.down.q80` | — | tennessee_eastman |
| TIT01:trough | s | TIT02:upq20 | 57.785 | 46.308 | 56 | True | `MID.trough -s-> MID.up.q20` | — | tennessee_eastman |
| VT01:upq80 | l | VYT02:downq80 | 57.46 | 92.29 | 6 | False | `MID-S.up.q80 -l-> SLOW.down.q80` | — | tennessee_eastman |
| VYT03:upq20 | s | VYT03:downq20 | 55.566 | 42.137 | 24 | True | `SLOW.up.q20 -s-> SLOW.down.q20 [same role]` | — | tennessee_eastman |
| B2004:downq20 | s | B3004:downq80 | 55.4 | 57.15 | 5 | False | `SET.down.q20 -s-> SET.down.q80` | — | — |
| B2004:downq50 | s | B3004:downq80 | 54.841 | 52.541 | 5 | False | `SET.down.q50 -s-> SET.down.q80` | — | — |
| TIT01:trough | s | TIT02:upq50 | 54.689 | 42.282 | 53 | True | `MID.trough -s-> MID.up.q50` | — | tennessee_eastman |
| B4005:downq20 | s | B400B:downq20 | 53.673 | 62.107 | 43 | True | `MID-S.down.q20 -s-> MID-S.down.q20` | — | tennessee_eastman |
| B4005:downq20 | s | FT02:downq20 | 53.673 | 59.889 | 43 | True | `MID-S.down.q20 -s-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B4005:downq20 | s | FT02Z:downq20 | 53.673 | 59.889 | 43 | True | `MID-S.down.q20 -s-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| VYT02:upq50 | s | VYT02:downq50 | 53.632 | 58.546 | 25 | True | `SLOW.up.q50 -s-> SLOW.down.q50 [same role]` | — | tennessee_eastman |
| B4005:upq50 | s | B400B:upq50 | 52.729 | 47.226 | 41 | True | `MID-S.up.q50 -s-> MID-S.up.q50` | — | tennessee_eastman |
| B4005:upq50 | s | FT02:upq50 | 52.729 | 47.226 | 41 | True | `MID-S.up.q50 -s-> MID-S.up.q50` | — | tennessee_eastman |
| B4005:upq50 | s | FT02Z:upq50 | 52.729 | 47.226 | 41 | True | `MID-S.up.q50 -s-> MID-S.up.q50` | — | tennessee_eastman |
| VYT02:downq80 | s | VYT03:downq50 | 50.19 | 14.99 | 4 | False | `SLOW.down.q80 -s-> SLOW.down.q50` | — | tennessee_eastman |
| VXT03:upq50 | s | VXT03:downq50 | 49.357 | 56.143 | 12 | False | `SLOW.up.q50 -s-> SLOW.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| FT01:downq50 | s | B3005:downq10 | 49.014 | 111.677 | 3 | False | `MID.down.q50 -s-> SET.down.q10` | — | tennessee_eastman, building_59 |
| FT02:downq50 | s | FCV02Z:upq50 | 48.73 | 56.858 | 34 | True | `MID-S.down.q50 -s-> MID-S.up.q50` | — | tennessee_eastman |
| FT02Z:downq50 | s | FCV02Z:upq50 | 48.73 | 57.616 | 34 | True | `MID-S.down.q50 -s-> MID-S.up.q50` | — | tennessee_eastman |
| B400B:downq50 | s | FCV02Z:upq50 | 48.73 | 57.616 | 34 | True | `MID-S.down.q50 -s-> MID-S.up.q50` | — | tennessee_eastman |
| TIT02:upq20 | s | TIT02:upq80 | 48.676 | 62.197 | 40 | True | `MID.up.q20 -s-> MID.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| B4005:upq20 | s | B400B:upq20 | 45.913 | 47.6 | 40 | True | `MID-S.up.q20 -s-> MID-S.up.q20` | — | tennessee_eastman |
| B4005:upq20 | s | FT02:upq20 | 45.913 | 44.318 | 40 | True | `MID-S.up.q20 -s-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B4005:upq20 | s | FT02Z:upq20 | 45.913 | 44.318 | 40 | True | `MID-S.up.q20 -s-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| PIT02:upq10 | s | FCV01D:downq10 | 43.922 | 44.292 | 23 | True | `MID.up.q10 -s-> MID-S.down.q10` | building_59 | tennessee_eastman |
| VYT03:downq80 | l | VYT02:upq80 | 43.873 | 55.313 | 4 | False | `SLOW.down.q80 -l-> SLOW.up.q80` | — | tennessee_eastman |
| ST_TT01:upq10 | s | TIT02:upq80 | 43.762 | 44.077 | 57 | True | `MID.up.q10 -s-> MID.up.q80` | — | tennessee_eastman, building_59 |
| VYT02:downq50 | s | VYT02:upq50 | 42.882 | 39.24 | 22 | True | `SLOW.down.q50 -s-> SLOW.up.q50 [same role]` | — | tennessee_eastman |
| VXT03:upq80 | s | VXT03:downq80 | 42.454 | 36.97 | 20 | False | `SLOW.up.q80 -s-> SLOW.down.q80 [same role]` | — | tennessee_eastman, building_59 |
| B3005:downq10 | s | FT01:downq20 | 42.359 | 65.656 | 4 | False | `SET.down.q10 -s-> MID.down.q20` | — | tennessee_eastman, building_59 |
| FCV02Z:downq80 | s | PIT02:upq10 | 41.518 | 38.674 | 24 | True | `MID-S.down.q80 -s-> MID.up.q10` | — | tennessee_eastman, building_59 |
| VXT03:downq50 | s | VXT03:upq50 | 40.916 | 69.118 | 6 | False | `SLOW.down.q50 -s-> SLOW.up.q50 [same role]` | — | tennessee_eastman, building_59 |
| B4005:downq20 | s | FCV02Z:upq80 | 40.582 | 41.873 | 31 | True | `MID-S.down.q20 -s-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| B4005:upq20 | s | FCV02Z:downq80 | 39.726 | 39.594 | 33 | True | `MID-S.up.q20 -s-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| B4005:downq50 | s | B400B:downq50 | 39.622 | 61.992 | 48 | True | `MID-S.down.q50 -s-> MID-S.down.q50` | — | tennessee_eastman |
| B4005:downq50 | s | FT02:downq50 | 39.622 | 61.992 | 48 | True | `MID-S.down.q50 -s-> MID-S.down.q50` | — | tennessee_eastman |
| B4005:downq50 | s | FT02Z:downq50 | 39.622 | 61.992 | 48 | True | `MID-S.down.q50 -s-> MID-S.down.q50` | — | tennessee_eastman |
| VXT03:downq20 | m | VXT03:upq20 | 39.536 | 29.511 | 24 | True | `SLOW.down.q20 -m-> SLOW.up.q20 [same role]` | — | tennessee_eastman, building_59 |
| FT02:downq50 | s | FCV02Z:upq20 | 38.747 | 25.619 | 16 | True | `MID-S.down.q50 -s-> MID-S.up.q20` | — | tennessee_eastman |
| FT02Z:downq50 | s | FCV02Z:upq20 | 38.747 | 25.96 | 16 | True | `MID-S.down.q50 -s-> MID-S.up.q20` | — | tennessee_eastman |
| B400B:downq50 | s | FCV02Z:upq20 | 38.747 | 25.96 | 16 | True | `MID-S.down.q50 -s-> MID-S.up.q20` | — | tennessee_eastman |
| VYT02:downq20 | s | VYT02:upq20 | 37.534 | 51.331 | 46 | True | `SLOW.down.q20 -s-> SLOW.up.q20 [same role]` | — | tennessee_eastman |
| VYT03:downq20 | s | VYT03:upq20 | 35.732 | 25.949 | 21 | True | `SLOW.down.q20 -s-> SLOW.up.q20 [same role]` | — | tennessee_eastman |
| FT02Z:upq20 | s | PIT02:upq10 | 35.587 | 29.062 | 30 | True | `MID-S.up.q20 -s-> MID.up.q10` | — | tennessee_eastman, building_59 |
| B400B:upq20 | s | PIT02:upq10 | 35.587 | 29.228 | 30 | True | `MID-S.up.q20 -s-> MID.up.q10` | — | tennessee_eastman |
| PIT02:upq90 | s | FCV02Z:upq50 | 34.614 | 35.132 | 31 | True | `MID.up.q90 -s-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| FT02:upq20 | s | PIT02:upq10 | 34.359 | 29.062 | 30 | True | `MID-S.up.q20 -s-> MID.up.q10` | — | tennessee_eastman, building_59 |
| VXT02:upq50 | s | VXT02:downq50 | 34.345 | 16.721 | 21 | True | `SLOW.up.q50 -s-> SLOW.down.q50 [same role]` | building_59 | tennessee_eastman |
| FCV02Z:upq50 | s | PIT02:downq90 | 34.191 | 29.135 | 35 | True | `MID-S.up.q50 -s-> MID.down.q90` | — | tennessee_eastman, building_59 |
| FCV02Z:upq20 | s | PIT02:downq90 | 34.191 | 15.097 | 21 | True | `MID-S.up.q20 -s-> MID.down.q90` | — | tennessee_eastman, building_59 |
| B4022:upq80 | s | B4022:downq80 | 34.184 | 31.781 | 34 | True | `SLOW.up.q80 -s-> SLOW.down.q80 [same role]` | tennessee_eastman, building_59 | — |
| VYT03:upq50 | s | VYT03:downq50 | 33.94 | 35.406 | 22 | True | `SLOW.up.q50 -s-> SLOW.down.q50 [same role]` | — | tennessee_eastman |
| VXT02:downq50 | s | VXT02:upq50 | 33.503 | 61.758 | 12 | False | `SLOW.down.q50 -s-> SLOW.up.q50 [same role]` | building_59 | tennessee_eastman |
| VYT03:downq50 | s | VYT03:upq50 | 32.953 | 34.941 | 22 | True | `SLOW.down.q50 -s-> SLOW.up.q50 [same role]` | — | tennessee_eastman |
| FCV01Z:peak | s | B4005:downq50 | 32.676 | 26.634 | 25 | True | `MID-S.peak -s-> MID-S.down.q50` | — | tennessee_eastman |
| VXT02:upq80 | s | VXT02:downq80 | 32.147 | 44.356 | 27 | True | `SLOW.up.q80 -s-> SLOW.down.q80 [same role]` | building_59 | tennessee_eastman |
| PIT02:upq90 | s | FCV02Z:upq20 | 32.073 | 17.808 | 17 | True | `MID.up.q90 -s-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B2004:downq20 | s | B3004:downq50 | 32.009 | 30.956 | 4 | False | `SET.down.q20 -s-> SET.down.q50` | — | — |
| FCV01D:upq10 | s | B4005:upq20 | 31.56 | 24.969 | 22 | True | `MID-S.up.q10 -s-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FT02:downq50 | s | PIT02:upq90 | 31.396 | 24.037 | 38 | True | `MID-S.down.q50 -s-> MID.up.q90` | — | tennessee_eastman |
| FT02Z:downq50 | s | PIT02:upq90 | 31.396 | 24.357 | 38 | True | `MID-S.down.q50 -s-> MID.up.q90` | — | tennessee_eastman |
| B400B:downq50 | s | PIT02:upq90 | 31.396 | 24.357 | 38 | True | `MID-S.down.q50 -s-> MID.up.q90` | — | tennessee_eastman |
| PIT02:downq10 | s | B400B:downq20 | 30.824 | 26.749 | 40 | True | `MID.down.q10 -s-> MID-S.down.q20` | — | tennessee_eastman |
| PIT02:downq10 | s | FT02:downq20 | 30.824 | 26.749 | 40 | True | `MID.down.q10 -s-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| PIT02:downq10 | s | FT02Z:downq20 | 30.824 | 26.749 | 40 | True | `MID.down.q10 -s-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| SIT02:trough | s | CO_rpm:trough | 30.294 | 19.636 | 59 | True | `MID.trough -s-> MID.trough` | — | — |
| FCV02Z:upq50 | s | B4005:downq20 | 29.408 | 41.275 | 17 | True | `MID-S.up.q50 -s-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| SIT01:trough | s | CO_rpm:trough | 29.258 | 19.636 | 56 | True | `MID.trough -s-> MID.trough` | — | — |
| TIT01:peak | s | FCV02Z:upq50 | 28.56 | 36.466 | 23 | True | `MID.peak -s-> MID-S.up.q50` | — | tennessee_eastman |
| CO_rpm:peak | s | SIT02:peak | 27.251 | 22.939 | 60 | True | `MID.peak -s-> MID.peak` | — | — |
| CO_rpm:peak | s | SIT01:peak | 27.068 | 22.785 | 60 | True | `MID.peak -s-> MID.peak` | — | — |
| FCV01Z:trough | s | B4005:upq20 | 27.008 | 28.13 | 18 | True | `MID-S.trough -s-> MID-S.up.q20` | — | tennessee_eastman |
| FCV01D:upq10 | s | PIT02:downq10 | 26.733 | 23.501 | 33 | True | `MID-S.up.q10 -s-> MID.down.q10` | — | tennessee_eastman, building_59 |
| VYT02:downq50 | l | VYT03:upq80 | 26.684 | 82.63 | 5 | True | `SLOW.down.q50 -l-> SLOW.up.q80` | — | tennessee_eastman |
| PIT02:downq10 | s | FCV02Z:upq80 | 26.671 | 29.329 | 33 | True | `MID.down.q10 -s-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| HILout:upq80 | m | HILout:downq80 | 26.189 | 16.819 | 46 | True | `SLOW.up.q80 -m-> SLOW.down.q80 [same role]` | — | tennessee_eastman, building_59 |
| LCV01Z:downq50 | s | B3005:downq10 | 25.949 | 81.595 | 3 | False | `MID.down.q50 -s-> SET.down.q10` | — | tennessee_eastman, building_59 |
| PIT02:downq90 | s | B4005:upq50 | 25.665 | 20.658 | 27 | True | `MID.down.q90 -s-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| FT02Z:downq20 | m | FCV01D:downq10 | 25.483 | 18.456 | 37 | True | `MID-S.down.q20 -m-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| FT02:downq20 | m | FCV01D:downq10 | 25.483 | 18.51 | 37 | True | `MID-S.down.q20 -m-> MID-S.down.q10` | building_59 | tennessee_eastman |
| B400B:downq20 | m | FCV01D:downq10 | 25.483 | 18.142 | 37 | True | `MID-S.down.q20 -m-> MID-S.down.q10` | — | tennessee_eastman |
| B3004:downq20 | s | FT01:upq50 | 25.4 | 19.05 | 4 | False | `SET.down.q20 -s-> MID.up.q50` | — | tennessee_eastman |
| FT01:downq50 | s | B3004:downq80 | 25.135 | 20.617 | 5 | False | `MID.down.q50 -s-> SET.down.q80` | — | tennessee_eastman |
| HILout:upq80 | s | HILout:downq80 | 24.999 | 51.331 | 12 | False | `SLOW.up.q80 -s-> SLOW.down.q80 [same role]` | — | tennessee_eastman, building_59 |
| B3005:downq10 | m | FT01Z:trough | 24.75 | 13.803 | 3 | False | `SET.down.q10 -m-> MID.trough` | — | tennessee_eastman |
| FCV01Z:trough | s | PIT02:downq10 | 24.572 | 14.441 | 29 | True | `MID-S.trough -s-> MID.down.q10` | — | tennessee_eastman |
| VYT02:upq50 | l | VYT03:upq80 | 24.55 | 87.996 | 5 | True | `SLOW.up.q50 -l-> SLOW.up.q80` | — | tennessee_eastman |
| VXT03:downq50 | s | VXT02:downq50 | 24.355 | 22.786 | 5 | True | `SLOW.down.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| VXT03:downq50 | m | VXT03:upq50 | 24.317 | 30.956 | 20 | False | `SLOW.down.q50 -m-> SLOW.up.q50 [same role]` | — | tennessee_eastman, building_59 |
| HILout:downq20 | s | HILout:upq20 | 24.317 | 30.498 | 8 | True | `SLOW.down.q20 -s-> SLOW.up.q20 [same role]` | building_59 | tennessee_eastman |
| VXT02:downq80 | s | VXT03:downq80 | 24.199 | 12.148 | 12 | False | `SLOW.down.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, building_59 |
| SIT02:peak | s | CO_rpm:peak | 24.183 | 27.073 | 36 | True | `MID.peak -s-> MID.peak` | — | — |
| HILout:downq80 | s | HILout:upq80 | 24.077 | 27.861 | 7 | False | `SLOW.down.q80 -s-> SLOW.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| HILout:downq50 | s | HILout:upq50 | 24.051 | 15.009 | 14 | False | `SLOW.down.q50 -s-> SLOW.up.q50 [same role]` | building_59 | tennessee_eastman |
| VT01:upq50 | l | VYT03:upq80 | 24.027 | 118.872 | 4 | True | `MID-S.up.q50 -l-> SLOW.up.q80` | — | tennessee_eastman |
| FCV01Z:trough | s | FCV01D:upq10 | 24.007 | 23.381 | 14 | True | `MID-S.trough -s-> MID-S.up.q10` | — | tennessee_eastman |
| FCV02Z:upq80 | s | B400B:downq20 | 23.66 | 54.713 | 8 | False | `MID-S.up.q80 -s-> MID-S.down.q20` | — | tennessee_eastman |
| FCV02Z:upq80 | s | FT02:downq20 | 23.66 | 49.242 | 8 | False | `MID-S.up.q80 -s-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| FCV02Z:upq80 | s | FT02Z:downq20 | 23.66 | 49.242 | 8 | False | `MID-S.up.q80 -s-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| SIT01:peak | s | CO_rpm:peak | 23.444 | 27.073 | 37 | True | `MID.peak -s-> MID.peak` | — | — |
| FCV02Z:upq80 | m | FCV01D:downq10 | 23.399 | 19.642 | 33 | True | `MID-S.up.q80 -m-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| VYT03:upq50 | l | VYT03:upq80 | 23.381 | 99.367 | 4 | True | `SLOW.up.q50 -l-> SLOW.up.q80 [same role]` | — | tennessee_eastman |
| B3004:downq80 | s | FT01:upq50 | 22.981 | 26.811 | 4 | False | `SET.down.q80 -s-> MID.up.q50` | — | tennessee_eastman |
| VXT03:upq80 | s | VXT02:downq80 | 22.86 | 12.065 | 12 | False | `SLOW.up.q80 -s-> SLOW.down.q80` | — | tennessee_eastman, building_59 |
| VYT03:downq80 | l | VYT02:downq50 | 22.406 | 6.954 | 13 | False | `SLOW.down.q80 -l-> SLOW.down.q50` | — | tennessee_eastman |
| VXT03:downq80 | s | VXT03:upq80 | 22.406 | 12.604 | 10 | False | `SLOW.down.q80 -s-> SLOW.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| VYT03:downq20 | m | VYT03:upq20 | 22.219 | 17.896 | 35 | True | `SLOW.down.q20 -m-> SLOW.up.q20 [same role]` | — | tennessee_eastman |
| B4005:downq20 | m | FCV01D:downq10 | 22.167 | 16.805 | 37 | True | `MID-S.down.q20 -m-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| FCV02Z:downq20 | s | FCV02Z:upq20 | 22.125 | 58.411 | 4 | False | `MID-S.down.q20 -s-> MID-S.up.q20 [same role]` | — | tennessee_eastman, building_59 |
| VXT02:downq80 | s | VXT02:upq80 | 21.717 | 39.247 | 12 | False | `SLOW.down.q80 -s-> SLOW.up.q80 [same role]` | building_59 | tennessee_eastman |
| FT01:downq80 | s | FT01:downq50 | 21.674 | 32.904 | 10 | True | `MID.down.q80 -s-> MID.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| VYT02:downq50 | l | VYT03:downq80 | 21.347 | 61.973 | 4 | False | `SLOW.down.q50 -l-> SLOW.down.q80` | — | tennessee_eastman |
| B3005:upq10 | s | LCV01Z:upq50 | 21.027 | 10.798 | 3 | False | `SET.up.q10 -s-> MID.up.q50` | — | tennessee_eastman, building_59 |
| VYT02:upq80 | l | VYT02:downq50 | 21.006 | 9.022 | 15 | False | `SLOW.up.q80 -l-> SLOW.down.q50 [same role]` | — | tennessee_eastman |
| VT01:downq80 | l | VYT02:downq50 | 20.972 | 11.349 | 13 | False | `MID-S.down.q80 -l-> SLOW.down.q50` | — | tennessee_eastman |
| VYT02:upq50 | m | VYT02:downq50 | 20.908 | 12.958 | 31 | True | `SLOW.up.q50 -m-> SLOW.down.q50 [same role]` | — | tennessee_eastman |
| FCV01D:upq10 | s | FT02:upq20 | 20.818 | 24.776 | 13 | True | `MID-S.up.q10 -s-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| VYT02:upq80 | l | VYT02:upq50 | 20.71 | 7.325 | 15 | False | `SLOW.up.q80 -l-> SLOW.up.q50 [same role]` | — | tennessee_eastman |
| VXT02:upq50 | s | VXT03:upq80 | 20.607 | 15.049 | 14 | False | `SLOW.up.q50 -s-> SLOW.up.q80` | — | tennessee_eastman, building_59 |
| VXT02:upq50 | s | VXT03:upq50 | 20.607 | 42.137 | 9 | False | `SLOW.up.q50 -s-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| VXT02:downq50 | s | VXT03:downq50 | 20.305 | 38.498 | 5 | False | `SLOW.down.q50 -s-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| VYT02:downq80 | l | VYT02:downq50 | 20.301 | 10.113 | 15 | False | `SLOW.down.q80 -l-> SLOW.down.q50 [same role]` | — | tennessee_eastman |
| VYT02:downq80 | l | VYT02:upq50 | 20.015 | 7.624 | 15 | False | `SLOW.down.q80 -l-> SLOW.up.q50 [same role]` | — | tennessee_eastman |
| VYT02:upq50 | l | VYT03:downq80 | 19.64 | 73.33 | 4 | False | `SLOW.up.q50 -l-> SLOW.down.q80` | — | tennessee_eastman |
| B400B:upq80 | s | B400B:downq80 | 19.33 | 16.51 | 19 | False | `MID-S.up.q80 -s-> MID-S.down.q80 [same role]` | — | tennessee_eastman |
| VYT03:upq50 | m | VYT03:downq50 | 19.317 | 13.802 | 39 | True | `SLOW.up.q50 -m-> SLOW.down.q50 [same role]` | — | tennessee_eastman |
| VXT03:downq20 | m | VXT02:upq20 | 19.297 | 13.296 | 26 | True | `SLOW.down.q20 -m-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| LCP01D:downq20 | s | LCP01D:upq20 | 19.267 | 23.388 | 24 | True | `MID-S.down.q20 -s-> MID-S.up.q20 [same role]` | tennessee_eastman, nasa_battery | building_59, fingrid |
| FT01Z:trough | s | B3004:downq80 | 19.253 | 32.575 | 5 | False | `MID.trough -s-> SET.down.q80` | — | tennessee_eastman |
| FCV01D:upq10 | s | B400B:upq20 | 19.216 | 24.776 | 12 | True | `MID-S.up.q10 -s-> MID-S.up.q20` | — | tennessee_eastman |
| FCV01D:upq10 | s | FT02Z:upq20 | 19.216 | 24.776 | 12 | True | `MID-S.up.q10 -s-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| VT01:downq80 | l | VYT02:upq50 | 19.086 | 8.607 | 12 | False | `MID-S.down.q80 -l-> SLOW.up.q50` | — | tennessee_eastman |
| VT01:upq50 | m | VYT03:downq50 | 18.979 | 18.821 | 12 | True | `MID-S.up.q50 -m-> SLOW.down.q50` | — | tennessee_eastman |
| FT01Z:peak | s | B3004:upq80 | 18.939 | 42.169 | 6 | True | `MID.peak -s-> SET.up.q80` | — | tennessee_eastman |
| TIT01:peak | s | FCV02Z:upq20 | 18.883 | 24.646 | 9 | True | `MID.peak -s-> MID-S.up.q20` | — | tennessee_eastman |
| LCV01D:downq50 | s | B3005:downq10 | 18.846 | 44.955 | 4 | True | `MID.down.q50 -s-> SET.down.q10` | — | tennessee_eastman, building_59 |
| VYT02:downq50 | m | VYT02:upq50 | 18.815 | 18.892 | 30 | True | `SLOW.down.q50 -m-> SLOW.up.q50 [same role]` | — | tennessee_eastman |
| PIT02:downq90 | s | B4005:downq20 | 18.813 | 32.277 | 19 | False | `MID.down.q90 -s-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| CO_rpm:trough | s | SIT02:trough | 18.807 | 16.668 | 42 | True | `MID.trough -s-> MID.trough` | — | — |
| VXT02:upq80 | m | VXT03:downq80 | 18.71 | 10.719 | 36 | True | `SLOW.up.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, building_59 |
| CO_rpm:trough | s | SIT01:trough | 18.681 | 14.717 | 42 | True | `MID.trough -s-> MID.trough` | — | — |
| PIT02:upq90 | s | PIT02:downq90 | 18.667 | 18.227 | 29 | True | `MID.up.q90 -s-> MID.down.q90 [same role]` | building_59 | tennessee_eastman |
| FT02:downq50 | s | TIT01:peak | 18.655 | 29.021 | 17 | True | `MID-S.down.q50 -s-> MID.peak` | — | tennessee_eastman |
| FT02Z:downq50 | s | TIT01:peak | 18.655 | 29.408 | 17 | True | `MID-S.down.q50 -s-> MID.peak` | — | tennessee_eastman |
| B400B:downq50 | s | TIT01:peak | 18.655 | 29.408 | 17 | True | `MID-S.down.q50 -s-> MID.peak` | — | tennessee_eastman |
| VXT02:upq80 | s | VXT03:upq80 | 18.574 | 21.747 | 14 | True | `SLOW.up.q80 -s-> SLOW.up.q80` | — | tennessee_eastman, building_59 |
| VXT03:downq80 | m | VXT03:upq80 | 18.495 | 18.738 | 31 | True | `SLOW.down.q80 -m-> SLOW.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| HILout:downq20 | m | HILout:upq20 | 18.492 | 16.07 | 22 | True | `SLOW.down.q20 -m-> SLOW.up.q20 [same role]` | building_59 | tennessee_eastman |
| LCP01D:upq80 | s | LCP01D:downq80 | 18.148 | 23.015 | 33 | True | `MID-S.up.q80 -s-> MID-S.down.q80 [same role]` | tennessee_eastman, nasa_battery | building_59, fingrid |
| FCV01D:upq10 | m | FCV02Z:downq80 | 18.084 | 10.186 | 26 | True | `MID-S.up.q10 -m-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| VXT03:upq50 | m | VXT03:downq50 | 18.038 | 25.495 | 14 | False | `SLOW.up.q50 -m-> SLOW.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| VYT02:upq50 | l | VYT02:upq80 | 17.854 | 69.997 | 8 | False | `SLOW.up.q50 -l-> SLOW.up.q80 [same role]` | — | tennessee_eastman |
| FT01:downq50 | s | B2004:downq20 | 17.823 | 24.366 | 3 | False | `MID.down.q50 -s-> SET.down.q20` | — | building_59 |
| VYT03:downq50 | m | VYT03:upq50 | 17.758 | 15.319 | 37 | False | `SLOW.down.q50 -m-> SLOW.up.q50 [same role]` | — | tennessee_eastman |
| FT01:upq20 | m | FT01:downq20 | 17.586 | 10.049 | 24 | True | `MID.up.q20 -m-> MID.down.q20 [same role]` | — | tennessee_eastman, building_59 |
| FCV02Z:upq50 | s | PIT02:downq10 | 17.584 | 23.308 | 18 | True | `MID-S.up.q50 -s-> MID.down.q10` | — | tennessee_eastman, building_59 |
| FCV02Z:upq50 | m | B400B:downq20 | 17.545 | 20.432 | 38 | True | `MID-S.up.q50 -m-> MID-S.down.q20` | — | tennessee_eastman |
| FCV02Z:upq50 | m | FT02:downq20 | 17.545 | 20.432 | 38 | True | `MID-S.up.q50 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| FCV02Z:upq50 | m | FT02Z:downq20 | 17.545 | 20.432 | 38 | True | `MID-S.up.q50 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| FCV03D:peak | s | FT03Z:peak | 17.508 | 16.771 | 16 | False | `MID.peak -s-> MID.peak` | — | tennessee_eastman |
| VXT02:downq50 | m | VXT02:upq50 | 17.212 | 13.671 | 27 | False | `SLOW.down.q50 -m-> SLOW.up.q50 [same role]` | building_59 | tennessee_eastman |
| VYT02:downq50 | l | VYT02:upq80 | 16.981 | 65.729 | 7 | False | `SLOW.down.q50 -l-> SLOW.up.q80 [same role]` | — | tennessee_eastman |
| FCV02Z:upq50 | m | FCV02Z:upq80 | 16.948 | 20.0 | 35 | True | `MID-S.up.q50 -m-> MID-S.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| LCV01Z:downq20 | s | FT01:downq20 | 16.922 | 18.699 | 15 | True | `MID.down.q20 -s-> MID.down.q20` | — | tennessee_eastman, building_59 |
| FT02Z:upq80 | s | FT02Z:downq80 | 16.855 | 16.805 | 18 | False | `MID-S.up.q80 -s-> MID-S.down.q80 [same role]` | building_59 | tennessee_eastman |
| VXT02:upq80 | m | VXT02:downq80 | 16.791 | 12.626 | 36 | True | `SLOW.up.q80 -m-> SLOW.down.q80 [same role]` | building_59 | tennessee_eastman |
| LCV01D:upq20 | s | B3005:upq10 | 16.725 | 37.643 | 3 | False | `MID.up.q20 -s-> SET.up.q10` | — | tennessee_eastman, building_59 |
| VXT03:upq80 | m | VXT03:downq80 | 16.62 | 14.733 | 30 | True | `SLOW.up.q80 -m-> SLOW.down.q80 [same role]` | — | tennessee_eastman, building_59 |
| FCV01D:upq10 | m | B400B:upq20 | 16.58 | 10.684 | 25 | True | `MID-S.up.q10 -m-> MID-S.up.q20` | — | tennessee_eastman |
| FCV01D:upq10 | m | FT02Z:upq20 | 16.58 | 10.684 | 25 | True | `MID-S.up.q10 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| VYT03:upq50 | s | VYT02:downq50 | 16.529 | 7.986 | 10 | False | `SLOW.up.q50 -s-> SLOW.down.q50` | — | tennessee_eastman |
| VYT03:downq20 | s | VXT03:upq80 | 16.529 | 25.207 | 10 | False | `SLOW.down.q20 -s-> SLOW.up.q80` | — | tennessee_eastman |
| ST_TT01:upq10 | s | TIT02:upq50 | 16.406 | 15.6 | 21 | True | `MID.up.q10 -s-> MID.up.q50` | — | tennessee_eastman, building_59 |
| B400B:upq80 | s | FT02Z:downq80 | 16.278 | 13.208 | 16 | False | `MID-S.up.q80 -s-> MID-S.down.q80` | — | tennessee_eastman |
| B4005:upq20 | s | PIT02:upq10 | 16.259 | 17.437 | 28 | True | `MID-S.up.q20 -s-> MID.up.q10` | — | tennessee_eastman, building_59 |
| PIT02:downq10 | s | B400B:upq20 | 16.183 | 14.59 | 21 | False | `MID.down.q10 -s-> MID-S.up.q20` | — | tennessee_eastman |
| PIT02:downq10 | s | FT02:upq20 | 16.183 | 15.806 | 21 | False | `MID.down.q10 -s-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| PIT02:downq10 | s | FT02Z:upq20 | 16.183 | 15.806 | 21 | False | `MID.down.q10 -s-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| VYT03:upq50 | m | VT01:upq50 | 16.151 | 14.321 | 10 | True | `SLOW.up.q50 -m-> MID-S.up.q50` | — | tennessee_eastman |
| FCV02Z:upq20 | m | FCV02Z:upq80 | 16.139 | 7.766 | 18 | True | `MID-S.up.q20 -m-> MID-S.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| FCV03D:peak | s | FT03:peak | 16.092 | 16.443 | 15 | False | `MID.peak -s-> MID.peak` | — | — |
| FCV01D:downq10 | m | FCV01D:upq10 | 16.005 | 11.95 | 20 | False | `MID-S.down.q10 -m-> MID-S.up.q10 [same role]` | building_59 | tennessee_eastman, nasa_battery |
| FT02Z:upq80 | s | B400B:downq80 | 15.919 | 16.805 | 17 | False | `MID-S.up.q80 -s-> MID-S.down.q80` | — | tennessee_eastman |
| FCV01D:upq10 | m | FT02:upq20 | 15.917 | 10.684 | 24 | True | `MID-S.up.q10 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| VT01:downq50 | m | VYT03:downq50 | 15.888 | 12.98 | 13 | True | `MID-S.down.q50 -m-> SLOW.down.q50` | — | tennessee_eastman |
| VT01:downq50 | m | VYT03:upq50 | 15.679 | 12.809 | 13 | True | `MID-S.down.q50 -m-> SLOW.up.q50` | — | tennessee_eastman |
| FCV03D:trough | s | FT03:trough | 15.55 | 19.089 | 15 | True | `MID.trough -s-> MID.trough` | — | — |
| VXT02:upq50 | m | VXT02:downq50 | 15.522 | 16.445 | 23 | False | `SLOW.up.q50 -m-> SLOW.down.q50 [same role]` | building_59 | tennessee_eastman |
| FCV01Z:trough | m | B400B:upq20 | 15.498 | 14.773 | 33 | True | `MID-S.trough -m-> MID-S.up.q20` | — | tennessee_eastman |
| FCV01Z:trough | m | FT02Z:upq20 | 15.498 | 14.773 | 33 | True | `MID-S.trough -m-> MID-S.up.q20` | — | tennessee_eastman |
| FCV02Z:upq20 | m | B400B:downq20 | 15.388 | 7.405 | 18 | True | `MID-S.up.q20 -m-> MID-S.down.q20` | — | tennessee_eastman |
| FCV02Z:upq20 | m | FT02:downq20 | 15.388 | 7.405 | 18 | True | `MID-S.up.q20 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| FCV02Z:upq20 | m | FT02Z:downq20 | 15.388 | 7.405 | 18 | True | `MID-S.up.q20 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| FT02:downq50 | m | B400B:downq20 | 15.363 | 20.202 | 38 | True | `MID-S.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman |
| FT02:downq50 | m | FT02:downq20 | 15.363 | 20.202 | 38 | True | `MID-S.down.q50 -m-> MID-S.down.q20 [same role]` | — | tennessee_eastman |
| FT02:downq50 | m | FT02Z:downq20 | 15.363 | 20.202 | 38 | True | `MID-S.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman |
| FT02Z:downq50 | m | B400B:downq20 | 15.363 | 20.28 | 38 | True | `MID-S.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman |
| FT02Z:downq50 | m | FT02:downq20 | 15.363 | 20.28 | 38 | True | `MID-S.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman |
| FT02Z:downq50 | m | FT02Z:downq20 | 15.363 | 20.28 | 38 | True | `MID-S.down.q50 -m-> MID-S.down.q20 [same role]` | — | tennessee_eastman |
| B400B:downq50 | m | B400B:downq20 | 15.363 | 20.28 | 38 | True | `MID-S.down.q50 -m-> MID-S.down.q20 [same role]` | — | tennessee_eastman |
| B400B:downq50 | m | FT02:downq20 | 15.363 | 20.28 | 38 | True | `MID-S.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman |
| B400B:downq50 | m | FT02Z:downq20 | 15.363 | 20.28 | 38 | True | `MID-S.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman |
| SIT01:trough | s | HILout:upq20 | 15.287 | 8.618 | 10 | False | `MID.trough -s-> SLOW.up.q20` | — | — |
| HILout:upq20 | s | CO_rpm:peak | 15.253 | 7.445 | 7 | True | `SLOW.up.q20 -s-> MID.peak` | — | building_59 |
| B4005:downq50 | s | TIT01:peak | 15.168 | 16.752 | 24 | True | `MID-S.down.q50 -s-> MID.peak` | — | tennessee_eastman |
| FCV02Z:upq50 | m | FCV01D:downq10 | 15.127 | 19.524 | 32 | True | `MID-S.up.q50 -m-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| LCV01Z:downq50 | s | FT01:downq50 | 15.081 | 6.277 | 17 | True | `MID.down.q50 -s-> MID.down.q50` | — | tennessee_eastman, building_59 |
| FCV01Z:trough | m | FT02:upq20 | 15.029 | 14.773 | 32 | True | `MID-S.trough -m-> MID-S.up.q20` | — | tennessee_eastman |
| SIT02:trough | s | HILout:upq20 | 15.023 | 8.618 | 10 | False | `MID.trough -s-> SLOW.up.q20` | — | — |
| B4005:upq50 | m | FCV02Z:downq50 | 14.945 | 14.698 | 29 | True | `MID-S.up.q50 -m-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| B4005:downq50 | m | FCV02Z:upq50 | 14.873 | 17.124 | 46 | True | `MID-S.down.q50 -m-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| LCV01Z:downq20 | s | LCV01Z:upq20 | 14.866 | 8.646 | 38 | True | `MID.down.q20 -s-> MID.up.q20 [same role]` | tennessee_eastman, building_59 | — |
| FT02:downq50 | m | FCV02Z:upq80 | 14.84 | 21.187 | 35 | True | `MID-S.down.q50 -m-> MID-S.up.q80` | — | tennessee_eastman |
| FT02Z:downq50 | m | FCV02Z:upq80 | 14.84 | 21.269 | 35 | True | `MID-S.down.q50 -m-> MID-S.up.q80` | — | tennessee_eastman |
| B400B:downq50 | m | FCV02Z:upq80 | 14.84 | 21.269 | 35 | True | `MID-S.down.q50 -m-> MID-S.up.q80` | — | tennessee_eastman |
| B3005:downq10 | s | LCV01Z:downq20 | 14.571 | 22.586 | 4 | False | `SET.down.q10 -s-> MID.down.q20` | — | tennessee_eastman, building_59 |
| VYT02:downq50 | l | VYT02:downq80 | 14.555 | 53.209 | 6 | False | `SLOW.down.q50 -l-> SLOW.down.q80 [same role]` | — | tennessee_eastman |
| LCV01Z:upq80 | s | LCV01Z:downq80 | 14.544 | 23.824 | 35 | True | `MID.up.q80 -s-> MID.down.q80 [same role]` | tennessee_eastman, building_59 | — |
| VT01:downq80 | l | VXT02:downq80 | 14.478 | 9.401 | 10 | False | `MID-S.down.q80 -l-> SLOW.down.q80` | — | tennessee_eastman |
| VYT02:upq50 | m | VT01:upq50 | 14.368 | 14.789 | 7 | True | `SLOW.up.q50 -m-> MID-S.up.q50` | — | tennessee_eastman |
| VYT03:upq20 | m | VYT03:downq20 | 14.365 | 9.241 | 21 | True | `SLOW.up.q20 -m-> SLOW.down.q20 [same role]` | — | tennessee_eastman |
| FT02Z:downq20 | m | PIT02:upq10 | 14.293 | 12.479 | 42 | True | `MID-S.down.q20 -m-> MID.up.q10` | — | tennessee_eastman, building_59 |
| FT02:downq20 | m | PIT02:upq10 | 14.293 | 12.515 | 42 | True | `MID-S.down.q20 -m-> MID.up.q10` | — | tennessee_eastman, building_59 |
| B400B:downq20 | m | PIT02:upq10 | 14.293 | 12.267 | 42 | True | `MID-S.down.q20 -m-> MID.up.q10` | — | tennessee_eastman |
| FCV01Z:trough | m | FCV02Z:downq80 | 14.284 | 15.493 | 29 | False | `MID-S.trough -m-> MID-S.down.q80` | — | tennessee_eastman |
| B4005:downq50 | m | FCV02Z:upq20 | 14.204 | 6.808 | 26 | True | `MID-S.down.q50 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FT02:downq50 | m | B4005:downq20 | 14.125 | 18.097 | 39 | True | `MID-S.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman |
| FT02Z:downq50 | m | B4005:downq20 | 14.125 | 18.167 | 39 | True | `MID-S.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman |
| B400B:downq50 | m | B4005:downq20 | 14.125 | 18.167 | 39 | True | `MID-S.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman |
| FT02:upq80 | s | FT02:downq80 | 14.046 | 15.754 | 16 | True | `MID-S.up.q80 -s-> MID-S.down.q80 [same role]` | building_59 | tennessee_eastman |
| LCV01Z:downq80 | s | FT01:downq50 | 14.046 | 6.961 | 13 | True | `MID.down.q80 -s-> MID.down.q50` | — | tennessee_eastman, building_59 |
| B3004:downq20 | s | LCV01Z:upq50 | 14.018 | 11.682 | 6 | False | `SET.down.q20 -s-> MID.up.q50` | tennessee_eastman | — |
| VYT02:upq50 | s | VYT03:downq50 | 14.016 | 18.214 | 7 | False | `SLOW.up.q50 -s-> SLOW.down.q50` | — | tennessee_eastman |
| VXT02:downq80 | m | VXT02:upq80 | 13.986 | 15.529 | 33 | True | `SLOW.down.q80 -m-> SLOW.up.q80 [same role]` | building_59 | tennessee_eastman |
| VYT03:upq20 | s | VXT02:downq80 | 13.921 | 36.195 | 7 | True | `SLOW.up.q20 -s-> SLOW.down.q80` | — | tennessee_eastman |
| B4005:downq20 | m | PIT02:upq10 | 13.913 | 12.455 | 47 | True | `MID-S.down.q20 -m-> MID.up.q10` | — | tennessee_eastman, building_59 |
| FT01Z:trough | s | B3004:downq50 | 13.905 | 23.527 | 5 | False | `MID.trough -s-> SET.down.q50` | — | tennessee_eastman |
| B400B:upq50 | m | FCV02Z:downq50 | 13.845 | 16.946 | 26 | True | `MID-S.up.q50 -m-> MID-S.down.q50` | — | tennessee_eastman |
| FT02Z:upq50 | m | FCV02Z:downq50 | 13.845 | 16.946 | 26 | True | `MID-S.up.q50 -m-> MID-S.down.q50` | — | tennessee_eastman |
| FT02:upq50 | m | FCV02Z:downq50 | 13.845 | 16.946 | 26 | True | `MID-S.up.q50 -m-> MID-S.down.q50` | — | tennessee_eastman |
| FCV03D:trough | s | FT03Z:trough | 13.746 | 19.47 | 13 | True | `MID.trough -s-> MID.trough` | — | tennessee_eastman |
| 24Vdc:peak | l | VYT03:downq50 | 13.732 | 6.416 | 17 | False | `SLOW.peak -l-> SLOW.down.q50` | — | — |
| FCV02Z:downq80 | m | TIT02:downq50 | 13.682 | 6.27 | 20 | True | `MID-S.down.q80 -m-> MID.down.q50` | — | tennessee_eastman, building_59 |
| FT01Z:peak | s | B3004:upq50 | 13.678 | 30.455 | 6 | True | `MID.peak -s-> SET.up.q50` | — | tennessee_eastman |
| B4005:downq50 | m | B400B:downq20 | 13.632 | 17.217 | 37 | True | `MID-S.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman |
| B4005:downq50 | m | FT02:downq20 | 13.632 | 17.217 | 37 | True | `MID-S.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B4005:downq50 | m | FT02Z:downq20 | 13.632 | 17.217 | 37 | True | `MID-S.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| PCV01Z:peak | s | FT01:downq50 | 13.63 | 17.514 | 9 | False | `MID-S.peak -s-> MID.down.q50` | — | — |
| PIT02:downq10 | m | FCV01D:downq10 | 13.616 | 10.96 | 38 | True | `MID.down.q10 -m-> MID-S.down.q10` | building_59 | tennessee_eastman |
| TIT01:peak | s | PIT02:downq90 | 13.601 | 10.511 | 19 | True | `MID.peak -s-> MID.down.q90` | — | tennessee_eastman |
| VT01:upq80 | l | VXT02:upq80 | 13.506 | 9.916 | 10 | False | `MID-S.up.q80 -l-> SLOW.up.q80` | — | tennessee_eastman |
| FCV01Z:trough | s | FT02:upq20 | 13.399 | 8.564 | 8 | False | `MID-S.trough -s-> MID-S.up.q20` | — | tennessee_eastman |
| FCV03Z:trough | s | FT01Z:trough | 13.398 | 10.753 | 14 | True | `MID.trough -s-> MID.trough` | — | — |
| B3004:downq50 | s | LCV01Z:upq50 | 13.317 | 12.683 | 9 | False | `SET.down.q50 -s-> MID.up.q50` | — | tennessee_eastman |
| LCV01Z:downq50 | s | B3004:downq80 | 13.307 | 18.83 | 5 | False | `MID.down.q50 -s-> SET.down.q80` | — | tennessee_eastman |
| B400B:upq20 | m | TIT02:downq50 | 13.224 | 6.719 | 22 | True | `MID-S.up.q20 -m-> MID.down.q50` | — | tennessee_eastman |
| B4005:downq50 | m | FCV02Z:upq80 | 13.138 | 18.057 | 34 | True | `MID-S.down.q50 -m-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| FT01:upq20 | s | FT01:downq20 | 13.066 | 12.01 | 8 | True | `MID.up.q20 -s-> MID.down.q20 [same role]` | — | tennessee_eastman, building_59 |
| FT02:upq20 | m | TIT02:downq50 | 13.065 | 7.448 | 22 | True | `MID-S.up.q20 -m-> MID.down.q50` | — | tennessee_eastman, building_59 |
| FT02Z:upq20 | m | TIT02:downq50 | 13.034 | 7.284 | 22 | True | `MID-S.up.q20 -m-> MID.down.q50` | — | tennessee_eastman, building_59 |
| HILout:upq50 | m | HILout:upq80 | 12.809 | 12.113 | 32 | True | `SLOW.up.q50 -m-> SLOW.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| VT01:upq80 | l | VYT03:downq50 | 12.641 | 6.446 | 9 | False | `MID-S.up.q80 -l-> SLOW.down.q50` | — | tennessee_eastman |
| VYT02:upq80 | l | VXT02:downq80 | 12.568 | 7.62 | 10 | False | `SLOW.up.q80 -l-> SLOW.down.q80` | — | tennessee_eastman |
| VXT03:upq80 | m | VXT02:downq80 | 12.43 | 10.743 | 25 | False | `SLOW.up.q80 -m-> SLOW.down.q80` | — | tennessee_eastman, building_59 |
| B400B:upq80 | s | FT02:downq80 | 12.399 | 12.382 | 13 | False | `MID-S.up.q80 -s-> MID-S.down.q80` | — | tennessee_eastman |
| PIT02:downq10 | m | PIT02:upq10 | 12.393 | 9.928 | 70 | True | `MID.down.q10 -m-> MID.up.q10 [same role]` | building_59 | tennessee_eastman |
| FT02:downq50 | s | PIT02:downq90 | 12.393 | 10.926 | 15 | True | `MID-S.down.q50 -s-> MID.down.q90` | — | tennessee_eastman |
| FT02Z:downq50 | s | PIT02:downq90 | 12.393 | 13.286 | 15 | True | `MID-S.down.q50 -s-> MID.down.q90` | — | tennessee_eastman |
| B400B:downq50 | s | PIT02:downq90 | 12.393 | 13.286 | 15 | True | `MID-S.down.q50 -s-> MID.down.q90` | — | tennessee_eastman |
| VXT03:downq80 | m | VXT02:upq80 | 12.315 | 11.211 | 23 | False | `SLOW.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, building_59 |
| VXT02:upq80 | s | VYT03:upq20 | 12.291 | 10.176 | 9 | True | `SLOW.up.q80 -s-> SLOW.up.q20` | — | tennessee_eastman |
| FT02Z:upq80 | s | FT02:downq80 | 12.29 | 12.604 | 14 | False | `MID-S.up.q80 -s-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| FCV02Z:upq80 | m | PIT02:upq10 | 12.263 | 10.784 | 35 | True | `MID-S.up.q80 -m-> MID.up.q10` | — | tennessee_eastman, building_59 |
| FCV03D:peak | s | FT01Z:peak | 12.263 | 7.229 | 13 | False | `MID.peak -s-> MID.peak` | — | tennessee_eastman |
| B4005:downq50 | m | B4005:downq20 | 12.212 | 16.452 | 37 | True | `MID-S.down.q50 -m-> MID-S.down.q20 [same role]` | — | tennessee_eastman, building_59 |
| LIT01:upq80 | s | LIT01:downq80 | 12.196 | 11.038 | 152 | True | `MID.up.q80 -s-> MID.down.q80 [same role]` | tennessee_eastman | — |
| LCV01Z:upq50 | s | FT01:upq50 | 12.115 | 21.638 | 16 | False | `MID.up.q50 -s-> MID.up.q50` | — | tennessee_eastman, building_59 |
| FT03:peak | s | FT01Z:peak | 12.114 | 10.582 | 11 | False | `MID.peak -s-> MID.peak` | — | — |
| LCV01Z:upq80 | s | FT01:upq80 | 12.037 | 8.963 | 11 | False | `MID.up.q80 -s-> MID.up.q80` | — | tennessee_eastman, building_59 |
| B4022:upq50 | s | B4022:downq50 | 12.016 | 14.217 | 95 | True | `SLOW.up.q50 -s-> SLOW.down.q50 [same role]` | building_59 | tennessee_eastman |
| TIT01:trough | m | TIT02:upq80 | 11.998 | 13.994 | 56 | True | `MID.trough -m-> MID.up.q80` | — | tennessee_eastman |
| VXT03:upq80 | m | VXT02:upq80 | 11.932 | 5.785 | 24 | False | `SLOW.up.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, building_59 |
| VYT03:downq20 | s | VXT02:upq80 | 11.867 | 45.244 | 8 | True | `SLOW.down.q20 -s-> SLOW.up.q80` | — | tennessee_eastman |
| TIT01:trough | m | TIT01:peak | 11.844 | 14.888 | 61 | True | `MID.trough -m-> MID.peak [same role]` | — | tennessee_eastman, nasa_battery, physionet_slp |
| VXT02:downq80 | m | VXT03:upq80 | 11.807 | 9.317 | 25 | True | `SLOW.down.q80 -m-> SLOW.up.q80` | — | tennessee_eastman, building_59 |
| TIT01:peak | m | B400B:downq20 | 11.758 | 13.871 | 37 | True | `MID.peak -m-> MID-S.down.q20` | — | tennessee_eastman |
| TIT01:peak | m | FT02:downq20 | 11.758 | 13.871 | 37 | True | `MID.peak -m-> MID-S.down.q20` | — | tennessee_eastman |
| TIT01:peak | m | FT02Z:downq20 | 11.758 | 13.871 | 37 | True | `MID.peak -m-> MID-S.down.q20` | — | tennessee_eastman |
| FCV01Z:trough | s | B400B:upq20 | 11.724 | 8.564 | 7 | False | `MID-S.trough -s-> MID-S.up.q20` | — | tennessee_eastman |
| FCV01Z:trough | s | FT02Z:upq20 | 11.724 | 8.564 | 7 | False | `MID-S.trough -s-> MID-S.up.q20` | — | tennessee_eastman |
| VXT03:upq50 | m | VXT02:downq50 | 11.698 | 12.613 | 13 | False | `SLOW.up.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| HILout:downq80 | m | HILout:upq80 | 11.672 | 11.609 | 23 | True | `SLOW.down.q80 -m-> SLOW.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| B4005:upq20 | m | TIT02:downq50 | 11.661 | 5.326 | 21 | True | `MID-S.up.q20 -m-> MID.down.q50` | — | tennessee_eastman, building_59 |
| FT02:downq50 | m | FCV01D:downq10 | 11.589 | 18.097 | 28 | True | `MID-S.down.q50 -m-> MID-S.down.q10` | — | tennessee_eastman |
| FT02Z:downq50 | m | FCV01D:downq10 | 11.589 | 18.167 | 28 | True | `MID-S.down.q50 -m-> MID-S.down.q10` | — | tennessee_eastman |
| B400B:downq50 | m | FCV01D:downq10 | 11.589 | 18.167 | 28 | True | `MID-S.down.q50 -m-> MID-S.down.q10` | — | tennessee_eastman |
| FCV03D:peak | s | FCV03Z:peak | 11.574 | 18.814 | 11 | False | `MID.peak -s-> MID.peak` | — | building_59 |
| LCV01D:downq20 | s | FT01:downq20 | 11.564 | 10.902 | 18 | True | `MID.down.q20 -s-> MID.down.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:downq50 | s | B3004:downq50 | 11.533 | 18.132 | 6 | False | `MID.down.q50 -s-> SET.down.q50` | — | tennessee_eastman |
| HILout:downq20 | s | CO_rpm:trough | 11.427 | 4.467 | 11 | False | `SLOW.down.q20 -s-> MID.trough` | — | building_59 |
| VYT03:upq50 | s | VYT02:upq50 | 11.408 | 9.842 | 7 | True | `SLOW.up.q50 -s-> SLOW.up.q50` | — | tennessee_eastman |
| FT03:trough | s | FT01Z:trough | 11.393 | 11.963 | 9 | True | `MID.trough -s-> MID.trough` | — | — |
| FT01:downq20 | s | FT01Z:trough | 11.393 | 17.09 | 5 | True | `MID.down.q20 -s-> MID.trough` | — | tennessee_eastman |
| FT03Z:peak | s | FT01Z:peak | 11.392 | 10.582 | 11 | False | `MID.peak -s-> MID.peak` | — | tennessee_eastman |
| TIT02:upq20 | m | TIT01:peak | 11.357 | 13.528 | 57 | True | `MID.up.q20 -m-> MID.peak` | — | tennessee_eastman |
| VT01:downq50 | l | VYT03:downq50 | 11.324 | 4.876 | 29 | True | `MID-S.down.q50 -l-> SLOW.down.q50` | — | tennessee_eastman |
| LCV01Z:upq20 | s | LCV01Z:downq20 | 11.323 | 8.915 | 38 | True | `MID.up.q20 -s-> MID.down.q20 [same role]` | building_59 | tennessee_eastman |
| PIT02:downq10 | s | FCV02Z:downq80 | 11.315 | 11.476 | 14 | False | `MID.down.q10 -s-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| FCV02Z:downq50 | s | TIT02:downq20 | 11.257 | 17.689 | 5 | False | `MID-S.down.q50 -s-> MID.down.q20` | — | tennessee_eastman, building_59 |
| FT02:upq80 | s | B400B:downq80 | 11.237 | 16.805 | 12 | False | `MID-S.up.q80 -s-> MID-S.down.q80` | — | tennessee_eastman |
| FT02:upq80 | s | FT02Z:downq80 | 11.237 | 16.805 | 12 | False | `MID-S.up.q80 -s-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| TIT02:upq20 | m | B4005:downq50 | 11.221 | 12.046 | 44 | True | `MID.up.q20 -m-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| TIT02:upq20 | m | B400B:downq50 | 11.19 | 11.523 | 43 | True | `MID.up.q20 -m-> MID-S.down.q50` | — | tennessee_eastman |
| TIT02:upq20 | m | FT02:downq50 | 11.19 | 11.523 | 43 | True | `MID.up.q20 -m-> MID-S.down.q50` | — | tennessee_eastman |
| TIT02:upq20 | m | FT02Z:downq50 | 11.19 | 11.523 | 43 | True | `MID.up.q20 -m-> MID-S.down.q50` | — | tennessee_eastman |
| B4022:downq20 | s | B4022:upq20 | 11.117 | 14.27 | 108 | True | `SLOW.down.q20 -s-> SLOW.up.q20 [same role]` | tennessee_eastman, building_59 | — |
| PIT02:upq90 | s | TIT01:peak | 11.114 | 10.759 | 13 | False | `MID.up.q90 -s-> MID.peak` | — | tennessee_eastman |
| TIT02:upq50 | m | B4005:downq50 | 11.096 | 11.153 | 45 | True | `MID.up.q50 -m-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| HILout:downq20 | s | SIT02:trough | 11.091 | 6.359 | 10 | False | `SLOW.down.q20 -s-> MID.trough` | — | — |
| SIT02:trough | m | HILout:upq50 | 11.073 | 6.654 | 57 | True | `MID.trough -m-> SLOW.up.q50` | — | — |
| TIT02:upq50 | m | B400B:downq50 | 11.07 | 10.67 | 44 | True | `MID.up.q50 -m-> MID-S.down.q50` | — | tennessee_eastman |
| TIT02:upq50 | m | FT02:downq50 | 11.07 | 10.67 | 44 | True | `MID.up.q50 -m-> MID-S.down.q50` | — | tennessee_eastman |
| TIT02:upq50 | m | FT02Z:downq50 | 11.07 | 10.67 | 44 | True | `MID.up.q50 -m-> MID-S.down.q50` | — | tennessee_eastman |
| HILout:upq20 | m | HILout:downq20 | 11.056 | 24.347 | 14 | True | `SLOW.up.q20 -m-> SLOW.down.q20 [same role]` | building_59 | tennessee_eastman |
| CO_rpm:trough | s | HILout:upq20 | 11.045 | 10.152 | 9 | False | `MID.trough -s-> SLOW.up.q20` | — | building_59 |
| VYT03:upq20 | m | HILout:upq20 | 11.033 | 11.465 | 13 | True | `SLOW.up.q20 -m-> SLOW.up.q20` | — | tennessee_eastman |
| HILout:downq20 | s | SIT01:trough | 11.016 | 6.316 | 10 | False | `SLOW.down.q20 -s-> MID.trough` | — | — |
| TIT01:peak | m | FCV02Z:upq80 | 10.999 | 14.548 | 33 | True | `MID.peak -m-> MID-S.up.q80` | — | tennessee_eastman |
| TIT02:upq50 | m | TIT01:peak | 10.98 | 12.526 | 57 | True | `MID.up.q50 -m-> MID.peak` | — | tennessee_eastman |
| B3004:upq80 | s | LCV01Z:downq50 | 10.896 | 5.627 | 9 | True | `SET.up.q80 -s-> MID.down.q50` | tennessee_eastman | — |
| FT03Z:trough | s | FT01Z:trough | 10.821 | 12.269 | 9 | False | `MID.trough -s-> MID.trough` | — | tennessee_eastman |
| SIT01:trough | m | HILout:upq50 | 10.765 | 6.502 | 57 | True | `MID.trough -m-> SLOW.up.q50` | — | — |
| TIT02:upq80 | m | B400B:downq50 | 10.748 | 11.242 | 46 | True | `MID.up.q80 -m-> MID-S.down.q50` | — | tennessee_eastman |
| TIT02:upq80 | m | FT02:downq50 | 10.748 | 11.242 | 46 | True | `MID.up.q80 -m-> MID-S.down.q50` | — | tennessee_eastman |
| TIT02:upq80 | m | FT02Z:downq50 | 10.748 | 11.242 | 46 | True | `MID.up.q80 -m-> MID-S.down.q50` | — | tennessee_eastman |
| TIT01:peak | s | PIT02:upq90 | 10.737 | 10.511 | 15 | True | `MID.peak -s-> MID.up.q90` | — | tennessee_eastman |
| VT01:upq50 | l | VYT02:downq50 | 10.726 | 3.184 | 25 | True | `MID-S.up.q50 -l-> SLOW.down.q50` | — | tennessee_eastman |
| FT01:downq80 | s | LCV01Z:downq80 | 10.7 | 8.122 | 10 | True | `MID.down.q80 -s-> MID.down.q80` | — | tennessee_eastman, building_59 |
| HILout:downq50 | m | HILout:downq20 | 10.675 | 5.833 | 23 | True | `SLOW.down.q50 -m-> SLOW.down.q20 [same role]` | — | tennessee_eastman, building_59 |
| LCV01Z:upq20 | s | FT01:upq20 | 10.642 | 5.896 | 12 | True | `MID.up.q20 -s-> MID.up.q20` | — | tennessee_eastman, building_59 |
| PIT02:downq90 | s | PIT02:downq10 | 10.624 | 18.227 | 19 | False | `MID.down.q90 -s-> MID.down.q10 [same role]` | — | tennessee_eastman, building_59 |
| B3004:downq80 | s | LCV01Z:upq50 | 10.569 | 12.331 | 5 | False | `SET.down.q80 -s-> MID.up.q50` | — | tennessee_eastman |
| FCV01Z:trough | m | B4005:upq20 | 10.518 | 8.087 | 25 | True | `MID-S.trough -m-> MID-S.up.q20` | — | tennessee_eastman |
| VYT03:downq20 | m | VXT02:downq80 | 10.515 | 23.402 | 19 | True | `SLOW.down.q20 -m-> SLOW.down.q80` | — | tennessee_eastman |
| VYT03:downq50 | l | HILout:downq20 | 10.452 | 9.577 | 18 | True | `SLOW.down.q50 -l-> SLOW.down.q20` | — | tennessee_eastman |
| TIT01:trough | m | B4005:downq50 | 10.438 | 10.587 | 42 | True | `MID.trough -m-> MID-S.down.q50` | — | tennessee_eastman |
| TIT02:upq80 | m | TIT01:peak | 10.375 | 12.373 | 58 | True | `MID.up.q80 -m-> MID.peak` | — | tennessee_eastman |
| FT01:upq50 | s | FT01:upq80 | 10.319 | 12.717 | 5 | False | `MID.up.q50 -s-> MID.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| LCV01Z:upq50 | s | LCV01Z:downq50 | 10.308 | 9.409 | 37 | True | `MID.up.q50 -s-> MID.down.q50 [same role]` | building_59 | tennessee_eastman |
| FT01:upq80 | s | LCV01Z:upq80 | 10.21 | 18.809 | 12 | False | `MID.up.q80 -s-> MID.up.q80` | — | tennessee_eastman, building_59 |
| FCV03Z:trough | s | FT03Z:trough | 10.164 | 12.689 | 9 | True | `MID.trough -s-> MID.trough` | — | — |
| VYT02:upq50 | l | VYT03:downq50 | 10.147 | 6.355 | 31 | False | `SLOW.up.q50 -l-> SLOW.down.q50` | — | tennessee_eastman |
| LCV01Z:upq80 | s | B3004:upq80 | 10.101 | 15.512 | 4 | False | `MID.up.q80 -s-> SET.up.q80` | — | tennessee_eastman |
| FCV01D:upq10 | m | B4005:upq20 | 10.1 | 7.831 | 17 | True | `MID-S.up.q10 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| TIT02:upq80 | m | B4005:downq50 | 10.075 | 9.64 | 44 | True | `MID.up.q80 -m-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| FT02:upq20 | s | TIT02:downq80 | 10.071 | 18.253 | 6 | False | `MID-S.up.q20 -s-> MID.down.q80` | — | tennessee_eastman, building_59 |
| FCV01D:upq10 | m | PIT02:upq10 | 10.065 | 10.318 | 30 | True | `MID-S.up.q10 -m-> MID.up.q10` | building_59 | tennessee_eastman |
| FT01Z:trough | s | FT03Z:trough | 10.011 | 8.47 | 10 | True | `MID.trough -s-> MID.trough` | — | tennessee_eastman |
| FT02Z:downq80 | m | FCV02Z:upq20 | 10.002 | 5.369 | 21 | True | `MID-S.down.q80 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FCV03Z:trough | s | FT03:trough | 9.964 | 9.33 | 9 | True | `MID.trough -s-> MID.trough` | — | — |
| VYT02:downq50 | m | VYT03:upq50 | 9.961 | 14.287 | 17 | False | `SLOW.down.q50 -m-> SLOW.up.q50` | — | tennessee_eastman |
| VXT03:upq20 | l | VYT03:upq50 | 9.929 | 10.319 | 17 | False | `SLOW.up.q20 -l-> SLOW.up.q50` | — | tennessee_eastman |
| FCV03Z:peak | s | FCV03Z:trough | 9.916 | 9.812 | 8 | True | `MID.peak -s-> MID.trough [same role]` | — | building_59, fingrid |
| LCV01Z:downq20 | s | FT01Z:trough | 9.866 | 13.628 | 12 | True | `MID.down.q20 -s-> MID.trough` | — | tennessee_eastman |
| B400B:downq80 | m | FCV02Z:upq20 | 9.838 | 5.234 | 21 | True | `MID-S.down.q80 -m-> MID-S.up.q20` | — | tennessee_eastman |
| LCP01D:downq20 | m | LCP01D:upq20 | 9.83 | 9.483 | 56 | True | `MID-S.down.q20 -m-> MID-S.up.q20 [same role]` | tennessee_eastman, nasa_battery, fingrid | building_59 |
| FT02:downq80 | m | FCV02Z:upq20 | 9.782 | 6.11 | 21 | True | `MID-S.down.q80 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B3004:upq80 | s | LCV01Z:downq80 | 9.746 | 7.55 | 6 | False | `SET.up.q80 -s-> MID.down.q80` | tennessee_eastman | — |
| HT_LD:trough | s | VYT03:downq80 | 9.746 | 18.372 | 3 | False | `MID-S.trough -s-> SLOW.down.q80` | — | — |
| PIT02:downq10 | s | TIT02:downq80 | 9.712 | 7.211 | 17 | True | `MID.down.q10 -s-> MID.down.q80` | — | tennessee_eastman, building_59 |
| B400B:downq80 | s | TIT02:upq50 | 9.712 | 14.741 | 12 | False | `MID-S.down.q80 -s-> MID.up.q50` | — | tennessee_eastman |
| B2004:downq20 | l | B2004:upq20 | 9.692 | 9.909 | 5 | False | `SET.down.q20 -l-> SET.up.q20 [same role]` | — | — |
| TIT01:peak | m | B4005:downq20 | 9.679 | 9.941 | 34 | True | `MID.peak -m-> MID-S.down.q20` | — | tennessee_eastman |
| HILout:downq80 | m | HILout:downq50 | 9.642 | 17.645 | 25 | False | `SLOW.down.q80 -m-> SLOW.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| VT01:downq50 | l | VYT03:upq50 | 9.634 | 6.737 | 25 | False | `MID-S.down.q50 -l-> SLOW.up.q50` | — | tennessee_eastman |
| FT03:trough | s | FT01:upq50 | 9.575 | 13.573 | 5 | False | `MID.trough -s-> MID.up.q50` | — | — |
| PCV01Z:trough | s | FT03Z:peak | 9.552 | 8.963 | 9 | False | `MID-S.trough -s-> MID.peak` | — | — |
| FCV01Z:peak | m | B400B:downq50 | 9.483 | 5.025 | 29 | True | `MID-S.peak -m-> MID-S.down.q50` | — | tennessee_eastman |
| FCV01Z:peak | m | FT02:downq50 | 9.483 | 5.025 | 29 | True | `MID-S.peak -m-> MID-S.down.q50` | — | tennessee_eastman |
| FCV01Z:peak | m | FT02Z:downq50 | 9.483 | 5.025 | 29 | True | `MID-S.peak -m-> MID-S.down.q50` | — | tennessee_eastman |
| VYT02:downq50 | l | VYT03:upq50 | 9.48 | 7.248 | 27 | False | `SLOW.down.q50 -l-> SLOW.up.q50` | — | tennessee_eastman |
| VYT03:upq50 | l | VYT02:upq50 | 9.467 | 8.644 | 23 | True | `SLOW.up.q50 -l-> SLOW.up.q50` | — | tennessee_eastman |
| VYT03:downq20 | m | HILout:downq20 | 9.419 | 8.85 | 12 | True | `SLOW.down.q20 -m-> SLOW.down.q20` | — | tennessee_eastman |
| VXT03:downq50 | m | VXT02:upq50 | 9.404 | 14.511 | 11 | False | `SLOW.down.q50 -m-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| TIT01:trough | m | B400B:downq50 | 9.383 | 10.803 | 37 | True | `MID.trough -m-> MID-S.down.q50` | — | tennessee_eastman |
| TIT01:trough | m | FT02:downq50 | 9.383 | 10.803 | 37 | True | `MID.trough -m-> MID-S.down.q50` | — | tennessee_eastman |
| TIT01:trough | m | FT02Z:downq50 | 9.383 | 10.803 | 37 | True | `MID.trough -m-> MID-S.down.q50` | — | tennessee_eastman |
| LCV01Z:downq50 | s | FT01Z:trough | 9.383 | 6.915 | 16 | True | `MID.down.q50 -s-> MID.trough` | — | tennessee_eastman |
| VYT03:downq50 | m | VYT02:downq50 | 9.379 | 10.395 | 18 | True | `SLOW.down.q50 -m-> SLOW.down.q50` | — | tennessee_eastman |
| CO_rpm:trough | m | HILout:upq20 | 9.312 | 9.652 | 28 | True | `MID.trough -m-> SLOW.up.q20` | — | building_59 |
| SIT01:trough | s | VYT02:upq50 | 9.301 | 8.739 | 8 | True | `MID.trough -s-> SLOW.up.q50` | — | — |
| VXT02:upq80 | s | VYT02:upq20 | 9.287 | 4.152 | 10 | True | `SLOW.up.q80 -s-> SLOW.up.q20` | — | tennessee_eastman |
| HILout:downq50 | m | HILout:upq50 | 9.282 | 9.722 | 36 | False | `SLOW.down.q50 -m-> SLOW.up.q50 [same role]` | building_59 | tennessee_eastman |
| FT01Z:peak | s | FCV03D:trough | 9.266 | 6.631 | 14 | False | `MID.peak -s-> MID.trough` | — | tennessee_eastman |
| LIT01:downq80 | s | LIT01:downq50 | 9.26 | 8.432 | 143 | True | `MID.down.q80 -s-> MID.down.q50 [same role]` | tennessee_eastman | — |
| VYT02:downq50 | l | VXT02:upq80 | 9.237 | 7.062 | 27 | True | `SLOW.down.q50 -l-> SLOW.up.q80` | — | tennessee_eastman |
| LCP01D:upq80 | m | LCP01D:downq80 | 9.231 | 8.654 | 74 | True | `MID-S.up.q80 -m-> MID-S.down.q80 [same role]` | tennessee_eastman, nasa_battery, fingrid | building_59 |
| VYT02:downq50 | s | VYT03:downq50 | 9.226 | 9.906 | 5 | False | `SLOW.down.q50 -s-> SLOW.down.q50` | — | tennessee_eastman |
| HILout:upq20 | m | HILout:upq50 | 9.213 | 2.818 | 21 | True | `SLOW.up.q20 -m-> SLOW.up.q50 [same role]` | — | tennessee_eastman, building_59 |
| HILout:upq50 | m | SIT01:peak | 9.188 | 5.149 | 45 | True | `SLOW.up.q50 -m-> MID.peak` | — | — |
| PCV01D:trough | s | FT03Z:peak | 9.14 | 7.117 | 9 | False | `MID-S.trough -s-> MID.peak` | — | — |
| VYT03:downq50 | l | VYT02:downq50 | 9.125 | 10.534 | 20 | True | `SLOW.down.q50 -l-> SLOW.down.q50` | — | tennessee_eastman |
| VYT02:downq50 | s | VYT03:upq50 | 9.105 | 12.22 | 5 | True | `SLOW.down.q50 -s-> SLOW.up.q50` | — | tennessee_eastman |
| PIT02:downq90 | m | B400B:upq50 | 9.1 | 10.912 | 38 | True | `MID.down.q90 -m-> MID-S.up.q50` | — | tennessee_eastman |
| PIT02:downq90 | m | FT02:upq50 | 9.1 | 10.912 | 38 | True | `MID.down.q90 -m-> MID-S.up.q50` | — | tennessee_eastman |
| PIT02:downq90 | m | FT02Z:upq50 | 9.1 | 10.912 | 38 | True | `MID.down.q90 -m-> MID-S.up.q50` | — | tennessee_eastman |
| FT03Z:trough | s | FT01:upq50 | 9.094 | 13.921 | 5 | False | `MID.trough -s-> MID.up.q50` | — | tennessee_eastman |
| VYT02:upq50 | l | VYT03:upq50 | 9.045 | 6.272 | 28 | True | `SLOW.up.q50 -l-> SLOW.up.q50` | — | tennessee_eastman |
| CO_rpm:trough | s | VXT03:downq50 | 9.037 | 9.344 | 6 | False | `MID.trough -s-> SLOW.down.q50` | — | building_59 |
| SIT01:peak | m | HILout:downq50 | 8.991 | 5.771 | 40 | True | `MID.peak -m-> SLOW.down.q50` | — | — |
| ST_TT01:downq10 | m | TIT02:upq20 | 8.93 | 7.664 | 52 | True | `MID.down.q10 -m-> MID.up.q20` | — | tennessee_eastman, building_59 |
| B2004:downq50 | l | B2004:upq20 | 8.912 | 7.841 | 5 | False | `SET.down.q50 -l-> SET.up.q20 [same role]` | — | — |
| SIT02:peak | m | HILout:downq50 | 8.908 | 5.807 | 39 | True | `MID.peak -m-> SLOW.down.q50` | — | — |
| SIT02:trough | m | HILout:upq20 | 8.904 | 17.427 | 25 | True | `MID.trough -m-> SLOW.up.q20` | — | — |
| VYT03:upq50 | s | VXT02:downq80 | 8.9 | 7.167 | 6 | True | `SLOW.up.q50 -s-> SLOW.down.q80` | — | tennessee_eastman |
| TIT02:upq80 | m | FCV02Z:upq50 | 8.878 | 10.54 | 38 | True | `MID.up.q80 -m-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| LCV01Z:downq50 | s | FT01:downq20 | 8.851 | 13.283 | 11 | True | `MID.down.q50 -s-> MID.down.q20` | — | tennessee_eastman, building_59 |
| TIT02:upq20 | m | FCV02Z:upq50 | 8.848 | 11.523 | 34 | True | `MID.up.q20 -m-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| FCV01D:downq10 | m | FCV01Z:trough | 8.845 | 5.503 | 15 | False | `MID-S.down.q10 -m-> MID-S.trough` | — | tennessee_eastman |
| PIT02:downq90 | s | FT02:downq20 | 8.843 | 12.01 | 8 | False | `MID.down.q90 -s-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| PIT02:downq90 | s | FT02Z:downq20 | 8.843 | 12.01 | 8 | False | `MID.down.q90 -s-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| FT01Z:trough | s | FT03:trough | 8.834 | 8.304 | 9 | True | `MID.trough -s-> MID.trough` | — | — |
| SIT02:peak | m | VXT03:upq80 | 8.81 | 7.658 | 27 | False | `MID.peak -m-> SLOW.up.q80` | — | — |
| TIT02:upq50 | m | FCV02Z:upq50 | 8.806 | 10.67 | 35 | True | `MID.up.q50 -m-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| LCP01D:upq50 | s | LCP01D:downq50 | 8.709 | 8.956 | 28 | True | `MID-S.up.q50 -s-> MID-S.down.q50 [same role]` | — | tennessee_eastman, building_59, fingrid |
| CO_rpm:trough | m | HILout:upq50 | 8.708 | 7.02 | 48 | False | `MID.trough -m-> SLOW.up.q50` | — | building_59 |
| FT02Z:upq20 | s | TIT02:downq80 | 8.692 | 16.225 | 5 | False | `MID-S.up.q20 -s-> MID.down.q80` | — | tennessee_eastman, building_59 |
| B400B:upq20 | s | TIT02:downq80 | 8.692 | 15.576 | 5 | False | `MID-S.up.q20 -s-> MID.down.q80` | — | tennessee_eastman |
| FCV02Z:upq50 | m | B4005:downq20 | 8.686 | 9.762 | 21 | True | `MID-S.up.q50 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| VXT03:downq50 | m | VXT02:downq50 | 8.685 | 8.845 | 10 | False | `SLOW.down.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| FT01Z:peak | s | FCV03Z:trough | 8.68 | 10.542 | 11 | True | `MID.peak -s-> MID.trough` | — | — |
| SIT01:peak | m | VXT03:upq80 | 8.67 | 7.61 | 27 | False | `MID.peak -m-> SLOW.up.q80` | — | — |
| SIT01:trough | m | HILout:upq20 | 8.656 | 17.881 | 25 | True | `MID.trough -m-> SLOW.up.q20` | — | — |
| FT01:downq50 | s | LCV01Z:downq50 | 8.631 | 8.428 | 14 | True | `MID.down.q50 -s-> MID.down.q50` | — | tennessee_eastman, building_59 |
| VXT03:downq80 | l | VXT02:upq80 | 8.618 | 7.511 | 27 | True | `SLOW.down.q80 -l-> SLOW.up.q80` | — | tennessee_eastman, building_59 |
| FCV01Z:peak | m | B400B:downq20 | 8.57 | 7.634 | 23 | True | `MID-S.peak -m-> MID-S.down.q20` | — | tennessee_eastman |
| FCV01Z:peak | m | FT02:downq20 | 8.57 | 7.634 | 23 | True | `MID-S.peak -m-> MID-S.down.q20` | — | tennessee_eastman |
| FCV01Z:peak | m | FT02Z:downq20 | 8.57 | 7.634 | 23 | True | `MID-S.peak -m-> MID-S.down.q20` | — | tennessee_eastman |
| FT01:upq50 | s | FT01Z:peak | 8.54 | 13.156 | 8 | False | `MID.up.q50 -s-> MID.peak` | — | tennessee_eastman |
| B4005:upq20 | s | TIT02:downq80 | 8.51 | 9.735 | 10 | True | `MID-S.up.q20 -s-> MID.down.q80` | — | tennessee_eastman, building_59 |
| FCV01Z:peak | m | FCV02Z:upq50 | 8.502 | 5.025 | 26 | True | `MID-S.peak -m-> MID-S.up.q50` | — | tennessee_eastman |
| LCV01Z:downq50 | s | LCV01Z:upq50 | 8.486 | 5.388 | 26 | False | `MID.down.q50 -s-> MID.up.q50 [same role]` | building_59 | tennessee_eastman |
| LCV01D:upq80 | s | FT01:upq80 | 8.449 | 5.171 | 13 | True | `MID.up.q80 -s-> MID.up.q80` | — | tennessee_eastman, building_59 |
| PIT02:downq10 | m | FCV02Z:downq80 | 8.442 | 7.485 | 23 | True | `MID.down.q10 -m-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| FT01:upq50 | m | FT01:downq50 | 8.434 | 14.102 | 12 | False | `MID.up.q50 -m-> MID.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| HILout:upq50 | m | SIT02:peak | 8.428 | 5.184 | 41 | True | `SLOW.up.q50 -m-> MID.peak` | — | — |
| ST_TT01:downq10 | m | TIT02:upq50 | 8.415 | 5.748 | 49 | True | `MID.down.q10 -m-> MID.up.q50` | — | tennessee_eastman, building_59 |
| CO_rpm:peak | m | HILout:downq20 | 8.385 | 10.208 | 23 | True | `MID.peak -m-> SLOW.down.q20` | — | building_59 |
| VYT03:upq50 | l | VYT02:downq50 | 8.35 | 7.933 | 20 | True | `SLOW.up.q50 -l-> SLOW.down.q50` | — | tennessee_eastman |
| TIT02:downq20 | s | LCV01Z:downq80 | 8.35 | 13.236 | 5 | False | `MID.down.q20 -s-> MID.down.q80` | — | tennessee_eastman, building_59 |
| VXT02:downq50 | m | VXT03:downq50 | 8.345 | 14.583 | 9 | False | `SLOW.down.q50 -m-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| FT02Z:downq80 | s | TIT02:upq50 | 8.331 | 13.952 | 11 | False | `MID-S.down.q80 -s-> MID.up.q50` | — | tennessee_eastman, building_59 |
| LCV01Z:upq20 | m | FT01:downq20 | 8.326 | 5.249 | 28 | True | `MID.up.q20 -m-> MID.down.q20` | — | tennessee_eastman, building_59 |
| PCV01Z:trough | s | FT03:peak | 8.324 | 8.787 | 8 | False | `MID-S.trough -s-> MID.peak` | — | — |
| SIT02:trough | m | VXT03:downq50 | 8.305 | 6.416 | 19 | False | `MID.trough -m-> SLOW.down.q50` | — | — |
| PIT02:downq90 | m | FCV02Z:upq80 | 8.3 | 8.694 | 29 | False | `MID.down.q90 -m-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| VYT03:downq50 | l | HILout:upq20 | 8.28 | 10.404 | 14 | True | `SLOW.down.q50 -l-> SLOW.up.q20` | — | tennessee_eastman |
| TIT02:upq80 | m | B400B:downq20 | 8.254 | 10.409 | 31 | True | `MID.up.q80 -m-> MID-S.down.q20` | — | tennessee_eastman |
| TIT02:upq80 | m | FT02:downq20 | 8.254 | 10.409 | 31 | True | `MID.up.q80 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| TIT02:upq80 | m | FT02Z:downq20 | 8.254 | 10.409 | 31 | True | `MID.up.q80 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B400B:upq50 | m | FCV01Z:peak | 8.24 | 14.568 | 18 | True | `MID-S.up.q50 -m-> MID-S.peak` | — | tennessee_eastman |
| FT02Z:upq50 | m | FCV01Z:peak | 8.24 | 14.568 | 18 | True | `MID-S.up.q50 -m-> MID-S.peak` | — | tennessee_eastman |
| FT02:upq50 | m | FCV01Z:peak | 8.24 | 14.568 | 18 | True | `MID-S.up.q50 -m-> MID-S.peak` | — | tennessee_eastman |
| PIT02:upq90 | m | B400B:downq20 | 8.234 | 8.896 | 30 | True | `MID.up.q90 -m-> MID-S.down.q20` | — | tennessee_eastman |
| PIT02:upq90 | m | FT02:downq20 | 8.234 | 8.896 | 30 | True | `MID.up.q90 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| PIT02:upq90 | m | FT02Z:downq20 | 8.234 | 8.896 | 30 | True | `MID.up.q90 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| VYT03:downq20 | m | VXT02:downq50 | 8.223 | 7.726 | 12 | True | `SLOW.down.q20 -m-> SLOW.down.q50` | — | tennessee_eastman |
| LCV01D:downq50 | s | FT01:downq50 | 8.215 | 4.611 | 17 | True | `MID.down.q50 -s-> MID.down.q50` | — | tennessee_eastman, building_59 |
| HILout:upq50 | m | HILout:downq50 | 8.214 | 11.508 | 27 | False | `SLOW.up.q50 -m-> SLOW.down.q50 [same role]` | building_59 | tennessee_eastman |
| FCV01Z:peak | m | FCV02Z:upq80 | 8.207 | 7.006 | 21 | False | `MID-S.peak -m-> MID-S.up.q80` | — | tennessee_eastman |
| HILout:upq50 | l | HILout:downq80 | 8.206 | 7.695 | 50 | True | `SLOW.up.q50 -l-> SLOW.down.q80 [same role]` | — | tennessee_eastman, building_59 |
| FCV02Z:upq50 | m | PIT02:upq10 | 8.175 | 8.958 | 35 | True | `MID-S.up.q50 -m-> MID.up.q10` | — | tennessee_eastman, building_59 |
| PCV01Z:trough | s | FCV03Z:trough | 8.164 | 10.772 | 8 | True | `MID-S.trough -s-> MID.trough` | — | — |
| B4022:upq80 | m | B4022:downq80 | 8.153 | 14.382 | 22 | False | `SLOW.up.q80 -m-> SLOW.down.q80 [same role]` | tennessee_eastman, building_59 | — |
| TIT01:peak | m | FCV01D:downq10 | 8.134 | 12.308 | 25 | True | `MID.peak -m-> MID-S.down.q10` | — | tennessee_eastman, nasa_battery |
| TIT01:trough | m | FCV02Z:upq50 | 8.115 | 10.083 | 32 | True | `MID.trough -m-> MID-S.up.q50` | — | tennessee_eastman |
| SIT01:trough | m | VXT03:downq50 | 8.074 | 6.27 | 19 | False | `MID.trough -m-> SLOW.down.q50` | — | — |
| PIT02:upq90 | m | FCV02Z:upq80 | 8.06 | 9.33 | 28 | False | `MID.up.q90 -m-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| VXT02:upq80 | m | VYT03:upq20 | 8.025 | 4.138 | 15 | False | `SLOW.up.q80 -m-> SLOW.up.q20` | — | tennessee_eastman |
| CO_rpm:peak | m | HILout:downq50 | 8.02 | 6.015 | 40 | True | `MID.peak -m-> SLOW.down.q50` | building_59 | — |
| CO_rpm:peak | m | VXT03:upq80 | 8.02 | 7.448 | 28 | False | `MID.peak -m-> SLOW.up.q80` | — | building_59 |
| FT02:downq50 | m | PIT02:downq10 | 7.976 | 10.22 | 39 | True | `MID-S.down.q50 -m-> MID.down.q10` | — | tennessee_eastman |
| FT02Z:downq50 | m | PIT02:downq10 | 7.976 | 10.259 | 39 | True | `MID-S.down.q50 -m-> MID.down.q10` | — | tennessee_eastman |
| B400B:downq50 | m | PIT02:downq10 | 7.976 | 10.259 | 39 | True | `MID-S.down.q50 -m-> MID.down.q10` | — | tennessee_eastman |
| PCV01D:trough | s | FT03:peak | 7.965 | 6.978 | 8 | False | `MID-S.trough -s-> MID.peak` | — | — |
| ST_TT01:downq10 | m | TIT01:trough | 7.954 | 8.106 | 52 | True | `MID.down.q10 -m-> MID.trough` | — | tennessee_eastman |
| B3004:upq80 | l | B2004:downq20 | 7.912 | 9.987 | 5 | False | `SET.up.q80 -l-> SET.down.q20` | — | — |
| LIT01:upq50 | s | LIT01:upq80 | 7.909 | 8.689 | 153 | True | `MID.up.q50 -s-> MID.up.q80 [same role]` | tennessee_eastman | — |
| HILout:downq80 | l | HILout:upq50 | 7.905 | 10.243 | 53 | True | `SLOW.down.q80 -l-> SLOW.up.q50 [same role]` | — | tennessee_eastman, building_59 |
| PIT02:downq90 | m | FCV02Z:downq50 | 7.902 | 4.365 | 33 | True | `MID.down.q90 -m-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| HILout:upq50 | m | CO_rpm:peak | 7.894 | 4.856 | 41 | True | `SLOW.up.q50 -m-> MID.peak` | — | building_59 |
| LCV01Z:upq80 | s | FT03Z:peak | 7.879 | 9.411 | 12 | True | `MID.up.q80 -s-> MID.peak` | — | tennessee_eastman |
| VXT03:downq50 | l | VXT02:upq50 | 7.877 | 5.976 | 24 | True | `SLOW.down.q50 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| TIT02:upq80 | m | B4005:downq20 | 7.871 | 10.042 | 33 | True | `MID.up.q80 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| VYT02:upq50 | l | VXT02:upq80 | 7.868 | 7.051 | 25 | True | `SLOW.up.q50 -l-> SLOW.up.q80` | — | tennessee_eastman |
| HILout:downq50 | l | HILout:downq80 | 7.852 | 8.899 | 49 | False | `SLOW.down.q50 -l-> SLOW.down.q80 [same role]` | — | tennessee_eastman, building_59 |
| VXT02:upq80 | s | VYT02:upq50 | 7.848 | 5.848 | 6 | True | `SLOW.up.q80 -s-> SLOW.up.q50` | — | tennessee_eastman |
| FCV01Z:trough | m | PIT02:upq10 | 7.84 | 7.888 | 33 | False | `MID-S.trough -m-> MID.up.q10` | — | tennessee_eastman |
| 24Vdc:trough | m | CO_rpm:peak | 7.837 | 7.445 | 5 | False | `SLOW.trough -m-> MID.peak` | — | — |
| PCV01D:trough | s | FCV03Z:trough | 7.812 | 9.125 | 8 | True | `MID-S.trough -s-> MID.trough` | — | fingrid |
| LCV01D:downq80 | s | FT01:downq50 | 7.736 | 3.906 | 14 | True | `MID.down.q80 -s-> MID.down.q50` | — | tennessee_eastman, building_59 |
| FCV01Z:peak | m | B4005:downq20 | 7.678 | 6.839 | 23 | True | `MID-S.peak -m-> MID-S.down.q20` | — | tennessee_eastman |
| FT03Z:peak | s | LCV01Z:downq80 | 7.604 | 12.948 | 10 | True | `MID.peak -s-> MID.down.q80` | — | tennessee_eastman |
| PIT02:downq10 | s | B4005:upq20 | 7.594 | 8.714 | 11 | False | `MID.down.q10 -s-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| TIT02:downq80 | m | FCV01D:downq10 | 7.565 | 3.489 | 14 | True | `MID.down.q80 -m-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| VYT02:upq50 | l | VXT02:downq80 | 7.554 | 7.521 | 24 | True | `SLOW.up.q50 -l-> SLOW.down.q80` | — | tennessee_eastman |
| LCP01D:upq50 | s | LCP01D:upq80 | 7.546 | 3.812 | 18 | True | `MID-S.up.q50 -s-> MID-S.up.q80 [same role]` | tennessee_eastman, fingrid | building_59 |
| LIT01:upq20 | s | LIT01:upq50 | 7.545 | 8.694 | 132 | True | `MID.up.q20 -s-> MID.up.q50 [same role]` | tennessee_eastman | — |
| FCV02Z:downq80 | s | B2016:peak | 7.541 | 2.975 | 10 | True | `MID-S.down.q80 -s-> MID.peak` | — | tennessee_eastman |
| B4005:upq50 | m | TIT02:downq20 | 7.531 | 7.581 | 17 | False | `MID-S.up.q50 -m-> MID.down.q20` | — | tennessee_eastman, building_59 |
| VXT02:downq50 | l | VXT02:upq80 | 7.529 | 10.341 | 28 | True | `SLOW.down.q50 -l-> SLOW.up.q80 [same role]` | building_59 | tennessee_eastman |
| HT_PS:downq20 | l | B2004:downq20 | 7.461 | 9.577 | 4 | False | `SET.down.q20 -l-> SET.down.q20` | — | building_59 |
| ST_PS:downq20 | l | B2004:downq20 | 7.461 | 9.577 | 4 | False | `SET.down.q20 -l-> SET.down.q20` | — | — |
| B3004:upq20 | s | LCV01Z:downq20 | 7.446 | 9.411 | 6 | True | `SET.up.q20 -s-> MID.down.q20` | — | tennessee_eastman |
| VXT02:downq80 | l | HILout:downq20 | 7.439 | 6.382 | 20 | True | `SLOW.down.q80 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| LCV01D:upq20 | s | FT01:upq20 | 7.433 | 3.585 | 14 | True | `MID.up.q20 -s-> MID.up.q20` | — | tennessee_eastman, building_59 |
| VYT03:upq50 | m | VYT02:downq50 | 7.429 | 12.772 | 14 | True | `SLOW.up.q50 -m-> SLOW.down.q50` | — | tennessee_eastman |
| VYT02:downq50 | m | HILout:upq20 | 7.422 | 14.194 | 9 | False | `SLOW.down.q50 -m-> SLOW.up.q20` | — | tennessee_eastman |
| LCV01Z:downq20 | l | B3005:upq10 | 7.414 | 22.251 | 3 | False | `MID.down.q20 -l-> SET.up.q10` | — | tennessee_eastman, building_59 |
| FT01:upq80 | m | LCV01Z:downq80 | 7.411 | 10.152 | 18 | False | `MID.up.q80 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| VYT03:downq20 | m | VXT03:downq80 | 7.4 | 12.169 | 12 | False | `SLOW.down.q20 -m-> SLOW.down.q80` | — | tennessee_eastman |
| B2004:downq80 | s | LCV01Z:upq50 | 7.398 | 13.317 | 3 | False | `SET.down.q80 -s-> MID.up.q50` | — | — |
| FT01Z:peak | s | FT03Z:peak | 7.386 | 8.223 | 9 | False | `MID.peak -s-> MID.peak` | — | tennessee_eastman |
| LCV01Z:upq80 | m | FT01:downq80 | 7.383 | 3.698 | 15 | False | `MID.up.q80 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| PIT02:upq90 | m | B4005:downq20 | 7.377 | 7.97 | 30 | True | `MID.up.q90 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B2004:upq50 | s | LCV01Z:downq80 | 7.368 | 11.912 | 4 | False | `SET.up.q50 -s-> MID.down.q80` | — | — |
| FT02:downq50 | m | PIT02:upq10 | 7.363 | 8.304 | 36 | True | `MID-S.down.q50 -m-> MID.up.q10` | — | tennessee_eastman |
| FT02Z:downq50 | m | PIT02:upq10 | 7.363 | 8.336 | 36 | True | `MID-S.down.q50 -m-> MID.up.q10` | — | tennessee_eastman |
| B400B:downq50 | m | PIT02:upq10 | 7.363 | 8.336 | 36 | True | `MID-S.down.q50 -m-> MID.up.q10` | — | tennessee_eastman |
| LCV01D:upq50 | s | FT01:upq50 | 7.353 | 11.707 | 18 | True | `MID.up.q50 -s-> MID.up.q50` | — | tennessee_eastman, building_59 |
| FCV02Z:downq50 | m | TIT02:downq20 | 7.35 | 9.84 | 13 | True | `MID-S.down.q50 -m-> MID.down.q20` | — | tennessee_eastman, building_59 |
| LCP01D:upq20 | m | LCP01D:downq20 | 7.348 | 6.321 | 44 | True | `MID-S.up.q20 -m-> MID-S.down.q20 [same role]` | — | tennessee_eastman, nasa_battery, building_59, fingrid |
| FCV02Z:downq80 | m | PIT02:upq90 | 7.34 | 4.204 | 16 | False | `MID-S.down.q80 -m-> MID.up.q90` | — | tennessee_eastman, building_59 |
| FT01:downq20 | m | LCV01Z:upq20 | 7.325 | 4.554 | 24 | True | `MID.down.q20 -m-> MID.up.q20` | — | tennessee_eastman, building_59 |
| B400B:upq50 | m | TIT02:downq20 | 7.324 | 8.741 | 16 | False | `MID-S.up.q50 -m-> MID.down.q20` | — | tennessee_eastman |
| FT02Z:upq50 | m | TIT02:downq20 | 7.324 | 8.741 | 16 | False | `MID-S.up.q50 -m-> MID.down.q20` | — | tennessee_eastman |
| FT02:upq50 | m | TIT02:downq20 | 7.324 | 8.741 | 16 | False | `MID-S.up.q50 -m-> MID.down.q20` | — | tennessee_eastman |
| TIT01:peak | m | TIT02:downq80 | 7.304 | 6.856 | 31 | True | `MID.peak -m-> MID.down.q80` | — | tennessee_eastman |
| B400B:downq80 | s | TIT02:upq20 | 7.284 | 14.741 | 9 | False | `MID-S.down.q80 -s-> MID.up.q20` | — | tennessee_eastman |
| FT03:peak | s | LCV01Z:downq80 | 7.277 | 12.948 | 9 | True | `MID.peak -s-> MID.down.q80` | — | — |
| LCV01D:downq50 | s | B3004:downq80 | 7.249 | 10.374 | 5 | True | `MID.down.q50 -s-> SET.down.q80` | — | tennessee_eastman |
| FT01Z:peak | s | FT03:peak | 7.241 | 8.062 | 9 | False | `MID.peak -s-> MID.peak` | — | — |
| CO_rpm:peak | l | CO_rpm:peak | 7.198 | 5.011 | 148 | True | `MID.peak -l-> MID.peak [same role]` | — | building_59, fingrid |
| VXT02:downq80 | l | HILout:upq20 | 7.198 | 8.358 | 19 | False | `SLOW.down.q80 -l-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| CO_rpm:trough | m | VXT03:upq50 | 7.184 | 10.617 | 18 | False | `MID.trough -m-> SLOW.up.q50` | — | building_59 |
| LCP01D:downq50 | s | LCP01D:upq50 | 7.171 | 10.119 | 24 | True | `MID-S.down.q50 -s-> MID-S.up.q50 [same role]` | — | tennessee_eastman, building_59, fingrid |
| VXT02:upq80 | l | HILout:downq20 | 7.169 | 9.014 | 20 | True | `SLOW.up.q80 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| FCV03D:trough | s | FT01Z:trough | 7.169 | 11.0 | 8 | False | `MID.trough -s-> MID.trough` | — | tennessee_eastman |
| VYT02:upq50 | l | HILout:downq20 | 7.142 | 6.666 | 16 | True | `SLOW.up.q50 -l-> SLOW.down.q20` | — | tennessee_eastman |
| LCV01D:downq20 | s | LCV01D:upq20 | 7.112 | 6.22 | 69 | True | `MID.down.q20 -s-> MID.up.q20 [same role]` | tennessee_eastman | building_59 |
| HILout:downq50 | m | CO_rpm:trough | 7.109 | 7.107 | 44 | True | `SLOW.down.q50 -m-> MID.trough` | — | building_59 |
| TIT02:upq80 | m | FCV02Z:upq20 | 7.106 | 8.311 | 18 | True | `MID.up.q80 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B4005:upq50 | m | FCV01Z:peak | 7.088 | 10.108 | 16 | True | `MID-S.up.q50 -m-> MID-S.peak` | — | tennessee_eastman |
| VXT02:upq50 | m | HILout:upq20 | 7.086 | 5.996 | 9 | False | `SLOW.up.q50 -m-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| B4005:downq50 | m | PIT02:downq90 | 7.083 | 6.387 | 38 | True | `MID-S.down.q50 -m-> MID.down.q90` | — | tennessee_eastman, building_59 |
| LCV01Z:upq80 | s | FT03:peak | 7.081 | 9.226 | 11 | True | `MID.up.q80 -s-> MID.peak` | — | — |
| HILout:upq80 | m | SIT01:peak | 7.061 | 8.692 | 24 | True | `SLOW.up.q80 -m-> MID.peak` | — | — |
| VXT03:downq50 | l | HILout:upq50 | 7.002 | 3.512 | 33 | True | `SLOW.down.q50 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| B3004:upq50 | m | FT01Z:trough | 6.996 | 7.25 | 5 | True | `SET.up.q50 -m-> MID.trough` | — | tennessee_eastman |
| B3004:upq50 | s | LCV01Z:downq50 | 6.957 | 7.264 | 7 | True | `SET.up.q50 -s-> MID.down.q50` | — | tennessee_eastman |
| TIT02:downq80 | m | PIT02:upq10 | 6.942 | 4.597 | 26 | True | `MID.down.q80 -m-> MID.up.q10` | — | tennessee_eastman, building_59 |
| VXT02:upq80 | l | HILout:upq20 | 6.937 | 8.214 | 19 | True | `SLOW.up.q80 -l-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| HILout:upq80 | m | CO_rpm:peak | 6.936 | 9.836 | 25 | True | `SLOW.up.q80 -m-> MID.peak` | — | building_59 |
| LCV01Z:downq80 | s | LCV01Z:upq80 | 6.934 | 13.745 | 13 | True | `MID.down.q80 -s-> MID.up.q80 [same role]` | building_59 | tennessee_eastman |
| TIT02:upq80 | m | TIT02:downq80 | 6.909 | 6.53 | 35 | True | `MID.up.q80 -m-> MID.down.q80 [same role]` | building_59 | tennessee_eastman |
| VYT03:upq50 | l | HILout:downq20 | 6.908 | 9.033 | 13 | True | `SLOW.up.q50 -l-> SLOW.down.q20` | — | tennessee_eastman |
| SIT02:peak | l | VT01:upq80 | 6.899 | 26.238 | 4 | True | `MID.peak -l-> MID-S.up.q80` | — | — |
| B4005:downq50 | m | PIT02:downq10 | 6.896 | 9.291 | 37 | True | `MID-S.down.q50 -m-> MID.down.q10` | — | tennessee_eastman, building_59 |
| LCV01Z:upq50 | s | FT01:upq80 | 6.891 | 7.672 | 7 | False | `MID.up.q50 -s-> MID.up.q80` | — | tennessee_eastman, building_59 |
| SIT01:trough | m | HILout:upq80 | 6.888 | 3.025 | 28 | True | `MID.trough -m-> SLOW.up.q80` | — | — |
| HILout:downq50 | m | SIT01:trough | 6.853 | 7.536 | 40 | True | `SLOW.down.q50 -m-> MID.trough` | — | — |
| LCV01Z:upq50 | s | FCV03Z:trough | 6.815 | 4.426 | 12 | False | `MID.up.q50 -s-> MID.trough` | — | building_59 |
| FT01:upq20 | m | LCV01Z:downq20 | 6.806 | 4.609 | 27 | True | `MID.up.q20 -m-> MID.down.q20` | — | tennessee_eastman, building_59 |
| B4022:upq20 | s | FCV01D:upq10 | 6.806 | 6.665 | 13 | False | `SLOW.up.q20 -s-> MID-S.up.q10` | building_59 | tennessee_eastman |
| TIT02:upq50 | m | FCV02Z:upq20 | 6.802 | 6.009 | 16 | True | `MID.up.q50 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| VYT02:downq50 | l | HILout:downq20 | 6.792 | 7.512 | 14 | True | `SLOW.down.q50 -l-> SLOW.down.q20` | — | tennessee_eastman |
| B3005:downq10 | s | LCV01D:downq20 | 6.771 | 10.495 | 4 | False | `SET.down.q10 -s-> MID.down.q20` | — | tennessee_eastman, building_59 |
| ST_TT01:upq10 | m | B4005:downq50 | 6.747 | 6.752 | 45 | True | `MID.up.q10 -m-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| VXT03:upq50 | l | HILout:upq50 | 6.721 | 2.606 | 28 | False | `SLOW.up.q50 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| FCV01D:upq10 | s | FCV02Z:downq80 | 6.718 | 22.736 | 4 | False | `MID-S.up.q10 -s-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| PCV01Z:trough | s | LCV01Z:downq80 | 6.717 | 7.091 | 10 | False | `MID-S.trough -s-> MID.down.q80` | — | — |
| B3004:downq80 | l | B2004:upq20 | 6.71 | 13.162 | 4 | False | `SET.down.q80 -l-> SET.up.q20` | — | — |
| PIT02:downq90 | m | FCV01D:downq10 | 6.705 | 6.79 | 24 | True | `MID.down.q90 -m-> MID-S.down.q10` | building_59 | tennessee_eastman |
| FT01:downq50 | s | FT01:upq50 | 6.703 | 16.036 | 4 | False | `MID.down.q50 -s-> MID.up.q50 [same role]` | — | tennessee_eastman, building_59 |
| HILout:downq20 | m | SIT01:trough | 6.702 | 4.271 | 22 | True | `SLOW.down.q20 -m-> MID.trough` | — | — |
| LIT01:upq20 | s | FT01:downq20 | 6.7 | 3.802 | 12 | True | `MID.up.q20 -s-> MID.down.q20` | — | tennessee_eastman |
| B3004:upq80 | l | B3004:downq80 | 6.694 | 8.45 | 5 | False | `SET.up.q80 -l-> SET.down.q80 [same role]` | — | tennessee_eastman |
| LCV01D:downq20 | s | LCV01Z:upq20 | 6.683 | 4.201 | 30 | True | `MID.down.q20 -s-> MID.up.q20` | — | tennessee_eastman, building_59 |
| TIT02:upq50 | m | B4005:downq20 | 6.678 | 10.166 | 26 | True | `MID.up.q50 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| ST_TT01:upq10 | m | TIT01:peak | 6.677 | 7.583 | 57 | True | `MID.up.q10 -m-> MID.peak` | — | tennessee_eastman |
| B3004:upq50 | s | LCV01Z:downq80 | 6.667 | 9.746 | 5 | False | `SET.up.q50 -s-> MID.down.q80` | tennessee_eastman | — |
| B4005:downq50 | s | PIT02:upq90 | 6.662 | 8.409 | 14 | True | `MID-S.down.q50 -s-> MID.up.q90` | — | tennessee_eastman, building_59 |
| TIT02:downq50 | m | PIT02:upq90 | 6.633 | 5.751 | 26 | True | `MID.down.q50 -m-> MID.up.q90` | — | tennessee_eastman, building_59 |
| VXT03:upq80 | m | CO_rpm:peak | 6.627 | 3.264 | 27 | True | `SLOW.up.q80 -m-> MID.peak` | — | building_59 |
| FT01:upq20 | s | LCV01Z:upq50 | 6.625 | 9.744 | 10 | True | `MID.up.q20 -s-> MID.up.q50` | — | tennessee_eastman, building_59 |
| PIT02:upq90 | m | B4005:upq50 | 6.609 | 6.121 | 28 | True | `MID.up.q90 -m-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| TIT02:upq20 | m | FCV02Z:upq20 | 6.596 | 6.49 | 15 | True | `MID.up.q20 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| LCP01D:upq20 | m | LCP01D:upq50 | 6.595 | 6.218 | 65 | True | `MID-S.up.q20 -m-> MID-S.up.q50 [same role]` | tennessee_eastman | building_59, fingrid |
| ST_TT01:downq10 | m | TIT02:upq80 | 6.582 | 3.766 | 39 | True | `MID.down.q10 -m-> MID.up.q80` | — | tennessee_eastman, building_59 |
| ST_TT01:upq10 | m | B400B:downq50 | 6.579 | 6.459 | 43 | True | `MID.up.q10 -m-> MID-S.down.q50` | — | tennessee_eastman |
| ST_TT01:upq10 | m | FT02:downq50 | 6.579 | 6.459 | 43 | True | `MID.up.q10 -m-> MID-S.down.q50` | — | tennessee_eastman |
| ST_TT01:upq10 | m | FT02Z:downq50 | 6.579 | 6.459 | 43 | True | `MID.up.q10 -m-> MID-S.down.q50` | — | tennessee_eastman |
| HILout:downq20 | l | VXT03:downq50 | 6.527 | 10.598 | 20 | False | `SLOW.down.q20 -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| FT01Z:peak | m | FT01:downq80 | 6.519 | 3.836 | 11 | False | `MID.peak -m-> MID.down.q80` | — | tennessee_eastman |
| VXT02:downq20 | l | CO_rpm:peak | 6.474 | 3.927 | 40 | True | `SLOW.down.q20 -l-> MID.peak` | — | building_59 |
| LCV01Z:downq20 | m | LCV01Z:upq20 | 6.446 | 6.941 | 62 | True | `MID.down.q20 -m-> MID.up.q20 [same role]` | tennessee_eastman, building_59 | — |
| LCV01Z:downq20 | m | FT01:upq20 | 6.446 | 6.148 | 21 | True | `MID.down.q20 -m-> MID.up.q20` | — | tennessee_eastman, building_59 |
| TIT01:trough | m | FCV02Z:upq20 | 6.427 | 4.868 | 15 | True | `MID.trough -m-> MID-S.up.q20` | — | tennessee_eastman |
| PCV01D:trough | s | LCV01Z:downq80 | 6.427 | 7.508 | 10 | False | `MID-S.trough -s-> MID.down.q80` | — | — |
| SIT01:trough | l | HILout:downq20 | 6.42 | 9.656 | 43 | False | `MID.trough -l-> SLOW.down.q20` | — | — |
| CO_rpm:trough | m | VXT03:upq80 | 6.414 | 7.446 | 25 | False | `MID.trough -m-> SLOW.up.q80` | — | building_59 |
| B4022:upq20 | s | B4005:upq20 | 6.413 | 7.498 | 14 | False | `SLOW.up.q20 -s-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:upq20 | m | FT01:upq20 | 6.393 | 4.397 | 21 | True | `MID.up.q20 -m-> MID.up.q20` | — | tennessee_eastman, building_59 |
| SIT01:peak | l | HILout:upq50 | 6.392 | 4.054 | 85 | True | `MID.peak -l-> SLOW.up.q50` | — | — |
| FT01:downq50 | m | FT01:upq50 | 6.392 | 9.525 | 8 | False | `MID.down.q50 -m-> MID.up.q50 [same role]` | — | tennessee_eastman, building_59 |
| PIT02:upq90 | m | PIT02:downq90 | 6.387 | 6.301 | 46 | True | `MID.up.q90 -m-> MID.down.q90 [same role]` | building_59 | tennessee_eastman |
| B400B:upq80 | m | FT02:downq80 | 6.361 | 5.738 | 27 | True | `MID-S.up.q80 -m-> MID-S.down.q80` | — | tennessee_eastman |
| SIT02:peak | l | SIT01:peak | 6.344 | 4.931 | 137 | True | `MID.peak -l-> MID.peak` | — | — |
| TIT01:peak | s | B4005:downq20 | 6.338 | 14.89 | 5 | False | `MID.peak -s-> MID-S.down.q20` | — | tennessee_eastman |
| B4005:downq50 | m | PIT02:upq10 | 6.337 | 7.549 | 34 | True | `MID-S.down.q50 -m-> MID.up.q10` | — | tennessee_eastman, building_59 |
| VYT02:downq50 | m | SIT02:peak | 6.318 | 2.589 | 21 | True | `SLOW.down.q50 -m-> MID.peak` | — | — |
| ST_PS:downq20 | l | B3004:downq80 | 6.313 | 8.103 | 4 | False | `SET.down.q20 -l-> SET.down.q80` | — | — |
| TIT02:upq50 | m | B400B:downq20 | 6.308 | 11.348 | 22 | True | `MID.up.q50 -m-> MID-S.down.q20` | — | tennessee_eastman |
| TIT02:upq50 | m | FT02:downq20 | 6.308 | 11.348 | 22 | True | `MID.up.q50 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| TIT02:upq50 | m | FT02Z:downq20 | 6.308 | 11.348 | 22 | True | `MID.up.q50 -m-> MID-S.down.q20` | building_59 | tennessee_eastman |
| FCV01D:downq10 | m | B4005:upq20 | 6.302 | 5.228 | 9 | False | `MID-S.down.q10 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| PIT02:downq10 | m | B400B:upq20 | 6.3 | 8.921 | 18 | True | `MID.down.q10 -m-> MID-S.up.q20` | — | tennessee_eastman |
| PIT02:downq10 | m | FT02:upq20 | 6.3 | 7.731 | 18 | True | `MID.down.q10 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| PIT02:downq10 | m | FT02Z:upq20 | 6.3 | 8.326 | 18 | True | `MID.down.q10 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| SIT01:trough | l | HILout:downq80 | 6.292 | 4.356 | 59 | True | `MID.trough -l-> SLOW.down.q80` | — | — |
| LCV01D:downq50 | s | B3004:downq50 | 6.282 | 7.493 | 6 | False | `MID.down.q50 -s-> SET.down.q50` | — | tennessee_eastman |
| VYT02:downq50 | m | SIT01:peak | 6.276 | 2.572 | 21 | True | `SLOW.down.q50 -m-> MID.peak` | — | — |
| SIT02:peak | l | VYT02:downq80 | 6.272 | 53.668 | 10 | False | `MID.peak -l-> SLOW.down.q80` | — | — |
| CO_rpm:peak | l | HILout:upq20 | 6.261 | 9.101 | 44 | True | `MID.peak -l-> SLOW.up.q20` | — | building_59 |
| VYT02:upq20 | l | VXT02:upq80 | 6.258 | 7.167 | 25 | True | `SLOW.up.q20 -l-> SLOW.up.q80` | — | tennessee_eastman |
| VYT02:upq20 | l | VXT02:downq80 | 6.258 | 7.167 | 25 | True | `SLOW.up.q20 -l-> SLOW.down.q80` | — | tennessee_eastman |
| FT01:upq50 | m | LCV01Z:downq80 | 6.245 | 4.641 | 18 | True | `MID.up.q50 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| CO_rpm:trough | m | VXT02:upq80 | 6.217 | 9.466 | 27 | True | `MID.trough -m-> SLOW.up.q80` | — | building_59 |
| HILout:upq20 | l | VXT02:upq80 | 6.209 | 6.17 | 34 | True | `SLOW.up.q20 -l-> SLOW.up.q80` | — | tennessee_eastman, building_59 |
| PIT02:upq90 | m | FCV01D:downq10 | 6.182 | 7.287 | 22 | True | `MID.up.q90 -m-> MID-S.down.q10` | building_59 | tennessee_eastman |
| LCV01D:upq80 | s | LCV01Z:downq80 | 6.17 | 9.818 | 25 | True | `MID.up.q80 -s-> MID.down.q80` | — | tennessee_eastman, building_59 |
| LCV01Z:downq20 | s | LCV01D:upq20 | 6.154 | 3.667 | 34 | True | `MID.down.q20 -s-> MID.up.q20` | — | tennessee_eastman, building_59 |
| LCP01D:downq80 | s | LCP01D:downq50 | 6.144 | 9.159 | 17 | True | `MID-S.down.q80 -s-> MID-S.down.q50 [same role]` | tennessee_eastman, fingrid | building_59 |
| CO_rpm:peak | l | HILout:upq50 | 6.132 | 3.861 | 79 | False | `MID.peak -l-> SLOW.up.q50` | — | building_59 |
| TIT01:peak | m | FCV02Z:upq20 | 6.126 | 4.113 | 13 | True | `MID.peak -m-> MID-S.up.q20` | — | tennessee_eastman |
| TIT02:upq20 | m | B4005:downq20 | 6.11 | 10.195 | 23 | True | `MID.up.q20 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| SIT02:trough | l | HILout:downq80 | 6.094 | 4.116 | 62 | True | `MID.trough -l-> SLOW.down.q80` | — | — |
| FT02:upq80 | m | FT02:downq80 | 6.084 | 6.274 | 30 | False | `MID-S.up.q80 -m-> MID-S.down.q80 [same role]` | building_59 | tennessee_eastman |
| SIT01:trough | l | CO_rpm:peak | 6.081 | 4.777 | 117 | True | `MID.trough -l-> MID.peak` | — | — |
| HILout:downq20 | l | VXT02:downq80 | 6.075 | 5.978 | 33 | True | `SLOW.down.q20 -l-> SLOW.down.q80` | — | tennessee_eastman, building_59 |
| PIT02:upq10 | m | TIT02:downq50 | 6.07 | 4.422 | 20 | True | `MID.up.q10 -m-> MID.down.q50` | — | tennessee_eastman, building_59 |
| ST_TT01:upq90 | l | VYT02:downq50 | 6.07 | 1.638 | 9 | False | `MID.up.q90 -l-> SLOW.down.q50` | — | tennessee_eastman |
| SIT01:peak | l | HILout:upq20 | 6.066 | 8.97 | 44 | True | `MID.peak -l-> SLOW.up.q20` | — | — |
| PCV01Z:trough | s | B4022:upq20 | 6.065 | 6.935 | 24 | True | `MID-S.trough -s-> SLOW.up.q20` | — | — |
| FT02Z:downq80 | s | TIT02:upq20 | 6.059 | 13.952 | 8 | False | `MID-S.down.q80 -s-> MID.up.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:upq80 | m | FT01:downq50 | 6.058 | 3.555 | 16 | False | `MID.up.q80 -m-> MID.down.q50` | — | tennessee_eastman, building_59 |
| FT02:upq80 | m | FT02Z:downq80 | 6.057 | 6.692 | 28 | True | `MID-S.up.q80 -m-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| LCV01Z:upq20 | m | LCV01Z:downq20 | 6.035 | 6.566 | 59 | True | `MID.up.q20 -m-> MID.down.q20 [same role]` | tennessee_eastman, building_59 | — |
| HILout:downq20 | m | CO_rpm:trough | 6.033 | 4.76 | 21 | True | `SLOW.down.q20 -m-> MID.trough` | — | building_59 |
| B4022:downq20 | s | B400B:downq20 | 6.033 | 4.585 | 12 | False | `SLOW.down.q20 -s-> MID-S.down.q20` | — | tennessee_eastman |
| B4022:downq20 | s | FT02:downq20 | 6.033 | 3.668 | 12 | False | `SLOW.down.q20 -s-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B4022:downq20 | s | FT02Z:downq20 | 6.033 | 4.585 | 12 | False | `SLOW.down.q20 -s-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| VXT03:upq80 | m | SIT02:peak | 6.027 | 3.92 | 23 | False | `SLOW.up.q80 -m-> MID.peak` | — | — |
| FT01Z:peak | m | FT01Z:trough | 6.027 | 2.601 | 20 | True | `MID.peak -m-> MID.trough [same role]` | — | tennessee_eastman |
| HILout:upq50 | l | SIT01:trough | 6.022 | 4.678 | 71 | True | `SLOW.up.q50 -l-> MID.trough` | — | — |
| FCV01Z:peak | m | TIT01:peak | 6.009 | 3.847 | 24 | True | `MID-S.peak -m-> MID.peak` | — | tennessee_eastman |
| PIT02:downq90 | m | B400B:downq20 | 6.003 | 8.29 | 22 | True | `MID.down.q90 -m-> MID-S.down.q20` | — | tennessee_eastman |
| PIT02:downq90 | m | FT02Z:downq20 | 6.003 | 7.461 | 22 | True | `MID.down.q90 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| LCV01D:upq80 | s | B3004:upq80 | 5.999 | 8.949 | 4 | False | `MID.up.q80 -s-> SET.up.q80` | — | tennessee_eastman |
| VYT03:upq50 | l | VXT02:upq80 | 5.995 | 8.243 | 16 | True | `SLOW.up.q50 -l-> SLOW.up.q80` | — | tennessee_eastman |
| VXT03:upq80 | m | SIT01:peak | 5.986 | 3.893 | 23 | False | `SLOW.up.q80 -m-> MID.peak` | — | — |
| HILout:upq50 | l | SIT02:trough | 5.977 | 4.71 | 70 | True | `SLOW.up.q50 -l-> MID.trough` | — | — |
| PIT01:trough | s | FT01Z:peak | 5.971 | 4.56 | 21 | True | `MID.trough -s-> MID.peak` | — | tennessee_eastman |
| B4022:upq50 | s | FCV01D:upq10 | 5.963 | 5.896 | 11 | False | `SLOW.up.q50 -s-> MID-S.up.q10` | building_59 | tennessee_eastman |
| FCV01D:downq10 | m | PIT02:downq10 | 5.931 | 5.167 | 15 | False | `MID-S.down.q10 -m-> MID.down.q10` | — | tennessee_eastman, building_59 |
| ST_PO:peak | s | B2016:peak | 5.922 | 5.521 | 85 | True | `MID.peak -s-> MID.peak` | — | physionet_slp |
| SIT02:trough | l | HILout:downq20 | 5.918 | 9.123 | 43 | False | `MID.trough -l-> SLOW.down.q20` | — | — |
| ST_TT01:downq90 | l | VYT02:downq50 | 5.912 | 1.758 | 9 | False | `MID.down.q90 -l-> SLOW.down.q50` | — | tennessee_eastman |
| LCP01D:downq50 | m | LCP01D:downq20 | 5.91 | 5.38 | 59 | True | `MID-S.down.q50 -m-> MID-S.down.q20 [same role]` | tennessee_eastman | building_59, fingrid |
| CO_rpm:trough | l | HILout:downq50 | 5.905 | 3.745 | 73 | True | `MID.trough -l-> SLOW.down.q50` | — | building_59 |
| SIT01:peak | l | SIT01:trough | 5.896 | 5.294 | 118 | True | `MID.peak -l-> MID.trough [same role]` | — | — |
| B3004:upq80 | m | PIT02:downq10 | 5.896 | 4.332 | 6 | True | `SET.up.q80 -m-> MID.down.q10` | — | tennessee_eastman |
| CO_rpm:trough | l | HILout:downq80 | 5.883 | 4.303 | 56 | False | `MID.trough -l-> SLOW.down.q80` | — | building_59 |
| B4022:downq20 | s | B4005:downq20 | 5.855 | 7.393 | 13 | False | `SLOW.down.q20 -s-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| SIT02:peak | l | HILout:upq50 | 5.854 | 3.843 | 84 | True | `MID.peak -l-> SLOW.up.q50` | — | — |
| B4005:downq20 | l | FCV01D:upq10 | 5.846 | 4.761 | 41 | True | `MID-S.down.q20 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| FT02:upq80 | m | B400B:downq80 | 5.841 | 5.019 | 27 | True | `MID-S.up.q80 -m-> MID-S.down.q80` | — | tennessee_eastman |
| B400B:downq20 | l | FCV01D:upq10 | 5.827 | 4.504 | 40 | True | `MID-S.down.q20 -l-> MID-S.up.q10` | — | tennessee_eastman |
| TIT02:upq20 | m | FCV01Z:peak | 5.817 | 3.962 | 26 | True | `MID.up.q20 -m-> MID-S.peak` | — | tennessee_eastman |
| PCV01D:trough | s | B4022:upq20 | 5.803 | 6.778 | 24 | True | `MID-S.trough -s-> SLOW.up.q20` | — | — |
| FT02Z:downq20 | l | FCV01D:upq10 | 5.8 | 4.372 | 40 | True | `MID-S.down.q20 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| HILout:upq80 | l | SIT01:trough | 5.798 | 5.722 | 56 | True | `SLOW.up.q80 -l-> MID.trough` | — | — |
| HILout:downq50 | l | SIT01:peak | 5.797 | 4.369 | 70 | True | `SLOW.down.q50 -l-> MID.peak` | — | — |
| VXT02:downq50 | m | SIT02:trough | 5.789 | 3.153 | 21 | True | `SLOW.down.q50 -m-> MID.trough` | — | — |
| TIT01:peak | m | PIT02:downq10 | 5.788 | 5.614 | 36 | True | `MID.peak -m-> MID.down.q10` | — | tennessee_eastman |
| SIT01:peak | l | SIT02:trough | 5.785 | 5.236 | 115 | True | `MID.peak -l-> MID.trough` | — | — |
| B400B:upq80 | m | B400B:downq80 | 5.78 | 6.886 | 23 | True | `MID-S.up.q80 -m-> MID-S.down.q80 [same role]` | — | tennessee_eastman |
| LCP01D:downq80 | m | LCP01D:downq50 | 5.764 | 4.724 | 66 | True | `MID-S.down.q80 -m-> MID-S.down.q50 [same role]` | tennessee_eastman, fingrid | building_59 |
| HILout:upq50 | l | CO_rpm:trough | 5.759 | 5.294 | 72 | True | `SLOW.up.q50 -l-> MID.trough` | — | building_59 |
| VXT02:downq50 | m | SIT01:trough | 5.75 | 3.132 | 21 | True | `SLOW.down.q50 -m-> MID.trough` | — | — |
| B4002:downq10 | l | B4005:upq20 | 5.744 | 12.382 | 5 | False | `SET.down.q10 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:downq80 | s | FT01Z:trough | 5.714 | 6.135 | 8 | False | `MID.down.q80 -s-> MID.trough` | — | tennessee_eastman |
| LCV01D:upq50 | s | LCV01Z:downq50 | 5.712 | 3.231 | 38 | True | `MID.up.q50 -s-> MID.down.q50` | tennessee_eastman | building_59 |
| FT02Z:upq80 | m | FT02Z:downq80 | 5.711 | 6.942 | 24 | True | `MID-S.up.q80 -m-> MID-S.down.q80 [same role]` | building_59 | tennessee_eastman |
| B4022:upq50 | s | B4005:upq20 | 5.692 | 9.459 | 12 | True | `SLOW.up.q50 -s-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:upq80 | s | FCV03Z:trough | 5.682 | 3.878 | 9 | False | `MID.up.q80 -s-> MID.trough` | building_59 | — |
| HILout:downq50 | l | SIT02:peak | 5.669 | 4.399 | 68 | True | `SLOW.down.q50 -l-> MID.peak` | — | — |
| TIT01:trough | m | FCV01Z:peak | 5.668 | 3.715 | 26 | True | `MID.trough -m-> MID-S.peak` | — | tennessee_eastman |
| FT01:upq20 | s | LCV01Z:upq20 | 5.664 | 4.165 | 10 | True | `MID.up.q20 -s-> MID.up.q20` | — | tennessee_eastman, building_59 |
| SIT01:trough | l | SIT02:peak | 5.659 | 4.722 | 102 | True | `MID.trough -l-> MID.peak` | — | — |
| PIT02:downq10 | m | B4005:upq20 | 5.643 | 7.991 | 18 | True | `MID.down.q10 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| LIT01:downq50 | s | LIT01:downq20 | 5.636 | 6.971 | 77 | True | `MID.down.q50 -s-> MID.down.q20 [same role]` | tennessee_eastman | — |
| B3004:downq50 | m | LCV01Z:downq80 | 5.634 | 6.498 | 7 | False | `SET.down.q50 -m-> MID.down.q80` | — | tennessee_eastman |
| HILout:downq50 | l | CO_rpm:peak | 5.623 | 4.988 | 72 | True | `SLOW.down.q50 -l-> MID.peak` | — | building_59 |
| SIT02:peak | l | HILout:upq20 | 5.622 | 8.503 | 44 | True | `MID.peak -l-> SLOW.up.q20` | — | — |
| LCV01D:downq20 | s | FT01Z:trough | 5.618 | 7.946 | 12 | True | `MID.down.q20 -s-> MID.trough` | — | tennessee_eastman |
| FT02:upq80 | s | B400B:upq80 | 5.618 | 10.083 | 6 | False | `MID-S.up.q80 -s-> MID-S.up.q80` | — | tennessee_eastman |
| LCP01D:downq50 | m | LCP01D:upq50 | 5.599 | 4.699 | 92 | True | `MID-S.down.q50 -m-> MID-S.up.q50 [same role]` | tennessee_eastman, fingrid | building_59 |
| B3004:downq20 | s | LIT01:downq20 | 5.586 | 4.655 | 6 | True | `SET.down.q20 -s-> MID.down.q20` | — | tennessee_eastman |
| FT01:downq80 | s | LCV01Z:downq50 | 5.582 | 10.089 | 7 | True | `MID.down.q80 -s-> MID.down.q50` | — | tennessee_eastman, building_59 |
| VYT03:downq20 | l | SIT02:trough | 5.578 | 3.289 | 30 | True | `SLOW.down.q20 -l-> MID.trough` | — | — |
| FCV03Z:trough | m | FT01:upq50 | 5.578 | 4.68 | 9 | False | `MID.trough -m-> MID.up.q50` | — | building_59 |
| FT02Z:upq80 | m | FT02:downq80 | 5.577 | 6.508 | 25 | True | `MID-S.up.q80 -m-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| CO_rpm:peak | l | SIT01:trough | 5.57 | 5.314 | 108 | True | `MID.peak -l-> MID.trough` | — | — |
| B3004:upq80 | m | B4022:upq20 | 5.568 | 2.338 | 14 | True | `SET.up.q80 -m-> SLOW.up.q20` | — | tennessee_eastman |
| SIT01:peak | l | CO_rpm:trough | 5.56 | 4.905 | 118 | True | `MID.peak -l-> MID.trough` | — | — |
| PIT02:upq90 | m | B400B:upq50 | 5.54 | 3.904 | 23 | True | `MID.up.q90 -m-> MID-S.up.q50` | — | tennessee_eastman |
| PIT02:upq90 | m | FT02:upq50 | 5.54 | 3.904 | 23 | True | `MID.up.q90 -m-> MID-S.up.q50` | — | tennessee_eastman |
| PIT02:upq90 | m | FT02Z:upq50 | 5.54 | 3.904 | 23 | True | `MID.up.q90 -m-> MID-S.up.q50` | — | tennessee_eastman |
| CO_rpm:trough | l | SIT01:peak | 5.538 | 4.544 | 102 | True | `MID.trough -l-> MID.peak` | — | — |
| LCV01D:upq20 | s | LCV01Z:downq20 | 5.53 | 3.915 | 31 | True | `MID.up.q20 -s-> MID.down.q20` | — | tennessee_eastman, building_59 |
| VXT03:downq50 | m | SIT01:peak | 5.508 | 3.116 | 15 | False | `SLOW.down.q50 -m-> MID.peak` | — | — |
| LCP01D:upq50 | m | LCP01D:downq50 | 5.488 | 5.751 | 88 | True | `MID-S.up.q50 -m-> MID-S.down.q50 [same role]` | tennessee_eastman | building_59, fingrid |
| CO_rpm:trough | l | CO_rpm:peak | 5.478 | 4.467 | 107 | True | `MID.trough -l-> MID.peak [same role]` | building_59 | fingrid |
| FT02Z:upq80 | m | B400B:downq80 | 5.473 | 5.4 | 23 | True | `MID-S.up.q80 -m-> MID-S.down.q80` | — | tennessee_eastman |
| HT_PS:downq20 | l | VXT03:upq50 | 5.471 | 7.023 | 12 | False | `SET.down.q20 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| ST_PS:downq20 | l | VXT03:upq50 | 5.471 | 7.023 | 12 | False | `SET.down.q20 -l-> SLOW.up.q50` | — | — |
| CO_rpm:trough | l | SIT02:peak | 5.466 | 4.574 | 100 | True | `MID.trough -l-> MID.peak` | — | — |
| TIT01:peak | m | PIT02:upq10 | 5.466 | 5.614 | 34 | True | `MID.peak -m-> MID.up.q10` | — | tennessee_eastman |
| SIT02:peak | l | SIT01:trough | 5.464 | 5.019 | 118 | True | `MID.peak -l-> MID.trough` | — | — |
| B4005:downq50 | m | TIT02:downq80 | 5.463 | 2.553 | 20 | True | `MID-S.down.q50 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| VXT02:upq80 | l | SIT02:trough | 5.462 | 4.055 | 41 | True | `SLOW.up.q80 -l-> MID.trough` | — | — |
| VXT03:upq50 | l | SIT02:trough | 5.459 | 4.483 | 34 | False | `SLOW.up.q50 -l-> MID.trough` | — | — |
| CO_rpm:peak | l | SIT02:trough | 5.452 | 5.258 | 105 | True | `MID.peak -l-> MID.trough` | — | — |
| B2004:downq20 | s | LCV01Z:upq50 | 5.436 | 5.257 | 4 | False | `SET.down.q20 -s-> MID.up.q50` | — | building_59 |
| ST_PO:trough | s | B2016:trough | 5.428 | 5.275 | 80 | True | `MID.trough -s-> MID.trough` | — | physionet_slp |
| LCV01Z:upq20 | s | LCV01D:downq20 | 5.4 | 3.913 | 39 | True | `MID.up.q20 -s-> MID.down.q20` | — | tennessee_eastman, building_59 |
| HILout:downq20 | l | SIT01:peak | 5.397 | 3.983 | 56 | True | `SLOW.down.q20 -l-> MID.peak` | — | — |
| B2004:downq50 | s | LCV01Z:upq50 | 5.381 | 10.74 | 4 | False | `SET.down.q50 -s-> MID.up.q50` | — | — |
| HILout:downq20 | l | CO_rpm:peak | 5.362 | 4.159 | 59 | True | `SLOW.down.q20 -l-> MID.peak` | — | building_59 |
| HILout:downq20 | l | SIT02:peak | 5.337 | 4.01 | 55 | True | `SLOW.down.q20 -l-> MID.peak` | — | — |
| B4022:downq50 | s | B4005:downq50 | 5.327 | 2.921 | 11 | True | `SLOW.down.q50 -s-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| B4022:downq20 | s | PCV01Z:trough | 5.326 | 7.429 | 17 | True | `SLOW.down.q20 -s-> MID-S.trough` | — | — |
| LCV01Z:downq80 | m | LCV01Z:upq80 | 5.318 | 8.42 | 25 | True | `MID.down.q80 -m-> MID.up.q80 [same role]` | tennessee_eastman | building_59 |
| LCP01D:downq80 | m | LCP01D:upq80 | 5.297 | 6.367 | 45 | True | `MID-S.down.q80 -m-> MID-S.up.q80 [same role]` | — | tennessee_eastman, nasa_battery, building_59, fingrid |
| FT02:downq80 | s | FT02:upq80 | 5.286 | 25.526 | 10 | False | `MID-S.down.q80 -s-> MID-S.up.q80 [same role]` | building_59 | tennessee_eastman |
| VXT02:upq50 | s | VXT02:upq80 | 5.284 | 13.506 | 4 | False | `SLOW.up.q50 -s-> SLOW.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| FCV02Z:upq80 | l | B400B:upq20 | 5.275 | 6.089 | 35 | True | `MID-S.up.q80 -l-> MID-S.up.q20` | — | tennessee_eastman |
| FCV02Z:upq80 | l | FT02:upq20 | 5.275 | 6.089 | 35 | True | `MID-S.up.q80 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FCV02Z:upq80 | l | FT02Z:upq20 | 5.275 | 6.089 | 35 | True | `MID-S.up.q80 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| SIT02:trough | l | SIT02:peak | 5.268 | 4.461 | 103 | True | `MID.trough -l-> MID.peak [same role]` | — | — |
| B400B:downq20 | l | B400B:upq20 | 5.265 | 4.949 | 37 | True | `MID-S.down.q20 -l-> MID-S.up.q20 [same role]` | — | tennessee_eastman |
| B400B:downq20 | l | FT02:upq20 | 5.265 | 4.949 | 37 | True | `MID-S.down.q20 -l-> MID-S.up.q20` | — | tennessee_eastman |
| B400B:downq20 | l | FT02Z:upq20 | 5.265 | 4.949 | 37 | True | `MID-S.down.q20 -l-> MID-S.up.q20` | — | tennessee_eastman |
| FT02:downq20 | l | FT02:upq20 | 5.251 | 4.867 | 37 | True | `MID-S.down.q20 -l-> MID-S.up.q20 [same role]` | building_59 | tennessee_eastman |
| FT02:downq20 | l | FT02Z:upq20 | 5.251 | 4.867 | 37 | True | `MID-S.down.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FCV02Z:upq50 | l | FCV01D:upq10 | 5.243 | 6.218 | 41 | True | `MID-S.up.q50 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| FT02Z:downq20 | l | B400B:upq20 | 5.24 | 4.804 | 37 | True | `MID-S.down.q20 -l-> MID-S.up.q20` | — | tennessee_eastman |
| FT02Z:downq20 | l | FT02:upq20 | 5.24 | 4.804 | 37 | True | `MID-S.down.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FT02Z:downq20 | l | FT02Z:upq20 | 5.24 | 4.804 | 37 | True | `MID-S.down.q20 -l-> MID-S.up.q20 [same role]` | building_59 | tennessee_eastman |
| LCV01Z:upq80 | m | LCV01Z:downq80 | 5.233 | 6.319 | 28 | False | `MID.up.q80 -m-> MID.down.q80 [same role]` | tennessee_eastman, building_59 | — |
| FT01:downq20 | l | FT01:upq20 | 5.232 | 2.192 | 17 | True | `MID.down.q20 -l-> MID.up.q20 [same role]` | — | tennessee_eastman, building_59 |
| PCV02Z:trough | l | PIT02:upq10 | 5.231 | 5.827 | 8 | False | `SLOW-S.trough -l-> MID.up.q10` | — | tennessee_eastman |
| HILout:upq20 | m | CO_rpm:peak | 5.223 | 4.944 | 19 | False | `SLOW.up.q20 -m-> MID.peak` | — | building_59 |
| FT01:downq20 | l | LCV01Z:upq20 | 5.212 | 4.702 | 50 | True | `MID.down.q20 -l-> MID.up.q20` | — | tennessee_eastman, building_59 |
| ST_TT01:upq10 | m | FCV02Z:upq50 | 5.202 | 6.459 | 34 | True | `MID.up.q10 -m-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| SIT02:peak | l | CO_rpm:trough | 5.196 | 4.65 | 119 | True | `MID.peak -l-> MID.trough` | — | — |
| TIT02:downq20 | m | FCV03D:peak | 5.196 | 4.615 | 11 | True | `MID.down.q20 -m-> MID.peak` | — | tennessee_eastman, building_59 |
| FT01Z:trough | s | LCV01Z:upq50 | 5.195 | 5.327 | 11 | False | `MID.trough -s-> MID.up.q50` | — | tennessee_eastman |
| TIT02:upq50 | m | FCV01Z:peak | 5.191 | 3.669 | 24 | True | `MID.up.q50 -m-> MID-S.peak` | — | tennessee_eastman |
| FT02Z:downq50 | l | FCV01D:upq10 | 5.188 | 6.195 | 42 | True | `MID-S.down.q50 -l-> MID-S.up.q10` | — | tennessee_eastman |
| B400B:downq50 | l | FCV01D:upq10 | 5.188 | 6.195 | 42 | True | `MID-S.down.q50 -l-> MID-S.up.q10` | — | tennessee_eastman |
| FT02:downq50 | l | FCV01D:upq10 | 5.188 | 6.195 | 42 | True | `MID-S.down.q50 -l-> MID-S.up.q10` | — | tennessee_eastman |
| ST_TT01:downq90 | l | VYT02:upq50 | 5.181 | 1.609 | 8 | False | `MID.down.q90 -l-> SLOW.up.q50` | — | tennessee_eastman |
| B4022:downq20 | s | PCV01D:trough | 5.176 | 6.664 | 17 | True | `SLOW.down.q20 -s-> MID-S.trough` | — | — |
| VYT02:upq50 | l | CO_rpm:trough | 5.127 | 2.553 | 33 | True | `SLOW.up.q50 -l-> MID.trough` | — | — |
| TIT02:upq50 | m | TIT02:downq80 | 5.101 | 4.807 | 24 | True | `MID.up.q50 -m-> MID.down.q80 [same role]` | — | tennessee_eastman, building_59 |
| B400B:downq20 | l | B4005:upq20 | 5.099 | 4.187 | 40 | True | `MID-S.down.q20 -l-> MID-S.up.q20` | — | tennessee_eastman |
| FCV02Z:upq80 | l | FCV01D:upq10 | 5.092 | 4.818 | 33 | True | `MID-S.up.q80 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| FT02:downq20 | l | B4005:upq20 | 5.086 | 4.118 | 40 | True | `MID-S.down.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FCV03D:trough | s | FCV03Z:trough | 5.084 | 9.361 | 5 | False | `MID.trough -s-> MID.trough` | — | building_59 |
| FT02Z:downq20 | l | B4005:upq20 | 5.075 | 4.065 | 40 | True | `MID-S.down.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| LCV01D:upq80 | s | FT03Z:peak | 5.069 | 4.654 | 13 | True | `MID.up.q80 -s-> MID.peak` | — | tennessee_eastman |
| PIT02:downq10 | s | PIT02:upq10 | 5.068 | 7.381 | 13 | True | `MID.down.q10 -s-> MID.up.q10 [same role]` | building_59 | tennessee_eastman |
| LCV01Z:upq80 | s | FT01:upq50 | 5.05 | 6.894 | 6 | False | `MID.up.q80 -s-> MID.up.q50` | — | tennessee_eastman, building_59 |
| TIT02:upq20 | m | B400B:downq20 | 5.041 | 8.754 | 17 | True | `MID.up.q20 -m-> MID-S.down.q20` | — | tennessee_eastman |
| TIT02:upq20 | m | FT02:downq20 | 5.041 | 9.63 | 17 | True | `MID.up.q20 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| TIT02:upq20 | m | FT02Z:downq20 | 5.041 | 9.63 | 17 | True | `MID.up.q20 -m-> MID-S.down.q20` | building_59 | tennessee_eastman |
| FCV02Z:upq50 | l | B4005:upq20 | 5.036 | 8.161 | 45 | True | `MID-S.up.q50 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B2004:upq50 | l | B2004:downq50 | 5.023 | 9.084 | 4 | False | `SET.up.q50 -l-> SET.down.q50 [same role]` | — | — |
| FT01Z:peak | m | FT01:downq50 | 5.014 | 3.934 | 11 | False | `MID.peak -m-> MID.down.q50` | — | tennessee_eastman |
| LIT01:downq20 | s | FT01:upq50 | 5.004 | 10.196 | 6 | True | `MID.down.q20 -s-> MID.up.q50` | — | tennessee_eastman |
| FCV02Z:upq50 | l | B400B:upq20 | 4.997 | 8.807 | 40 | True | `MID-S.up.q50 -l-> MID-S.up.q20` | — | tennessee_eastman |
| FCV02Z:upq50 | l | FT02:upq20 | 4.997 | 8.199 | 40 | True | `MID-S.up.q50 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FCV02Z:upq50 | l | FT02Z:upq20 | 4.997 | 8.503 | 40 | True | `MID-S.up.q50 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B4005:downq50 | l | FCV01D:upq10 | 4.986 | 6.083 | 42 | True | `MID-S.down.q50 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| FCV02Z:downq20 | m | FT02Z:downq80 | 4.986 | 4.953 | 12 | False | `MID-S.down.q20 -m-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| TIT02:downq80 | m | FCV02Z:downq80 | 4.982 | 3.574 | 9 | True | `MID.down.q80 -m-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| VT01:upq80 | l | SIT02:peak | 4.982 | 4.573 | 7 | False | `MID-S.up.q80 -l-> MID.peak` | — | — |
| FCV01D:upq10 | s | B4022:downq50 | 4.973 | 4.439 | 13 | True | `MID-S.up.q10 -s-> SLOW.down.q50` | building_59 | tennessee_eastman |
| FT02Z:downq50 | l | B4005:upq20 | 4.972 | 7.86 | 46 | True | `MID-S.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman |
| B400B:downq50 | l | B4005:upq20 | 4.972 | 7.86 | 46 | True | `MID-S.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman |
| FT02:downq50 | l | B4005:upq20 | 4.972 | 7.86 | 46 | True | `MID-S.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman |
| FT01:downq50 | s | LCV01Z:downq80 | 4.963 | 3.393 | 6 | True | `MID.down.q50 -s-> MID.down.q80` | — | tennessee_eastman, building_59 |
| LCP01D:upq50 | m | LCP01D:upq80 | 4.959 | 6.09 | 59 | True | `MID-S.up.q50 -m-> MID-S.up.q80 [same role]` | tennessee_eastman, fingrid | building_59 |
| FT02Z:downq50 | l | B400B:upq20 | 4.947 | 8.774 | 41 | True | `MID-S.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman |
| FT02Z:downq50 | l | FT02:upq20 | 4.947 | 8.472 | 41 | True | `MID-S.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman |
| FT02Z:downq50 | l | FT02Z:upq20 | 4.947 | 8.774 | 41 | True | `MID-S.down.q50 -l-> MID-S.up.q20 [same role]` | — | tennessee_eastman |
| B400B:downq50 | l | B400B:upq20 | 4.947 | 8.774 | 41 | True | `MID-S.down.q50 -l-> MID-S.up.q20 [same role]` | — | tennessee_eastman |
| B400B:downq50 | l | FT02:upq20 | 4.947 | 8.472 | 41 | True | `MID-S.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman |
| B400B:downq50 | l | FT02Z:upq20 | 4.947 | 8.774 | 41 | True | `MID-S.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman |
| FT02:downq50 | l | B400B:upq20 | 4.947 | 8.774 | 41 | True | `MID-S.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman |
| FT02:downq50 | l | FT02:upq20 | 4.947 | 8.472 | 41 | True | `MID-S.down.q50 -l-> MID-S.up.q20 [same role]` | — | tennessee_eastman |
| FT02:downq50 | l | FT02Z:upq20 | 4.947 | 8.774 | 41 | True | `MID-S.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman |
| PIT02:downq10 | l | FCV01D:upq10 | 4.909 | 4.994 | 41 | True | `MID.down.q10 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| FCV02Z:upq50 | m | PIT02:downq10 | 4.905 | 5.513 | 21 | True | `MID-S.up.q50 -m-> MID.down.q10` | — | tennessee_eastman, building_59 |
| FCV01D:downq10 | l | B400B:upq20 | 4.895 | 7.642 | 34 | True | `MID-S.down.q10 -l-> MID-S.up.q20` | — | tennessee_eastman |
| FCV01D:downq10 | l | FT02:upq20 | 4.895 | 7.005 | 34 | True | `MID-S.down.q10 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FCV01D:downq10 | l | FT02Z:upq20 | 4.895 | 7.323 | 34 | True | `MID-S.down.q10 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B4022:upq20 | s | B4022:upq50 | 4.886 | 7.109 | 40 | True | `SLOW.up.q20 -s-> SLOW.up.q50 [same role]` | tennessee_eastman | building_59 |
| B4005:downq20 | l | B400B:upq20 | 4.875 | 5.471 | 35 | True | `MID-S.down.q20 -l-> MID-S.up.q20` | — | tennessee_eastman |
| B4005:downq20 | l | FT02Z:upq20 | 4.875 | 5.471 | 35 | True | `MID-S.down.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FT02:downq80 | m | FT02Z:upq80 | 4.863 | 9.45 | 27 | True | `MID-S.down.q80 -m-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| LCV01Z:upq20 | s | PCV01Z:trough | 4.858 | 9.87 | 9 | True | `MID.up.q20 -s-> MID-S.trough` | — | — |
| FT01:upq50 | s | FT03:peak | 4.856 | 7.481 | 4 | False | `MID.up.q50 -s-> MID.peak` | — | — |
| PCV01D:peak | s | B4022:downq50 | 4.851 | 7.352 | 12 | False | `MID-S.peak -s-> SLOW.down.q50` | — | — |
| TIT02:upq80 | m | PIT02:upq90 | 4.849 | 4.051 | 36 | True | `MID.up.q80 -m-> MID.up.q90` | — | tennessee_eastman, building_59 |
| FCV02Z:upq50 | l | FCV02Z:downq80 | 4.847 | 7.644 | 37 | True | `MID-S.up.q50 -l-> MID-S.down.q80 [same role]` | — | tennessee_eastman, building_59 |
| ST_TT01:downq90 | l | VYT03:upq50 | 4.84 | 1.735 | 8 | False | `MID.down.q90 -l-> SLOW.up.q50` | — | tennessee_eastman |
| B400B:upq20 | m | PIT02:upq90 | 4.837 | 3.218 | 12 | False | `MID-S.up.q20 -m-> MID.up.q90` | — | tennessee_eastman |
| PIT02:downq10 | s | B4005:downq20 | 4.832 | 8.714 | 7 | False | `MID.down.q10 -s-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| FT02Z:downq50 | l | FCV02Z:downq80 | 4.808 | 7.616 | 38 | True | `MID-S.down.q50 -l-> MID-S.down.q80` | — | tennessee_eastman |
| B400B:downq50 | l | FCV02Z:downq80 | 4.808 | 7.616 | 38 | True | `MID-S.down.q50 -l-> MID-S.down.q80` | — | tennessee_eastman |
| FT02:downq50 | l | FCV02Z:downq80 | 4.808 | 7.616 | 38 | True | `MID-S.down.q50 -l-> MID-S.down.q80` | — | tennessee_eastman |
| LCV01Z:upq20 | s | FCV03D:peak | 4.806 | 3.994 | 8 | False | `MID.up.q20 -s-> MID.peak` | — | tennessee_eastman, building_59 |
| FCV01D:downq10 | m | B4022:upq20 | 4.801 | 4.183 | 30 | True | `MID-S.down.q10 -m-> SLOW.up.q20` | building_59 | tennessee_eastman |
| LCP01D:downq80 | l | LCP01D:upq20 | 4.791 | 4.247 | 69 | True | `MID-S.down.q80 -l-> MID-S.up.q20 [same role]` | — | tennessee_eastman, nasa_battery, building_59, fingrid |
| LCV01D:upq20 | m | FT01:downq20 | 4.788 | 2.667 | 30 | True | `MID.up.q20 -m-> MID.down.q20` | — | tennessee_eastman, building_59 |
| LCV01D:upq80 | s | LCV01D:downq80 | 4.785 | 5.824 | 67 | True | `MID.up.q80 -s-> MID.down.q80 [same role]` | tennessee_eastman | building_59 |
| B3004:downq80 | s | LCV01D:upq50 | 4.782 | 4.782 | 7 | False | `SET.down.q80 -s-> MID.up.q50` | — | tennessee_eastman |
| FT02:upq20 | m | PIT02:upq90 | 4.779 | 3.122 | 12 | False | `MID-S.up.q20 -m-> MID.up.q90` | — | tennessee_eastman, building_59 |
| B4005:downq50 | l | B4005:upq20 | 4.778 | 7.984 | 46 | True | `MID-S.down.q50 -l-> MID-S.up.q20 [same role]` | — | tennessee_eastman, building_59 |
| B400B:downq20 | l | FCV02Z:downq80 | 4.776 | 5.19 | 32 | True | `MID-S.down.q20 -l-> MID-S.down.q80` | — | tennessee_eastman |
| FCV02Z:downq80 | m | B4022:downq50 | 4.766 | 4.963 | 22 | True | `MID-S.down.q80 -m-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| FT02:downq20 | l | FCV02Z:downq80 | 4.763 | 5.105 | 32 | True | `MID-S.down.q20 -l-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| B400B:upq20 | m | B4022:upq50 | 4.759 | 4.255 | 25 | False | `MID-S.up.q20 -m-> SLOW.up.q50` | — | tennessee_eastman |
| B4005:downq50 | l | B400B:upq20 | 4.754 | 8.615 | 41 | True | `MID-S.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman |
| B4005:downq50 | l | FT02:upq20 | 4.754 | 8.318 | 41 | True | `MID-S.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B4005:downq50 | l | FT02Z:upq20 | 4.754 | 8.615 | 41 | True | `MID-S.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FT02Z:downq20 | l | FCV02Z:downq80 | 4.753 | 5.038 | 32 | True | `MID-S.down.q20 -l-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| TIT02:downq80 | m | B400B:upq20 | 4.75 | 5.68 | 9 | True | `MID.down.q80 -m-> MID-S.up.q20` | — | tennessee_eastman |
| B4022:downq50 | s | B4022:downq20 | 4.727 | 8.113 | 41 | True | `SLOW.down.q50 -s-> SLOW.down.q20 [same role]` | tennessee_eastman | building_59 |
| B400B:downq80 | m | FT02Z:upq80 | 4.71 | 7.421 | 26 | True | `MID-S.down.q80 -m-> MID-S.up.q80` | — | tennessee_eastman |
| FT02:downq50 | m | PIT02:downq90 | 4.704 | 3.832 | 23 | True | `MID-S.down.q50 -m-> MID.down.q90` | — | tennessee_eastman |
| FT02Z:downq50 | m | PIT02:downq90 | 4.704 | 3.206 | 23 | True | `MID-S.down.q50 -m-> MID.down.q90` | — | tennessee_eastman |
| B400B:downq50 | m | PIT02:downq90 | 4.704 | 3.206 | 23 | True | `MID-S.down.q50 -m-> MID.down.q90` | — | tennessee_eastman |
| FT02:upq20 | m | B4022:upq50 | 4.702 | 4.127 | 25 | False | `MID-S.up.q20 -m-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| FT02Z:upq20 | m | B4022:upq50 | 4.69 | 4.036 | 25 | False | `MID-S.up.q20 -m-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| FCV01D:downq10 | m | FT02:upq20 | 4.69 | 5.836 | 6 | False | `MID-S.down.q10 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FCV01D:downq10 | l | FCV02Z:downq80 | 4.681 | 6.679 | 31 | True | `MID-S.down.q10 -l-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| B3004:upq20 | s | LIT01:upq20 | 4.665 | 4.422 | 8 | True | `SET.up.q20 -s-> MID.up.q20` | — | tennessee_eastman |
| HT_PS:downq20 | l | VXT03:downq50 | 4.663 | 7.182 | 10 | False | `SET.down.q20 -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| ST_PS:downq20 | l | VXT03:downq50 | 4.663 | 7.182 | 10 | False | `SET.down.q20 -l-> SLOW.down.q50` | — | — |
| B4005:downq50 | m | PIT02:upq90 | 4.66 | 4.065 | 25 | True | `MID-S.down.q50 -m-> MID.up.q90` | — | tennessee_eastman, building_59 |
| LCP01D:upq80 | l | LCP01D:downq20 | 4.653 | 4.109 | 72 | True | `MID-S.up.q80 -l-> MID-S.down.q20 [same role]` | tennessee_eastman, fingrid | nasa_battery, building_59 |
| LIT01:downq20 | m | LIT01:upq20 | 4.641 | 4.63 | 170 | True | `MID.down.q20 -m-> MID.up.q20 [same role]` | tennessee_eastman | — |
| LCP01D:downq80 | m | LIT01:upq80 | 4.634 | 3.967 | 99 | True | `MID-S.down.q80 -m-> MID.up.q80` | — | tennessee_eastman |
| LCP01D:upq50 | l | LCP01D:upq20 | 4.632 | 5.652 | 80 | False | `MID-S.up.q50 -l-> MID-S.up.q20 [same role]` | tennessee_eastman | building_59, fingrid |
| PCV02Z:trough | l | B4022:downq50 | 4.631 | 4.815 | 15 | False | `SLOW-S.trough -l-> SLOW.down.q50` | — | tennessee_eastman |
| LCP01D:upq80 | l | LCP01D:upq20 | 4.629 | 4.146 | 71 | True | `MID-S.up.q80 -l-> MID-S.up.q20 [same role]` | — | tennessee_eastman, nasa_battery, building_59, fingrid |
| ST_GOV:trough | s | B2016:trough | 4.628 | 4.954 | 67 | True | `MID.trough -s-> MID.trough` | — | tennessee_eastman, physionet_slp |
| B4005:downq20 | l | B4005:upq20 | 4.616 | 4.411 | 37 | True | `MID-S.down.q20 -l-> MID-S.up.q20 [same role]` | — | tennessee_eastman, building_59 |
| ST_GOV:peak | s | B2016:peak | 4.592 | 4.95 | 68 | True | `MID.peak -s-> MID.peak` | physionet_slp | tennessee_eastman |
| LCV01D:upq80 | s | FT03:peak | 4.588 | 4.562 | 12 | True | `MID.up.q80 -s-> MID.peak` | — | — |
| FCV02Z:upq20 | l | FT02:upq20 | 4.575 | 5.672 | 21 | True | `MID-S.up.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FCV02Z:upq20 | l | FT02Z:upq20 | 4.575 | 5.672 | 21 | True | `MID-S.up.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FT01:upq20 | m | LCV01Z:upq20 | 4.574 | 2.904 | 18 | True | `MID.up.q20 -m-> MID.up.q20` | — | tennessee_eastman, building_59 |
| B2004:downq80 | l | LCV01Z:upq80 | 4.573 | 4.601 | 13 | False | `SET.down.q80 -l-> MID.up.q80` | — | — |
| B400B:upq20 | m | B4022:downq50 | 4.568 | 4.559 | 24 | True | `MID-S.up.q20 -m-> SLOW.down.q50` | — | tennessee_eastman |
| ST_PT01:trough | s | B3004:upq80 | 4.55 | 4.735 | 6 | True | `MID.trough -s-> SET.up.q80` | — | tennessee_eastman |
| FT02Z:upq80 | s | LCV01Z:upq20 | 4.531 | 6.099 | 8 | True | `MID-S.up.q80 -s-> MID.up.q20` | — | tennessee_eastman, building_59 |
| FCV01Z:trough | m | TIT02:downq80 | 4.526 | 9.735 | 13 | True | `MID-S.trough -m-> MID.down.q80` | — | tennessee_eastman |
| FCV03Z:trough | s | LCV01Z:downq20 | 4.517 | 6.344 | 10 | True | `MID.trough -s-> MID.down.q20` | — | building_59 |
| FCV01D:downq10 | l | B4005:upq20 | 4.514 | 7.131 | 35 | True | `MID-S.down.q10 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FT02:upq20 | m | B4022:downq50 | 4.514 | 4.717 | 24 | True | `MID-S.up.q20 -m-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| FT02:downq80 | m | B400B:upq80 | 4.503 | 11.025 | 25 | True | `MID-S.down.q80 -m-> MID-S.up.q80` | — | tennessee_eastman |
| FT02Z:upq20 | m | B4022:downq50 | 4.503 | 4.325 | 24 | True | `MID-S.up.q20 -m-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| B4005:downq50 | l | FCV02Z:downq80 | 4.5 | 7.478 | 37 | True | `MID-S.down.q50 -l-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| TIT02:upq50 | m | PIT02:upq90 | 4.496 | 4.101 | 31 | True | `MID.up.q50 -m-> MID.up.q90` | — | tennessee_eastman, building_59 |
| LCV01D:upq20 | s | LCV01Z:upq20 | 4.496 | 3.946 | 25 | True | `MID.up.q20 -s-> MID.up.q20` | — | tennessee_eastman, building_59 |
| LCP01D:downq50 | l | LCP01D:downq80 | 4.492 | 4.772 | 91 | True | `MID-S.down.q50 -l-> MID-S.down.q80 [same role]` | tennessee_eastman | building_59, fingrid |
| FCV02Z:upq20 | l | B4005:upq20 | 4.488 | 6.352 | 23 | True | `MID-S.up.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| LIT01:upq20 | m | LCP01D:upq20 | 4.482 | 4.088 | 65 | True | `MID.up.q20 -m-> MID-S.up.q20` | — | tennessee_eastman |
| FCV01D:downq10 | m | B4022:upq50 | 4.481 | 3.834 | 24 | True | `MID-S.down.q10 -m-> SLOW.up.q50` | building_59 | tennessee_eastman |
| LCV01D:downq50 | s | FT01Z:trough | 4.472 | 3.81 | 14 | True | `MID.down.q50 -s-> MID.trough` | — | tennessee_eastman |
| FCV02Z:upq20 | l | FCV01D:upq10 | 4.46 | 4.355 | 20 | True | `MID-S.up.q20 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| TIT02:upq80 | m | PIT02:downq10 | 4.445 | 6.481 | 33 | True | `MID.up.q80 -m-> MID.down.q10` | — | tennessee_eastman, building_59 |
| FCV02Z:upq20 | l | FCV01Z:trough | 4.437 | 4.279 | 27 | True | `MID-S.up.q20 -l-> MID-S.trough` | — | tennessee_eastman |
| PIT02:upq10 | m | FT01:upq50 | 4.436 | 2.873 | 10 | False | `MID.up.q10 -m-> MID.up.q50` | — | tennessee_eastman, building_59 |
| FT01:downq50 | s | FT01Z:trough | 4.431 | 4.543 | 4 | False | `MID.down.q50 -s-> MID.trough` | — | tennessee_eastman |
| HT_LD:trough | s | VYT02:downq80 | 4.43 | 11.135 | 3 | False | `MID-S.trough -s-> SLOW.down.q80` | — | — |
| B4022:downq50 | l | FCV01D:upq10 | 4.424 | 3.755 | 29 | True | `SLOW.down.q50 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| PIT01:trough | s | FT01:upq80 | 4.398 | 3.306 | 8 | True | `MID.trough -s-> MID.up.q80` | — | tennessee_eastman |
| ST_PS:downq20 | l | B2004:downq50 | 4.397 | 7.525 | 3 | False | `SET.down.q20 -l-> SET.down.q50` | — | — |
| FT01:upq50 | m | LCV01Z:downq50 | 4.396 | 1.729 | 17 | True | `MID.up.q50 -m-> MID.down.q50` | — | tennessee_eastman, building_59 |
| LCV01D:downq50 | s | FT01:downq20 | 4.383 | 6.273 | 10 | True | `MID.down.q50 -s-> MID.down.q20` | — | tennessee_eastman, building_59 |
| B3004:upq80 | m | B4022:downq20 | 4.375 | 2.338 | 11 | True | `SET.up.q80 -m-> SLOW.down.q20` | — | tennessee_eastman |
| B2004:upq20 | l | PCV01D:peak | 4.37 | 3.525 | 12 | False | `SET.up.q20 -l-> MID-S.peak` | — | — |
| TIT02:upq20 | m | PIT02:upq90 | 4.351 | 4.429 | 29 | True | `MID.up.q20 -m-> MID.up.q90` | — | tennessee_eastman, building_59 |
| B400B:downq80 | m | B400B:upq80 | 4.348 | 8.095 | 24 | True | `MID-S.down.q80 -m-> MID-S.up.q80 [same role]` | — | tennessee_eastman |
| FCV02Z:upq20 | l | FCV02Z:downq80 | 4.341 | 5.205 | 19 | True | `MID-S.up.q20 -l-> MID-S.down.q80 [same role]` | — | tennessee_eastman, building_59 |
| FCV01Z:peak | m | PIT02:downq10 | 4.336 | 3.862 | 23 | True | `MID-S.peak -m-> MID.down.q10` | — | tennessee_eastman |
| FCV01D:upq10 | l | B3004:downq80 | 4.324 | 3.572 | 9 | False | `MID-S.up.q10 -l-> SET.down.q80` | — | tennessee_eastman |
| B4022:upq50 | s | LCV01Z:downq80 | 4.323 | 6.27 | 15 | True | `SLOW.up.q50 -s-> MID.down.q80` | — | tennessee_eastman, building_59 |
| FCV02Z:upq80 | m | FCV03D:trough | 4.323 | 2.218 | 9 | False | `MID-S.up.q80 -m-> MID.trough` | — | tennessee_eastman, building_59 |
| FT01:upq20 | l | LCV01Z:upq20 | 4.318 | 2.087 | 33 | True | `MID.up.q20 -l-> MID.up.q20` | — | tennessee_eastman, building_59 |
| PIT02:upq90 | m | PIT02:downq10 | 4.305 | 4.501 | 31 | True | `MID.up.q90 -m-> MID.down.q10 [same role]` | — | tennessee_eastman, building_59 |
| B3004:downq50 | s | LCV01D:upq50 | 4.304 | 4.099 | 9 | True | `SET.down.q50 -s-> MID.up.q50` | — | tennessee_eastman |
| LCV01Z:downq80 | m | B400B:downq20 | 4.299 | 1.719 | 11 | True | `MID.down.q80 -m-> MID-S.down.q20` | — | tennessee_eastman |
| LCV01Z:downq80 | m | FT02:downq20 | 4.299 | 1.719 | 11 | True | `MID.down.q80 -m-> MID-S.down.q20` | building_59 | tennessee_eastman |
| LCV01Z:downq80 | m | FT02Z:downq20 | 4.299 | 1.719 | 11 | True | `MID.down.q80 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B4022:upq20 | s | B4022:downq20 | 4.293 | 2.095 | 41 | False | `SLOW.up.q20 -s-> SLOW.down.q20 [same role]` | building_59 | tennessee_eastman |
| LCV01Z:downq50 | m | FT01:upq50 | 4.293 | 7.255 | 13 | False | `MID.down.q50 -m-> MID.up.q50` | — | tennessee_eastman, building_59 |
| FT02Z:downq50 | l | FCV01Z:trough | 4.278 | 4.565 | 47 | True | `MID-S.down.q50 -l-> MID-S.trough` | — | tennessee_eastman |
| B400B:downq50 | l | FCV01Z:trough | 4.278 | 4.565 | 47 | True | `MID-S.down.q50 -l-> MID-S.trough` | — | tennessee_eastman |
| FT02:downq50 | l | FCV01Z:trough | 4.278 | 4.565 | 47 | True | `MID-S.down.q50 -l-> MID-S.trough` | — | tennessee_eastman |
| FT02:downq80 | m | FT02:upq80 | 4.275 | 6.729 | 25 | True | `MID-S.down.q80 -m-> MID-S.up.q80 [same role]` | building_59 | tennessee_eastman |
| PIT02:upq10 | m | PIT02:upq90 | 4.274 | 2.307 | 21 | True | `MID.up.q10 -m-> MID.up.q90 [same role]` | — | tennessee_eastman, building_59 |
| TIT02:downq80 | m | B4005:upq20 | 4.255 | 4.07 | 9 | True | `MID.down.q80 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:downq50 | m | LCV01Z:upq50 | 4.253 | 2.373 | 35 | True | `MID.down.q50 -m-> MID.up.q50 [same role]` | tennessee_eastman, building_59 | — |
| LCP01D:upq50 | l | LCP01D:downq20 | 4.246 | 4.53 | 74 | False | `MID-S.up.q50 -l-> MID-S.down.q20 [same role]` | tennessee_eastman, fingrid | building_59 |
| B4005:upq20 | l | FT02:upq50 | 4.244 | 4.811 | 34 | False | `MID-S.up.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| B4005:upq20 | l | FT02Z:upq50 | 4.244 | 4.811 | 34 | False | `MID-S.up.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| LCP01D:upq80 | l | LCP01D:upq50 | 4.24 | 5.243 | 108 | True | `MID-S.up.q80 -l-> MID-S.up.q50 [same role]` | — | tennessee_eastman, building_59, fingrid |
| FT01:downq20 | l | LCV01Z:downq20 | 4.24 | 4.173 | 41 | True | `MID.down.q20 -l-> MID.down.q20` | — | tennessee_eastman, building_59 |
| TIT01:trough | m | PIT02:upq90 | 4.239 | 4.567 | 29 | True | `MID.trough -m-> MID.up.q90` | — | tennessee_eastman |
| FCV02Z:downq80 | l | B400B:upq50 | 4.236 | 4.586 | 32 | False | `MID-S.down.q80 -l-> MID-S.up.q50` | — | tennessee_eastman |
| FCV02Z:downq80 | l | FT02:upq50 | 4.236 | 4.586 | 32 | False | `MID-S.down.q80 -l-> MID-S.up.q50` | — | tennessee_eastman |
| FCV02Z:downq80 | l | FT02Z:upq50 | 4.236 | 4.586 | 32 | False | `MID-S.down.q80 -l-> MID-S.up.q50` | — | tennessee_eastman |
| B4005:downq20 | l | FCV02Z:downq80 | 4.236 | 4.877 | 29 | False | `MID-S.down.q20 -l-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| FT02Z:downq80 | m | FT02Z:upq80 | 4.236 | 8.304 | 23 | True | `MID-S.down.q80 -m-> MID-S.up.q80 [same role]` | building_59 | tennessee_eastman |
| B4022:upq50 | s | FT02Z:upq20 | 4.236 | 8.639 | 8 | True | `SLOW.up.q50 -s-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FT01:downq50 | m | FT01Z:trough | 4.225 | 4.722 | 8 | True | `MID.down.q50 -m-> MID.trough` | — | tennessee_eastman |
| FT02:downq80 | m | TIT01:peak | 4.221 | 2.769 | 20 | False | `MID-S.down.q80 -m-> MID.peak` | — | tennessee_eastman |
| B4005:upq20 | m | B4022:upq50 | 4.22 | 3.935 | 24 | True | `MID-S.up.q20 -m-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| B4005:upq20 | m | B4022:downq50 | 4.22 | 5.341 | 24 | True | `MID-S.up.q20 -m-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| TIT02:upq80 | m | FCV01Z:peak | 4.218 | 2.416 | 21 | True | `MID.up.q80 -m-> MID-S.peak` | — | tennessee_eastman |
| B400B:upq20 | l | B400B:upq50 | 4.214 | 4.801 | 33 | False | `MID-S.up.q20 -l-> MID-S.up.q50 [same role]` | — | tennessee_eastman |
| B400B:upq20 | l | FT02:upq50 | 4.214 | 4.801 | 33 | False | `MID-S.up.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| B400B:upq20 | l | FT02Z:upq50 | 4.214 | 4.801 | 33 | False | `MID-S.up.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| B3004:upq50 | s | LCV01Z:downq20 | 4.214 | 8.213 | 5 | True | `SET.up.q50 -s-> MID.down.q20` | — | tennessee_eastman |
| FT02:upq20 | l | B400B:upq50 | 4.21 | 4.718 | 33 | False | `MID-S.up.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| FT02:upq20 | l | FT02:upq50 | 4.21 | 4.718 | 33 | False | `MID-S.up.q20 -l-> MID-S.up.q50 [same role]` | — | tennessee_eastman |
| FT02:upq20 | l | FT02Z:upq50 | 4.21 | 4.718 | 33 | False | `MID-S.up.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| FT02Z:upq20 | l | B400B:upq50 | 4.21 | 4.713 | 33 | False | `MID-S.up.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| FT02Z:upq20 | l | FT02:upq50 | 4.21 | 4.713 | 33 | False | `MID-S.up.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| FT02Z:upq20 | l | FT02Z:upq50 | 4.21 | 4.713 | 33 | False | `MID-S.up.q20 -l-> MID-S.up.q50 [same role]` | — | tennessee_eastman |
| FCV01D:upq10 | l | FT02:upq50 | 4.207 | 4.738 | 33 | False | `MID-S.up.q10 -l-> MID-S.up.q50` | — | tennessee_eastman |
| FCV01D:upq10 | l | FT02Z:upq50 | 4.207 | 4.738 | 33 | False | `MID-S.up.q10 -l-> MID-S.up.q50` | — | tennessee_eastman |
| FCV01D:upq10 | l | B3004:downq50 | 4.164 | 2.58 | 12 | False | `MID-S.up.q10 -l-> SET.down.q50` | — | tennessee_eastman |
| B4005:upq20 | l | B4005:upq50 | 4.159 | 4.715 | 34 | False | `MID-S.up.q20 -l-> MID-S.up.q50 [same role]` | — | tennessee_eastman, building_59 |
| FT01Z:peak | s | LCV01Z:downq80 | 4.155 | 5.204 | 8 | False | `MID.peak -s-> MID.down.q80` | — | tennessee_eastman |
| FCV02Z:downq80 | l | B4005:upq50 | 4.152 | 4.495 | 32 | False | `MID-S.down.q80 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| LCV01Z:upq50 | m | LCV01Z:downq50 | 4.145 | 2.193 | 38 | True | `MID.up.q50 -m-> MID.down.q50 [same role]` | tennessee_eastman, building_59 | — |
| TIT01:peak | l | FCV01D:upq10 | 4.144 | 4.279 | 42 | True | `MID.peak -l-> MID-S.up.q10` | — | tennessee_eastman, nasa_battery |
| LCP01D:downq80 | l | LCP01D:upq50 | 4.14 | 4.29 | 99 | True | `MID-S.down.q80 -l-> MID-S.up.q50 [same role]` | tennessee_eastman | building_59, fingrid |
| B4022:upq20 | s | PIT02:downq10 | 4.139 | 3.764 | 16 | False | `SLOW.up.q20 -s-> MID.down.q10` | — | tennessee_eastman, building_59 |
| TIT02:upq80 | l | FCV01D:downq10 | 4.138 | 4.591 | 42 | True | `MID.up.q80 -l-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| TIT02:upq80 | l | FCV01D:upq10 | 4.138 | 4.362 | 42 | True | `MID.up.q80 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| B4022:downq50 | l | B4005:upq20 | 4.138 | 5.915 | 31 | True | `SLOW.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FT02Z:upq20 | s | B2016:peak | 4.137 | 1.81 | 8 | True | `MID-S.up.q20 -s-> MID.peak` | — | tennessee_eastman |
| B400B:upq20 | l | B4005:upq50 | 4.13 | 4.705 | 33 | False | `MID-S.up.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| B400B:downq80 | m | FT02:upq80 | 4.127 | 5.764 | 24 | True | `MID-S.down.q80 -m-> MID-S.up.q80` | — | tennessee_eastman |
| LIT01:downq50 | s | LIT01:upq50 | 4.126 | 4.235 | 89 | True | `MID.down.q50 -s-> MID.up.q50 [same role]` | — | tennessee_eastman |
| FT02:upq20 | l | B4005:upq50 | 4.126 | 4.623 | 33 | False | `MID-S.up.q20 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| FT02Z:upq20 | l | B4005:upq50 | 4.126 | 4.619 | 33 | False | `MID-S.up.q20 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| FCV01D:upq10 | l | B4005:upq50 | 4.122 | 4.643 | 33 | False | `MID-S.up.q10 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| PIT02:upq10 | m | B4022:upq20 | 4.119 | 3.334 | 50 | True | `MID.up.q10 -m-> SLOW.up.q20` | building_59 | tennessee_eastman |
| TIT02:upq50 | l | FCV01D:downq10 | 4.119 | 4.533 | 42 | True | `MID.up.q50 -l-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| TIT02:upq50 | l | FCV01D:upq10 | 4.119 | 4.533 | 42 | True | `MID.up.q50 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| LCV01Z:upq50 | s | LCV01Z:upq80 | 4.112 | 6.798 | 11 | False | `MID.up.q50 -s-> MID.up.q80 [same role]` | tennessee_eastman, building_59 | — |
| FCV02Z:upq20 | l | TIT02:downq50 | 4.108 | 2.674 | 25 | True | `MID-S.up.q20 -l-> MID.down.q50` | — | tennessee_eastman, building_59 |
| B400B:downq80 | l | FCV01D:upq10 | 4.102 | 2.483 | 30 | True | `MID-S.down.q80 -l-> MID-S.up.q10` | — | tennessee_eastman |
| FT02Z:downq80 | m | TIT01:peak | 4.1 | 3.244 | 19 | False | `MID-S.down.q80 -m-> MID.peak` | — | tennessee_eastman |
| LCP01D:downq50 | l | LCP01D:upq80 | 4.098 | 4.374 | 83 | True | `MID-S.down.q50 -l-> MID-S.up.q80 [same role]` | tennessee_eastman | building_59, fingrid |
| B4022:upq20 | s | B400B:downq20 | 4.091 | 3.72 | 8 | False | `SLOW.up.q20 -s-> MID-S.down.q20` | — | tennessee_eastman |
| B4022:upq20 | s | FT02:downq20 | 4.091 | 4.65 | 8 | False | `SLOW.up.q20 -s-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| LIT01:upq20 | s | LIT01:upq80 | 4.082 | 4.869 | 59 | True | `MID.up.q20 -s-> MID.up.q80 [same role]` | tennessee_eastman | — |
| PIT01:peak | s | PCV01Z:peak | 4.08 | 1.558 | 14 | True | `MID.peak -s-> MID-S.peak` | — | — |
| FCV01D:upq10 | l | FCV02Z:downq50 | 4.079 | 4.106 | 32 | False | `MID-S.up.q10 -l-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| FT02:downq80 | l | FCV01D:upq10 | 4.066 | 2.236 | 30 | True | `MID-S.down.q80 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| FT02Z:upq80 | m | FT02:upq80 | 4.066 | 5.126 | 18 | False | `MID-S.up.q80 -m-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| B4022:downq50 | l | FCV02Z:downq80 | 4.063 | 5.386 | 26 | False | `SLOW.down.q50 -l-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| ST_TT01:upq10 | m | B4005:downq20 | 4.061 | 5.715 | 26 | True | `MID.up.q10 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| FT02Z:downq80 | l | FCV01D:upq10 | 4.059 | 2.154 | 30 | True | `MID-S.down.q80 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| TIT02:upq20 | l | FCV01D:downq10 | 4.056 | 4.591 | 42 | True | `MID.up.q20 -l-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| TIT02:upq20 | l | FCV01D:upq10 | 4.056 | 4.362 | 42 | True | `MID.up.q20 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| LCV01Z:downq80 | m | TIT02:downq80 | 4.056 | 1.699 | 14 | True | `MID.down.q80 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| FCV02Z:upq50 | l | FCV01Z:trough | 4.052 | 4.582 | 43 | True | `MID-S.up.q50 -l-> MID-S.trough` | — | tennessee_eastman |
| B3004:downq80 | l | FCV02Z:upq80 | 4.051 | 2.648 | 9 | False | `SET.down.q80 -l-> MID-S.up.q80` | — | tennessee_eastman |
| FCV01D:downq10 | l | B400B:upq50 | 4.043 | 2.235 | 32 | False | `MID-S.down.q10 -l-> MID-S.up.q50` | — | tennessee_eastman |
| FCV01D:downq10 | l | FT02:upq50 | 4.043 | 2.235 | 32 | False | `MID-S.down.q10 -l-> MID-S.up.q50` | — | tennessee_eastman |
| FCV01D:downq10 | l | FT02Z:upq50 | 4.043 | 2.235 | 32 | False | `MID-S.down.q10 -l-> MID-S.up.q50` | — | tennessee_eastman |
| B3004:upq20 | s | LCV01D:downq20 | 4.037 | 4.373 | 7 | True | `SET.up.q20 -s-> MID.down.q20` | — | tennessee_eastman |
| B400B:downq80 | m | TIT01:peak | 4.033 | 3.162 | 19 | False | `MID-S.down.q80 -m-> MID.peak` | — | tennessee_eastman |
| B3004:downq20 | l | B4022:upq50 | 4.031 | 5.637 | 33 | False | `SET.down.q20 -l-> SLOW.up.q50` | — | tennessee_eastman |
| B400B:downq80 | l | TIT02:downq50 | 4.03 | 2.44 | 40 | True | `MID-S.down.q80 -l-> MID.down.q50` | — | tennessee_eastman |
| LIT01:upq20 | m | LCP01D:upq50 | 4.027 | 3.82 | 97 | True | `MID.up.q20 -m-> MID-S.up.q50` | — | tennessee_eastman |
| B4005:downq50 | l | FCV01Z:trough | 4.024 | 4.482 | 46 | True | `MID-S.down.q50 -l-> MID-S.trough` | — | tennessee_eastman |
| FT01:upq20 | l | LCV01Z:downq20 | 4.024 | 2.76 | 31 | True | `MID.up.q20 -l-> MID.down.q20` | — | tennessee_eastman, building_59 |
| PCV01Z:peak | m | B400B:downq20 | 4.018 | 2.822 | 10 | False | `MID-S.peak -m-> MID-S.down.q20` | — | — |
| PCV01D:trough | m | FT02Z:upq20 | 4.012 | 2.736 | 11 | False | `MID-S.trough -m-> MID-S.up.q20` | — | — |
| FT02Z:downq50 | l | TIT02:downq50 | 4.005 | 3.652 | 44 | True | `MID-S.down.q50 -l-> MID.down.q50` | — | tennessee_eastman |
| B400B:downq50 | l | TIT02:downq50 | 4.005 | 3.652 | 44 | True | `MID-S.down.q50 -l-> MID.down.q50` | — | tennessee_eastman |
| FT02:downq50 | l | TIT02:downq50 | 4.005 | 3.652 | 44 | True | `MID-S.down.q50 -l-> MID.down.q50` | — | tennessee_eastman |
| FCV01D:downq10 | m | B4022:downq20 | 4.001 | 3.884 | 25 | True | `MID-S.down.q10 -m-> SLOW.down.q20` | building_59 | tennessee_eastman |
| FT02:downq80 | l | TIT02:downq50 | 3.994 | 2.196 | 40 | True | `MID-S.down.q80 -l-> MID.down.q50` | — | tennessee_eastman, building_59 |
| LIT01:downq50 | s | FT01:upq50 | 3.994 | 3.881 | 8 | True | `MID.down.q50 -s-> MID.up.q50` | — | tennessee_eastman |
| LCV01D:downq20 | m | FT01:upq20 | 3.991 | 3.089 | 23 | True | `MID.down.q20 -m-> MID.up.q20` | — | tennessee_eastman, building_59 |
| FT02Z:downq80 | l | TIT02:downq50 | 3.988 | 1.587 | 40 | True | `MID-S.down.q80 -l-> MID.down.q50` | — | tennessee_eastman, building_59 |
| FCV01D:upq10 | l | B3004:downq20 | 3.975 | 5.628 | 7 | False | `MID-S.up.q10 -l-> SET.down.q20` | — | tennessee_eastman |
| TIT01:peak | l | B4005:upq20 | 3.972 | 5.241 | 46 | True | `MID.peak -l-> MID-S.up.q20` | — | tennessee_eastman |
| B2004:downq20 | l | B400B:upq20 | 3.967 | 3.169 | 8 | True | `SET.down.q20 -l-> MID-S.up.q20` | — | — |
| B2004:downq20 | l | FT02:upq20 | 3.967 | 2.535 | 8 | True | `SET.down.q20 -l-> MID-S.up.q20` | — | building_59 |
| LCP01D:upq80 | s | LCV01D:upq20 | 3.965 | 3.073 | 14 | False | `MID-S.up.q80 -s-> MID.up.q20` | — | tennessee_eastman, building_59 |
| FCV01D:downq10 | l | B4005:upq50 | 3.962 | 2.464 | 32 | False | `MID-S.down.q10 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| FT02:downq80 | m | B400B:downq80 | 3.962 | 6.3 | 22 | False | `MID-S.down.q80 -m-> MID-S.down.q80` | — | tennessee_eastman |
| FCV02Z:upq50 | l | TIT02:downq50 | 3.958 | 3.895 | 42 | True | `MID-S.up.q50 -l-> MID.down.q50` | — | tennessee_eastman, building_59 |
| LIT01:downq20 | m | LCP01D:upq20 | 3.955 | 4.229 | 61 | True | `MID.down.q20 -m-> MID-S.up.q20` | — | tennessee_eastman |
| TIT01:peak | l | B400B:upq20 | 3.952 | 5.851 | 41 | True | `MID.peak -l-> MID-S.up.q20` | — | tennessee_eastman |
| TIT01:peak | l | FT02:upq20 | 3.952 | 5.433 | 41 | True | `MID.peak -l-> MID-S.up.q20` | — | tennessee_eastman |
| TIT01:peak | l | FT02Z:upq20 | 3.952 | 5.642 | 41 | True | `MID.peak -l-> MID-S.up.q20` | — | tennessee_eastman |
| LCV01D:upq80 | s | LCV01Z:upq80 | 3.949 | 2.945 | 16 | True | `MID.up.q80 -s-> MID.up.q80` | — | tennessee_eastman, building_59 |
| TIT02:upq80 | l | B400B:upq20 | 3.946 | 5.606 | 41 | True | `MID.up.q80 -l-> MID-S.up.q20` | — | tennessee_eastman |
| TIT02:upq80 | l | FT02:upq20 | 3.946 | 5.382 | 41 | True | `MID.up.q80 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| TIT02:upq80 | l | FT02Z:upq20 | 3.946 | 5.606 | 41 | True | `MID.up.q80 -l-> MID-S.up.q20` | building_59 | tennessee_eastman |
| LCV01D:downq20 | m | LCV01D:upq20 | 3.943 | 3.872 | 145 | True | `MID.down.q20 -m-> MID.up.q20 [same role]` | tennessee_eastman | building_59 |
| TIT02:upq50 | l | B400B:upq20 | 3.927 | 5.534 | 41 | True | `MID.up.q50 -l-> MID-S.up.q20` | — | tennessee_eastman |
| TIT02:upq50 | l | FT02:upq20 | 3.927 | 5.313 | 41 | True | `MID.up.q50 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| TIT02:upq50 | l | FT02Z:upq20 | 3.927 | 5.534 | 41 | True | `MID.up.q50 -l-> MID-S.up.q20` | building_59 | tennessee_eastman |
| TIT02:downq50 | l | TIT02:downq20 | 3.926 | 4.586 | 53 | True | `MID.down.q50 -l-> MID.down.q20 [same role]` | building_59 | tennessee_eastman |
| TIT02:upq50 | l | PIT02:upq10 | 3.925 | 5.039 | 81 | True | `MID.up.q50 -l-> MID.up.q10` | — | tennessee_eastman, building_59 |
| TIT02:upq80 | l | TIT02:downq50 | 3.921 | 2.876 | 54 | True | `MID.up.q80 -l-> MID.down.q50 [same role]` | building_59 | tennessee_eastman |
| B3004:upq80 | l | B400B:upq50 | 3.907 | 1.681 | 11 | True | `SET.up.q80 -l-> MID-S.up.q50` | — | tennessee_eastman |
| B3004:upq80 | l | FT02:upq50 | 3.907 | 1.681 | 11 | True | `SET.up.q80 -l-> MID-S.up.q50` | — | tennessee_eastman |
| B3004:upq80 | l | FT02Z:upq50 | 3.907 | 1.681 | 11 | True | `SET.up.q80 -l-> MID-S.up.q50` | — | tennessee_eastman |
| PIT02:downq10 | l | B400B:upq50 | 3.9 | 4.029 | 38 | True | `MID.down.q10 -l-> MID-S.up.q50` | — | tennessee_eastman |
| PIT02:downq10 | l | FT02:upq50 | 3.9 | 4.029 | 38 | True | `MID.down.q10 -l-> MID-S.up.q50` | — | tennessee_eastman |
| PIT02:downq10 | l | FT02Z:upq50 | 3.9 | 4.029 | 38 | True | `MID.down.q10 -l-> MID-S.up.q50` | — | tennessee_eastman |
| PIT02:downq10 | l | FCV02Z:downq50 | 3.9 | 4.029 | 38 | True | `MID.down.q10 -l-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| FCV01Z:trough | m | TIT02:downq50 | 3.897 | 2.476 | 11 | True | `MID-S.trough -m-> MID.down.q50` | — | tennessee_eastman |
| B400B:downq50 | m | TIT02:downq80 | 3.896 | 2.819 | 13 | True | `MID-S.down.q50 -m-> MID.down.q80` | — | tennessee_eastman |
| TIT02:upq80 | l | PIT02:upq10 | 3.895 | 4.764 | 80 | True | `MID.up.q80 -l-> MID.up.q10` | — | tennessee_eastman, building_59 |
| FT02:downq80 | l | FCV01Z:trough | 3.894 | 2.196 | 39 | True | `MID-S.down.q80 -l-> MID-S.trough` | — | tennessee_eastman |
| FT02:upq80 | m | B400B:upq80 | 3.894 | 5.856 | 18 | False | `MID-S.up.q80 -m-> MID-S.up.q80` | — | tennessee_eastman |
| PIT02:upq10 | l | FT02:upq20 | 3.882 | 4.44 | 36 | True | `MID.up.q10 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| PIT02:upq10 | l | FT02Z:upq20 | 3.882 | 4.44 | 36 | True | `MID.up.q10 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| TIT02:upq80 | l | B4005:upq20 | 3.88 | 5.223 | 45 | True | `MID.up.q80 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B4022:downq20 | s | FT01:upq50 | 3.88 | 3.033 | 7 | False | `SLOW.down.q20 -s-> MID.up.q50` | — | tennessee_eastman, building_59 |
| LCV01D:downq20 | m | LCV01Z:upq20 | 3.879 | 3.899 | 66 | True | `MID.down.q20 -m-> MID.up.q20` | — | tennessee_eastman, building_59 |
| TIT01:trough | l | FCV01D:downq10 | 3.878 | 4.101 | 42 | True | `MID.trough -l-> MID-S.down.q10` | — | tennessee_eastman, nasa_battery |
| TIT01:trough | l | FCV01D:upq10 | 3.878 | 3.896 | 42 | True | `MID.trough -l-> MID-S.up.q10` | — | tennessee_eastman, nasa_battery |
| ST_TT01:upq10 | m | FCV02Z:upq20 | 3.878 | 3.638 | 15 | True | `MID.up.q10 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| LCV01D:upq20 | s | PCV01Z:trough | 3.878 | 5.455 | 12 | False | `MID.up.q20 -s-> MID-S.trough` | — | — |
| LCV01D:upq50 | s | LCV01D:downq50 | 3.874 | 3.469 | 80 | True | `MID.up.q50 -s-> MID.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| PIT02:upq10 | m | B4022:downq20 | 3.872 | 3.201 | 47 | True | `MID.up.q10 -m-> SLOW.down.q20` | building_59 | tennessee_eastman |
| B4002:downq10 | l | TIT02:downq50 | 3.87 | 7.82 | 4 | False | `SET.down.q10 -l-> MID.down.q50` | — | tennessee_eastman, building_59 |
| TIT02:upq20 | l | B400B:upq20 | 3.868 | 5.382 | 41 | True | `MID.up.q20 -l-> MID-S.up.q20` | — | tennessee_eastman |
| TIT02:upq20 | l | FT02:upq20 | 3.868 | 5.157 | 41 | True | `MID.up.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| TIT02:upq20 | l | FT02Z:upq20 | 3.868 | 5.382 | 41 | True | `MID.up.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| PIT02:downq10 | l | B3004:downq80 | 3.868 | 4.746 | 10 | False | `MID.down.q10 -l-> SET.down.q80` | — | tennessee_eastman |
| TIT02:upq20 | l | PIT02:upq10 | 3.865 | 4.991 | 81 | True | `MID.up.q20 -l-> MID.up.q10` | — | tennessee_eastman, building_59 |
| PIT02:downq90 | m | PIT02:upq10 | 3.865 | 3.355 | 28 | True | `MID.down.q90 -m-> MID.up.q10 [same role]` | — | tennessee_eastman, building_59 |
| TIT02:upq50 | l | B4005:upq20 | 3.862 | 4.958 | 45 | True | `MID.up.q50 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FT02Z:downq20 | m | B4022:downq20 | 3.857 | 3.497 | 28 | True | `MID-S.down.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| FT02:downq20 | m | B4022:downq20 | 3.857 | 3.507 | 28 | True | `MID-S.down.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| B400B:downq20 | m | B4022:downq20 | 3.857 | 4.01 | 28 | True | `MID-S.down.q20 -m-> SLOW.down.q20` | — | tennessee_eastman |
| LCP01D:downq50 | m | LIT01:upq80 | 3.849 | 3.668 | 118 | True | `MID-S.down.q50 -m-> MID.up.q80` | — | tennessee_eastman |
| B4005:downq50 | l | TIT02:downq50 | 3.849 | 3.362 | 44 | True | `MID-S.down.q50 -l-> MID.down.q50` | — | tennessee_eastman, building_59 |
| FT02:upq20 | l | B3004:downq80 | 3.847 | 3.334 | 8 | False | `MID-S.up.q20 -l-> SET.down.q80` | — | tennessee_eastman |
| FT03Z:peak | s | LCV01Z:downq20 | 3.844 | 6.547 | 8 | True | `MID.peak -s-> MID.down.q20` | — | tennessee_eastman |
| LCV01D:upq20 | m | LCV01Z:downq20 | 3.843 | 4.036 | 70 | True | `MID.up.q20 -m-> MID.down.q20` | — | tennessee_eastman, building_59 |
| TIT01:peak | l | FCV02Z:downq80 | 3.841 | 5.26 | 38 | True | `MID.peak -l-> MID-S.down.q80` | — | tennessee_eastman |
| FT02:upq50 | l | FT02:downq20 | 3.84 | 3.513 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q20 [same role]` | — | tennessee_eastman |
| FT02:upq50 | l | FT02Z:downq20 | 3.84 | 3.513 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q20` | — | tennessee_eastman |
| FT02Z:upq50 | l | B400B:downq20 | 3.84 | 3.513 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q20` | — | tennessee_eastman |
| FT02Z:upq50 | l | FT02:downq20 | 3.84 | 3.513 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q20` | — | tennessee_eastman |
| B400B:upq50 | l | B400B:downq20 | 3.84 | 3.513 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q20 [same role]` | — | tennessee_eastman |
| B400B:upq50 | l | FT02:downq20 | 3.84 | 3.513 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q20` | — | tennessee_eastman |
| B400B:upq50 | l | FT02Z:downq20 | 3.84 | 3.513 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q20` | — | tennessee_eastman |
| FCV02Z:downq80 | l | FCV02Z:downq50 | 3.839 | 4.586 | 29 | False | `MID-S.down.q80 -l-> MID-S.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| ST_TT01:upq10 | m | B400B:downq20 | 3.835 | 6.379 | 22 | True | `MID.up.q10 -m-> MID-S.down.q20` | — | tennessee_eastman |
| ST_TT01:upq10 | m | FT02:downq20 | 3.835 | 6.379 | 22 | True | `MID.up.q10 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| ST_TT01:upq10 | m | FT02Z:downq20 | 3.835 | 6.379 | 22 | True | `MID.up.q10 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B400B:downq80 | l | FCV01Z:trough | 3.829 | 1.83 | 38 | True | `MID-S.down.q80 -l-> MID-S.trough` | — | tennessee_eastman |
| FCV02Z:upq80 | m | B4022:upq20 | 3.829 | 3.928 | 27 | False | `MID-S.up.q80 -m-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| B4022:downq20 | l | B3004:downq80 | 3.828 | 5.389 | 6 | False | `SLOW.down.q20 -l-> SET.down.q80` | — | tennessee_eastman |
| PIT01:trough | s | PCV01Z:trough | 3.824 | 3.354 | 16 | True | `MID.trough -s-> MID-S.trough` | — | — |
| PIT02:downq10 | l | B4005:upq50 | 3.822 | 3.949 | 38 | True | `MID.down.q10 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| LCV01D:downq80 | s | LCV01Z:downq80 | 3.819 | 2.571 | 14 | True | `MID.down.q80 -s-> MID.down.q80` | — | tennessee_eastman, building_59 |
| LCV01D:upq20 | s | LCV01D:downq20 | 3.813 | 4.338 | 46 | True | `MID.up.q20 -s-> MID.down.q20 [same role]` | — | tennessee_eastman, building_59 |
| LCP01D:upq80 | l | LCP01D:downq50 | 3.808 | 4.161 | 97 | True | `MID-S.up.q80 -l-> MID-S.down.q50 [same role]` | tennessee_eastman, fingrid | building_59 |
| TIT02:upq20 | l | B4005:upq20 | 3.803 | 5.022 | 45 | True | `MID.up.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B4005:downq50 | l | FCV01D:downq10 | 3.799 | 5.171 | 32 | True | `MID-S.down.q50 -l-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| LIT01:upq80 | m | LIT01:downq50 | 3.794 | 3.515 | 240 | True | `MID.up.q80 -m-> MID.down.q50 [same role]` | tennessee_eastman | — |
| B4022:downq20 | m | B4005:upq20 | 3.791 | 4.317 | 28 | True | `SLOW.down.q20 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| PCV01Z:trough | m | FT02Z:upq20 | 3.791 | 2.655 | 10 | False | `MID-S.trough -m-> MID-S.up.q20` | — | — |
| FT02Z:downq80 | l | FCV01Z:trough | 3.789 | 1.587 | 38 | True | `MID-S.down.q80 -l-> MID-S.trough` | — | tennessee_eastman |
| B4022:downq20 | m | B400B:upq20 | 3.779 | 4.819 | 25 | True | `SLOW.down.q20 -m-> MID-S.up.q20` | — | tennessee_eastman |
| B4005:downq50 | m | FCV01D:downq10 | 3.772 | 3.525 | 10 | True | `MID-S.down.q50 -m-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| TIT02:upq80 | m | PIT02:downq90 | 3.771 | 4.051 | 28 | True | `MID.up.q80 -m-> MID.down.q90` | — | tennessee_eastman, building_59 |
| TIT02:upq50 | m | PIT02:downq10 | 3.771 | 5.741 | 26 | True | `MID.up.q50 -m-> MID.down.q10` | — | tennessee_eastman, building_59 |
| LCV01D:upq20 | s | PCV01D:trough | 3.769 | 5.832 | 12 | False | `MID.up.q20 -s-> MID-S.trough` | — | — |
| LCV01D:downq50 | s | FT03Z:trough | 3.769 | 4.496 | 10 | True | `MID.down.q50 -s-> MID.trough` | — | tennessee_eastman |
| B4022:downq50 | s | B4022:upq50 | 3.766 | 3.245 | 28 | False | `SLOW.down.q50 -s-> SLOW.up.q50 [same role]` | tennessee_eastman, building_59 | — |
| B4005:upq20 | l | B3004:downq80 | 3.764 | 3.4 | 8 | False | `MID-S.up.q20 -l-> SET.down.q80` | — | tennessee_eastman |
| FT03Z:peak | l | B2004:downq20 | 3.761 | 5.255 | 9 | True | `MID.peak -l-> SET.down.q20` | — | — |
| TIT02:upq50 | l | TIT02:downq50 | 3.758 | 2.672 | 52 | True | `MID.up.q50 -l-> MID.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| B400B:downq20 | l | FCV01Z:trough | 3.757 | 3.319 | 35 | True | `MID-S.down.q20 -l-> MID-S.trough` | — | tennessee_eastman |
| TIT02:downq80 | l | B4005:upq50 | 3.756 | 2.852 | 43 | True | `MID.down.q80 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| B3004:upq80 | l | FT03:trough | 3.754 | 2.692 | 11 | True | `SET.up.q80 -l-> MID.trough` | — | — |
| TIT02:upq20 | m | PIT02:downq90 | 3.75 | 3.986 | 25 | True | `MID.up.q20 -m-> MID.down.q90` | — | tennessee_eastman, building_59 |
| B4022:upq50 | s | PIT02:downq10 | 3.75 | 3.885 | 14 | False | `SLOW.up.q50 -s-> MID.down.q10` | — | tennessee_eastman, building_59 |
| PIT02:upq90 | m | PIT02:upq10 | 3.749 | 3.6 | 27 | True | `MID.up.q90 -m-> MID.up.q10 [same role]` | — | tennessee_eastman, building_59 |
| LCV01D:upq80 | s | FCV03Z:trough | 3.749 | 2.237 | 10 | True | `MID.up.q80 -s-> MID.trough` | — | building_59 |
| FT02:downq20 | l | FCV01Z:trough | 3.747 | 3.264 | 35 | True | `MID-S.down.q20 -l-> MID-S.trough` | — | tennessee_eastman |
| FT02Z:downq20 | l | FCV01Z:trough | 3.739 | 3.221 | 35 | True | `MID-S.down.q20 -l-> MID-S.trough` | — | tennessee_eastman |
| LCV01Z:upq50 | s | LCV01Z:downq80 | 3.738 | 4.856 | 10 | True | `MID.up.q50 -s-> MID.down.q80 [same role]` | — | tennessee_eastman, building_59 |
| TIT02:upq80 | l | FCV02Z:downq80 | 3.735 | 4.939 | 37 | True | `MID.up.q80 -l-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| B400B:upq20 | l | TIT02:downq20 | 3.732 | 3.87 | 34 | False | `MID-S.up.q20 -l-> MID.down.q20` | — | tennessee_eastman |
| FT02Z:upq20 | l | TIT02:downq20 | 3.729 | 3.798 | 34 | False | `MID-S.up.q20 -l-> MID.down.q20` | — | tennessee_eastman, building_59 |
| B4022:downq50 | l | B400B:upq20 | 3.725 | 6.235 | 25 | False | `SLOW.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman |
| B4022:downq50 | l | FT02:upq20 | 3.725 | 5.869 | 25 | False | `SLOW.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| LCV01D:downq80 | s | LCV01D:upq80 | 3.724 | 2.987 | 47 | True | `MID.down.q80 -s-> MID.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| LCV01D:upq50 | s | FT01:upq80 | 3.718 | 5.073 | 7 | False | `MID.up.q50 -s-> MID.up.q80` | — | tennessee_eastman, building_59 |
| TIT02:upq50 | l | FCV02Z:downq80 | 3.717 | 5.108 | 37 | True | `MID.up.q50 -l-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| B4022:upq50 | s | B400B:upq50 | 3.717 | 2.527 | 8 | False | `SLOW.up.q50 -s-> MID-S.up.q50` | — | tennessee_eastman |
| B4022:upq50 | s | FT02Z:upq50 | 3.717 | 2.527 | 8 | False | `SLOW.up.q50 -s-> MID-S.up.q50` | — | tennessee_eastman |
| LCV01Z:upq80 | s | LCV01Z:downq50 | 3.716 | 3.171 | 12 | True | `MID.up.q80 -s-> MID.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| B4005:upq50 | l | B400B:downq20 | 3.715 | 3.551 | 33 | False | `MID-S.up.q50 -l-> MID-S.down.q20` | — | tennessee_eastman |
| B4005:upq50 | l | FT02:downq20 | 3.715 | 3.551 | 33 | False | `MID-S.up.q50 -l-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B4005:upq50 | l | FT02Z:downq20 | 3.715 | 3.551 | 33 | False | `MID-S.up.q50 -l-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| LD:trough | m | VT01:downq80 | 3.715 | 7.422 | 4 | False | `MID.trough -m-> MID-S.down.q80` | — | — |
| FCV01Z:peak | l | FCV01D:downq10 | 3.713 | 2.997 | 36 | True | `MID-S.peak -l-> MID-S.down.q10` | — | tennessee_eastman |
| FCV01Z:peak | l | FCV01D:upq10 | 3.713 | 2.305 | 36 | True | `MID-S.peak -l-> MID-S.up.q10` | — | tennessee_eastman |
| B4005:downq20 | l | B4005:upq50 | 3.713 | 2.588 | 31 | False | `MID-S.down.q20 -l-> MID-S.up.q50 [same role]` | — | tennessee_eastman, building_59 |
| FCV01Z:trough | l | FCV02Z:downq50 | 3.71 | 3.389 | 40 | True | `MID-S.trough -l-> MID-S.down.q50` | — | tennessee_eastman |
| B4022:downq50 | s | LCV01Z:upq20 | 3.71 | 2.355 | 19 | True | `SLOW.down.q50 -s-> MID.up.q20` | — | tennessee_eastman, building_59 |
| B4022:downq50 | m | B4022:upq20 | 3.708 | 3.669 | 108 | True | `SLOW.down.q50 -m-> SLOW.up.q20 [same role]` | tennessee_eastman | building_59 |
| LIT01:upq80 | m | LCP01D:downq80 | 3.705 | 3.621 | 77 | True | `MID.up.q80 -m-> MID-S.down.q80` | — | tennessee_eastman |
| FCV02Z:upq80 | l | FT02:upq50 | 3.704 | 2.186 | 28 | False | `MID-S.up.q80 -l-> MID-S.up.q50` | — | tennessee_eastman |
| B400B:upq20 | l | FCV02Z:downq50 | 3.703 | 4.801 | 29 | False | `MID-S.up.q20 -l-> MID-S.down.q50` | — | tennessee_eastman |
| FT02:upq20 | l | FCV02Z:downq50 | 3.7 | 4.718 | 29 | False | `MID-S.up.q20 -l-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| FT02Z:upq20 | l | FCV02Z:downq50 | 3.7 | 4.713 | 29 | False | `MID-S.up.q20 -l-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| B3004:upq80 | s | LIT01:upq80 | 3.698 | 2.865 | 10 | True | `SET.up.q80 -s-> MID.up.q80` | — | tennessee_eastman |
| FCV02Z:downq50 | l | B400B:downq20 | 3.696 | 4.016 | 33 | True | `MID-S.down.q50 -l-> MID-S.down.q20` | — | tennessee_eastman |
| FCV02Z:downq50 | l | FT02:downq20 | 3.696 | 4.016 | 33 | True | `MID-S.down.q50 -l-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| FCV02Z:downq50 | l | FT02Z:downq20 | 3.696 | 4.016 | 33 | True | `MID-S.down.q50 -l-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B4022:upq20 | l | B4022:upq20 | 3.695 | 2.986 | 94 | True | `SLOW.up.q20 -l-> SLOW.up.q20 [same role]` | — | tennessee_eastman, building_59 |
| FCV01D:downq10 | l | TIT02:downq50 | 3.693 | 4.083 | 34 | True | `MID-S.down.q10 -l-> MID.down.q50` | — | tennessee_eastman, building_59 |
| LCP01D:upq20 | m | LIT01:downq20 | 3.689 | 3.58 | 52 | True | `MID-S.up.q20 -m-> MID.down.q20` | — | tennessee_eastman |
| B4022:upq50 | m | B4022:downq20 | 3.688 | 4.25 | 102 | True | `SLOW.up.q50 -m-> SLOW.down.q20 [same role]` | — | tennessee_eastman, building_59 |
| LCP01D:upq20 | l | LIT01:upq80 | 3.684 | 3.849 | 164 | True | `MID-S.up.q20 -l-> MID.up.q80` | — | tennessee_eastman |
| B3005:downq90 | m | B4022:downq20 | 3.676 | 4.481 | 7 | False | `SET.down.q90 -m-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| FT02:upq50 | l | FCV02Z:upq80 | 3.672 | 4.094 | 31 | False | `MID-S.up.q50 -l-> MID-S.up.q80` | — | tennessee_eastman |
| FT02Z:upq50 | l | FCV02Z:upq80 | 3.672 | 4.094 | 31 | False | `MID-S.up.q50 -l-> MID-S.up.q80` | — | tennessee_eastman |
| FT01:downq20 | m | LCV01D:upq20 | 3.671 | 1.806 | 26 | True | `MID.down.q20 -m-> MID.up.q20` | — | tennessee_eastman, building_59 |
| B4022:downq20 | s | LCV01Z:upq50 | 3.671 | 2.976 | 18 | True | `SLOW.down.q20 -s-> MID.up.q50` | — | tennessee_eastman, building_59 |
| FT03Z:trough | l | B2004:upq20 | 3.668 | 4.947 | 8 | False | `MID.trough -l-> SET.up.q20` | — | — |
| B4005:downq20 | l | FT02Z:upq50 | 3.667 | 2.641 | 30 | False | `MID-S.down.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| FCV01D:downq10 | l | FCV02Z:downq50 | 3.664 | 1.677 | 29 | False | `MID-S.down.q10 -l-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| TIT02:upq20 | l | FCV02Z:downq80 | 3.661 | 4.703 | 37 | True | `MID.up.q20 -l-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| B4005:upq50 | l | FCV02Z:upq80 | 3.66 | 3.724 | 31 | False | `MID-S.up.q50 -l-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| TIT02:downq80 | l | B400B:upq50 | 3.655 | 2.91 | 41 | True | `MID.down.q80 -l-> MID-S.up.q50` | — | tennessee_eastman |
| TIT02:downq80 | l | FT02:upq50 | 3.655 | 2.91 | 41 | True | `MID.down.q80 -l-> MID-S.up.q50` | — | tennessee_eastman |
| TIT02:downq80 | l | FT02Z:upq50 | 3.655 | 2.91 | 41 | True | `MID.down.q80 -l-> MID-S.up.q50` | — | tennessee_eastman |
| PCV01Z:trough | m | TIT02:downq80 | 3.654 | 2.624 | 13 | False | `MID-S.trough -m-> MID.down.q80` | — | — |
| FCV02Z:upq80 | m | LCV01Z:downq50 | 3.652 | 1.729 | 13 | True | `MID-S.up.q80 -m-> MID.down.q50` | — | tennessee_eastman, building_59 |
| B4022:upq50 | s | LCV01Z:downq50 | 3.651 | 2.336 | 17 | True | `SLOW.up.q50 -s-> MID.down.q50` | — | tennessee_eastman, building_59 |
| B4005:upq20 | l | TIT02:downq20 | 3.648 | 3.878 | 34 | False | `MID-S.up.q20 -l-> MID.down.q20` | — | tennessee_eastman, building_59 |
| PIT02:upq90 | s | B4022:downq20 | 3.648 | 3.279 | 14 | True | `MID.up.q90 -s-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| B3004:upq80 | l | B400B:upq20 | 3.643 | 4.471 | 9 | True | `SET.up.q80 -l-> MID-S.up.q20` | — | tennessee_eastman |
| B3004:upq80 | l | FT02:upq20 | 3.643 | 3.193 | 9 | True | `SET.up.q80 -l-> MID-S.up.q20` | — | tennessee_eastman |
| B3004:upq80 | l | FT02Z:upq20 | 3.643 | 3.832 | 9 | True | `SET.up.q80 -l-> MID-S.up.q20` | — | tennessee_eastman |
| FT02:downq20 | l | TIT02:downq50 | 3.64 | 2.448 | 34 | True | `MID-S.down.q20 -l-> MID.down.q50` | — | tennessee_eastman, building_59 |
| LIT01:upq20 | m | LCP01D:upq80 | 3.637 | 3.89 | 65 | True | `MID.up.q20 -m-> MID-S.up.q80` | — | tennessee_eastman |
| TIT02:upq20 | l | TIT02:downq80 | 3.637 | 3.657 | 52 | True | `MID.up.q20 -l-> MID.down.q80 [same role]` | — | tennessee_eastman, building_59 |
| TIT01:peak | l | FCV01Z:trough | 3.635 | 3.468 | 50 | True | `MID.peak -l-> MID-S.trough` | — | tennessee_eastman |
| TIT01:peak | l | TIT02:downq50 | 3.635 | 3.153 | 50 | True | `MID.peak -l-> MID.down.q50` | — | tennessee_eastman |
| FT02Z:downq20 | l | TIT02:downq50 | 3.632 | 2.416 | 34 | True | `MID-S.down.q20 -l-> MID.down.q50` | building_59 | tennessee_eastman |
| TIT02:upq20 | l | TIT02:downq50 | 3.629 | 2.707 | 51 | True | `MID.up.q20 -l-> MID.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| FCV02Z:upq80 | l | B4005:upq50 | 3.629 | 2.142 | 28 | False | `MID-S.up.q80 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| TIT02:upq50 | m | PIT02:downq90 | 3.626 | 3.69 | 25 | True | `MID.up.q50 -m-> MID.down.q90` | — | tennessee_eastman, building_59 |
| TIT01:trough | m | B4005:downq20 | 3.624 | 8.087 | 14 | True | `MID.trough -m-> MID-S.down.q20` | — | tennessee_eastman |
| B400B:upq80 | m | FCV03Z:peak | 3.624 | 3.311 | 10 | True | `MID-S.up.q80 -m-> MID.peak` | — | — |
| FCV03D:peak | m | TIT02:upq80 | 3.623 | 2.95 | 11 | False | `MID.peak -m-> MID.up.q80` | — | tennessee_eastman, building_59 |
| LCP01D:downq50 | m | LIT01:downq80 | 3.621 | 3.614 | 111 | True | `MID-S.down.q50 -m-> MID.down.q80` | — | tennessee_eastman |
| FT01:downq20 | l | FT03Z:trough | 3.619 | 1.841 | 14 | True | `MID.down.q20 -l-> MID.trough` | — | tennessee_eastman |
| FCV01D:upq10 | l | TIT02:downq20 | 3.616 | 2.715 | 33 | False | `MID-S.up.q10 -l-> MID.down.q20` | — | tennessee_eastman, building_59 |
| FCV02Z:downq50 | l | B4005:downq20 | 3.612 | 3.897 | 36 | True | `MID-S.down.q50 -l-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:upq80 | m | FCV02Z:upq80 | 3.601 | 2.706 | 10 | True | `MID.up.q80 -m-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| LIT01:downq80 | m | LCP01D:downq20 | 3.596 | 3.697 | 61 | True | `MID.down.q80 -m-> MID-S.down.q20` | tennessee_eastman | — |
| TIT01:trough | l | FCV02Z:upq80 | 3.594 | 4.201 | 38 | True | `MID.trough -l-> MID-S.up.q80` | — | tennessee_eastman |
| PIT02:downq10 | m | B4022:downq20 | 3.583 | 3.897 | 50 | True | `MID.down.q10 -m-> SLOW.down.q20` | building_59 | tennessee_eastman |
| PIT02:downq10 | m | B4022:upq20 | 3.583 | 3.044 | 50 | True | `MID.down.q10 -m-> SLOW.up.q20` | building_59 | tennessee_eastman |
| FT02:upq50 | l | TIT02:upq20 | 3.578 | 3.828 | 42 | False | `MID-S.up.q50 -l-> MID.up.q20` | — | tennessee_eastman |
| FT02:upq50 | l | TIT02:upq50 | 3.578 | 3.828 | 42 | False | `MID-S.up.q50 -l-> MID.up.q50` | — | tennessee_eastman |
| FT02Z:upq50 | l | TIT02:upq20 | 3.578 | 3.828 | 42 | False | `MID-S.up.q50 -l-> MID.up.q20` | — | tennessee_eastman |
| FT02Z:upq50 | l | TIT02:upq50 | 3.578 | 3.828 | 42 | False | `MID-S.up.q50 -l-> MID.up.q50` | — | tennessee_eastman |
| B400B:upq50 | l | TIT02:upq20 | 3.578 | 3.828 | 42 | False | `MID-S.up.q50 -l-> MID.up.q20` | — | tennessee_eastman |
| B400B:upq50 | l | TIT02:upq50 | 3.578 | 3.828 | 42 | False | `MID-S.up.q50 -l-> MID.up.q50` | — | tennessee_eastman |
| B4022:downq50 | l | FT02Z:upq20 | 3.576 | 5.869 | 24 | False | `SLOW.down.q50 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| TIT02:downq20 | l | TIT02:upq20 | 3.574 | 3.952 | 55 | True | `MID.down.q20 -l-> MID.up.q20 [same role]` | — | tennessee_eastman, building_59 |
| TIT02:downq20 | l | TIT02:upq50 | 3.574 | 3.952 | 55 | True | `MID.down.q20 -l-> MID.up.q50 [same role]` | building_59 | tennessee_eastman |
| B4005:downq20 | l | FCV01Z:trough | 3.572 | 3.302 | 34 | True | `MID-S.down.q20 -l-> MID-S.trough` | — | tennessee_eastman |
| FCV01Z:peak | l | FCV01Z:trough | 3.571 | 2.378 | 47 | True | `MID-S.peak -l-> MID-S.trough [same role]` | — | tennessee_eastman, fingrid |
| B4005:upq50 | l | TIT02:upq50 | 3.567 | 3.87 | 42 | False | `MID-S.up.q50 -l-> MID.up.q50` | — | tennessee_eastman, building_59 |
| B3004:upq80 | s | B4022:downq50 | 3.565 | 3.314 | 5 | False | `SET.up.q80 -s-> SLOW.down.q50` | — | tennessee_eastman |
| TIT02:upq80 | l | FCV01Z:trough | 3.558 | 3.552 | 49 | True | `MID.up.q80 -l-> MID-S.trough` | — | tennessee_eastman |
| TIT02:downq50 | l | TIT02:upq20 | 3.556 | 1.876 | 48 | False | `MID.down.q50 -l-> MID.up.q20 [same role]` | building_59 | tennessee_eastman |
| TIT01:trough | l | B4005:upq20 | 3.555 | 4.845 | 44 | True | `MID.trough -l-> MID-S.up.q20` | — | tennessee_eastman |
| B4022:downq20 | l | FCV01D:upq10 | 3.554 | 2.919 | 18 | True | `SLOW.down.q20 -l-> MID-S.up.q10` | building_59 | tennessee_eastman |
| B3004:upq80 | l | FCV02Z:downq50 | 3.552 | 1.681 | 10 | True | `SET.up.q80 -l-> MID-S.down.q50` | — | tennessee_eastman |
| TIT02:upq50 | l | FCV01Z:trough | 3.541 | 3.674 | 49 | True | `MID.up.q50 -l-> MID-S.trough` | — | tennessee_eastman |
| FT02:upq50 | l | B4005:downq20 | 3.541 | 3.497 | 35 | False | `MID-S.up.q50 -l-> MID-S.down.q20` | — | tennessee_eastman |
| FT02Z:upq50 | l | B4005:downq20 | 3.541 | 3.497 | 35 | False | `MID-S.up.q50 -l-> MID-S.down.q20` | — | tennessee_eastman |
| B2004:downq20 | m | B4022:upq20 | 3.538 | 3.102 | 8 | True | `SET.down.q20 -m-> SLOW.up.q20` | — | building_59 |
| FCV02Z:downq20 | l | B4005:upq20 | 3.536 | 4.808 | 19 | True | `MID-S.down.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| PIT02:upq10 | l | FCV01D:upq10 | 3.533 | 3.209 | 32 | True | `MID.up.q10 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| FCV02Z:downq20 | l | B400B:upq20 | 3.532 | 3.578 | 17 | True | `MID-S.down.q20 -l-> MID-S.up.q20` | — | tennessee_eastman |
| FCV02Z:downq20 | l | FT02:upq20 | 3.532 | 3.578 | 17 | True | `MID-S.down.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FCV02Z:downq20 | l | FT02Z:upq20 | 3.532 | 3.578 | 17 | True | `MID-S.down.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:downq20 | l | FT01:upq20 | 3.53 | 2.543 | 15 | True | `MID.down.q20 -l-> MID.up.q20` | — | tennessee_eastman, building_59 |
| TIT02:downq20 | l | FCV01D:downq10 | 3.528 | 4.086 | 40 | True | `MID.down.q20 -l-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| LIT01:upq80 | m | LCP01D:downq20 | 3.526 | 3.517 | 60 | True | `MID.up.q80 -m-> MID-S.down.q20` | — | tennessee_eastman |
| FCV02Z:upq80 | l | TIT02:downq50 | 3.525 | 2.715 | 31 | True | `MID-S.up.q80 -l-> MID.down.q50` | — | tennessee_eastman, building_59 |
| FCV01D:downq10 | s | LCV01D:downq80 | 3.525 | 6.306 | 6 | True | `MID-S.down.q10 -s-> MID.down.q80` | — | tennessee_eastman, building_59 |
| PIT02:upq10 | l | B4005:upq50 | 3.524 | 3.594 | 38 | True | `MID.up.q10 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| FCV02Z:downq50 | l | FCV02Z:upq80 | 3.524 | 3.861 | 30 | False | `MID-S.down.q50 -l-> MID-S.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| LCP01D:downq80 | s | PIT01:peak | 3.521 | 3.767 | 22 | True | `MID-S.down.q80 -s-> MID.peak` | — | tennessee_eastman |
| B4022:downq50 | m | B400B:downq20 | 3.521 | 4.961 | 21 | True | `SLOW.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman |
| B4022:downq50 | m | FT02:downq20 | 3.521 | 4.41 | 21 | True | `SLOW.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B4022:downq50 | m | FT02Z:downq20 | 3.521 | 4.686 | 21 | True | `SLOW.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| PIT02:downq90 | m | B4005:upq50 | 3.52 | 6.416 | 15 | False | `MID.down.q90 -m-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| B4022:downq50 | m | FCV02Z:upq80 | 3.517 | 3.758 | 20 | True | `SLOW.down.q50 -m-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| FT02Z:upq50 | l | TIT02:upq80 | 3.516 | 3.762 | 42 | False | `MID-S.up.q50 -l-> MID.up.q80` | — | tennessee_eastman |
| B400B:upq50 | l | TIT02:upq80 | 3.516 | 3.762 | 42 | False | `MID-S.up.q50 -l-> MID.up.q80` | — | tennessee_eastman |
| TIT01:trough | l | PIT02:upq10 | 3.513 | 4.154 | 77 | True | `MID.trough -l-> MID.up.q10` | — | tennessee_eastman |
| TIT02:downq20 | l | TIT02:upq80 | 3.512 | 3.884 | 55 | True | `MID.down.q20 -l-> MID.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| B2004:downq20 | l | PIT02:upq10 | 3.512 | 2.885 | 14 | True | `SET.down.q20 -l-> MID.up.q10` | — | building_59 |
| FCV01Z:trough | l | TIT02:downq20 | 3.508 | 2.719 | 44 | False | `MID-S.trough -l-> MID.down.q20` | — | tennessee_eastman |
| LCV01D:downq50 | s | LCV01D:upq50 | 3.505 | 2.33 | 61 | True | `MID.down.q50 -s-> MID.up.q50 [same role]` | — | tennessee_eastman, building_59 |
| PIT02:upq10 | l | B400B:upq50 | 3.502 | 3.667 | 37 | True | `MID.up.q10 -l-> MID-S.up.q50` | — | tennessee_eastman |
| PIT02:upq10 | l | FT02:upq50 | 3.502 | 3.667 | 37 | True | `MID.up.q10 -l-> MID-S.up.q50` | — | tennessee_eastman |
| PIT02:upq10 | l | FT02Z:upq50 | 3.502 | 3.667 | 37 | True | `MID.up.q10 -l-> MID-S.up.q50` | — | tennessee_eastman |
| LCV01Z:downq80 | m | B4005:downq20 | 3.501 | 1.54 | 10 | True | `MID.down.q80 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B4022:upq20 | m | B4022:downq50 | 3.494 | 4.45 | 94 | True | `SLOW.up.q20 -m-> SLOW.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| B4022:downq80 | m | B2016:trough | 3.491 | 2.154 | 30 | True | `SLOW.down.q80 -m-> MID.trough` | — | tennessee_eastman |
| TIT02:upq20 | l | FCV01Z:trough | 3.487 | 3.552 | 49 | True | `MID.up.q20 -l-> MID-S.trough` | — | tennessee_eastman |
| LIT01:downq80 | s | FT01:upq50 | 3.487 | 5.045 | 5 | True | `MID.down.q80 -s-> MID.up.q50` | — | tennessee_eastman |
| PCV01D:peak | m | B2016:trough | 3.485 | 2.479 | 35 | True | `MID-S.peak -m-> MID.trough` | — | — |
| LCP01D:upq80 | m | LIT01:downq50 | 3.484 | 3.427 | 85 | True | `MID-S.up.q80 -m-> MID.down.q50` | tennessee_eastman | — |
| LCV01Z:upq20 | m | LCV01D:upq20 | 3.483 | 2.68 | 73 | True | `MID.up.q20 -m-> MID.up.q20` | — | tennessee_eastman, building_59 |
| B3004:upq80 | l | B4022:upq50 | 3.481 | 3.051 | 36 | True | `SET.up.q80 -l-> SLOW.up.q50` | — | tennessee_eastman |
| B3004:upq80 | l | B4022:downq50 | 3.481 | 2.899 | 36 | True | `SET.up.q80 -l-> SLOW.down.q50` | — | tennessee_eastman |
| B3004:upq80 | l | B4005:upq50 | 3.481 | 1.648 | 10 | True | `SET.up.q80 -l-> MID-S.up.q50` | — | tennessee_eastman |
| TIT02:downq20 | l | B400B:downq50 | 3.477 | 3.503 | 46 | True | `MID.down.q20 -l-> MID-S.down.q50` | — | tennessee_eastman |
| TIT02:downq20 | l | FT02:downq50 | 3.477 | 3.503 | 46 | True | `MID.down.q20 -l-> MID-S.down.q50` | — | tennessee_eastman |
| TIT02:downq20 | l | FT02Z:downq50 | 3.477 | 3.503 | 46 | True | `MID.down.q20 -l-> MID-S.down.q50` | — | tennessee_eastman |
| B4022:downq20 | m | FT02:upq20 | 3.476 | 4.216 | 23 | True | `SLOW.down.q20 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B4022:downq20 | m | FT02Z:upq20 | 3.476 | 4.518 | 23 | True | `SLOW.down.q20 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B2004:downq20 | l | FT02:downq20 | 3.471 | 3.802 | 7 | False | `SET.down.q20 -l-> MID-S.down.q20` | — | building_59 |
| LIT01:downq20 | s | LCV01D:upq80 | 3.468 | 2.193 | 29 | False | `MID.down.q20 -s-> MID.up.q80` | — | tennessee_eastman |
| B4005:downq20 | l | TIT02:downq50 | 3.467 | 2.476 | 33 | True | `MID-S.down.q20 -l-> MID.down.q50` | — | tennessee_eastman, building_59 |
| FT01:upq80 | s | LCV01D:upq80 | 3.46 | 4.097 | 14 | True | `MID.up.q80 -s-> MID.up.q80` | — | tennessee_eastman, building_59 |
| B3004:downq80 | l | B4005:downq20 | 3.46 | 2.262 | 9 | False | `SET.down.q80 -l-> MID-S.down.q20` | — | tennessee_eastman |
| LCV01Z:downq50 | s | FT03Z:trough | 3.46 | 8.16 | 5 | False | `MID.down.q50 -s-> MID.trough` | — | tennessee_eastman |
| B4005:upq50 | l | B400B:downq50 | 3.458 | 3.809 | 35 | False | `MID-S.up.q50 -l-> MID-S.down.q50` | — | tennessee_eastman |
| B4005:upq50 | l | FT02:downq50 | 3.458 | 3.809 | 35 | False | `MID-S.up.q50 -l-> MID-S.down.q50` | — | tennessee_eastman |
| B4005:upq50 | l | FT02Z:downq50 | 3.458 | 3.809 | 35 | False | `MID-S.up.q50 -l-> MID-S.down.q50` | — | tennessee_eastman |
| B4005:upq50 | l | FCV02Z:upq50 | 3.458 | 3.463 | 35 | False | `MID-S.up.q50 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| B4022:upq50 | l | B4022:upq20 | 3.456 | 4.191 | 107 | True | `SLOW.up.q50 -l-> SLOW.up.q20 [same role]` | — | tennessee_eastman, building_59 |
| FCV01Z:trough | l | B4005:upq50 | 3.454 | 3.543 | 38 | False | `MID-S.trough -l-> MID-S.up.q50` | — | tennessee_eastman |
| FT02Z:downq80 | s | FT02Z:upq80 | 3.453 | 21.207 | 6 | False | `MID-S.down.q80 -s-> MID-S.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| B2004:downq20 | l | B4022:downq20 | 3.452 | 4.153 | 34 | True | `SET.down.q20 -l-> SLOW.down.q20` | — | building_59 |
| LIT01:upq50 | s | FCV03Z:trough | 3.449 | 1.977 | 10 | True | `MID.up.q50 -s-> MID.trough` | — | — |
| FCV01D:downq10 | m | B2016:peak | 3.447 | 2.574 | 20 | False | `MID-S.down.q10 -m-> MID.peak` | — | tennessee_eastman |
| TIT02:downq20 | l | B400B:downq20 | 3.446 | 3.991 | 40 | True | `MID.down.q20 -l-> MID-S.down.q20` | — | tennessee_eastman |
| TIT02:downq20 | l | FT02:downq20 | 3.446 | 3.991 | 40 | True | `MID.down.q20 -l-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| TIT02:downq20 | l | FT02Z:downq20 | 3.446 | 3.991 | 40 | True | `MID.down.q20 -l-> MID-S.down.q20` | building_59 | tennessee_eastman |
| LIT01:downq80 | m | LCP01D:downq50 | 3.438 | 3.31 | 96 | True | `MID.down.q80 -m-> MID-S.down.q50` | tennessee_eastman | — |
| FCV01Z:trough | l | B400B:upq50 | 3.432 | 3.615 | 37 | False | `MID-S.trough -l-> MID-S.up.q50` | — | tennessee_eastman |
| FCV01Z:trough | l | FT02:upq50 | 3.432 | 3.615 | 37 | False | `MID-S.trough -l-> MID-S.up.q50` | — | tennessee_eastman |
| FCV01Z:trough | l | FT02Z:upq50 | 3.432 | 3.615 | 37 | False | `MID-S.trough -l-> MID-S.up.q50` | — | tennessee_eastman |
| LCV01D:upq20 | m | FT01:upq20 | 3.431 | 2.184 | 21 | True | `MID.up.q20 -m-> MID.up.q20` | — | tennessee_eastman, building_59 |
| B3005:downq90 | l | LCV01Z:downq50 | 3.431 | 2.513 | 11 | False | `SET.down.q90 -l-> MID.down.q50` | — | tennessee_eastman, building_59 |
| LCV01D:upq20 | s | FCV03Z:trough | 3.431 | 3.619 | 8 | False | `MID.up.q20 -s-> MID.trough` | — | building_59 |
| LCP01D:upq80 | l | LIT01:upq80 | 3.43 | 3.568 | 163 | True | `MID-S.up.q80 -l-> MID.up.q80` | — | tennessee_eastman |
| LCV01Z:downq80 | m | FCV02Z:upq50 | 3.43 | 2.514 | 10 | False | `MID.down.q80 -m-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| B2004:upq50 | l | FCV02Z:downq80 | 3.43 | 3.102 | 8 | False | `SET.up.q50 -l-> MID-S.down.q80` | — | — |
| B4005:upq50 | l | B4005:downq20 | 3.429 | 3.181 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q20 [same role]` | — | tennessee_eastman, building_59 |
| LIT01:upq80 | m | LCP01D:downq50 | 3.427 | 3.602 | 96 | True | `MID.up.q80 -m-> MID-S.down.q50` | — | tennessee_eastman |
| TIT01:trough | l | B400B:upq20 | 3.427 | 5.007 | 38 | True | `MID.trough -l-> MID-S.up.q20` | — | tennessee_eastman |
| TIT01:trough | l | FT02:upq20 | 3.427 | 4.607 | 38 | True | `MID.trough -l-> MID-S.up.q20` | — | tennessee_eastman |
| TIT01:trough | l | FT02Z:upq20 | 3.427 | 4.807 | 38 | True | `MID.trough -l-> MID-S.up.q20` | — | tennessee_eastman |
| B400B:downq20 | l | B4005:upq50 | 3.427 | 2.364 | 28 | False | `MID-S.down.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| LIT01:upq80 | m | LIT01:downq80 | 3.425 | 2.88 | 179 | True | `MID.up.q80 -m-> MID.down.q80 [same role]` | tennessee_eastman | — |
| FCV01Z:peak | l | B400B:upq20 | 3.425 | 2.477 | 34 | True | `MID-S.peak -l-> MID-S.up.q20` | — | tennessee_eastman |
| FCV01Z:peak | l | FT02:upq20 | 3.425 | 2.477 | 34 | True | `MID-S.peak -l-> MID-S.up.q20` | — | tennessee_eastman |
| FCV01Z:peak | l | FT02Z:upq20 | 3.425 | 2.477 | 34 | True | `MID-S.peak -l-> MID-S.up.q20` | — | tennessee_eastman |
| B4005:upq50 | l | TIT02:upq80 | 3.422 | 3.51 | 41 | False | `MID-S.up.q50 -l-> MID.up.q80` | — | tennessee_eastman, building_59 |
| FT02:downq20 | l | B4005:upq50 | 3.418 | 2.326 | 28 | False | `MID-S.down.q20 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| B400B:downq80 | l | FCV01D:downq10 | 3.418 | 3.311 | 25 | True | `MID-S.down.q80 -l-> MID-S.down.q10` | — | tennessee_eastman |
| FCV03D:trough | m | B2016:peak | 3.416 | 2.129 | 31 | True | `MID.trough -m-> MID.peak` | — | tennessee_eastman |
| FT02:upq80 | m | FCV01Z:peak | 3.416 | 4.403 | 12 | False | `MID-S.up.q80 -m-> MID-S.peak` | — | tennessee_eastman |
| TIT02:downq20 | l | TIT01:trough | 3.415 | 3.52 | 59 | True | `MID.down.q20 -l-> MID.trough` | — | tennessee_eastman |
| FT02:upq50 | l | TIT01:trough | 3.414 | 3.409 | 45 | True | `MID-S.up.q50 -l-> MID.trough` | — | tennessee_eastman |
| FT02Z:upq50 | l | TIT01:trough | 3.414 | 3.409 | 45 | True | `MID-S.up.q50 -l-> MID.trough` | — | tennessee_eastman |
| B400B:upq50 | l | TIT01:trough | 3.414 | 3.409 | 45 | True | `MID-S.up.q50 -l-> MID.trough` | — | tennessee_eastman |
| FCV02Z:upq80 | l | FCV01Z:trough | 3.411 | 3.55 | 30 | True | `MID-S.up.q80 -l-> MID-S.trough` | — | tennessee_eastman |
| B4022:downq20 | l | B4022:downq50 | 3.41 | 3.697 | 74 | True | `SLOW.down.q20 -l-> SLOW.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| TIT01:trough | l | TIT02:downq80 | 3.41 | 3.118 | 51 | True | `MID.trough -l-> MID.down.q80` | — | tennessee_eastman |
| FT02Z:downq20 | l | B4005:upq50 | 3.41 | 2.295 | 28 | False | `MID-S.down.q20 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| TIT02:downq20 | l | B4005:downq50 | 3.408 | 3.432 | 46 | True | `MID.down.q20 -l-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| LCV01D:upq80 | m | LCV01D:downq80 | 3.407 | 3.47 | 154 | True | `MID.up.q80 -m-> MID.down.q80 [same role]` | tennessee_eastman | building_59 |
| LCP01D:upq50 | m | LIT01:upq20 | 3.401 | 2.801 | 78 | True | `MID-S.up.q50 -m-> MID.up.q20` | — | tennessee_eastman |
| LIT01:upq50 | m | LIT01:downq50 | 3.4 | 3.382 | 268 | True | `MID.up.q50 -m-> MID.down.q50 [same role]` | tennessee_eastman | — |
| LIT01:upq50 | m | LIT01:downq80 | 3.394 | 3.291 | 221 | True | `MID.up.q50 -m-> MID.down.q80 [same role]` | tennessee_eastman | — |
| B4005:downq20 | l | B4022:upq50 | 3.394 | 3.529 | 102 | True | `MID-S.down.q20 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| B4022:downq20 | m | B4022:upq50 | 3.394 | 4.461 | 94 | True | `SLOW.down.q20 -m-> SLOW.up.q50 [same role]` | tennessee_eastman | building_59 |
| PIT02:upq10 | l | FCV02Z:downq80 | 3.393 | 4.93 | 30 | True | `MID.up.q10 -l-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| LCP01D:downq80 | l | LIT01:downq20 | 3.392 | 3.115 | 116 | True | `MID-S.down.q80 -l-> MID.down.q20` | — | tennessee_eastman |
| FT02:downq80 | l | FCV01D:downq10 | 3.388 | 2.981 | 25 | True | `MID-S.down.q80 -l-> MID-S.down.q10` | building_59 | tennessee_eastman |
| TIT02:downq80 | l | FCV02Z:downq50 | 3.387 | 2.686 | 38 | True | `MID.down.q80 -l-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| FCV01Z:peak | l | FCV02Z:downq80 | 3.381 | 2.361 | 32 | False | `MID-S.peak -l-> MID-S.down.q80` | — | tennessee_eastman |
| FCV02Z:downq50 | l | TIT02:upq20 | 3.38 | 3.282 | 40 | True | `MID-S.down.q50 -l-> MID.up.q20` | — | tennessee_eastman, building_59 |
| FCV02Z:downq50 | l | TIT02:upq50 | 3.38 | 3.282 | 40 | True | `MID-S.down.q50 -l-> MID.up.q50` | — | tennessee_eastman, building_59 |
| LIT01:downq20 | s | LCV01Z:upq50 | 3.375 | 4.376 | 11 | True | `MID.down.q20 -s-> MID.up.q50` | — | tennessee_eastman |
| FT02:upq50 | l | B400B:downq50 | 3.369 | 3.768 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q50` | — | tennessee_eastman |
| FT02:upq50 | l | FT02:downq50 | 3.369 | 3.768 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q50 [same role]` | — | tennessee_eastman |
| FT02:upq50 | l | FT02Z:downq50 | 3.369 | 3.768 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q50` | — | tennessee_eastman |
| FT02Z:upq50 | l | B400B:downq50 | 3.369 | 3.768 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q50` | — | tennessee_eastman |
| FT02Z:upq50 | l | FT02:downq50 | 3.369 | 3.768 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q50` | — | tennessee_eastman |
| B400B:upq50 | l | B400B:downq50 | 3.369 | 3.768 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q50 [same role]` | — | tennessee_eastman |
| B400B:upq50 | l | FT02:downq50 | 3.369 | 3.768 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q50` | — | tennessee_eastman |
| B400B:upq50 | l | FT02Z:downq50 | 3.369 | 3.768 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q50` | — | tennessee_eastman |
| TIT02:upq20 | l | FCV02Z:upq80 | 3.364 | 3.763 | 34 | True | `MID.up.q20 -l-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| TIT01:trough | m | PIT02:downq90 | 3.362 | 3.321 | 23 | True | `MID.trough -m-> MID.down.q90` | — | tennessee_eastman |
| LCV01Z:downq20 | l | FT03Z:trough | 3.361 | 2.492 | 17 | False | `MID.down.q20 -l-> MID.trough` | — | tennessee_eastman |
| FT02:upq50 | l | FCV01D:downq10 | 3.353 | 3.197 | 29 | False | `MID-S.up.q50 -l-> MID-S.down.q10` | — | tennessee_eastman |
| FT02Z:upq50 | l | FCV01D:downq10 | 3.353 | 3.197 | 29 | False | `MID-S.up.q50 -l-> MID-S.down.q10` | — | tennessee_eastman |
| B400B:upq50 | l | FCV01D:downq10 | 3.353 | 3.197 | 29 | False | `MID-S.up.q50 -l-> MID-S.down.q10` | — | tennessee_eastman |
| PIT02:downq10 | l | B3004:downq50 | 3.353 | 2.742 | 12 | False | `MID.down.q10 -l-> SET.down.q50` | — | tennessee_eastman |
| B2016:peak | m | PCV01Z:peak | 3.343 | 1.742 | 39 | True | `MID.peak -m-> MID-S.peak` | — | — |
| TIT02:downq20 | l | FCV02Z:upq80 | 3.343 | 3.924 | 37 | False | `MID.down.q20 -l-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| FCV02Z:downq50 | l | B400B:downq50 | 3.342 | 3.524 | 34 | True | `MID-S.down.q50 -l-> MID-S.down.q50` | — | tennessee_eastman |
| FCV02Z:downq50 | l | FT02:downq50 | 3.342 | 3.524 | 34 | True | `MID-S.down.q50 -l-> MID-S.down.q50` | — | tennessee_eastman |
| FCV02Z:downq50 | l | FCV02Z:upq50 | 3.342 | 3.524 | 34 | True | `MID-S.down.q50 -l-> MID-S.up.q50 [same role]` | — | tennessee_eastman, building_59 |
| FT02:downq80 | s | FT02Z:upq80 | 3.341 | 20.913 | 6 | False | `MID-S.down.q80 -s-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| PIT01:trough | s | LCV01Z:upq80 | 3.34 | 3.348 | 16 | False | `MID.trough -s-> MID.up.q80` | — | tennessee_eastman |
| TIT01:trough | l | B400B:downq20 | 3.337 | 5.007 | 37 | True | `MID.trough -l-> MID-S.down.q20` | — | tennessee_eastman |
| TIT01:trough | l | FT02:downq20 | 3.337 | 4.406 | 37 | True | `MID.trough -l-> MID-S.down.q20` | — | tennessee_eastman |
| TIT01:trough | l | FT02Z:downq20 | 3.337 | 4.607 | 37 | True | `MID.trough -l-> MID-S.down.q20` | — | tennessee_eastman |
| B4022:upq80 | m | B2016:trough | 3.335 | 1.918 | 27 | True | `SLOW.up.q80 -m-> MID.trough` | — | tennessee_eastman |
| LCV01Z:upq50 | m | FCV03Z:peak | 3.335 | 2.555 | 15 | False | `MID.up.q50 -m-> MID.peak` | — | building_59 |
| TIT01:trough | l | FCV01Z:trough | 3.334 | 3.173 | 49 | True | `MID.trough -l-> MID-S.trough` | — | tennessee_eastman |
| LCV01Z:upq50 | m | FT01Z:trough | 3.331 | 1.689 | 17 | True | `MID.up.q50 -m-> MID.trough` | — | tennessee_eastman |
| B4022:downq20 | m | FCV02Z:upq80 | 3.329 | 2.843 | 21 | True | `SLOW.down.q20 -m-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| B4005:upq50 | l | TIT01:trough | 3.328 | 3.446 | 44 | True | `MID-S.up.q50 -l-> MID.trough` | — | tennessee_eastman |
| LCP01D:downq20 | m | LIT01:downq20 | 3.326 | 3.478 | 45 | False | `MID-S.down.q20 -m-> MID.down.q20` | tennessee_eastman | — |
| LCV01D:downq50 | s | FT03:trough | 3.326 | 4.407 | 9 | True | `MID.down.q50 -s-> MID.trough` | — | — |
| FCV02Z:downq50 | l | FCV01D:downq10 | 3.325 | 3.426 | 29 | True | `MID-S.down.q50 -l-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| FCV02Z:downq50 | l | TIT02:upq80 | 3.321 | 3.225 | 40 | True | `MID-S.down.q50 -l-> MID.up.q80` | — | tennessee_eastman, building_59 |
| LCV01Z:downq50 | s | LCV01Z:downq20 | 3.321 | 5.875 | 12 | True | `MID.down.q50 -s-> MID.down.q20 [same role]` | tennessee_eastman, building_59 | — |
| B2004:upq50 | l | LCV01Z:downq50 | 3.317 | 2.399 | 20 | False | `SET.up.q50 -l-> MID.down.q50` | — | — |
| FT02Z:downq80 | m | B400B:downq80 | 3.315 | 5.536 | 18 | False | `MID-S.down.q80 -m-> MID-S.down.q80` | — | tennessee_eastman |
| PCV01D:trough | m | PCV01D:peak | 3.314 | 2.761 | 15 | True | `MID-S.trough -m-> MID-S.peak [same role]` | — | fingrid |
| FCV02Z:upq80 | l | B4022:upq50 | 3.313 | 3.571 | 92 | True | `MID-S.up.q80 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| FCV02Z:upq80 | l | B4022:downq50 | 3.313 | 3.438 | 92 | True | `MID-S.up.q80 -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| LCP01D:downq20 | m | LCV01D:downq80 | 3.313 | 2.259 | 46 | False | `MID-S.down.q20 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| PIT02:upq10 | l | FCV02Z:downq50 | 3.312 | 3.667 | 35 | True | `MID.up.q10 -l-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| TIT02:upq50 | m | FCV02Z:upq80 | 3.308 | 10.201 | 11 | True | `MID.up.q50 -m-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| B4022:downq50 | m | B4005:downq20 | 3.304 | 3.457 | 22 | True | `SLOW.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B400B:upq50 | m | LCV01Z:downq80 | 3.303 | 3.153 | 10 | False | `MID-S.up.q50 -m-> MID.down.q80` | — | tennessee_eastman |
| FT02:upq50 | l | B4005:downq50 | 3.302 | 3.693 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q50` | — | tennessee_eastman |
| FT02Z:upq50 | l | B4005:downq50 | 3.302 | 3.693 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q50` | — | tennessee_eastman |
| B400B:upq50 | l | B4005:downq50 | 3.302 | 3.693 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q50` | — | tennessee_eastman |
| TIT02:downq50 | l | TIT01:trough | 3.299 | 2.042 | 50 | True | `MID.down.q50 -l-> MID.trough` | — | tennessee_eastman |
| LCV01Z:downq20 | l | FT03:trough | 3.295 | 2.094 | 17 | False | `MID.down.q20 -l-> MID.trough` | — | — |
| FT01:downq20 | l | FT03:trough | 3.295 | 1.805 | 13 | True | `MID.down.q20 -l-> MID.trough` | — | — |
| FT02:downq20 | m | LCV01Z:downq80 | 3.295 | 2.072 | 9 | True | `MID-S.down.q20 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| B4005:upq50 | l | B4005:downq50 | 3.292 | 3.733 | 34 | False | `MID-S.up.q50 -l-> MID-S.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| FCV02Z:downq20 | l | FCV01Z:trough | 3.292 | 4.049 | 21 | True | `MID-S.down.q20 -l-> MID-S.trough` | — | tennessee_eastman |
| B2004:upq50 | m | B4022:upq20 | 3.288 | 2.801 | 9 | False | `SET.up.q50 -m-> SLOW.up.q20` | — | — |
| FCV01Z:peak | m | FT01:downq50 | 3.287 | 3.157 | 8 | False | `MID-S.peak -m-> MID.down.q50` | — | tennessee_eastman |
| ST_PT01:trough | s | FT01:upq80 | 3.286 | 2.052 | 10 | False | `MID.trough -s-> MID.up.q80` | — | tennessee_eastman |
| FT01:upq20 | m | LCV01D:downq20 | 3.28 | 1.874 | 28 | True | `MID.up.q20 -m-> MID.down.q20` | — | tennessee_eastman, building_59 |
| FT02Z:downq80 | m | FT02:downq80 | 3.28 | 5.19 | 19 | False | `MID-S.down.q80 -m-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| FCV02Z:downq50 | l | B4005:downq50 | 3.275 | 3.453 | 34 | True | `MID-S.down.q50 -l-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| FT02Z:upq50 | l | FCV02Z:upq50 | 3.27 | 3.425 | 33 | False | `MID-S.up.q50 -l-> MID-S.up.q50` | — | tennessee_eastman |
| B400B:upq50 | l | FCV02Z:upq50 | 3.27 | 3.425 | 33 | False | `MID-S.up.q50 -l-> MID-S.up.q50` | — | tennessee_eastman |
| FCV02Z:downq20 | l | FCV02Z:downq80 | 3.269 | 2.814 | 15 | True | `MID-S.down.q20 -l-> MID-S.down.q80 [same role]` | — | tennessee_eastman, building_59 |
| LCP01D:upq20 | l | LIT01:upq50 | 3.266 | 3.149 | 176 | True | `MID-S.up.q20 -l-> MID.up.q50` | — | tennessee_eastman |
| LCV01Z:downq20 | m | B400B:upq80 | 3.266 | 3.73 | 19 | True | `MID.down.q20 -m-> MID-S.up.q80` | — | tennessee_eastman |
| B400B:downq20 | l | B4022:upq50 | 3.263 | 3.415 | 96 | True | `MID-S.down.q20 -l-> SLOW.up.q50` | — | tennessee_eastman |
| FT02:upq50 | l | TIT01:peak | 3.263 | 3.147 | 43 | False | `MID-S.up.q50 -l-> MID.peak` | — | tennessee_eastman |
| FT02Z:upq50 | l | TIT01:peak | 3.263 | 3.147 | 43 | False | `MID-S.up.q50 -l-> MID.peak` | — | tennessee_eastman |
| B4005:downq20 | l | B4022:downq50 | 3.261 | 3.66 | 98 | True | `MID-S.down.q20 -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| LIT01:upq80 | l | LIT01:upq20 | 3.258 | 2.862 | 164 | True | `MID.up.q80 -l-> MID.up.q20 [same role]` | — | tennessee_eastman |
| FT02:downq20 | l | B4022:upq50 | 3.255 | 3.424 | 96 | True | `MID-S.down.q20 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| LIT01:upq20 | m | LIT01:downq80 | 3.249 | 3.185 | 146 | True | `MID.up.q20 -m-> MID.down.q80 [same role]` | tennessee_eastman | — |
| B2004:downq20 | l | B4022:upq20 | 3.249 | 3.633 | 32 | True | `SET.down.q20 -l-> SLOW.up.q20` | — | building_59 |
| FT02Z:downq20 | l | B4022:upq50 | 3.248 | 3.379 | 96 | True | `MID-S.down.q20 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| B400B:downq20 | l | B400B:upq50 | 3.247 | 2.413 | 26 | False | `MID-S.down.q20 -l-> MID-S.up.q50 [same role]` | — | tennessee_eastman |
| B400B:downq20 | l | FT02:upq50 | 3.247 | 2.413 | 26 | False | `MID-S.down.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| B400B:downq20 | l | FT02Z:upq50 | 3.247 | 2.413 | 26 | False | `MID-S.down.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| B3004:upq20 | l | PCV01Z:trough | 3.247 | 2.573 | 9 | True | `SET.up.q20 -l-> MID-S.trough` | — | — |
| TIT02:downq20 | l | B4005:downq20 | 3.241 | 3.575 | 42 | True | `MID.down.q20 -l-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| PIT02:downq90 | l | FCV01D:upq10 | 3.241 | 3.281 | 34 | True | `MID.down.q90 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| FT02:downq20 | l | B400B:upq50 | 3.238 | 2.373 | 26 | False | `MID-S.down.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| FT02:downq20 | l | FT02:upq50 | 3.238 | 2.373 | 26 | False | `MID-S.down.q20 -l-> MID-S.up.q50 [same role]` | — | tennessee_eastman |
| FT02:downq20 | l | FT02Z:upq50 | 3.238 | 2.373 | 26 | False | `MID-S.down.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| B4022:downq50 | m | FCV02Z:upq50 | 3.237 | 2.177 | 22 | True | `SLOW.down.q50 -m-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| B400B:upq50 | l | FCV02Z:downq20 | 3.237 | 2.238 | 20 | False | `MID-S.up.q50 -l-> MID-S.down.q20` | — | tennessee_eastman |
| LCV01D:upq20 | s | FCV03D:peak | 3.237 | 2.429 | 9 | False | `MID.up.q20 -s-> MID.peak` | — | tennessee_eastman, building_59 |
| LCV01Z:upq50 | s | LCV01D:downq50 | 3.231 | 2.565 | 36 | True | `MID.up.q50 -s-> MID.down.q50` | tennessee_eastman | building_59 |
| FT02Z:downq20 | l | B400B:upq50 | 3.231 | 2.342 | 26 | False | `MID-S.down.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| FT02Z:downq20 | l | FT02:upq50 | 3.231 | 2.342 | 26 | False | `MID-S.down.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| FT02Z:downq20 | l | FT02Z:upq50 | 3.231 | 2.342 | 26 | False | `MID-S.down.q20 -l-> MID-S.up.q50 [same role]` | — | tennessee_eastman |
| B400B:upq80 | l | FCV01D:downq10 | 3.23 | 3.126 | 24 | False | `MID-S.up.q80 -l-> MID-S.down.q10` | — | tennessee_eastman |
| ST_PT01:trough | s | FT01Z:peak | 3.229 | 2.83 | 19 | True | `MID.trough -s-> MID.peak` | — | tennessee_eastman |
| B4005:upq50 | l | FCV01D:downq10 | 3.227 | 3.232 | 28 | False | `MID-S.up.q50 -l-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| ST_PO:trough | s | FCV02Z:upq80 | 3.227 | 2.091 | 10 | True | `MID.trough -s-> MID-S.up.q80` | — | — |
| FT02:upq20 | m | B4022:downq20 | 3.224 | 3.791 | 20 | True | `MID-S.up.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:downq20 | m | LCV01D:upq20 | 3.223 | 3.292 | 67 | True | `MID.down.q20 -m-> MID.up.q20` | — | tennessee_eastman, building_59 |
| TIT02:upq80 | l | B3004:upq50 | 3.219 | 1.607 | 14 | True | `MID.up.q80 -l-> SET.up.q50` | — | tennessee_eastman |
| LIT01:upq80 | s | FCV03Z:trough | 3.213 | 4.138 | 6 | True | `MID.up.q80 -s-> MID.trough` | — | — |
| LIT01:upq50 | m | LCP01D:upq50 | 3.209 | 3.869 | 112 | True | `MID.up.q50 -m-> MID-S.up.q50` | — | tennessee_eastman |
| PCV01Z:peak | m | B4022:upq20 | 3.209 | 1.541 | 39 | False | `MID-S.peak -m-> SLOW.up.q20` | — | — |
| FT02Z:upq80 | l | FCV01D:downq10 | 3.207 | 2.885 | 24 | False | `MID-S.up.q80 -l-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| TIT02:upq50 | l | B3004:upq50 | 3.204 | 1.586 | 14 | True | `MID.up.q50 -l-> SET.up.q50` | — | tennessee_eastman |
| B400B:upq80 | l | FCV02Z:downq20 | 3.203 | 3.283 | 17 | False | `MID-S.up.q80 -l-> MID-S.down.q20` | — | tennessee_eastman |
| FCV02Z:upq80 | l | PIT02:downq10 | 3.202 | 3.921 | 42 | True | `MID-S.up.q80 -l-> MID.down.q10` | — | tennessee_eastman, building_59 |
| B3004:downq80 | l | FCV03Z:peak | 3.194 | 2.088 | 9 | False | `SET.down.q80 -l-> MID.peak` | — | — |
| TIT02:downq20 | l | TIT02:downq80 | 3.193 | 2.404 | 50 | True | `MID.down.q20 -l-> MID.down.q80 [same role]` | — | tennessee_eastman, building_59 |
| TIT02:downq20 | l | FCV02Z:upq20 | 3.193 | 2.959 | 25 | False | `MID.down.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| PCV01D:trough | m | TIT01:trough | 3.186 | 4.289 | 13 | True | `MID-S.trough -m-> MID.trough` | — | — |
| TIT02:downq20 | l | TIT01:peak | 3.183 | 3.52 | 55 | True | `MID.down.q20 -l-> MID.peak` | — | tennessee_eastman |
| B4022:downq20 | l | B4022:upq50 | 3.179 | 3.211 | 69 | True | `SLOW.down.q20 -l-> SLOW.up.q50 [same role]` | building_59 | tennessee_eastman |
| ST_TT01:upq90 | m | SIT02:trough | 3.179 | 1.866 | 3 | False | `MID.up.q90 -m-> MID.trough` | — | — |
| FT01:downq50 | s | LCV01D:downq50 | 3.178 | 2.716 | 16 | True | `MID.down.q50 -s-> MID.down.q50` | — | tennessee_eastman, building_59 |
| PIT02:downq10 | l | TIT02:downq20 | 3.176 | 2.598 | 36 | False | `MID.down.q10 -l-> MID.down.q20` | — | tennessee_eastman, building_59 |
| B4022:downq20 | m | FCV02Z:downq80 | 3.17 | 4.422 | 20 | True | `SLOW.down.q20 -m-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| B2016:peak | m | PCV01D:peak | 3.165 | 1.881 | 38 | True | `MID.peak -m-> MID-S.peak` | — | — |
| PIT02:downq90 | l | B400B:upq20 | 3.165 | 4.35 | 34 | True | `MID.down.q90 -l-> MID-S.up.q20` | — | tennessee_eastman |
| PIT02:downq90 | l | FT02:upq20 | 3.165 | 3.892 | 34 | True | `MID.down.q90 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| PIT02:downq90 | l | FT02Z:upq20 | 3.165 | 4.121 | 34 | True | `MID.down.q90 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B4022:upq50 | m | B4005:downq20 | 3.164 | 3.404 | 20 | True | `SLOW.up.q50 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B400B:downq20 | l | B4022:downq50 | 3.161 | 3.547 | 93 | True | `MID-S.down.q20 -l-> SLOW.down.q50` | — | tennessee_eastman |
| B4002:upq10 | l | B4022:upq20 | 3.161 | 3.418 | 19 | False | `SET.up.q10 -l-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| B2016:trough | m | B2016:peak | 3.157 | 2.62 | 111 | True | `MID.trough -m-> MID.peak [same role]` | — | tennessee_eastman, physionet_slp |
| ST_TT01:upq10 | m | FCV01Z:peak | 3.156 | 2.221 | 24 | True | `MID.up.q10 -m-> MID-S.peak` | — | tennessee_eastman |
| TIT02:upq20 | l | B3004:upq50 | 3.155 | 1.607 | 14 | True | `MID.up.q20 -l-> SET.up.q50` | — | tennessee_eastman |
| B4022:upq20 | m | B4022:downq20 | 3.154 | 4.752 | 99 | True | `SLOW.up.q20 -m-> SLOW.down.q20 [same role]` | tennessee_eastman, building_59 | — |
| FT02:downq20 | l | B4022:downq50 | 3.153 | 3.553 | 93 | True | `MID-S.down.q20 -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| FCV01Z:peak | l | B2004:upq20 | 3.15 | 3.521 | 8 | False | `MID-S.peak -l-> SET.up.q20` | — | — |
| B4022:downq50 | l | FCV01Z:trough | 3.148 | 2.214 | 28 | False | `SLOW.down.q50 -l-> MID-S.trough` | — | tennessee_eastman |
| FT02Z:downq20 | l | B4022:downq50 | 3.146 | 3.507 | 93 | True | `MID-S.down.q20 -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| LIT01:downq50 | m | LCP01D:downq20 | 3.145 | 3.248 | 70 | True | `MID.down.q50 -m-> MID-S.down.q20` | — | tennessee_eastman |
| PCV01D:trough | m | FT02Z:downq80 | 3.137 | 1.568 | 15 | True | `MID-S.trough -m-> MID-S.down.q80` | — | — |
| FT01:downq50 | s | LCV01Z:downq20 | 3.137 | 3.574 | 6 | True | `MID.down.q50 -s-> MID.down.q20` | — | tennessee_eastman, building_59 |
| B4022:downq20 | m | PIT02:upq10 | 3.135 | 3.657 | 41 | True | `SLOW.down.q20 -m-> MID.up.q10` | building_59 | tennessee_eastman |
| FCV03Z:peak | m | TIT02:upq50 | 3.135 | 2.692 | 8 | True | `MID.peak -m-> MID.up.q50` | — | building_59 |
| LIT01:downq80 | m | LIT01:downq20 | 3.13 | 2.645 | 125 | True | `MID.down.q80 -m-> MID.down.q20 [same role]` | — | tennessee_eastman |
| FCV01D:downq10 | l | B4022:downq50 | 3.13 | 3.423 | 91 | True | `MID-S.down.q10 -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| TIT01:trough | l | TIT02:downq50 | 3.13 | 2.418 | 46 | False | `MID.trough -l-> MID.down.q50` | — | tennessee_eastman |
| LIT01:downq20 | m | LIT01:upq50 | 3.129 | 3.346 | 181 | True | `MID.down.q20 -m-> MID.up.q50 [same role]` | tennessee_eastman | — |
| FCV02Z:downq80 | l | PIT02:downq90 | 3.129 | 2.644 | 41 | False | `MID-S.down.q80 -l-> MID.down.q90` | — | tennessee_eastman, building_59 |
| LIT01:upq50 | m | LCP01D:upq80 | 3.128 | 3.129 | 81 | True | `MID.up.q50 -m-> MID-S.up.q80` | — | tennessee_eastman |
| LCV01Z:upq50 | m | PIT02:downq90 | 3.128 | 1.563 | 23 | True | `MID.up.q50 -m-> MID.down.q90` | — | tennessee_eastman, building_59 |
| LIT01:upq50 | l | LIT01:upq20 | 3.127 | 2.505 | 164 | True | `MID.up.q50 -l-> MID.up.q20 [same role]` | tennessee_eastman | — |
| B4022:downq50 | m | B4022:upq50 | 3.124 | 4.28 | 78 | True | `SLOW.down.q50 -m-> SLOW.up.q50 [same role]` | tennessee_eastman, building_59 | — |
| LCV01D:upq20 | s | FT03Z:peak | 3.122 | 3.011 | 7 | True | `MID.up.q20 -s-> MID.peak` | — | tennessee_eastman |
| TIT01:trough | l | FCV02Z:downq80 | 3.121 | 3.781 | 33 | False | `MID.trough -l-> MID-S.down.q80` | — | tennessee_eastman |
| LIT01:downq50 | m | LIT01:upq20 | 3.112 | 2.83 | 163 | True | `MID.down.q50 -m-> MID.up.q20 [same role]` | tennessee_eastman | — |
| FT01Z:trough | m | B4022:upq20 | 3.11 | 2.632 | 31 | True | `MID.trough -m-> SLOW.up.q20` | — | tennessee_eastman |
| B4022:upq50 | l | B4005:upq20 | 3.109 | 4.075 | 22 | False | `SLOW.up.q50 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:downq50 | m | TIT02:downq80 | 3.109 | 2.168 | 14 | True | `MID.down.q50 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| B4022:downq50 | m | LCV01Z:upq80 | 3.103 | 3.901 | 34 | True | `SLOW.down.q50 -m-> MID.up.q80` | — | tennessee_eastman, building_59 |
| PIT02:downq10 | l | B4022:upq50 | 3.101 | 4.182 | 111 | True | `MID.down.q10 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| FT01:downq80 | s | LCV01D:downq80 | 3.096 | 2.35 | 10 | True | `MID.down.q80 -s-> MID.down.q80` | — | tennessee_eastman, building_59 |
| B4022:downq20 | m | FCV01D:upq10 | 3.095 | 3.392 | 20 | True | `SLOW.down.q20 -m-> MID-S.up.q10` | building_59 | tennessee_eastman |
| TIT02:downq20 | l | PIT02:downq10 | 3.094 | 2.902 | 71 | True | `MID.down.q20 -l-> MID.down.q10` | — | tennessee_eastman, building_59 |
| B4005:upq20 | l | PIT02:downq90 | 3.094 | 2.774 | 43 | False | `MID-S.up.q20 -l-> MID.down.q90` | — | tennessee_eastman, building_59 |
| B400B:upq20 | l | PIT02:downq90 | 3.092 | 2.768 | 42 | False | `MID-S.up.q20 -l-> MID.down.q90` | — | tennessee_eastman |
| B4022:downq50 | m | B4022:downq20 | 3.09 | 2.935 | 90 | True | `SLOW.down.q50 -m-> SLOW.down.q20 [same role]` | — | tennessee_eastman, building_59 |
| FCV01Z:trough | l | FT02Z:upq80 | 3.09 | 1.771 | 51 | True | `MID-S.trough -l-> MID-S.up.q80` | — | tennessee_eastman |
| B4022:downq50 | m | B400B:downq50 | 3.09 | 1.935 | 21 | True | `SLOW.down.q50 -m-> MID-S.down.q50` | — | tennessee_eastman |
| B4022:downq50 | m | FT02:downq50 | 3.09 | 2.177 | 21 | True | `SLOW.down.q50 -m-> MID-S.down.q50` | — | tennessee_eastman |
| B4022:downq50 | m | FT02Z:downq50 | 3.09 | 1.935 | 21 | True | `SLOW.down.q50 -m-> MID-S.down.q50` | — | tennessee_eastman |
| B4022:downq50 | m | FCV01D:downq10 | 3.09 | 2.258 | 18 | True | `SLOW.down.q50 -m-> MID-S.down.q10` | building_59 | tennessee_eastman |
| FT02:upq20 | l | PIT02:downq90 | 3.089 | 2.72 | 42 | False | `MID-S.up.q20 -l-> MID.down.q90` | — | tennessee_eastman, building_59 |
| FT02Z:upq20 | l | PIT02:downq90 | 3.089 | 2.717 | 42 | False | `MID-S.up.q20 -l-> MID.down.q90` | — | tennessee_eastman, building_59 |
| LIT01:downq50 | s | LCV01D:upq50 | 3.087 | 2.769 | 52 | True | `MID.down.q50 -s-> MID.up.q50` | — | tennessee_eastman |
| TIT02:downq20 | l | FCV01D:upq10 | 3.087 | 2.299 | 35 | True | `MID.down.q20 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| PIT02:downq10 | m | FT01:downq50 | 3.087 | 3.279 | 8 | False | `MID.down.q10 -m-> MID.down.q50` | — | tennessee_eastman, building_59 |
| PIT02:downq90 | l | B4005:upq20 | 3.086 | 3.897 | 37 | True | `MID.down.q90 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B3004:downq20 | l | TIT02:downq20 | 3.086 | 2.322 | 8 | False | `SET.down.q20 -l-> MID.down.q20` | — | tennessee_eastman |
| B4022:upq20 | m | B4022:upq50 | 3.085 | 3.21 | 83 | True | `SLOW.up.q20 -m-> SLOW.up.q50 [same role]` | — | tennessee_eastman, building_59 |
| B3004:upq80 | s | LCV01Z:downq20 | 3.08 | 6.362 | 3 | True | `SET.up.q80 -s-> MID.down.q20` | tennessee_eastman | — |
| LCV01Z:upq80 | m | B4005:downq20 | 3.076 | 2.311 | 10 | True | `MID.up.q80 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:upq20 | l | PCV01D:peak | 3.071 | 2.499 | 20 | False | `MID.up.q20 -l-> MID-S.peak` | — | — |
| FCV01D:upq10 | l | TIT02:downq50 | 3.068 | 4.073 | 28 | True | `MID-S.up.q10 -l-> MID.down.q50` | — | tennessee_eastman, building_59 |
| LCV01Z:downq20 | m | LCV01D:downq20 | 3.067 | 2.56 | 64 | True | `MID.down.q20 -m-> MID.down.q20` | — | tennessee_eastman, building_59 |
| B4005:upq50 | l | FCV02Z:downq20 | 3.066 | 1.697 | 19 | False | `MID-S.up.q50 -l-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| FT01:downq50 | l | FT03:trough | 3.063 | 1.651 | 22 | True | `MID.down.q50 -l-> MID.trough` | — | — |
| TIT01:trough | l | PIT02:downq10 | 3.057 | 3.546 | 67 | True | `MID.trough -l-> MID.down.q10` | — | tennessee_eastman |
| FCV01D:upq10 | l | B4022:upq50 | 3.054 | 3.526 | 88 | False | `MID-S.up.q10 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| B3004:downq80 | l | PIT02:downq10 | 3.039 | 2.555 | 14 | False | `SET.down.q80 -l-> MID.down.q10` | — | tennessee_eastman |
| PIT01:peak | m | B3005:upq90 | 3.039 | 3.032 | 6 | True | `MID.peak -m-> SET.up.q90` | — | tennessee_eastman |
| FT01Z:peak | m | FCV02Z:upq80 | 3.035 | 3.742 | 7 | False | `MID.peak -m-> MID-S.up.q80` | — | tennessee_eastman |
| FCV01Z:trough | l | TIT02:downq50 | 3.03 | 3.496 | 38 | True | `MID-S.trough -l-> MID.down.q50` | — | tennessee_eastman |
| FCV01Z:trough | l | B3004:downq50 | 3.03 | 2.46 | 12 | False | `MID-S.trough -l-> SET.down.q50` | — | tennessee_eastman |
| LCV01Z:downq20 | l | FCV03D:trough | 3.029 | 2.297 | 19 | False | `MID.down.q20 -l-> MID.trough` | — | tennessee_eastman, building_59 |
| LCV01D:upq80 | s | FT01Z:peak | 3.025 | 2.674 | 9 | True | `MID.up.q80 -s-> MID.peak` | — | tennessee_eastman |
| LCV01D:downq50 | s | LCV01Z:downq50 | 3.023 | 2.545 | 17 | False | `MID.down.q50 -s-> MID.down.q50` | — | tennessee_eastman, building_59 |
| LCV01D:downq50 | s | LCV01Z:upq50 | 3.023 | 2.969 | 17 | False | `MID.down.q50 -s-> MID.up.q50` | tennessee_eastman | building_59 |
| PIT02:downq90 | l | FCV01Z:trough | 3.02 | 2.59 | 43 | True | `MID.down.q90 -l-> MID-S.trough` | — | tennessee_eastman |
| B3004:downq20 | s | LCV01D:upq50 | 3.02 | 3.775 | 4 | False | `SET.down.q20 -s-> MID.up.q50` | — | tennessee_eastman |
| B4022:upq80 | l | FCV03Z:trough | 3.016 | 2.502 | 15 | False | `SLOW.up.q80 -l-> MID.trough` | — | building_59 |
| FCV01D:upq10 | l | PIT02:downq90 | 3.013 | 2.731 | 41 | False | `MID-S.up.q10 -l-> MID.down.q90` | building_59 | tennessee_eastman |
| PIT02:upq10 | l | TIT02:downq20 | 3.01 | 2.955 | 37 | False | `MID.up.q10 -l-> MID.down.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:upq80 | s | LCV01D:downq80 | 3.006 | 4.924 | 25 | True | `MID.up.q80 -s-> MID.down.q80` | — | tennessee_eastman, building_59 |
| B2016:peak | m | B4022:downq80 | 3.002 | 1.849 | 33 | False | `MID.peak -m-> SLOW.down.q80` | — | tennessee_eastman |
| FT03Z:trough | l | FCV01D:downq10 | 3.002 | 1.814 | 25 | False | `MID.trough -l-> MID-S.down.q10` | — | tennessee_eastman |
| LCV01D:upq80 | s | FT01:upq50 | 3.0 | 5.966 | 6 | False | `MID.up.q80 -s-> MID.up.q50` | — | tennessee_eastman, building_59 |
| FT02:downq20 | l | B4022:upq20 | 2.993 | 3.156 | 103 | True | `MID-S.down.q20 -l-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| B4022:upq20 | m | PIT02:upq10 | 2.991 | 3.244 | 38 | True | `SLOW.up.q20 -m-> MID.up.q10` | building_59 | tennessee_eastman |
| B3004:downq50 | s | LIT01:downq50 | 2.988 | 2.667 | 8 | True | `SET.down.q50 -s-> MID.down.q50` | — | tennessee_eastman |
| FCV02Z:upq50 | l | B4022:upq50 | 2.984 | 3.047 | 100 | True | `MID-S.up.q50 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| FCV01D:upq10 | l | B4022:downq50 | 2.984 | 3.526 | 86 | True | `MID-S.up.q10 -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| FT01:downq50 | l | FT03Z:trough | 2.982 | 1.684 | 21 | True | `MID.down.q50 -l-> MID.trough` | — | tennessee_eastman |
| FCV03Z:peak | m | B2016:trough | 2.978 | 1.836 | 26 | True | `MID.peak -m-> MID.trough` | — | — |
| LCV01Z:downq80 | l | B4005:upq20 | 2.976 | 3.865 | 22 | True | `MID.down.q80 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B400B:downq80 | l | PIT02:upq10 | 2.973 | 2.454 | 44 | True | `MID-S.down.q80 -l-> MID.up.q10` | — | tennessee_eastman |
| B400B:downq20 | l | B4022:upq20 | 2.972 | 3.096 | 102 | True | `MID-S.down.q20 -l-> SLOW.up.q20` | — | tennessee_eastman |
| B2016:peak | m | B2016:trough | 2.972 | 2.671 | 98 | True | `MID.peak -m-> MID.trough [same role]` | — | tennessee_eastman, physionet_slp |
| LIT01:downq80 | m | LIT01:upq50 | 2.966 | 2.696 | 187 | True | `MID.down.q80 -m-> MID.up.q50 [same role]` | tennessee_eastman | — |
| B4005:downq20 | l | B4022:upq20 | 2.966 | 3.025 | 104 | True | `MID-S.down.q20 -l-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| FCV02Z:downq50 | l | FT01:downq50 | 2.964 | 3.321 | 24 | True | `MID-S.down.q50 -l-> MID.down.q50` | — | tennessee_eastman, building_59 |
| FCV02Z:upq80 | l | B4022:downq20 | 2.963 | 3.117 | 96 | True | `MID-S.up.q80 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| LCP01D:downq20 | m | LCV01D:upq80 | 2.963 | 2.267 | 41 | False | `MID-S.down.q20 -m-> MID.up.q80` | — | tennessee_eastman, building_59 |
| B2004:downq20 | l | B4022:downq50 | 2.962 | 3.179 | 25 | True | `SET.down.q20 -l-> SLOW.down.q50` | — | building_59 |
| B4022:upq80 | l | LCV01Z:upq50 | 2.959 | 1.841 | 30 | False | `SLOW.up.q80 -l-> MID.up.q50` | — | tennessee_eastman, building_59 |
| ST_GOV:trough | s | FCV02Z:upq80 | 2.957 | 3.04 | 9 | False | `MID.trough -s-> MID-S.up.q80` | — | tennessee_eastman |
| B3004:upq20 | s | LIT01:upq50 | 2.955 | 3.734 | 8 | True | `SET.up.q20 -s-> MID.up.q50` | — | tennessee_eastman |
| FT03Z:trough | l | FCV02Z:upq80 | 2.952 | 2.389 | 24 | False | `MID.trough -l-> MID-S.up.q80` | — | tennessee_eastman |
| B400B:downq20 | l | PIT02:downq10 | 2.951 | 4.034 | 41 | True | `MID-S.down.q20 -l-> MID.down.q10` | — | tennessee_eastman |
| FT02Z:downq80 | l | FCV03Z:trough | 2.951 | 2.9 | 27 | True | `MID-S.down.q80 -l-> MID.trough` | — | building_59 |
| PIT02:upq90 | l | FCV02Z:downq80 | 2.949 | 3.687 | 30 | False | `MID.up.q90 -l-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| LCV01Z:upq20 | m | LCV01D:downq20 | 2.947 | 3.051 | 62 | True | `MID.up.q20 -m-> MID.down.q20` | — | tennessee_eastman, building_59 |
| B4022:upq50 | s | PIT02:downq90 | 2.946 | 2.428 | 11 | True | `SLOW.up.q50 -s-> MID.down.q90` | — | tennessee_eastman, building_59 |
| LIT01:downq20 | l | LCP01D:downq80 | 2.937 | 3.238 | 90 | True | `MID.down.q20 -l-> MID-S.down.q80` | tennessee_eastman | — |
| FT02Z:downq20 | l | PIT02:downq10 | 2.937 | 3.915 | 41 | True | `MID-S.down.q20 -l-> MID.down.q10` | — | tennessee_eastman, building_59 |
| B4022:upq20 | m | FCV02Z:downq80 | 2.937 | 3.523 | 18 | True | `SLOW.up.q20 -m-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| B4022:upq20 | s | B2016:trough | 2.932 | 2.256 | 26 | True | `SLOW.up.q20 -s-> MID.trough` | — | tennessee_eastman |
| B4022:upq20 | m | B4005:downq20 | 2.927 | 2.736 | 21 | True | `SLOW.up.q20 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B4022:downq20 | m | B4022:downq50 | 2.925 | 4.173 | 81 | True | `SLOW.down.q20 -m-> SLOW.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| FCV01D:upq10 | m | B2016:peak | 2.925 | 1.928 | 20 | True | `MID-S.up.q10 -m-> MID.peak` | — | tennessee_eastman |
| B3004:upq20 | m | PIT01:peak | 2.923 | 1.921 | 8 | True | `SET.up.q20 -m-> MID.peak` | — | tennessee_eastman |
| B4022:downq20 | l | PCV01D:peak | 2.92 | 2.467 | 25 | False | `SLOW.down.q20 -l-> MID-S.peak` | — | — |
| B4022:downq20 | m | FCV02Z:upq50 | 2.918 | 1.586 | 22 | True | `SLOW.down.q20 -m-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| TIT02:upq50 | l | FCV02Z:upq80 | 2.913 | 2.786 | 29 | False | `MID.up.q50 -l-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| FCV02Z:upq80 | l | FCV02Z:downq50 | 2.91 | 2.186 | 22 | False | `MID-S.up.q80 -l-> MID-S.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| LIT01:upq80 | s | LCV01D:upq20 | 2.909 | 2.248 | 28 | True | `MID.up.q80 -s-> MID.up.q20` | — | tennessee_eastman |
| FCV02Z:upq50 | l | PIT02:upq10 | 2.907 | 5.377 | 46 | True | `MID-S.up.q50 -l-> MID.up.q10` | — | tennessee_eastman, building_59 |
| PIT02:upq90 | l | FT02:upq20 | 2.905 | 3.735 | 31 | True | `MID.up.q90 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| LCV01D:downq20 | l | B3005:upq10 | 2.903 | 7.25 | 3 | False | `MID.down.q20 -l-> SET.up.q10` | — | tennessee_eastman, building_59 |
| LIT01:downq50 | m | LIT01:upq50 | 2.902 | 2.98 | 240 | True | `MID.down.q50 -m-> MID.up.q50 [same role]` | tennessee_eastman | — |
| B3004:upq80 | l | B4022:upq20 | 2.901 | 3.269 | 35 | True | `SET.up.q80 -l-> SLOW.up.q20` | — | tennessee_eastman |
| PIT02:upq90 | l | TIT02:downq20 | 2.899 | 2.321 | 41 | True | `MID.up.q90 -l-> MID.down.q20` | — | tennessee_eastman, building_59 |
| B4022:downq50 | l | FCV01D:downq10 | 2.899 | 2.253 | 19 | True | `SLOW.down.q50 -l-> MID-S.down.q10` | building_59 | tennessee_eastman |
| LCV01D:downq50 | s | FCV03Z:trough | 2.899 | 3.458 | 8 | False | `MID.down.q50 -s-> MID.trough` | — | building_59 |
| TIT01:peak | m | PIT02:downq90 | 2.894 | 3.742 | 18 | True | `MID.peak -m-> MID.down.q90` | — | tennessee_eastman |
| LCV01Z:upq50 | m | B4005:upq20 | 2.89 | 4.152 | 12 | True | `MID.up.q50 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B4005:downq20 | l | PIT02:downq10 | 2.889 | 3.875 | 41 | True | `MID-S.down.q20 -l-> MID.down.q10` | — | tennessee_eastman, building_59 |
| PIT02:downq90 | m | FCV01Z:peak | 2.882 | 4.378 | 14 | False | `MID.down.q90 -m-> MID-S.peak` | — | tennessee_eastman |
| PIT02:downq90 | l | TIT02:upq20 | 2.88 | 2.072 | 41 | False | `MID.down.q90 -l-> MID.up.q20` | — | tennessee_eastman, building_59 |
| LD:peak | m | B3005:upq10 | 2.878 | 7.643 | 3 | False | `MID.peak -m-> SET.up.q10` | — | — |
| TIT02:upq50 | m | FCV02Z:downq20 | 2.877 | 3.485 | 7 | False | `MID.up.q50 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| TIT02:downq80 | l | FT02:upq80 | 2.875 | 1.666 | 52 | True | `MID.down.q80 -l-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| FT02Z:downq50 | l | PIT02:upq10 | 2.869 | 5.357 | 47 | True | `MID-S.down.q50 -l-> MID.up.q10` | — | tennessee_eastman |
| TIT02:upq20 | l | PIT02:downq10 | 2.863 | 3.743 | 60 | True | `MID.up.q20 -l-> MID.down.q10` | — | tennessee_eastman, building_59 |
| FT03Z:peak | s | LCV01D:downq80 | 2.86 | 2.248 | 13 | True | `MID.peak -s-> MID.down.q80` | — | tennessee_eastman |
| LCV01Z:upq50 | m | PIT02:upq90 | 2.856 | 2.345 | 21 | False | `MID.up.q50 -m-> MID.up.q90` | — | tennessee_eastman, building_59 |
| FCV01Z:peak | l | PIT02:upq10 | 2.854 | 2.848 | 56 | True | `MID-S.peak -l-> MID.up.q10` | — | tennessee_eastman |
| PIT02:upq90 | l | B4005:upq20 | 2.854 | 3.543 | 34 | True | `MID.up.q90 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| TIT02:downq80 | l | FT02Z:upq80 | 2.853 | 2.047 | 49 | True | `MID.down.q80 -l-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| FCV03D:peak | l | TIT02:downq80 | 2.842 | 2.106 | 40 | True | `MID.peak -l-> MID.down.q80` | — | tennessee_eastman, building_59 |
| FT01Z:trough | l | FCV02Z:upq80 | 2.841 | 2.49 | 27 | False | `MID.trough -l-> MID-S.up.q80` | — | tennessee_eastman |
| PIT02:downq10 | l | PIT02:downq90 | 2.84 | 2.323 | 48 | True | `MID.down.q10 -l-> MID.down.q90 [same role]` | — | tennessee_eastman, building_59 |
| B2016:trough | l | PCV01Z:peak | 2.835 | 2.384 | 53 | True | `MID.trough -l-> MID-S.peak` | — | — |
| FCV02Z:downq50 | l | PIT02:downq10 | 2.833 | 2.709 | 50 | True | `MID-S.down.q50 -l-> MID.down.q10` | — | tennessee_eastman, building_59 |
| TIT02:downq20 | l | PIT02:upq10 | 2.832 | 2.65 | 65 | True | `MID.down.q20 -l-> MID.up.q10` | — | tennessee_eastman, building_59 |
| B4022:downq20 | m | PIT02:downq10 | 2.829 | 2.895 | 37 | True | `SLOW.down.q20 -m-> MID.down.q10` | building_59 | tennessee_eastman |
| LCV01D:upq80 | m | LCV01Z:downq80 | 2.829 | 3.769 | 37 | True | `MID.up.q80 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| B4002:upq10 | l | B4022:downq20 | 2.829 | 3.418 | 17 | False | `SET.up.q10 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| LCV01D:upq50 | s | FCV03D:peak | 2.827 | 1.841 | 11 | False | `MID.up.q50 -s-> MID.peak` | — | tennessee_eastman, building_59 |
| PIT02:downq10 | l | B4022:upq20 | 2.826 | 3.819 | 118 | True | `MID.down.q10 -l-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| B4022:upq50 | m | FT02Z:downq20 | 2.825 | 2.631 | 16 | True | `SLOW.up.q50 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| LCV01D:upq50 | s | LCV01Z:upq80 | 2.823 | 4.816 | 14 | True | `MID.up.q50 -s-> MID.up.q80` | — | tennessee_eastman, building_59 |
| B4005:downq50 | l | PIT02:downq10 | 2.816 | 4.96 | 48 | True | `MID-S.down.q50 -l-> MID.down.q10` | — | tennessee_eastman, building_59 |
| B4005:downq50 | l | PIT02:upq10 | 2.816 | 5.26 | 48 | True | `MID-S.down.q50 -l-> MID.up.q10` | — | tennessee_eastman, building_59 |
| TIT02:downq50 | l | FCV01Z:peak | 2.815 | 2.71 | 38 | True | `MID.down.q50 -l-> MID-S.peak` | — | tennessee_eastman |
| LCV01Z:downq80 | l | B4022:upq50 | 2.814 | 2.811 | 78 | True | `MID.down.q80 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| FT02Z:downq20 | l | B4022:downq20 | 2.813 | 3.17 | 97 | True | `MID-S.down.q20 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| B2016:trough | m | PCV01Z:trough | 2.813 | 2.708 | 35 | True | `MID.trough -m-> MID-S.trough` | — | — |
| B400B:downq50 | l | PIT02:downq10 | 2.808 | 5.051 | 46 | True | `MID-S.down.q50 -l-> MID.down.q10` | — | tennessee_eastman |
| FT03:peak | s | LCV01D:downq80 | 2.808 | 2.248 | 12 | True | `MID.peak -s-> MID.down.q80` | — | — |
| PCV01Z:peak | l | PCV01Z:trough | 2.806 | 2.61 | 50 | True | `MID-S.peak -l-> MID-S.trough [same role]` | — | — |
| FCV02Z:upq20 | m | B4022:downq20 | 2.801 | 1.516 | 16 | False | `MID-S.up.q20 -m-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| TIT01:trough | l | B3004:upq50 | 2.801 | 1.914 | 13 | True | `MID.trough -l-> SET.up.q50` | — | tennessee_eastman |
| B4022:upq20 | m | B400B:upq20 | 2.8 | 3.97 | 18 | True | `SLOW.up.q20 -m-> MID-S.up.q20` | — | tennessee_eastman |
| B4022:upq20 | m | FT02Z:upq20 | 2.8 | 3.665 | 18 | True | `SLOW.up.q20 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B400B:upq80 | l | PIT02:downq10 | 2.793 | 2.317 | 42 | False | `MID-S.up.q80 -l-> MID.down.q10` | — | tennessee_eastman |
| B4022:upq50 | l | PIT02:upq10 | 2.793 | 2.877 | 35 | True | `SLOW.up.q50 -l-> MID.up.q10` | — | tennessee_eastman, building_59 |
| FCV01D:upq10 | l | PIT02:upq90 | 2.792 | 2.367 | 38 | False | `MID-S.up.q10 -l-> MID.up.q90` | building_59 | tennessee_eastman |
| LIT01:downq20 | l | LIT01:downq80 | 2.791 | 2.879 | 215 | True | `MID.down.q20 -l-> MID.down.q80 [same role]` | — | tennessee_eastman |
| B4022:downq50 | l | PIT02:downq10 | 2.789 | 3.34 | 37 | True | `SLOW.down.q50 -l-> MID.down.q10` | — | tennessee_eastman, building_59 |
| B4022:upq50 | m | FCV02Z:downq50 | 2.789 | 1.539 | 18 | True | `SLOW.up.q50 -m-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| B4022:upq50 | m | B400B:downq50 | 2.789 | 2.309 | 18 | True | `SLOW.up.q50 -m-> MID-S.down.q50` | — | tennessee_eastman |
| B4022:upq50 | m | B400B:upq50 | 2.789 | 2.052 | 18 | True | `SLOW.up.q50 -m-> MID-S.up.q50` | — | tennessee_eastman |
| B4022:upq50 | m | LCV01Z:upq80 | 2.787 | 4.455 | 29 | True | `SLOW.up.q50 -m-> MID.up.q80` | — | tennessee_eastman, building_59 |
| FT02Z:downq80 | l | FT03:trough | 2.786 | 1.774 | 25 | True | `MID-S.down.q80 -l-> MID.trough` | — | — |
| B4022:downq20 | m | B4022:upq20 | 2.785 | 2.467 | 90 | True | `SLOW.down.q20 -m-> SLOW.up.q20 [same role]` | tennessee_eastman, building_59 | — |
| B2016:peak | l | FCV02Z:downq80 | 2.781 | 3.044 | 32 | True | `MID.peak -l-> MID-S.down.q80` | — | tennessee_eastman |
| ST_PT01:trough | s | FT01:upq50 | 2.78 | 2.63 | 11 | True | `MID.trough -s-> MID.up.q50` | — | tennessee_eastman |
| PIT02:downq90 | l | B400B:downq50 | 2.778 | 2.21 | 34 | False | `MID.down.q90 -l-> MID-S.down.q50` | — | tennessee_eastman |
| PIT02:downq90 | l | FT02:downq50 | 2.778 | 2.21 | 34 | False | `MID.down.q90 -l-> MID-S.down.q50` | — | tennessee_eastman |
| PIT02:downq90 | l | FT02Z:downq50 | 2.778 | 2.21 | 34 | False | `MID.down.q90 -l-> MID-S.down.q50` | — | tennessee_eastman |
| PIT02:downq90 | l | FCV02Z:upq50 | 2.778 | 2.009 | 34 | False | `MID.down.q90 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| FT01:downq50 | l | PCV01Z:trough | 2.778 | 2.441 | 27 | True | `MID.down.q50 -l-> MID-S.trough` | — | — |
| B400B:upq80 | l | TIT02:upq20 | 2.777 | 1.728 | 28 | False | `MID-S.up.q80 -l-> MID.up.q20` | — | tennessee_eastman |
| FCV02Z:upq50 | l | B4022:downq50 | 2.775 | 3.192 | 93 | True | `MID-S.up.q50 -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| B3004:upq50 | s | LIT01:upq20 | 2.772 | 2.895 | 7 | True | `SET.up.q50 -s-> MID.up.q20` | — | tennessee_eastman |
| B4005:downq50 | l | B4022:upq50 | 2.77 | 3.052 | 100 | True | `MID-S.down.q50 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| TIT02:downq20 | l | FT02Z:downq80 | 2.766 | 1.573 | 56 | True | `MID.down.q20 -l-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| FT03:trough | l | B4005:downq20 | 2.764 | 2.454 | 27 | False | `MID.trough -l-> MID-S.down.q20` | — | — |
| FCV01Z:trough | l | FT03:peak | 2.762 | 1.737 | 31 | False | `MID-S.trough -l-> MID.peak` | — | — |
| PIT02:downq90 | l | TIT02:upq80 | 2.761 | 2.206 | 40 | False | `MID.down.q90 -l-> MID.up.q80` | — | tennessee_eastman, building_59 |
| FT01:downq80 | l | B4022:upq50 | 2.759 | 2.722 | 56 | False | `MID.down.q80 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| B3004:upq50 | s | LIT01:upq50 | 2.759 | 2.444 | 11 | True | `SET.up.q50 -s-> MID.up.q50` | — | tennessee_eastman |
| FT02Z:upq80 | l | TIT02:upq20 | 2.757 | 1.594 | 28 | False | `MID-S.up.q80 -l-> MID.up.q20` | — | tennessee_eastman, building_59 |
| FT02Z:upq80 | l | TIT02:upq50 | 2.757 | 1.594 | 28 | False | `MID-S.up.q80 -l-> MID.up.q50` | building_59 | tennessee_eastman |
| LCV01Z:upq80 | m | FT01Z:trough | 2.753 | 1.88 | 11 | False | `MID.up.q80 -m-> MID.trough` | — | tennessee_eastman |
| LCV01D:downq80 | s | LCV01D:downq50 | 2.751 | 2.315 | 42 | True | `MID.down.q80 -s-> MID.down.q50 [same role]` | tennessee_eastman | building_59 |
| B4022:upq50 | m | B4022:upq20 | 2.748 | 3.352 | 76 | True | `SLOW.up.q50 -m-> SLOW.up.q20 [same role]` | — | tennessee_eastman, building_59 |
| B400B:downq20 | l | FCV02Z:downq50 | 2.747 | 2.413 | 22 | False | `MID-S.down.q20 -l-> MID-S.down.q50` | — | tennessee_eastman |
| FT02:downq80 | l | PIT02:upq10 | 2.746 | 2.209 | 41 | True | `MID-S.down.q80 -l-> MID.up.q10` | — | tennessee_eastman, building_59 |
| PCV01Z:trough | l | PCV01Z:peak | 2.745 | 2.443 | 48 | True | `MID-S.trough -l-> MID-S.peak [same role]` | — | — |
| FT01:upq80 | l | B4022:downq20 | 2.744 | 3.126 | 65 | False | `MID.up.q80 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:downq80 | l | B4022:downq50 | 2.742 | 2.811 | 76 | True | `MID.down.q80 -l-> SLOW.down.q50` | building_59 | tennessee_eastman |
| FCV02Z:upq50 | m | B4022:upq20 | 2.742 | 2.231 | 29 | True | `MID-S.up.q50 -m-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| FT03:trough | l | FT02:downq20 | 2.742 | 2.491 | 24 | False | `MID.trough -l-> MID-S.down.q20` | — | — |
| B4005:upq20 | s | B4022:downq50 | 2.742 | 2.353 | 10 | True | `MID-S.up.q20 -s-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| FT02:downq20 | l | FCV02Z:downq50 | 2.74 | 2.373 | 22 | False | `MID-S.down.q20 -l-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| FT02Z:downq50 | l | B4022:upq50 | 2.738 | 3.108 | 95 | True | `MID-S.down.q50 -l-> SLOW.up.q50` | — | tennessee_eastman |
| B400B:downq50 | l | B4022:upq50 | 2.738 | 3.108 | 95 | True | `MID-S.down.q50 -l-> SLOW.up.q50` | — | tennessee_eastman |
| FT02:downq50 | l | B4022:upq50 | 2.738 | 3.108 | 95 | True | `MID-S.down.q50 -l-> SLOW.up.q50` | — | tennessee_eastman |
| LIT01:downq50 | m | LIT01:upq80 | 2.736 | 2.956 | 187 | True | `MID.down.q50 -m-> MID.up.q80 [same role]` | tennessee_eastman | — |
| PIT02:downq10 | l | TIT02:downq50 | 2.735 | 2.381 | 31 | True | `MID.down.q10 -l-> MID.down.q50` | — | tennessee_eastman, building_59 |
| FT01:downq20 | l | FCV03Z:trough | 2.735 | 4.131 | 11 | True | `MID.down.q20 -l-> MID.trough` | — | building_59 |
| B2016:trough | m | PCV01D:trough | 2.734 | 2.808 | 35 | True | `MID.trough -m-> MID-S.trough` | — | — |
| B2016:peak | l | FT02:upq20 | 2.734 | 3.244 | 33 | True | `MID.peak -l-> MID-S.up.q20` | — | tennessee_eastman |
| B2016:peak | l | FT02Z:upq20 | 2.734 | 3.244 | 33 | True | `MID.peak -l-> MID-S.up.q20` | — | tennessee_eastman |
| PCV01D:trough | l | PCV01Z:peak | 2.732 | 2.329 | 48 | True | `MID-S.trough -l-> MID-S.peak` | — | — |
| B4022:downq20 | l | PIT02:downq10 | 2.732 | 3.503 | 28 | True | `SLOW.down.q20 -l-> MID.down.q10` | building_59 | tennessee_eastman |
| B3004:upq50 | s | LIT01:upq80 | 2.732 | 2.219 | 9 | True | `SET.up.q50 -s-> MID.up.q80` | — | tennessee_eastman |
| B3004:upq80 | s | LCV01D:downq50 | 2.73 | 1.813 | 7 | True | `SET.up.q80 -s-> MID.down.q50` | — | tennessee_eastman |
| PCV01Z:peak | l | PCV01D:trough | 2.727 | 2.537 | 50 | True | `MID-S.peak -l-> MID-S.trough` | — | — |
| FT02:upq80 | l | FCV01D:upq10 | 2.723 | 2.105 | 20 | False | `MID-S.up.q80 -l-> MID-S.up.q10` | building_59 | tennessee_eastman |
| B4022:downq20 | m | FT02Z:downq20 | 2.721 | 3.614 | 18 | True | `SLOW.down.q20 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| ST_PS:downq20 | s | LCV01D:downq80 | 2.721 | 5.004 | 3 | False | `SET.down.q20 -s-> MID.down.q80` | — | — |
| LIT01:upq20 | s | LCV01Z:downq50 | 2.718 | 1.543 | 12 | True | `MID.up.q20 -s-> MID.down.q50` | — | tennessee_eastman |
| TIT02:downq20 | l | B400B:downq80 | 2.716 | 1.573 | 55 | True | `MID.down.q20 -l-> MID-S.down.q80` | — | tennessee_eastman |
| TIT02:downq20 | l | FCV02Z:downq20 | 2.716 | 2.145 | 22 | False | `MID.down.q20 -l-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| ST_TT01:upq10 | m | TIT02:downq80 | 2.714 | 2.183 | 21 | True | `MID.up.q10 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| PIT02:upq90 | l | TIT02:upq80 | 2.71 | 1.792 | 39 | False | `MID.up.q90 -l-> MID.up.q80` | — | tennessee_eastman, building_59 |
| FT01Z:peak | s | LCV01Z:downq50 | 2.71 | 3.879 | 7 | True | `MID.peak -s-> MID.down.q50` | — | tennessee_eastman |
| FT02Z:downq50 | l | B4022:downq50 | 2.709 | 2.963 | 94 | True | `MID-S.down.q50 -l-> SLOW.down.q50` | — | tennessee_eastman |
| B400B:downq50 | l | B4022:downq50 | 2.709 | 2.963 | 94 | True | `MID-S.down.q50 -l-> SLOW.down.q50` | — | tennessee_eastman |
| FT02:downq50 | l | B4022:downq50 | 2.709 | 2.963 | 94 | True | `MID-S.down.q50 -l-> SLOW.down.q50` | — | tennessee_eastman |
| B2016:trough | m | B400B:upq20 | 2.709 | 3.767 | 21 | True | `MID.trough -m-> MID-S.up.q20` | — | tennessee_eastman |
| B4022:downq20 | m | B4005:downq20 | 2.708 | 2.698 | 20 | True | `SLOW.down.q20 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B2004:downq20 | s | LIT01:upq20 | 2.708 | 2.095 | 5 | True | `SET.down.q20 -s-> MID.up.q20` | — | — |
| PIT02:upq90 | l | TIT01:trough | 2.707 | 1.772 | 43 | True | `MID.up.q90 -l-> MID.trough` | — | tennessee_eastman |
| LCV01D:upq50 | s | LCV01Z:upq50 | 2.705 | 2.154 | 18 | True | `MID.up.q50 -s-> MID.up.q50` | — | tennessee_eastman, building_59 |
| FT02:upq20 | s | B4022:downq50 | 2.704 | 4.575 | 5 | False | `MID-S.up.q20 -s-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| FCV02Z:downq80 | l | B4022:upq50 | 2.703 | 3.511 | 75 | False | `MID-S.down.q80 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| FT03Z:trough | l | FT02:downq20 | 2.698 | 2.531 | 23 | False | `MID.trough -l-> MID-S.down.q20` | — | tennessee_eastman |
| B4022:upq20 | l | B400B:upq50 | 2.696 | 2.075 | 16 | True | `SLOW.up.q20 -l-> MID-S.up.q50` | — | tennessee_eastman |
| B2004:upq50 | l | PIT02:downq10 | 2.689 | 2.494 | 13 | False | `SET.up.q50 -l-> MID.down.q10` | — | — |
| LCV01Z:upq50 | m | B400B:upq20 | 2.689 | 3.862 | 10 | False | `MID.up.q50 -m-> MID-S.up.q20` | — | tennessee_eastman |
| B4022:upq20 | l | B400B:downq20 | 2.688 | 4.729 | 14 | True | `SLOW.up.q20 -l-> MID-S.down.q20` | — | tennessee_eastman |
| B4005:downq50 | l | B4022:downq50 | 2.687 | 2.91 | 97 | True | `MID-S.down.q50 -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| PIT02:upq90 | l | TIT02:upq50 | 2.686 | 1.658 | 38 | False | `MID.up.q90 -l-> MID.up.q50` | — | tennessee_eastman, building_59 |
| B4005:downq50 | l | FCV03Z:trough | 2.685 | 1.72 | 28 | True | `MID-S.down.q50 -l-> MID.trough` | — | building_59 |
| B4005:upq20 | l | B4022:upq50 | 2.684 | 3.438 | 79 | False | `MID-S.up.q20 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| PCV01D:trough | l | FCV02Z:upq80 | 2.682 | 3.094 | 28 | False | `MID-S.trough -l-> MID-S.up.q80` | — | — |
| B3004:upq20 | s | LIT01:upq80 | 2.682 | 3.39 | 6 | True | `SET.up.q20 -s-> MID.up.q80` | — | tennessee_eastman |
| B400B:upq20 | l | B4022:upq50 | 2.677 | 3.431 | 77 | False | `MID-S.up.q20 -l-> SLOW.up.q50` | — | tennessee_eastman |
| LIT01:upq20 | l | LCP01D:downq50 | 2.676 | 3.532 | 107 | False | `MID.up.q20 -l-> MID-S.down.q50` | — | tennessee_eastman |
| LCV01Z:upq80 | l | B4022:upq50 | 2.675 | 3.044 | 75 | True | `MID.up.q80 -l-> SLOW.up.q50` | building_59 | tennessee_eastman |
| FT02Z:upq20 | l | B4022:upq50 | 2.674 | 3.368 | 77 | False | `MID-S.up.q20 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| LCV01Z:downq80 | l | FT03:trough | 2.674 | 2.645 | 21 | True | `MID.down.q80 -l-> MID.trough` | — | — |
| PIT02:downq90 | m | LCV01Z:downq80 | 2.674 | 3.61 | 18 | False | `MID.down.q90 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| B2016:peak | l | B4005:upq20 | 2.672 | 3.364 | 36 | True | `MID.peak -l-> MID-S.up.q20` | — | tennessee_eastman |
| LCV01D:upq20 | l | LCP01D:upq20 | 2.671 | 2.077 | 73 | True | `MID.up.q20 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FCV03Z:peak | l | TIT02:downq80 | 2.67 | 1.751 | 31 | True | `MID.peak -l-> MID.down.q80` | — | building_59 |
| FCV02Z:upq80 | l | PIT02:upq10 | 2.669 | 3.921 | 35 | True | `MID-S.up.q80 -l-> MID.up.q10` | — | tennessee_eastman, building_59 |
| FCV02Z:downq80 | l | B4022:downq50 | 2.667 | 3.355 | 74 | False | `MID-S.down.q80 -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| B3004:downq80 | s | LIT01:downq50 | 2.667 | 1.867 | 5 | True | `SET.down.q80 -s-> MID.down.q50` | — | tennessee_eastman |
| TIT01:trough | l | B4005:downq20 | 2.666 | 3.23 | 33 | True | `MID.trough -l-> MID-S.down.q20` | — | tennessee_eastman |
| LIT01:upq20 | l | LCP01D:downq80 | 2.663 | 3.151 | 79 | False | `MID.up.q20 -l-> MID-S.down.q80` | — | tennessee_eastman |
| FCV02Z:upq50 | l | PIT02:upq90 | 2.654 | 1.69 | 42 | True | `MID-S.up.q50 -l-> MID.up.q90` | — | tennessee_eastman, building_59 |
| FT03Z:peak | l | PCV01D:peak | 2.654 | 2.768 | 41 | False | `MID.peak -l-> MID-S.peak` | — | — |
| PCV01D:trough | m | B2016:peak | 2.654 | 2.413 | 33 | True | `MID-S.trough -m-> MID.peak` | — | — |
| FCV01D:downq10 | l | B4022:upq20 | 2.653 | 3.325 | 90 | True | `MID-S.down.q10 -l-> SLOW.up.q20` | building_59 | tennessee_eastman |
| B2016:trough | l | PCV01D:peak | 2.652 | 2.106 | 51 | True | `MID.trough -l-> MID-S.peak` | — | — |
| ST_TT01:upq10 | m | PIT02:upq90 | 2.646 | 2.482 | 30 | True | `MID.up.q10 -m-> MID.up.q90` | — | tennessee_eastman, building_59 |
| LIT01:upq80 | l | LCP01D:upq20 | 2.642 | 2.769 | 56 | False | `MID.up.q80 -l-> MID-S.up.q20` | — | tennessee_eastman |
| FCV03Z:trough | l | TIT02:downq20 | 2.642 | 1.9 | 31 | False | `MID.trough -l-> MID.down.q20` | — | building_59 |
| LCV01Z:upq50 | l | B4022:downq20 | 2.64 | 3.566 | 102 | True | `MID.up.q50 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| FT02:upq20 | l | B4022:downq50 | 2.64 | 3.612 | 76 | False | `MID-S.up.q20 -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| LCV01D:upq50 | s | LCV01D:upq80 | 2.636 | 3.777 | 45 | True | `MID.up.q50 -s-> MID.up.q80 [same role]` | tennessee_eastman | building_59 |
| FCV01Z:trough | l | FT03Z:peak | 2.636 | 1.771 | 29 | False | `MID-S.trough -l-> MID.peak` | — | tennessee_eastman |
| B4022:downq20 | m | FCV01D:downq10 | 2.631 | 1.85 | 17 | True | `SLOW.down.q20 -m-> MID-S.down.q10` | building_59 | tennessee_eastman |
| LIT01:upq80 | l | LIT01:upq50 | 2.63 | 2.64 | 209 | True | `MID.up.q80 -l-> MID.up.q50 [same role]` | tennessee_eastman | — |
| FT02:upq50 | l | PIT02:downq10 | 2.628 | 2.37 | 46 | False | `MID-S.up.q50 -l-> MID.down.q10` | — | tennessee_eastman |
| LIT01:upq50 | s | LCV01D:downq80 | 2.628 | 2.134 | 40 | True | `MID.up.q50 -s-> MID.down.q80` | — | tennessee_eastman |
| LIT01:upq80 | s | LCV01Z:downq50 | 2.627 | 1.624 | 10 | True | `MID.up.q80 -s-> MID.down.q50` | — | tennessee_eastman |
| FCV01D:downq10 | l | B4022:downq20 | 2.624 | 3.325 | 89 | True | `MID-S.down.q10 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| FT02Z:downq50 | l | PIT02:upq90 | 2.624 | 1.531 | 43 | True | `MID-S.down.q50 -l-> MID.up.q90` | — | tennessee_eastman |
| B400B:downq50 | l | PIT02:upq90 | 2.624 | 1.531 | 43 | True | `MID-S.down.q50 -l-> MID.up.q90` | — | tennessee_eastman |
| FT02:upq80 | l | PIT02:upq10 | 2.623 | 1.734 | 39 | False | `MID-S.up.q80 -l-> MID.up.q10` | — | tennessee_eastman, building_59 |
| FT01:downq80 | l | PCV01D:trough | 2.623 | 1.725 | 21 | False | `MID.down.q80 -l-> MID-S.trough` | — | — |
| FCV01D:upq10 | s | B4022:downq20 | 2.623 | 1.902 | 8 | False | `MID-S.up.q10 -s-> SLOW.down.q20` | building_59 | tennessee_eastman |
| B400B:downq80 | m | FCV01Z:peak | 2.622 | 3.551 | 11 | False | `MID-S.down.q80 -m-> MID-S.peak` | — | tennessee_eastman |
| FCV01Z:trough | l | PIT02:downq90 | 2.62 | 2.214 | 49 | False | `MID-S.trough -l-> MID.down.q90` | — | tennessee_eastman |
| FT02Z:downq50 | l | B4022:downq20 | 2.619 | 3.098 | 106 | True | `MID-S.down.q50 -l-> SLOW.down.q20` | — | tennessee_eastman |
| FT02Z:downq50 | l | B4022:upq20 | 2.619 | 3.222 | 106 | True | `MID-S.down.q50 -l-> SLOW.up.q20` | — | tennessee_eastman |
| FT02:downq50 | l | B4022:upq20 | 2.619 | 3.222 | 106 | True | `MID-S.down.q50 -l-> SLOW.up.q20` | — | tennessee_eastman |
| LIT01:downq20 | l | LIT01:downq50 | 2.617 | 2.67 | 244 | False | `MID.down.q20 -l-> MID.down.q50 [same role]` | tennessee_eastman | — |
| FT03:peak | l | PCV01D:peak | 2.616 | 2.77 | 41 | False | `MID.peak -l-> MID-S.peak` | — | — |
| LCV01Z:downq50 | l | PCV01D:trough | 2.613 | 1.747 | 34 | True | `MID.down.q50 -l-> MID-S.trough` | — | — |
| LCV01Z:downq50 | l | PCV01Z:trough | 2.61 | 1.798 | 33 | True | `MID.down.q50 -l-> MID-S.trough` | — | — |
| FT01Z:trough | l | B4005:downq20 | 2.606 | 2.127 | 29 | False | `MID.trough -l-> MID-S.down.q20` | — | tennessee_eastman |
| LCV01Z:upq80 | m | PIT02:upq90 | 2.606 | 2.284 | 15 | False | `MID.up.q80 -m-> MID.up.q90` | — | tennessee_eastman, building_59 |
| LIT01:upq50 | s | LCV01D:downq20 | 2.6 | 3.566 | 39 | True | `MID.up.q50 -s-> MID.down.q20` | — | tennessee_eastman |
| FCV01Z:peak | l | PIT02:downq10 | 2.599 | 2.392 | 51 | False | `MID-S.peak -l-> MID.down.q10` | — | tennessee_eastman |
| LCV01Z:downq80 | l | B4005:upq50 | 2.597 | 2.698 | 20 | False | `MID.down.q80 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| B4022:downq50 | m | FT03Z:peak | 2.595 | 2.607 | 18 | True | `SLOW.down.q50 -m-> MID.peak` | — | tennessee_eastman |
| B4022:downq20 | l | B2016:peak | 2.594 | 2.245 | 61 | True | `SLOW.down.q20 -l-> MID.peak` | — | tennessee_eastman |
| FT02Z:downq50 | l | FCV03Z:trough | 2.594 | 1.751 | 26 | True | `MID-S.down.q50 -l-> MID.trough` | — | — |
| B400B:downq50 | l | FCV03Z:trough | 2.594 | 1.751 | 26 | True | `MID-S.down.q50 -l-> MID.trough` | — | — |
| FCV02Z:downq20 | l | FCV03D:trough | 2.594 | 2.481 | 18 | False | `MID-S.down.q20 -l-> MID.trough` | — | tennessee_eastman, building_59 |
| PIT02:downq90 | l | B4022:upq20 | 2.593 | 3.328 | 136 | True | `MID.down.q90 -l-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| TIT02:downq50 | l | FCV03D:peak | 2.588 | 1.725 | 38 | False | `MID.down.q50 -l-> MID.peak` | — | tennessee_eastman, building_59 |
| LIT01:downq80 | l | LIT01:upq20 | 2.585 | 2.514 | 129 | False | `MID.down.q80 -l-> MID.up.q20 [same role]` | — | tennessee_eastman |
| FCV02Z:upq50 | l | B4022:downq20 | 2.583 | 3.171 | 101 | True | `MID-S.up.q50 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| LIT01:upq50 | s | LCV01Z:downq20 | 2.583 | 3.563 | 18 | True | `MID.up.q50 -s-> MID.down.q20` | — | tennessee_eastman |
| LIT01:downq20 | m | LCV01D:downq80 | 2.58 | 2.256 | 97 | True | `MID.down.q20 -m-> MID.down.q80` | — | tennessee_eastman |
| B4022:upq50 | l | PCV01D:trough | 2.58 | 2.755 | 27 | True | `SLOW.up.q50 -l-> MID-S.trough` | — | — |
| HT_LD:peak | s | VXT03:upq50 | 2.58 | 3.913 | 7 | False | `MID-S.peak -s-> SLOW.up.q50` | — | — |
| FCV03Z:trough | l | FT02:upq50 | 2.577 | 1.719 | 26 | True | `MID.trough -l-> MID-S.up.q50` | — | — |
| FCV03Z:trough | l | FT02Z:upq50 | 2.577 | 1.719 | 26 | True | `MID.trough -l-> MID-S.up.q50` | — | — |
| PIT02:upq10 | l | B4022:upq50 | 2.576 | 3.431 | 100 | True | `MID.up.q10 -l-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| FCV01D:upq10 | l | FT03:peak | 2.572 | 1.517 | 21 | False | `MID-S.up.q10 -l-> MID.peak` | — | — |
| PIT02:upq90 | l | B4022:upq20 | 2.571 | 3.284 | 134 | True | `MID.up.q90 -l-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| TIT02:upq20 | l | FT01:upq80 | 2.569 | 1.607 | 19 | False | `MID.up.q20 -l-> MID.up.q80` | — | tennessee_eastman, building_59 |
| LCV01Z:upq80 | l | B4022:downq20 | 2.568 | 3.296 | 84 | True | `MID.up.q80 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| LIT01:downq50 | l | LIT01:downq80 | 2.566 | 2.533 | 177 | False | `MID.down.q50 -l-> MID.down.q80 [same role]` | tennessee_eastman | — |
| PIT02:downq90 | l | TIT01:peak | 2.565 | 2.153 | 41 | False | `MID.down.q90 -l-> MID.peak` | — | tennessee_eastman |
| PIT02:upq10 | l | PIT02:downq90 | 2.564 | 1.982 | 47 | True | `MID.up.q10 -l-> MID.down.q90 [same role]` | — | tennessee_eastman, building_59 |
| PIT02:downq10 | l | FT03:peak | 2.564 | 1.936 | 26 | False | `MID.down.q10 -l-> MID.peak` | — | — |
| B4005:upq20 | l | B4022:downq20 | 2.563 | 3.789 | 88 | False | `MID-S.up.q20 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| FCV01D:upq10 | l | B4022:upq20 | 2.558 | 3.98 | 86 | True | `MID-S.up.q10 -l-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| PCV01D:trough | l | FT02:downq20 | 2.557 | 2.95 | 28 | False | `MID-S.trough -l-> MID-S.down.q20` | — | — |
| LCV01D:downq80 | s | FT01Z:trough | 2.557 | 4.303 | 7 | True | `MID.down.q80 -s-> MID.trough` | — | tennessee_eastman |
| PIT02:downq10 | l | PCV01Z:trough | 2.551 | 1.609 | 35 | True | `MID.down.q10 -l-> MID-S.trough` | — | — |
| PIT02:downq10 | l | PCV01D:trough | 2.55 | 1.738 | 36 | True | `MID.down.q10 -l-> MID-S.trough` | — | — |
| FCV01D:downq10 | l | PIT02:upq10 | 2.549 | 4.188 | 35 | True | `MID-S.down.q10 -l-> MID.up.q10` | building_59 | tennessee_eastman |
| FCV01D:downq10 | l | PIT02:upq90 | 2.549 | 2.416 | 35 | True | `MID-S.down.q10 -l-> MID.up.q90` | — | tennessee_eastman, building_59 |
| PIT02:upq90 | l | FCV02Z:downq50 | 2.549 | 3.085 | 31 | True | `MID.up.q90 -l-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| PCV01D:trough | l | B4005:downq20 | 2.536 | 2.819 | 31 | False | `MID-S.trough -l-> MID-S.down.q20` | — | — |
| FT01:upq80 | l | FCV02Z:upq50 | 2.533 | 2.01 | 14 | False | `MID.up.q80 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| FCV03D:peak | l | FCV01Z:trough | 2.531 | 2.5 | 35 | True | `MID.peak -l-> MID-S.trough` | — | tennessee_eastman |
| LIT01:upq80 | m | LCV01D:upq50 | 2.53 | 2.043 | 125 | True | `MID.up.q80 -m-> MID.up.q50` | — | tennessee_eastman |
| FT02:upq20 | l | B4022:downq20 | 2.53 | 3.715 | 85 | False | `MID-S.up.q20 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| B2016:peak | l | PCV01Z:trough | 2.53 | 2.553 | 49 | True | `MID.peak -l-> MID-S.trough` | — | — |
| LCP01D:upq20 | m | LCV01D:downq50 | 2.524 | 2.378 | 44 | False | `MID-S.up.q20 -m-> MID.down.q50` | — | tennessee_eastman, building_59 |
| LIT01:downq80 | m | LCV01D:upq50 | 2.518 | 1.944 | 124 | True | `MID.down.q80 -m-> MID.up.q50` | — | tennessee_eastman |
| PIT02:downq90 | l | B4022:downq20 | 2.516 | 3.234 | 132 | True | `MID.down.q90 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| PIT02:downq90 | l | B4022:upq50 | 2.513 | 3.227 | 113 | True | `MID.down.q90 -l-> SLOW.up.q50` | building_59 | tennessee_eastman |
| FT02Z:upq50 | l | FCV02Z:upq20 | 2.512 | 1.736 | 15 | False | `MID-S.up.q50 -l-> MID-S.up.q20` | — | tennessee_eastman |
| B2016:peak | l | PCV01D:trough | 2.509 | 2.378 | 50 | True | `MID.peak -l-> MID-S.trough` | — | — |
| FT01Z:trough | l | B400B:downq20 | 2.508 | 2.177 | 25 | False | `MID.trough -l-> MID-S.down.q20` | — | tennessee_eastman |
| ST_GOV:trough | s | B400B:downq20 | 2.506 | 2.174 | 8 | True | `MID.trough -s-> MID-S.down.q20` | — | tennessee_eastman |
| ST_GOV:trough | s | FT02:downq20 | 2.506 | 2.174 | 8 | True | `MID.trough -s-> MID-S.down.q20` | — | tennessee_eastman |
| B4022:upq50 | m | PIT02:downq10 | 2.501 | 2.366 | 28 | True | `SLOW.up.q50 -m-> MID.down.q10` | — | tennessee_eastman, building_59 |
| LIT01:downq80 | m | LCV01D:upq80 | 2.498 | 2.102 | 102 | True | `MID.down.q80 -m-> MID.up.q80` | — | tennessee_eastman |
| FCV02Z:upq20 | l | B4022:downq20 | 2.498 | 1.597 | 56 | True | `MID-S.up.q20 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| FCV01D:upq10 | l | FT03Z:peak | 2.498 | 1.548 | 20 | False | `MID-S.up.q10 -l-> MID.peak` | — | tennessee_eastman |
| LIT01:upq20 | s | LCV01Z:downq20 | 2.497 | 3.052 | 13 | True | `MID.up.q20 -s-> MID.down.q20` | — | tennessee_eastman |
| B2016:trough | m | B4022:upq50 | 2.496 | 3.322 | 81 | True | `MID.trough -m-> SLOW.up.q50` | — | tennessee_eastman |
| TIT02:upq20 | l | FCV03Z:trough | 2.496 | 2.04 | 32 | True | `MID.up.q20 -l-> MID.trough` | — | building_59 |
| FT03:peak | l | PCV01Z:peak | 2.495 | 2.851 | 38 | False | `MID.peak -l-> MID-S.peak` | — | — |
| B4022:downq80 | l | B2016:peak | 2.492 | 1.849 | 44 | False | `SLOW.down.q80 -l-> MID.peak` | — | tennessee_eastman |
| PIT02:upq90 | l | B4022:upq50 | 2.485 | 3.359 | 111 | True | `MID.up.q90 -l-> SLOW.up.q50` | building_59 | tennessee_eastman |
| FT02:downq50 | m | B4022:upq20 | 2.483 | 2.844 | 30 | True | `MID-S.down.q50 -m-> SLOW.up.q20` | — | tennessee_eastman |
| FT02Z:downq50 | m | B4022:upq20 | 2.483 | 2.855 | 30 | True | `MID-S.down.q50 -m-> SLOW.up.q20` | — | tennessee_eastman |
| B400B:downq50 | m | B4022:upq20 | 2.483 | 2.855 | 30 | True | `MID-S.down.q50 -m-> SLOW.up.q20` | — | tennessee_eastman |
| B4022:downq50 | m | B2016:trough | 2.477 | 2.188 | 67 | True | `SLOW.down.q50 -m-> MID.trough` | — | tennessee_eastman |
| FT02:downq20 | l | PCV01Z:peak | 2.477 | 1.854 | 28 | False | `MID-S.down.q20 -l-> MID-S.peak` | — | — |
| LD:trough | s | VXT03:upq80 | 2.476 | 1.85 | 9 | False | `MID.trough -s-> SLOW.up.q80` | — | — |
| PIT02:upq90 | l | FCV01Z:peak | 2.474 | 2.984 | 35 | True | `MID.up.q90 -l-> MID-S.peak` | — | tennessee_eastman |
| LIT01:upq80 | s | LCV01Z:downq80 | 2.467 | 1.634 | 7 | True | `MID.up.q80 -s-> MID.down.q80` | — | tennessee_eastman |
| FT03Z:peak | l | FCV02Z:upq80 | 2.466 | 2.538 | 22 | False | `MID.peak -l-> MID-S.up.q80` | — | tennessee_eastman |
| LIT01:downq80 | l | LCP01D:upq50 | 2.465 | 2.67 | 86 | False | `MID.down.q80 -l-> MID-S.up.q50` | — | tennessee_eastman |
| LCV01D:downq80 | m | LCP01D:upq80 | 2.465 | 2.106 | 54 | True | `MID.down.q80 -m-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| FT03Z:peak | l | PCV01Z:peak | 2.465 | 2.848 | 37 | False | `MID.peak -l-> MID-S.peak` | — | — |
| LCV01Z:upq80 | l | B4022:downq50 | 2.461 | 3.204 | 69 | True | `MID.up.q80 -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| B4022:downq50 | m | PIT02:downq90 | 2.46 | 1.534 | 29 | True | `SLOW.down.q50 -m-> MID.down.q90` | — | tennessee_eastman, building_59 |
| PIT02:downq90 | m | B4022:downq20 | 2.459 | 2.546 | 44 | True | `MID.down.q90 -m-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| B4022:upq20 | m | B400B:upq50 | 2.458 | 1.876 | 18 | False | `SLOW.up.q20 -m-> MID-S.up.q50` | — | tennessee_eastman |
| B4022:upq20 | m | FT02:upq50 | 2.458 | 1.876 | 18 | False | `SLOW.up.q20 -m-> MID-S.up.q50` | — | tennessee_eastman |
| FT02:upq50 | l | B4022:downq20 | 2.451 | 2.877 | 106 | True | `MID-S.up.q50 -l-> SLOW.down.q20` | — | tennessee_eastman |
| FT02Z:upq50 | l | B4022:downq20 | 2.451 | 2.877 | 106 | True | `MID-S.up.q50 -l-> SLOW.down.q20` | — | tennessee_eastman |
| FT01:downq50 | l | B4022:downq50 | 2.446 | 3.275 | 62 | True | `MID.down.q50 -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| TIT01:peak | l | B4022:upq50 | 2.441 | 2.795 | 106 | True | `MID.peak -l-> SLOW.up.q50` | — | tennessee_eastman |
| B2016:trough | m | LCV01Z:downq20 | 2.44 | 3.289 | 55 | True | `MID.trough -m-> MID.down.q20` | — | tennessee_eastman |
| LCV01D:upq50 | l | B2004:upq20 | 2.44 | 3.064 | 9 | False | `MID.up.q50 -l-> SET.up.q20` | — | — |
| B4022:downq50 | l | PCV01D:peak | 2.437 | 2.221 | 27 | False | `SLOW.down.q50 -l-> MID-S.peak` | — | — |
| B4022:downq50 | m | PCV01D:trough | 2.437 | 1.836 | 24 | True | `SLOW.down.q50 -m-> MID-S.trough` | — | — |
| LCV01D:downq20 | m | LIT01:upq80 | 2.436 | 2.175 | 116 | True | `MID.down.q20 -m-> MID.up.q80` | tennessee_eastman | — |
| FT03:peak | l | FCV02Z:upq80 | 2.431 | 2.54 | 22 | False | `MID.peak -l-> MID-S.up.q80` | — | — |
| ST_PT01:trough | s | PCV01Z:trough | 2.429 | 3.271 | 17 | True | `MID.trough -s-> MID-S.trough` | — | — |
| PCV01D:peak | s | PIT01:peak | 2.425 | 3.151 | 14 | True | `MID-S.peak -s-> MID.peak` | — | — |
| LIT01:downq80 | l | B2004:upq20 | 2.423 | 3.685 | 5 | True | `MID.down.q80 -l-> SET.up.q20` | — | — |
| PCV01D:trough | s | PIT01:trough | 2.418 | 1.977 | 20 | True | `MID-S.trough -s-> MID.trough` | — | — |
| PIT02:upq10 | l | PCV01D:trough | 2.417 | 1.582 | 37 | True | `MID.up.q10 -l-> MID-S.trough` | — | — |
| LCV01Z:downq50 | l | B4022:downq20 | 2.416 | 3.217 | 93 | True | `MID.down.q50 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| FCV01Z:peak | l | B4022:upq20 | 2.413 | 2.443 | 117 | True | `MID-S.peak -l-> SLOW.up.q20` | — | tennessee_eastman |
| FT01:downq20 | l | LCV01D:upq20 | 2.412 | 2.176 | 50 | True | `MID.down.q20 -l-> MID.up.q20` | — | tennessee_eastman, building_59 |
| TIT01:peak | m | B4022:upq20 | 2.408 | 2.083 | 37 | True | `MID.peak -m-> SLOW.up.q20` | — | tennessee_eastman |
| LIT01:downq20 | m | LCV01D:downq50 | 2.406 | 2.304 | 109 | True | `MID.down.q20 -m-> MID.down.q50` | — | tennessee_eastman |
| LCV01Z:upq80 | l | B2016:peak | 2.403 | 2.07 | 73 | True | `MID.up.q80 -l-> MID.peak` | — | tennessee_eastman |
| LIT01:upq80 | l | B2004:downq20 | 2.402 | 3.418 | 5 | True | `MID.up.q80 -l-> SET.down.q20` | — | — |
| PCV01Z:trough | s | PIT01:trough | 2.401 | 1.867 | 19 | True | `MID-S.trough -s-> MID.trough` | — | — |
| B400B:downq80 | m | FT03:peak | 2.398 | 2.976 | 9 | False | `MID-S.down.q80 -m-> MID.peak` | — | — |
| B4005:upq50 | l | B4022:downq20 | 2.397 | 3.151 | 104 | True | `MID-S.up.q50 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| FT03Z:peak | l | B4005:downq20 | 2.394 | 2.649 | 25 | True | `MID.peak -l-> MID-S.down.q20` | — | tennessee_eastman |
| LCP01D:downq80 | l | LCV01D:downq80 | 2.393 | 1.686 | 84 | False | `MID-S.down.q80 -l-> MID.down.q80` | — | tennessee_eastman, building_59 |
| PCV01Z:trough | l | PCV01D:peak | 2.39 | 2.137 | 43 | False | `MID-S.trough -l-> MID-S.peak` | — | — |
| FCV03D:trough | l | LCV01Z:upq80 | 2.389 | 3.314 | 45 | False | `MID.trough -l-> MID.up.q80` | building_59 | tennessee_eastman |
| LCV01D:downq20 | l | LIT01:downq20 | 2.386 | 2.099 | 164 | True | `MID.down.q20 -l-> MID.down.q20` | — | tennessee_eastman |
| ST_LD:peak | s | LCV01D:downq80 | 2.386 | 2.706 | 36 | True | `MID.peak -s-> MID.down.q80` | — | tennessee_eastman |
| TIT01:trough | l | FT01:upq50 | 2.386 | 3.092 | 24 | False | `MID.trough -l-> MID.up.q50` | — | tennessee_eastman |
| ST_PT01:peak | l | B3005:downq10 | 2.386 | 4.543 | 4 | False | `MID.peak -l-> SET.down.q10` | — | tennessee_eastman |
| PIT02:upq90 | l | FT02Z:downq50 | 2.385 | 1.543 | 29 | False | `MID.up.q90 -l-> MID-S.down.q50` | — | tennessee_eastman |
| FCV01D:upq10 | l | FT03Z:trough | 2.373 | 1.548 | 19 | False | `MID-S.up.q10 -l-> MID.trough` | — | tennessee_eastman |
| B4022:downq20 | m | PIT02:upq90 | 2.37 | 1.981 | 31 | True | `SLOW.down.q20 -m-> MID.up.q90` | — | tennessee_eastman, building_59 |
| LCV01D:downq50 | m | LIT01:upq80 | 2.369 | 2.143 | 147 | True | `MID.down.q50 -m-> MID.up.q80` | — | tennessee_eastman |
| B2016:peak | m | B4022:downq20 | 2.365 | 2.798 | 84 | True | `MID.peak -m-> SLOW.down.q20` | — | tennessee_eastman |
| LCV01Z:downq50 | l | B4022:upq20 | 2.364 | 3.02 | 91 | True | `MID.down.q50 -l-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| FCV02Z:upq50 | m | B4022:downq20 | 2.364 | 3.068 | 25 | False | `MID-S.up.q50 -m-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| PIT02:upq90 | m | B4022:upq20 | 2.361 | 2.915 | 42 | False | `MID.up.q90 -m-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| B4022:upq20 | m | PIT02:upq90 | 2.361 | 1.854 | 30 | True | `SLOW.up.q20 -m-> MID.up.q90` | — | tennessee_eastman, building_59 |
| FT03:peak | l | B4005:upq20 | 2.359 | 2.652 | 25 | True | `MID.peak -l-> MID-S.up.q20` | — | — |
| B3004:downq50 | s | LIT01:downq20 | 2.359 | 4.212 | 4 | True | `SET.down.q50 -s-> MID.down.q20` | — | tennessee_eastman |
| PIT01:peak | l | B3005:downq10 | 2.358 | 6.02 | 4 | False | `MID.peak -l-> SET.down.q10` | — | tennessee_eastman |
| FCV01D:downq10 | l | FT03Z:peak | 2.353 | 1.917 | 19 | False | `MID-S.down.q10 -l-> MID.peak` | — | tennessee_eastman |
| PIT02:upq90 | l | B4022:downq50 | 2.351 | 3.464 | 105 | True | `MID.up.q90 -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| HT_LD:trough | s | VYT03:upq50 | 2.351 | 3.626 | 11 | False | `MID-S.trough -s-> SLOW.up.q50` | — | — |
| B3004:upq50 | s | LCV01D:downq20 | 2.35 | 3.816 | 6 | True | `SET.up.q50 -s-> MID.down.q20` | — | tennessee_eastman |
| B3004:upq80 | s | LCV01D:downq80 | 2.35 | 2.185 | 5 | True | `SET.up.q80 -s-> MID.down.q80` | — | tennessee_eastman |
| TIT01:peak | l | B4022:downq50 | 2.349 | 2.795 | 102 | True | `MID.peak -l-> SLOW.down.q50` | — | tennessee_eastman |
| ST_TT01:downq10 | m | B400B:downq80 | 2.349 | 1.82 | 18 | True | `MID.down.q10 -m-> MID-S.down.q80` | — | tennessee_eastman |
| PIT02:downq90 | m | B4022:downq50 | 2.347 | 3.367 | 36 | True | `MID.down.q90 -m-> SLOW.down.q50` | building_59 | tennessee_eastman |
| LIT01:downq50 | m | LCV01D:downq80 | 2.344 | 1.758 | 126 | True | `MID.down.q50 -m-> MID.down.q80` | — | tennessee_eastman |
| TIT01:trough | m | PIT02:downq10 | 2.339 | 4.567 | 16 | True | `MID.trough -m-> MID.down.q10` | — | tennessee_eastman |
| FT01Z:trough | l | PIT02:upq10 | 2.335 | 2.102 | 46 | True | `MID.trough -l-> MID.up.q10` | — | tennessee_eastman |
| FCV01Z:peak | l | B4022:downq20 | 2.331 | 2.305 | 113 | True | `MID-S.peak -l-> SLOW.down.q20` | — | tennessee_eastman |
| FT01Z:trough | l | LCV01Z:upq20 | 2.331 | 2.951 | 67 | True | `MID.trough -l-> MID.up.q20` | — | tennessee_eastman |
| LCV01D:upq20 | l | LIT01:upq20 | 2.326 | 2.171 | 151 | True | `MID.up.q20 -l-> MID.up.q20` | — | tennessee_eastman |
| LIT01:upq20 | l | LIT01:downq20 | 2.326 | 1.889 | 133 | True | `MID.up.q20 -l-> MID.down.q20 [same role]` | tennessee_eastman | — |
| LCV01D:upq80 | s | FCV01D:downq10 | 2.321 | 2.77 | 5 | False | `MID.up.q80 -s-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| LIT01:upq20 | s | LCV01D:downq20 | 2.32 | 2.837 | 26 | True | `MID.up.q20 -s-> MID.down.q20` | — | tennessee_eastman |
| ST_LD:peak | s | VXT02:downq80 | 2.32 | 1.578 | 10 | True | `MID.peak -s-> SLOW.down.q80` | — | tennessee_eastman |
| LCP01D:upq50 | l | LCV01D:upq50 | 2.313 | 1.684 | 117 | True | `MID-S.up.q50 -l-> MID.up.q50` | — | tennessee_eastman, building_59 |
| B2016:peak | l | TIT02:downq20 | 2.313 | 1.545 | 37 | True | `MID.peak -l-> MID.down.q20` | — | tennessee_eastman |
| LCV01D:downq50 | s | LCV01D:downq20 | 2.312 | 4.011 | 33 | True | `MID.down.q50 -s-> MID.down.q20 [same role]` | tennessee_eastman | building_59 |
| FCV03Z:trough | s | LCV01D:downq20 | 2.309 | 2.358 | 11 | True | `MID.trough -s-> MID.down.q20` | — | building_59 |
| LIT01:downq80 | s | FT01Z:trough | 2.305 | 2.501 | 5 | True | `MID.down.q80 -s-> MID.trough` | — | tennessee_eastman |
| LIT01:upq80 | l | LCV01D:downq80 | 2.304 | 1.756 | 119 | True | `MID.up.q80 -l-> MID.down.q80` | — | tennessee_eastman |
| PIT02:upq90 | m | B4022:downq20 | 2.304 | 3.461 | 41 | False | `MID.up.q90 -m-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:upq80 | m | B4022:upq50 | 2.297 | 4.314 | 28 | True | `MID.up.q80 -m-> SLOW.up.q50` | — | tennessee_eastman, building_59 |
| LCV01Z:upq20 | m | B2016:trough | 2.295 | 2.315 | 35 | True | `MID.up.q20 -m-> MID.trough` | — | tennessee_eastman |
| PIT02:upq90 | m | B4022:downq50 | 2.295 | 3.188 | 35 | True | `MID.up.q90 -m-> SLOW.down.q50` | building_59 | tennessee_eastman |
| ST_TT01:upq10 | m | PIT02:downq10 | 2.293 | 3.227 | 26 | True | `MID.up.q10 -m-> MID.down.q10` | — | tennessee_eastman, building_59 |
| LCP01D:upq50 | m | PIT01:peak | 2.292 | 1.819 | 83 | True | `MID-S.up.q50 -m-> MID.peak` | — | tennessee_eastman |
| B4022:downq50 | m | PIT02:upq90 | 2.29 | 1.534 | 27 | True | `SLOW.down.q50 -m-> MID.up.q90` | building_59 | tennessee_eastman |
| FT01Z:trough | l | FT02:downq50 | 2.289 | 1.563 | 26 | False | `MID.trough -l-> MID-S.down.q50` | — | tennessee_eastman |
| FT01Z:trough | s | LCV01D:upq50 | 2.289 | 1.721 | 15 | True | `MID.trough -s-> MID.up.q50` | — | tennessee_eastman |
| LIT01:upq80 | l | LIT01:downq20 | 2.285 | 2.085 | 115 | False | `MID.up.q80 -l-> MID.down.q20 [same role]` | — | tennessee_eastman |
| TIT02:upq20 | l | B4022:downq20 | 2.279 | 2.571 | 118 | True | `MID.up.q20 -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| TIT02:downq20 | l | FCV03Z:trough | 2.279 | 2.475 | 32 | True | `MID.down.q20 -l-> MID.trough` | — | building_59 |
| HT_PO:peak | s | LCV01D:downq80 | 2.274 | 1.894 | 46 | True | `MID-S.peak -s-> MID.down.q80` | — | — |
| TIT01:trough | l | B4022:upq20 | 2.271 | 2.42 | 123 | True | `MID.trough -l-> SLOW.up.q20` | — | tennessee_eastman |
| LCV01D:downq20 | m | LIT01:downq80 | 2.268 | 2.175 | 108 | True | `MID.down.q20 -m-> MID.down.q80` | — | tennessee_eastman |
| TIT02:upq20 | l | B4022:upq20 | 2.26 | 2.433 | 117 | True | `MID.up.q20 -l-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| FCV03D:trough | l | B4022:downq50 | 2.26 | 3.025 | 97 | False | `MID.trough -l-> SLOW.down.q50` | — | tennessee_eastman, building_59 |
| LIT01:downq80 | l | LIT01:upq50 | 2.259 | 2.268 | 178 | True | `MID.down.q80 -l-> MID.up.q50 [same role]` | — | tennessee_eastman |
| FT01:downq50 | l | B2016:trough | 2.258 | 1.9 | 62 | True | `MID.down.q50 -l-> MID.trough` | — | tennessee_eastman |
| LCV01D:downq50 | s | LIT01:downq50 | 2.244 | 2.676 | 50 | True | `MID.down.q50 -s-> MID.down.q50` | — | tennessee_eastman |
| FCV03D:trough | l | B4022:downq20 | 2.237 | 2.743 | 112 | False | `MID.trough -l-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| FT02:downq50 | m | B4022:downq20 | 2.235 | 2.844 | 27 | False | `MID-S.down.q50 -m-> SLOW.down.q20` | — | tennessee_eastman |
| B400B:downq50 | m | B4022:downq20 | 2.235 | 2.855 | 27 | False | `MID-S.down.q50 -m-> SLOW.down.q20` | — | tennessee_eastman |
| LCV01D:downq80 | m | LCV01Z:upq80 | 2.233 | 4.159 | 28 | True | `MID.down.q80 -m-> MID.up.q80` | tennessee_eastman | building_59 |
| LCV01D:upq50 | s | FT03Z:peak | 2.231 | 3.044 | 7 | False | `MID.up.q50 -s-> MID.peak` | — | tennessee_eastman |
| FT01:upq80 | l | B2016:trough | 2.228 | 1.515 | 49 | False | `MID.up.q80 -l-> MID.trough` | — | tennessee_eastman |
| PIT02:upq90 | m | LCV01Z:downq50 | 2.227 | 1.804 | 20 | False | `MID.up.q90 -m-> MID.down.q50` | building_59 | tennessee_eastman |
| ST_PT01:trough | s | PCV01D:trough | 2.221 | 3.179 | 16 | True | `MID.trough -s-> MID-S.trough` | — | — |
| FCV03D:trough | l | B4022:upq20 | 2.217 | 2.543 | 111 | False | `MID.trough -l-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| LIT01:upq20 | l | FT01:upq20 | 2.216 | 1.61 | 20 | False | `MID.up.q20 -l-> MID.up.q20` | — | tennessee_eastman |
| ST_LD:peak | s | B400B:downq50 | 2.216 | 2.512 | 6 | False | `MID.peak -s-> MID-S.down.q50` | — | tennessee_eastman |
| B2016:trough | l | B4022:downq50 | 2.215 | 3.115 | 108 | True | `MID.trough -l-> SLOW.down.q50` | — | tennessee_eastman |
| LCP01D:upq80 | m | PIT01:peak | 2.213 | 1.823 | 54 | False | `MID-S.up.q80 -m-> MID.peak` | — | tennessee_eastman |
| LCV01D:upq80 | m | LCP01D:upq20 | 2.211 | 1.813 | 41 | True | `MID.up.q80 -m-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| FT01:upq50 | m | LCV01D:downq80 | 2.209 | 1.567 | 22 | True | `MID.up.q50 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| B2016:peak | l | B4022:upq20 | 2.206 | 2.761 | 130 | True | `MID.peak -l-> SLOW.up.q20` | — | tennessee_eastman |
| B2016:peak | l | FCV01D:upq10 | 2.206 | 2.097 | 26 | True | `MID.peak -l-> MID-S.up.q10` | — | tennessee_eastman |
| ST_TT01:upq10 | m | PIT02:downq90 | 2.205 | 2.234 | 25 | True | `MID.up.q10 -m-> MID.down.q90` | — | tennessee_eastman, building_59 |
| LCV01D:upq80 | m | LIT01:downq20 | 2.203 | 2.34 | 97 | True | `MID.up.q80 -m-> MID.down.q20` | — | tennessee_eastman |
| LCV01D:downq80 | m | LCP01D:upq50 | 2.201 | 1.563 | 65 | True | `MID.down.q80 -m-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| LCV01D:downq50 | m | LCV01D:upq50 | 2.2 | 2.23 | 129 | True | `MID.down.q50 -m-> MID.up.q50 [same role]` | — | tennessee_eastman, building_59 |
| LCP01D:downq20 | m | PIT01:trough | 2.2 | 1.632 | 47 | False | `MID-S.down.q20 -m-> MID.trough` | — | tennessee_eastman |
| LCV01D:upq50 | s | FT01Z:peak | 2.198 | 1.968 | 8 | True | `MID.up.q50 -s-> MID.peak` | — | tennessee_eastman |
| FCV01Z:peak | l | PCV01D:trough | 2.196 | 1.909 | 36 | True | `MID-S.peak -l-> MID-S.trough` | — | fingrid |
| B2004:downq20 | s | LCV01D:upq50 | 2.196 | 1.699 | 5 | True | `SET.down.q20 -s-> MID.up.q50` | — | building_59 |
| LCV01D:upq50 | m | LCV01D:downq50 | 2.193 | 2.219 | 137 | True | `MID.up.q50 -m-> MID.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| FT03Z:peak | l | B2016:peak | 2.192 | 2.371 | 93 | True | `MID.peak -l-> MID.peak` | — | tennessee_eastman |
| PIT01:peak | s | LCP01D:upq80 | 2.186 | 2.596 | 15 | False | `MID.peak -s-> MID-S.up.q80` | — | tennessee_eastman |
| FT03:peak | l | PIT02:downq10 | 2.185 | 1.906 | 41 | True | `MID.peak -l-> MID.down.q10` | — | — |
| FT03:peak | l | B2016:peak | 2.184 | 2.373 | 94 | True | `MID.peak -l-> MID.peak` | — | — |
| B2016:peak | l | B4022:upq50 | 2.177 | 2.977 | 110 | True | `MID.peak -l-> SLOW.up.q50` | — | tennessee_eastman |
| LCV01D:upq20 | s | LCV01D:upq50 | 2.176 | 2.295 | 32 | True | `MID.up.q20 -s-> MID.up.q50 [same role]` | tennessee_eastman | building_59 |
| B4022:upq20 | m | PCV01D:trough | 2.167 | 2.034 | 23 | True | `SLOW.up.q20 -m-> MID-S.trough` | — | — |
| PCV01Z:peak | s | LCV01D:downq80 | 2.163 | 2.502 | 10 | True | `MID-S.peak -s-> MID.down.q80` | — | — |
| B3004:upq50 | m | PIT01:peak | 2.162 | 2.037 | 11 | False | `SET.up.q50 -m-> MID.peak` | — | tennessee_eastman |
| LCV01D:upq50 | m | FT01:downq50 | 2.161 | 3.744 | 16 | True | `MID.up.q50 -m-> MID.down.q50` | — | tennessee_eastman, building_59 |
| HT_PO:trough | s | LCV01D:upq20 | 2.158 | 2.726 | 44 | True | `MID-S.trough -s-> MID.up.q20` | — | — |
| FT01Z:trough | s | PIT01:peak | 2.145 | 3.025 | 18 | True | `MID.trough -s-> MID.peak` | — | tennessee_eastman |
| FT01:upq80 | m | LCV01D:downq80 | 2.145 | 3.525 | 18 | True | `MID.up.q80 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| B2016:peak | l | LCV01Z:downq20 | 2.138 | 2.643 | 75 | True | `MID.peak -l-> MID.down.q20` | — | tennessee_eastman |
| LCV01D:upq80 | m | LCP01D:downq20 | 2.138 | 1.677 | 40 | False | `MID.up.q80 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| B2004:upq50 | s | LCV01D:downq80 | 2.132 | 3.447 | 4 | False | `SET.up.q50 -s-> MID.down.q80` | — | — |
| B4022:upq20 | m | B2016:peak | 2.127 | 2.088 | 62 | True | `SLOW.up.q20 -m-> MID.peak` | — | tennessee_eastman |
| LCP01D:downq80 | m | LCV01D:upq20 | 2.121 | 2.732 | 35 | False | `MID-S.down.q80 -m-> MID.up.q20` | building_59 | tennessee_eastman |
| LIT01:downq50 | l | LCP01D:upq80 | 2.114 | 1.611 | 58 | False | `MID.down.q50 -l-> MID-S.up.q80` | — | tennessee_eastman |
| B4005:downq50 | m | B4022:downq20 | 2.112 | 3.055 | 28 | False | `MID-S.down.q50 -m-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:upq80 | m | LCV01D:downq80 | 2.109 | 1.829 | 39 | True | `MID.up.q80 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| PCV01Z:peak | s | PIT01:peak | 2.109 | 2.71 | 15 | True | `MID-S.peak -s-> MID.peak` | — | — |
| LIT01:downq20 | m | LCV01D:downq20 | 2.106 | 1.996 | 78 | True | `MID.down.q20 -m-> MID.down.q20` | — | tennessee_eastman |
| LCV01D:downq50 | l | B2004:upq20 | 2.101 | 2.861 | 8 | False | `MID.down.q50 -l-> SET.up.q20` | — | — |
| LCV01Z:downq20 | l | LCV01D:downq20 | 2.095 | 1.787 | 57 | True | `MID.down.q20 -l-> MID.down.q20` | — | tennessee_eastman, building_59 |
| TIT01:peak | m | B4022:downq20 | 2.082 | 2.462 | 32 | False | `MID.peak -m-> SLOW.down.q20` | — | tennessee_eastman |
| HT_PO:trough | s | CO_rpm:trough | 2.08 | 2.386 | 25 | False | `MID-S.trough -s-> MID.trough` | — | — |
| HT_PO:peak | s | VXT02:upq80 | 2.076 | 1.989 | 12 | True | `MID-S.peak -s-> SLOW.up.q80` | — | — |
| FT01:upq50 | s | LCV01D:upq50 | 2.076 | 1.939 | 11 | True | `MID.up.q50 -s-> MID.up.q50` | — | tennessee_eastman, building_59 |
| B2004:downq20 | s | LIT01:upq80 | 2.076 | 1.606 | 5 | True | `SET.down.q20 -s-> MID.up.q80` | — | — |
| B2004:downq20 | s | LIT01:downq80 | 2.076 | 2.141 | 5 | True | `SET.down.q20 -s-> MID.down.q80` | — | — |
| LCP01D:downq50 | m | LCV01D:upq50 | 2.071 | 2.027 | 60 | False | `MID-S.down.q50 -m-> MID.up.q50` | — | tennessee_eastman, building_59 |
| LCV01D:downq50 | m | LCP01D:upq80 | 2.067 | 1.651 | 51 | True | `MID.down.q50 -m-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| ST_TT01:upq10 | l | FCV01D:downq10 | 2.063 | 2.258 | 42 | True | `MID.up.q10 -l-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| ST_TT01:upq10 | l | FCV01D:upq10 | 2.063 | 2.258 | 42 | True | `MID.up.q10 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| LIT01:upq80 | m | LCV01D:upq20 | 2.056 | 2.542 | 83 | True | `MID.up.q80 -m-> MID.up.q20` | — | tennessee_eastman |
| B2004:downq50 | s | LIT01:downq80 | 2.055 | 1.968 | 5 | True | `SET.down.q50 -s-> MID.down.q80` | — | — |
| LIT01:downq50 | m | LCV01D:downq50 | 2.053 | 1.831 | 133 | True | `MID.down.q50 -m-> MID.down.q50` | — | tennessee_eastman |
| LIT01:upq20 | m | LCV01D:upq20 | 2.046 | 2.121 | 71 | True | `MID.up.q20 -m-> MID.up.q20` | — | tennessee_eastman |
| HT_PO:trough | s | SIT02:trough | 2.043 | 1.752 | 23 | False | `MID-S.trough -s-> MID.trough` | — | — |
| LCV01D:upq20 | l | LCV01D:downq80 | 2.041 | 1.733 | 136 | False | `MID.up.q20 -l-> MID.down.q80 [same role]` | — | tennessee_eastman, building_59 |
| B2004:downq50 | s | LIT01:downq50 | 2.037 | 1.626 | 6 | True | `SET.down.q50 -s-> MID.down.q50` | — | — |
| LIT01:upq50 | m | LCV01D:upq20 | 2.028 | 2.256 | 102 | True | `MID.up.q50 -m-> MID.up.q20` | — | tennessee_eastman |
| LCV01D:upq20 | m | LIT01:downq50 | 2.026 | 1.884 | 124 | True | `MID.up.q20 -m-> MID.down.q50` | — | tennessee_eastman |
| LCV01D:upq80 | s | LCV01Z:downq50 | 2.023 | 2.195 | 11 | True | `MID.up.q80 -s-> MID.down.q50` | — | tennessee_eastman, building_59 |
| LCV01D:upq50 | s | LCV01Z:downq80 | 2.017 | 2.89 | 10 | False | `MID.up.q50 -s-> MID.down.q80` | — | tennessee_eastman, building_59 |
| LCV01D:upq50 | m | LCV01D:upq80 | 2.014 | 1.834 | 104 | True | `MID.up.q50 -m-> MID.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| LIT01:downq80 | l | LCV01D:downq80 | 2.011 | 2.153 | 103 | False | `MID.down.q80 -l-> MID.down.q80` | — | tennessee_eastman |
| LCV01D:downq50 | m | FT01:upq50 | 2.008 | 4.305 | 14 | False | `MID.down.q50 -m-> MID.up.q50` | — | tennessee_eastman, building_59 |
| LIT01:downq20 | l | LCV01D:upq50 | 2.005 | 1.87 | 146 | False | `MID.down.q20 -l-> MID.up.q50` | — | tennessee_eastman |
| LCV01D:upq80 | l | LIT01:downq80 | 1.998 | 2.047 | 227 | True | `MID.up.q80 -l-> MID.down.q80` | — | tennessee_eastman |
| ST_PT01:trough | s | LCV01Z:upq80 | 1.996 | 2.337 | 16 | True | `MID.trough -s-> MID.up.q80` | — | tennessee_eastman |
| LCV01D:upq20 | s | LIT01:downq80 | 1.992 | 1.953 | 31 | True | `MID.up.q20 -s-> MID.down.q80` | — | tennessee_eastman |
| LCV01D:upq20 | m | LCP01D:downq80 | 1.989 | 1.911 | 40 | True | `MID.up.q20 -m-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| LCV01D:upq20 | m | LIT01:downq80 | 1.978 | 1.785 | 100 | True | `MID.up.q20 -m-> MID.down.q80` | tennessee_eastman | — |
| ST_LD:trough | s | B2016:trough | 1.978 | 1.92 | 22 | False | `MID.trough -s-> MID.trough` | — | tennessee_eastman |
| LIT01:upq50 | l | LCP01D:downq20 | 1.975 | 1.842 | 44 | False | `MID.up.q50 -l-> MID-S.down.q20` | — | tennessee_eastman |
| LIT01:downq50 | s | PCV01Z:trough | 1.975 | 1.645 | 7 | True | `MID.down.q50 -s-> MID-S.trough` | — | — |
| LCP01D:downq80 | m | PIT01:trough | 1.972 | 1.674 | 51 | False | `MID-S.down.q80 -m-> MID.trough` | — | tennessee_eastman |
| LCV01D:downq80 | m | LCV01D:upq80 | 1.968 | 2.37 | 85 | True | `MID.down.q80 -m-> MID.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| ST_TT01:upq10 | l | B400B:upq20 | 1.967 | 2.647 | 41 | True | `MID.up.q10 -l-> MID-S.up.q20` | — | tennessee_eastman |
| ST_TT01:upq10 | l | FT02:upq20 | 1.967 | 2.536 | 41 | True | `MID.up.q10 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| ST_TT01:upq10 | l | FT02Z:upq20 | 1.967 | 2.647 | 41 | True | `MID.up.q10 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| ST_TT01:upq10 | l | PIT02:upq10 | 1.966 | 2.455 | 81 | True | `MID.up.q10 -l-> MID.up.q10` | — | tennessee_eastman, building_59 |
| ST_LD:trough | s | LCV01D:upq20 | 1.963 | 1.677 | 30 | True | `MID.trough -s-> MID.up.q20` | — | tennessee_eastman |
| TIT01:peak | m | B2016:trough | 1.962 | 2.243 | 28 | True | `MID.peak -m-> MID.trough` | — | tennessee_eastman, physionet_slp |
| ST_TT01:downq10 | l | B400B:downq20 | 1.951 | 2.719 | 42 | True | `MID.down.q10 -l-> MID-S.down.q20` | — | tennessee_eastman |
| ST_TT01:downq10 | l | FT02:downq20 | 1.951 | 2.601 | 42 | True | `MID.down.q10 -l-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| ST_TT01:downq10 | l | FT02Z:downq20 | 1.951 | 2.719 | 42 | True | `MID.down.q10 -l-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| ST_TT01:downq10 | l | FCV01D:downq10 | 1.95 | 2.179 | 41 | True | `MID.down.q10 -l-> MID-S.down.q10` | — | tennessee_eastman, building_59 |
| LCV01D:upq50 | m | LCV01D:downq80 | 1.949 | 2.006 | 101 | True | `MID.up.q50 -m-> MID.down.q80 [same role]` | tennessee_eastman | building_59 |
| LIT01:upq80 | s | FT01:downq20 | 1.942 | 5.004 | 3 | False | `MID.up.q80 -s-> MID.down.q20` | — | tennessee_eastman |
| PIT01:peak | m | PIT01:trough | 1.941 | 2.14 | 230 | True | `MID.peak -m-> MID.trough [same role]` | — | tennessee_eastman |
| ST_PO:peak | m | B3005:upq90 | 1.941 | 2.55 | 5 | False | `MID.peak -m-> SET.up.q90` | — | — |
| ST_TT01:upq10 | l | B4005:upq20 | 1.934 | 2.47 | 45 | True | `MID.up.q10 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| B3004:upq80 | s | LIT01:upq20 | 1.93 | 2.242 | 4 | True | `SET.up.q80 -s-> MID.up.q20` | — | tennessee_eastman |
| LCP01D:upq50 | l | LCV01D:downq20 | 1.928 | 2.053 | 80 | True | `MID-S.up.q50 -l-> MID.down.q20` | — | tennessee_eastman, building_59 |
| LCV01D:upq20 | s | LIT01:upq80 | 1.928 | 2.17 | 30 | True | `MID.up.q20 -s-> MID.up.q80` | tennessee_eastman | — |
| LCV01D:downq80 | l | LIT01:downq80 | 1.923 | 2.141 | 220 | True | `MID.down.q80 -l-> MID.down.q80` | — | tennessee_eastman |
| LCV01D:upq50 | l | LCP01D:downq80 | 1.923 | 1.954 | 89 | True | `MID.up.q50 -l-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| LCV01D:downq20 | l | LCV01D:upq80 | 1.921 | 1.679 | 135 | False | `MID.down.q20 -l-> MID.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| LIT01:downq50 | s | PCV01D:trough | 1.92 | 2.132 | 7 | True | `MID.down.q50 -s-> MID-S.trough` | — | — |
| LCV01D:upq50 | m | LIT01:downq50 | 1.919 | 2.289 | 153 | True | `MID.up.q50 -m-> MID.down.q50` | — | tennessee_eastman |
| LCV01D:downq20 | l | LCV01D:downq50 | 1.918 | 1.631 | 163 | False | `MID.down.q20 -l-> MID.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| LCV01D:downq80 | m | LCV01D:downq50 | 1.915 | 1.882 | 100 | True | `MID.down.q80 -m-> MID.down.q50 [same role]` | — | tennessee_eastman, building_59 |
| LCV01D:downq20 | l | LCV01D:downq80 | 1.914 | 1.726 | 135 | False | `MID.down.q20 -l-> MID.down.q80 [same role]` | — | tennessee_eastman, building_59 |
| LCV01D:upq80 | l | LIT01:upq80 | 1.91 | 1.987 | 217 | True | `MID.up.q80 -l-> MID.up.q80` | — | tennessee_eastman |
| B3004:upq80 | s | LCV01D:downq20 | 1.908 | 2.217 | 4 | False | `SET.up.q80 -s-> MID.down.q20` | — | tennessee_eastman |
| ST_TT01:downq10 | l | FCV01D:upq10 | 1.902 | 1.815 | 40 | True | `MID.down.q10 -l-> MID-S.up.q10` | — | tennessee_eastman, building_59 |
| LCV01D:downq80 | s | LIT01:downq50 | 1.899 | 1.572 | 37 | False | `MID.down.q80 -s-> MID.down.q50` | — | tennessee_eastman |
| ST_PT01:peak | l | FT01:downq50 | 1.897 | 1.98 | 31 | True | `MID.peak -l-> MID.down.q50` | — | tennessee_eastman |
| LIT01:downq20 | l | LCV01D:upq20 | 1.882 | 2.125 | 112 | False | `MID.down.q20 -l-> MID.up.q20` | — | tennessee_eastman |
| LCV01D:upq50 | l | LCP01D:upq80 | 1.88 | 2.101 | 87 | True | `MID.up.q50 -l-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| LCP01D:upq80 | l | LCV01D:upq20 | 1.88 | 2.137 | 69 | True | `MID-S.up.q80 -l-> MID.up.q20` | — | tennessee_eastman, building_59 |
| LCV01D:downq80 | m | LIT01:upq50 | 1.875 | 1.745 | 125 | True | `MID.down.q80 -m-> MID.up.q50` | — | tennessee_eastman |
| ST_TT01:downq10 | l | B400B:downq50 | 1.875 | 1.66 | 46 | True | `MID.down.q10 -l-> MID-S.down.q50` | — | tennessee_eastman |
| ST_TT01:downq10 | l | FT02:downq50 | 1.875 | 1.66 | 46 | True | `MID.down.q10 -l-> MID-S.down.q50` | — | tennessee_eastman |
| ST_TT01:downq10 | l | FT02Z:downq50 | 1.875 | 1.66 | 46 | True | `MID.down.q10 -l-> MID-S.down.q50` | — | tennessee_eastman |
| ST_TT01:upq10 | l | FCV02Z:downq80 | 1.862 | 2.429 | 37 | True | `MID.up.q10 -l-> MID-S.down.q80` | — | tennessee_eastman, building_59 |
| LCV01D:upq50 | m | LIT01:downq20 | 1.861 | 2.013 | 94 | True | `MID.up.q50 -m-> MID.down.q20` | — | tennessee_eastman |
| HT_LD:peak | s | LIT01:upq50 | 1.856 | 1.747 | 47 | True | `MID-S.peak -s-> MID.up.q50` | — | — |
| HT_PO:trough | s | SIT01:trough | 1.852 | 1.74 | 21 | False | `MID-S.trough -s-> MID.trough` | — | — |
| ST_TT01:downq10 | l | FCV02Z:upq80 | 1.851 | 2.48 | 38 | False | `MID.down.q10 -l-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| LCV01D:downq50 | m | LCV01D:downq20 | 1.85 | 2.095 | 89 | True | `MID.down.q50 -m-> MID.down.q20 [same role]` | — | tennessee_eastman, building_59 |
| PIT01:trough | m | PIT01:peak | 1.839 | 1.94 | 235 | True | `MID.trough -m-> MID.peak [same role]` | — | tennessee_eastman |
| LCV01D:downq50 | m | LIT01:upq50 | 1.838 | 2.113 | 138 | True | `MID.down.q50 -m-> MID.up.q50` | — | tennessee_eastman |
| ST_TT01:downq10 | l | B4005:downq50 | 1.838 | 1.627 | 46 | True | `MID.down.q10 -l-> MID-S.down.q50` | — | tennessee_eastman, building_59 |
| LIT01:downq50 | s | LCV01Z:upq50 | 1.837 | 2.142 | 10 | True | `MID.down.q50 -s-> MID.up.q50` | — | tennessee_eastman |
| B4022:upq80 | m | PIT01:peak | 1.835 | 2.226 | 32 | False | `SLOW.up.q80 -m-> MID.peak` | — | tennessee_eastman |
| ST_TT01:downq10 | l | PIT02:downq10 | 1.833 | 2.272 | 78 | True | `MID.down.q10 -l-> MID.down.q10` | — | tennessee_eastman, building_59 |
| ST_TT01:downq10 | l | B4005:downq20 | 1.831 | 2.33 | 44 | True | `MID.down.q10 -l-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| FCV03D:peak | s | LCV01D:downq20 | 1.831 | 1.559 | 9 | False | `MID.peak -s-> MID.down.q20` | — | tennessee_eastman, building_59 |
| PIT01:peak | m | LCV01Z:upq20 | 1.83 | 2.454 | 64 | True | `MID.peak -m-> MID.up.q20` | — | tennessee_eastman |
| ST_TT01:downq10 | l | TIT02:downq80 | 1.825 | 1.84 | 53 | True | `MID.down.q10 -l-> MID.down.q80` | — | tennessee_eastman, building_59 |
| LIT01:upq50 | s | LCV01Z:downq80 | 1.816 | 2.168 | 8 | True | `MID.up.q50 -s-> MID.down.q80` | — | tennessee_eastman |
| ST_TT01:downq10 | l | TIT01:peak | 1.81 | 1.827 | 58 | True | `MID.down.q10 -l-> MID.peak` | — | tennessee_eastman |
| ST_PT01:peak | m | VYT03:downq80 | 1.807 | 11.152 | 4 | False | `MID.peak -m-> SLOW.down.q80` | — | tennessee_eastman |
| FT01:downq80 | s | LCV01D:downq50 | 1.798 | 3.25 | 7 | True | `MID.down.q80 -s-> MID.down.q50` | — | tennessee_eastman, building_59 |
| ST_TT01:downq10 | l | FCV02Z:upq50 | 1.794 | 1.66 | 44 | True | `MID.down.q10 -l-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| HT_PO:peak | m | B2004:upq80 | 1.794 | 2.368 | 6 | False | `MID-S.peak -m-> SET.up.q80` | — | — |
| ST_TT01:downq10 | l | FCV02Z:upq20 | 1.791 | 1.578 | 26 | False | `MID.down.q10 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| PIT01:trough | m | LCV01Z:downq80 | 1.789 | 2.36 | 43 | True | `MID.trough -m-> MID.down.q80` | — | tennessee_eastman |
| PIT01:trough | m | LCV01Z:downq20 | 1.788 | 2.376 | 68 | True | `MID.trough -m-> MID.down.q20` | — | tennessee_eastman |
| LD:peak | s | B4022:upq50 | 1.787 | 1.913 | 17 | True | `MID.peak -s-> SLOW.up.q50` | — | — |
| FT03Z:peak | s | LCV01D:downq20 | 1.786 | 2.282 | 8 | False | `MID.peak -s-> MID.down.q20` | — | tennessee_eastman |
| FT01:downq80 | m | PIT01:peak | 1.785 | 2.101 | 18 | False | `MID.down.q80 -m-> MID.peak` | — | tennessee_eastman |
| FT01:downq50 | m | PIT01:peak | 1.781 | 1.658 | 24 | True | `MID.down.q50 -m-> MID.peak` | — | tennessee_eastman |
| LCP01D:upq50 | l | PIT01:trough | 1.775 | 1.956 | 115 | False | `MID-S.up.q50 -l-> MID.trough` | — | tennessee_eastman |
| ST_TT01:upq10 | l | FCV01Z:trough | 1.774 | 1.83 | 49 | True | `MID.up.q10 -l-> MID-S.trough` | — | tennessee_eastman |
| LD:peak | m | B3004:downq80 | 1.771 | 1.764 | 6 | False | `MID.peak -m-> SET.down.q80` | — | — |
| ST_TT01:downq10 | l | FT02:upq20 | 1.765 | 1.773 | 38 | True | `MID.down.q10 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| ST_TT01:downq10 | l | FT02Z:upq20 | 1.765 | 1.891 | 38 | True | `MID.down.q10 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| LCV01Z:downq50 | m | LCV01D:downq50 | 1.762 | 1.624 | 45 | True | `MID.down.q50 -m-> MID.down.q50` | — | tennessee_eastman, building_59 |
| LCV01D:upq80 | l | LCV01D:upq50 | 1.76 | 1.766 | 189 | False | `MID.up.q80 -l-> MID.up.q50 [same role]` | — | tennessee_eastman, building_59 |
| PIT01:peak | l | FT01:downq50 | 1.754 | 2.223 | 29 | True | `MID.peak -l-> MID.down.q50` | — | tennessee_eastman |
| PIT01:trough | m | B4022:downq50 | 1.753 | 1.727 | 96 | True | `MID.trough -m-> SLOW.down.q50` | — | tennessee_eastman |
| PIT01:peak | m | PCV01D:trough | 1.748 | 1.595 | 35 | True | `MID.peak -m-> MID-S.trough` | — | — |
| PIT01:peak | m | B2016:trough | 1.745 | 1.778 | 96 | True | `MID.peak -m-> MID.trough` | — | tennessee_eastman |
| LCV01D:upq50 | s | B4022:upq20 | 1.745 | 2.355 | 23 | True | `MID.up.q50 -s-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| FCV02Z:upq80 | m | LCV01D:downq80 | 1.745 | 1.511 | 16 | True | `MID-S.up.q80 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| LCV01D:upq80 | m | LIT01:downq50 | 1.74 | 1.933 | 121 | True | `MID.up.q80 -m-> MID.down.q50` | — | tennessee_eastman |
| ST_TT01:downq10 | l | PIT02:upq10 | 1.739 | 1.973 | 74 | True | `MID.down.q10 -l-> MID.up.q10` | — | tennessee_eastman, building_59 |
| B2004:downq50 | s | LCV01D:upq50 | 1.739 | 3.471 | 4 | False | `SET.down.q50 -s-> MID.up.q50` | — | — |
| LIT01:downq50 | m | LCV01D:downq20 | 1.737 | 2.204 | 92 | True | `MID.down.q50 -m-> MID.down.q20` | — | tennessee_eastman |
| LCV01D:downq50 | l | LCV01D:downq80 | 1.735 | 1.89 | 164 | False | `MID.down.q50 -l-> MID.down.q80 [same role]` | tennessee_eastman | building_59 |
| B4005:downq50 | s | B4022:upq20 | 1.733 | 2.553 | 9 | False | `MID-S.down.q50 -s-> SLOW.up.q20` | — | tennessee_eastman, building_59 |
| LCV01D:downq50 | l | LCV01D:upq80 | 1.72 | 1.689 | 162 | False | `MID.down.q50 -l-> MID.up.q80 [same role]` | — | tennessee_eastman, building_59 |
| FT01:upq20 | s | LCV01D:upq50 | 1.713 | 1.575 | 8 | True | `MID.up.q20 -s-> MID.up.q50` | — | tennessee_eastman, building_59 |
| ST_TT01:downq10 | l | B4005:upq20 | 1.706 | 1.694 | 41 | True | `MID.down.q10 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| HT_LD:peak | m | VYT02:downq80 | 1.701 | 10.933 | 6 | False | `MID-S.peak -m-> SLOW.down.q80` | — | — |
| PIT01:trough | l | LCP01D:downq50 | 1.7 | 1.602 | 126 | True | `MID.trough -l-> MID-S.down.q50` | — | tennessee_eastman |
| LCP01D:downq20 | l | PIT01:peak | 1.697 | 1.802 | 90 | False | `MID-S.down.q20 -l-> MID.peak` | — | tennessee_eastman |
| LIT01:upq80 | m | PIT01:peak | 1.692 | 1.568 | 107 | True | `MID.up.q80 -m-> MID.peak` | — | tennessee_eastman |
| ST_LD:peak | m | LIT01:upq20 | 1.681 | 1.597 | 127 | True | `MID.peak -m-> MID.up.q20` | — | tennessee_eastman |
| PIT01:trough | l | LCP01D:downq80 | 1.673 | 2.018 | 92 | True | `MID.trough -l-> MID-S.down.q80` | — | tennessee_eastman |
| PIT01:trough | m | LCP01D:upq20 | 1.673 | 1.85 | 57 | True | `MID.trough -m-> MID-S.up.q20` | — | tennessee_eastman |
| LCV01D:downq80 | m | TIT01:peak | 1.673 | 1.58 | 17 | True | `MID.down.q80 -m-> MID.peak` | — | tennessee_eastman |
| LIT01:upq20 | l | PIT01:peak | 1.662 | 1.679 | 150 | False | `MID.up.q20 -l-> MID.peak` | — | tennessee_eastman |
| ST_TT01:downq10 | m | PCV01D:trough | 1.655 | 2.692 | 12 | True | `MID.down.q10 -m-> MID-S.trough` | — | — |
| ST_TT01:downq10 | l | FCV01Z:trough | 1.647 | 1.605 | 47 | True | `MID.down.q10 -l-> MID-S.trough` | — | tennessee_eastman |
| ST_LD:peak | s | LIT01:downq20 | 1.633 | 1.697 | 24 | True | `MID.peak -s-> MID.down.q20` | — | tennessee_eastman |
| LCV01D:downq20 | m | PIT01:peak | 1.631 | 1.657 | 94 | True | `MID.down.q20 -m-> MID.peak` | — | tennessee_eastman |
| LCV01D:upq80 | m | FCV02Z:upq80 | 1.621 | 1.65 | 11 | True | `MID.up.q80 -m-> MID-S.up.q80` | — | tennessee_eastman, building_59 |
| LCV01Z:downq50 | m | LCV01D:upq50 | 1.61 | 1.534 | 41 | True | `MID.down.q50 -m-> MID.up.q50` | — | tennessee_eastman, building_59 |
| LCV01D:downq80 | l | LCV01D:upq50 | 1.609 | 1.699 | 174 | False | `MID.down.q80 -l-> MID.up.q50 [same role]` | — | tennessee_eastman, building_59 |
| LCV01D:downq80 | l | LCV01D:upq20 | 1.607 | 1.733 | 142 | False | `MID.down.q80 -l-> MID.up.q20 [same role]` | — | tennessee_eastman, building_59 |
| B2004:downq20 | s | LCV01D:downq20 | 1.606 | 2.071 | 3 | True | `SET.down.q20 -s-> MID.down.q20` | — | building_59 |
| B3004:upq50 | s | LCV01D:downq50 | 1.601 | 2.34 | 5 | False | `SET.up.q50 -s-> MID.down.q50` | — | tennessee_eastman |
| LCV01D:downq80 | m | LCV01Z:downq80 | 1.595 | 2.24 | 20 | False | `MID.down.q80 -m-> MID.down.q80` | — | tennessee_eastman, building_59 |
| ST_PT01:trough | m | FT01:downq50 | 1.592 | 1.513 | 28 | True | `MID.trough -m-> MID.down.q50` | — | tennessee_eastman |
| HT_LD:peak | m | HILout:downq20 | 1.587 | 2.291 | 28 | True | `MID-S.peak -m-> SLOW.down.q20` | — | — |
| ST_GOV:trough | m | FCV02Z:downq80 | 1.582 | 2.124 | 24 | True | `MID.trough -m-> MID-S.down.q80` | — | tennessee_eastman |
| LCV01D:downq80 | m | B4005:downq20 | 1.575 | 1.843 | 12 | False | `MID.down.q80 -m-> MID-S.down.q20` | — | tennessee_eastman, building_59 |
| PIT01:trough | m | B4022:upq50 | 1.57 | 1.842 | 86 | True | `MID.trough -m-> SLOW.up.q50` | — | tennessee_eastman |
| FCV03Z:peak | s | LCV01D:downq50 | 1.567 | 2.068 | 8 | False | `MID.peak -s-> MID.down.q50` | — | building_59 |
| LIT01:upq80 | s | LCV01Z:downq20 | 1.559 | 3.099 | 7 | True | `MID.up.q80 -s-> MID.down.q20` | — | tennessee_eastman |
| PIT01:peak | l | LCP01D:upq20 | 1.558 | 1.849 | 74 | True | `MID.peak -l-> MID-S.up.q20` | — | tennessee_eastman |
| LCV01D:downq80 | m | FCV02Z:upq50 | 1.543 | 1.547 | 12 | True | `MID.down.q80 -m-> MID-S.up.q50` | — | tennessee_eastman, building_59 |
| LCV01D:downq80 | m | B400B:downq50 | 1.543 | 1.547 | 12 | False | `MID.down.q80 -m-> MID-S.down.q50` | — | tennessee_eastman |
| LCV01D:downq80 | m | FT02Z:downq50 | 1.543 | 1.547 | 12 | False | `MID.down.q80 -m-> MID-S.down.q50` | — | tennessee_eastman |
| B3004:upq50 | s | LCV01D:downq80 | 1.543 | 2.82 | 4 | False | `SET.up.q50 -s-> MID.down.q80` | — | tennessee_eastman |
| LIT01:downq80 | s | LCV01Z:upq50 | 1.54 | 2.32 | 6 | True | `MID.down.q80 -s-> MID.up.q50` | — | tennessee_eastman |
| B4022:upq20 | s | LCV01D:downq80 | 1.53 | 2.197 | 19 | True | `SLOW.up.q20 -s-> MID.down.q80` | — | tennessee_eastman, building_59 |
| TIT02:upq80 | m | B4022:downq20 | 1.526 | 1.967 | 28 | True | `MID.up.q80 -m-> SLOW.down.q20` | — | tennessee_eastman, building_59 |
| LCV01D:downq80 | l | B4005:upq20 | 1.517 | 1.935 | 24 | False | `MID.down.q80 -l-> MID-S.up.q20` | — | tennessee_eastman, building_59 |
| ST_PO:trough | m | FCV02Z:downq80 | 1.504 | 1.798 | 23 | True | `MID.trough -m-> MID-S.down.q80` | — | — |

## Loops (returns; verdicts recorded, not promoted)

| X | l1 | Y | l2 | X′ | n | cond. lift | timing (g1 / g2) | determinism (p1 / p2) | used |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LIT01:upq80 | s | LCV01D:upq20 | s | LIT01:downq80 | 15 | 9.009 | unresolved (2.5 / 3.0) | unresolved (0.043 / 0.048) | False |
| LCP01D:upq80 | s | LCV01D:upq20 | m | LCP01D:downq80 | 10 | 6.428 | Y reacts (3.0 / 11.5) | Y reacts (0.058 / 0.019) | False |
| B2004:downq50 | s | LIT01:downq80 | l | B2004:upq20 | 4 | 6.158 | Y reacts (1.0 / 88.0) | Y reacts (0.048 / 0.003) | False |
| B2004:downq20 | s | LIT01:downq80 | l | B2004:upq20 | 4 | 5.951 | Y reacts (1.0 / 89.5) | Y reacts (0.053 / 0.003) | False |
| FCV01D:downq10 | m | B4022:downq20 | m | FCV01D:upq10 | 12 | 5.617 | unresolved (14.0 / 12.0) | Y reacts (0.058 / 0.010) | False |
| LCP01D:downq20 | m | PIT01:trough | m | LCP01D:upq20 | 23 | 5.609 | unresolved (16.0 / 13.0) | Y reacts (0.049 / 0.015) | False |
| FT01:downq50 | s | LCV01D:downq50 | m | FT01:upq50 | 4 | 4.593 | Y reacts (2.0 / 5.5) | Y reacts (0.063 / 0.012) | False |
| LCP01D:downq20 | l | PIT01:peak | s | LCP01D:upq80 | 10 | 4.179 | X reacts (73.0 / 2.0) | Y reacts (0.054 / 0.025) | False |
| FT02:downq50 | m | PIT02:upq10 | l | FT02:upq20 | 35 | 3.843 | Y reacts (19.0 / 54.0) | Y reacts (0.050 / 0.014) | False |
| FT02Z:downq50 | m | PIT02:upq10 | l | FT02Z:upq20 | 35 | 3.843 | Y reacts (18.5 / 54.0) | Y reacts (0.050 / 0.014) | False |
| FCV02Z:upq50 | m | PIT02:upq10 | l | FCV02Z:downq80 | 28 | 3.798 | Y reacts (16.0 / 57.0) | Y reacts (0.054 / 0.014) | False |
| FT01:downq20 | m | LCV01D:upq20 | m | FT01:upq20 | 7 | 3.686 | Y reacts (6.0 / 12.0) | Y reacts (0.034 / 0.006) | False |
| HILout:downq20 | m | CO_rpm:trough | m | HILout:upq20 | 16 | 3.565 | Y reacts (5.0 / 13.0) | unresolved (0.053 / 0.037) | False |
| VXT02:upq80 | s | VYT03:upq20 | s | VXT02:downq80 | 5 | 3.421 | X reacts (2.0 / 1.0) | X reacts (0.049 / 0.200) | False |
| LCP01D:downq20 | m | LCV01D:upq80 | m | LCP01D:upq20 | 15 | 3.288 | unresolved (13.0 / 15.0) | Y reacts (0.044 / 0.014) | False |
| FCV02Z:upq80 | m | PIT02:upq10 | l | FCV02Z:downq80 | 25 | 3.273 | Y reacts (10.0 / 46.0) | Y reacts (0.065 / 0.014) | False |
| B4022:upq50 | s | B4005:upq20 | s | B4022:downq50 | 9 | 3.258 | unresolved (1.5 / 2.0) | unresolved (0.032 / 0.030) | False |
| PIT02:upq90 | s | TIT01:peak | s | PIT02:downq90 | 12 | 3.118 | Y reacts (1.0 / 2.0) | unresolved (0.049 / 0.063) | False |
| B4022:downq20 | s | PCV01Z:trough | s | B4022:upq20 | 16 | 3.057 | unresolved (2.0 / 1.5) | X reacts (0.036 / 0.103) | False |
| B4022:downq20 | s | PCV01D:trough | s | B4022:upq20 | 16 | 3.038 | unresolved (2.0 / 2.0) | X reacts (0.034 / 0.101) | False |
| LCV01Z:upq20 | m | B2016:trough | m | LCV01Z:downq20 | 32 | 2.956 | Y reacts (10.0 / 15.0) | unresolved (0.032 / 0.029) | False |
| FT02:downq50 | s | PIT02:upq90 | l | FT02:upq20 | 30 | 2.892 | Y reacts (1.0 / 75.5) | Y reacts (0.145 / 0.011) | False |
| HILout:downq20 | s | SIT01:trough | m | HILout:upq20 | 4 | 2.876 | Y reacts (2.0 / 12.0) | unresolved (0.067 / 0.068) | False |
| VYT03:downq20 | s | VXT02:upq80 | m | VYT03:upq20 | 4 | 2.874 | Y reacts (2.0 / 10.5) | Y reacts (0.250 / 0.020) | False |
| LCV01Z:upq80 | m | LCV01D:downq80 | s | LCV01Z:downq80 | 8 | 2.857 | X reacts (13.0 / 1.0) | Y reacts (0.035 / 0.014) | False |
| HILout:upq20 | s | CO_rpm:peak | m | HILout:downq20 | 4 | 2.847 | Y reacts (2.5 / 11.0) | Y reacts (0.083 / 0.040) | False |
| VYT03:downq20 | s | VXT02:upq80 | s | VYT03:upq20 | 4 | 2.815 | Y reacts (1.0 / 4.0) | Y reacts (0.250 / 0.049) | False |
| HILout:downq20 | s | SIT02:trough | m | HILout:upq20 | 4 | 2.796 | Y reacts (2.0 / 12.0) | unresolved (0.067 / 0.067) | False |
| B4005:downq50 | s | PIT02:upq90 | l | B4005:upq20 | 13 | 2.75 | Y reacts (4.0 / 77.0) | Y reacts (0.051 / 0.012) | False |
| B4005:downq50 | m | PIT02:upq90 | l | B4005:upq20 | 20 | 2.666 | Y reacts (5.0 / 72.5) | Y reacts (0.024 / 0.012) | False |
| LCP01D:upq50 | l | PIT01:trough | l | LCP01D:downq50 | 78 | 2.551 | unresolved (63.0 / 48.0) | Y reacts (0.058 / 0.021) | False |
| VYT03:upq50 | s | VYT02:upq50 | l | VYT03:downq50 | 12 | 2.529 | Y reacts (1.0 / 36.0) | unresolved (0.050 / 0.034) | False |
| HILout:upq20 | m | CO_rpm:peak | m | HILout:downq20 | 10 | 2.468 | unresolved (13.5 / 11.5) | unresolved (0.055 / 0.040) | False |
| LCP01D:downq80 | l | LCV01D:downq80 | m | LCP01D:upq80 | 34 | 2.462 | X reacts (68.0 / 12.0) | Y reacts (0.033 / 0.021) | False |
| LCP01D:downq80 | m | LCV01D:upq20 | l | LCP01D:upq20 | 32 | 2.416 | Y reacts (8.0 / 65.0) | Y reacts (0.052 / 0.016) | False |
| FCV01D:downq10 | m | FCV01Z:trough | s | FCV01D:upq10 | 10 | 2.373 | X reacts (7.0 / 2.0) | X reacts (0.022 / 0.070) | False |
| FT01:upq20 | m | LCV01Z:upq20 | m | FT01:downq20 | 9 | 2.366 | X reacts (12.0 / 7.0) | Y reacts (0.026 / 0.016) | False |
| LIT01:upq80 | s | LCV01D:upq20 | m | LIT01:downq50 | 28 | 2.358 | Y reacts (2.0 / 10.0) | unresolved (0.043 / 0.056) | False |
| LCP01D:downq20 | l | PIT01:peak | l | LCP01D:upq20 | 33 | 2.34 | unresolved (69.5 / 56.0) | Y reacts (0.054 / 0.015) | False |
| B400B:downq50 | s | PIT02:downq90 | l | B400B:upq20 | 14 | 2.33 | Y reacts (4.0 / 78.0) | Y reacts (0.080 / 0.013) | False |
| FT02:downq50 | s | PIT02:downq90 | l | FT02:upq20 | 14 | 2.33 | Y reacts (4.0 / 74.0) | Y reacts (0.066 / 0.012) | False |
| FT02Z:downq50 | s | PIT02:downq90 | l | FT02Z:upq20 | 14 | 2.33 | Y reacts (4.0 / 74.0) | Y reacts (0.080 / 0.013) | False |
| B4005:downq50 | m | PIT02:downq90 | l | B4005:upq20 | 33 | 2.295 | Y reacts (8.0 / 73.0) | Y reacts (0.038 / 0.013) | False |
| LIT01:upq50 | m | LCV01D:upq20 | s | LIT01:downq80 | 23 | 2.28 | X reacts (16.0 / 3.0) | unresolved (0.043 / 0.048) | False |
| LIT01:upq50 | s | LCV01D:downq80 | s | LIT01:downq50 | 11 | 2.238 | unresolved (1.5 / 2.0) | unresolved (0.041 / 0.047) | False |
| B2004:downq50 | s | B3004:downq80 | l | B2004:upq20 | 4 | 2.237 | Y reacts (1.0 / 89.0) | Y reacts (0.048 / 0.010) | False |
| LIT01:upq80 | m | LCV01D:upq20 | s | LIT01:downq80 | 15 | 2.236 | X reacts (9.0 / 3.0) | unresolved (0.048 / 0.048) | False |
| LCV01Z:upq20 | m | LCV01D:upq20 | m | LCV01Z:downq20 | 40 | 2.222 | X reacts (15.0 / 9.0) | unresolved (0.051 / 0.036) | False |
| B400B:downq50 | m | PIT02:downq90 | l | B400B:upq20 | 16 | 2.221 | Y reacts (5.0 / 60.5) | unresolved (0.019 / 0.013) | False |
| FT02:downq50 | m | PIT02:downq90 | l | FT02:upq20 | 16 | 2.221 | Y reacts (5.0 / 70.0) | Y reacts (0.023 / 0.012) | False |
| FT02Z:downq50 | m | PIT02:downq90 | l | FT02Z:upq20 | 16 | 2.221 | Y reacts (5.0 / 60.5) | Y reacts (0.019 / 0.013) | False |
| LCP01D:downq20 | m | LCV01D:downq80 | m | LCP01D:upq50 | 19 | 2.213 | unresolved (8.5 / 11.5) | Y reacts (0.044 / 0.021) | False |
| B4022:upq50 | s | FCV01D:upq10 | s | B4022:downq50 | 6 | 2.2 | Y reacts (1.0 / 2.5) | X reacts (0.018 / 0.057) | False |
| FCV02Z:upq20 | l | B4022:downq20 | m | FCV02Z:downq80 | 11 | 2.192 | X reacts (64.5 / 18.5) | Y reacts (0.024 / 0.013) | False |
| LCV01Z:downq50 | m | LCV01D:upq50 | s | LCV01Z:upq80 | 5 | 2.182 | X reacts (8.0 / 1.0) | unresolved (0.036 / 0.027) | False |
| FCV02Z:upq80 | l | PIT02:downq10 | s | FCV02Z:downq80 | 14 | 2.173 | X reacts (52.0 / 3.0) | unresolved (0.024 / 0.033) | False |
| LCV01Z:downq20 | s | FT01Z:trough | l | LCV01Z:upq20 | 28 | 2.097 | Y reacts (3.0 / 74.0) | Y reacts (0.057 / 0.026) | False |
| FCV02Z:upq50 | l | B4022:downq20 | m | FCV02Z:downq80 | 20 | 2.078 | X reacts (68.5 / 14.0) | Y reacts (0.047 / 0.013) | False |
| B4005:downq20 | l | PIT02:downq10 | s | B4005:upq20 | 11 | 2.078 | X reacts (53.0 / 2.5) | unresolved (0.023 / 0.030) | False |
| FT02Z:downq50 | l | B4022:upq20 | m | FT02Z:upq20 | 18 | 2.077 | X reacts (68.5 / 12.0) | Y reacts (0.048 / 0.011) | False |
| LIT01:upq80 | m | LCV01D:upq20 | m | LIT01:downq80 | 56 | 2.076 | unresolved (15.0 / 10.5) | unresolved (0.048 / 0.044) | False |
| LCV01Z:downq20 | m | LCV01D:downq20 | s | LCV01Z:upq20 | 18 | 2.072 | X reacts (14.0 / 3.0) | unresolved (0.049 / 0.037) | False |
| TIT01:trough | m | PIT02:upq90 | s | TIT01:peak | 13 | 2.064 | X reacts (18.0 / 1.0) | X reacts (0.028 / 0.049) | False |
| LCP01D:downq50 | m | LIT01:downq80 | l | LCP01D:upq50 | 44 | 2.028 | Y reacts (17.0 / 44.0) | Y reacts (0.089 / 0.035) | False |
| B400B:downq50 | l | PIT02:upq90 | m | B400B:upq50 | 22 | 2.014 | X reacts (118.0 / 19.0) | unresolved (0.009 / 0.014) | False |
| FT02Z:downq50 | l | PIT02:upq90 | m | FT02Z:upq50 | 22 | 2.014 | X reacts (118.0 / 19.0) | unresolved (0.009 / 0.014) | False |
| FT02Z:downq50 | l | B4022:downq20 | m | FT02Z:upq20 | 23 | 2.011 | X reacts (68.0 / 14.0) | Y reacts (0.046 / 0.014) | False |
| LIT01:upq80 | s | LCV01D:upq20 | m | LIT01:downq80 | 19 | 1.984 | Y reacts (2.0 / 10.0) | unresolved (0.043 / 0.044) | False |
| LCP01D:downq50 | m | LIT01:upq80 | l | LCP01D:upq20 | 29 | 1.973 | Y reacts (17.0 / 40.5) | Y reacts (0.090 / 0.022) | False |
| B3004:upq80 | l | B2004:downq20 | s | B3004:downq80 | 5 | 1.96 | X reacts (91.0 / 1.0) | X reacts (0.008 / 0.053) | False |
| LIT01:upq80 | l | B2004:downq20 | s | LIT01:downq80 | 5 | 1.96 | X reacts (90.5 / 1.0) | X reacts (0.003 / 0.053) | False |
| B3004:upq80 | l | B2004:downq20 | s | B3004:downq50 | 4 | 1.96 | X reacts (92.0 / 1.0) | X reacts (0.008 / 0.039) | False |
| LCV01Z:downq20 | m | LCV01D:downq20 | m | LCV01Z:upq20 | 32 | 1.948 | unresolved (16.0 / 11.0) | unresolved (0.049 / 0.034) | False |
| LIT01:downq80 | m | LCV01D:upq80 | l | LIT01:upq80 | 114 | 1.927 | Y reacts (13.0 / 62.0) | unresolved (0.040 / 0.049) | False |
| LIT01:downq20 | s | LCV01D:upq80 | l | LIT01:upq80 | 31 | 1.919 | Y reacts (3.0 / 47.0) | unresolved (0.042 / 0.049) | False |
| LCV01Z:upq80 | m | B4022:upq50 | s | LCV01Z:downq80 | 4 | 1.9 | X reacts (9.0 / 2.0) | Y reacts (0.055 / 0.035) | False |
| HILout:downq50 | m | CO_rpm:trough | m | HILout:upq50 | 26 | 1.892 | unresolved (17.0 / 16.0) | Y reacts (0.080 / 0.049) | False |
| LCV01D:upq80 | m | FCV02Z:upq80 | m | LCV01D:downq80 | 7 | 1.885 | Y reacts (11.0 / 18.0) | X reacts (0.005 / 0.029) | False |
| FT01:downq20 | l | LCV01D:upq20 | m | FT01:upq20 | 8 | 1.818 | X reacts (53.0 / 11.0) | Y reacts (0.041 / 0.006) | False |
| LIT01:upq80 | l | LCV01D:downq80 | l | LIT01:downq80 | 147 | 1.814 | Y reacts (34.0 / 63.0) | X reacts (0.034 / 0.053) | False |
| HILout:upq80 | m | CO_rpm:peak | m | HILout:downq50 | 10 | 1.814 | unresolved (16.0 / 11.0) | Y reacts (0.110 / 0.043) | False |
| HILout:downq50 | m | SIT01:trough | m | HILout:upq50 | 26 | 1.813 | unresolved (17.0 / 13.0) | Y reacts (0.080 / 0.046) | False |
| FT02Z:downq50 | l | B4022:upq50 | s | FT02Z:upq20 | 8 | 1.777 | X reacts (73.0 / 3.0) | Y reacts (0.040 / 0.026) | False |
| LIT01:downq50 | m | LCV01D:downq50 | m | LIT01:upq80 | 96 | 1.776 | unresolved (15.5 / 16.5) | unresolved (0.043 / 0.053) | False |
| LIT01:upq80 | m | LCV01D:upq50 | m | LIT01:downq50 | 85 | 1.758 | unresolved (15.0 / 16.0) | unresolved (0.047 / 0.068) | False |
| LIT01:downq50 | m | LCV01D:downq80 | m | LIT01:upq50 | 85 | 1.744 | unresolved (16.0 / 17.0) | X reacts (0.034 / 0.052) | False |
| B400B:downq20 | l | B4022:upq50 | m | B400B:upq50 | 17 | 1.735 | X reacts (80.0 / 15.0) | Y reacts (0.044 / 0.007) | False |
| LIT01:downq50 | m | LCV01D:downq20 | m | LIT01:upq80 | 64 | 1.729 | unresolved (15.0 / 14.0) | unresolved (0.042 / 0.053) | False |
| LCV01Z:downq20 | s | LCV01D:upq20 | s | LCV01Z:upq20 | 7 | 1.721 | X reacts (2.5 / 1.0) | Y reacts (0.070 / 0.035) | False |
| LCP01D:downq20 | m | LIT01:downq20 | m | LCP01D:upq20 | 15 | 1.707 | unresolved (16.0 / 18.5) | Y reacts (0.066 / 0.034) | False |
| LIT01:downq20 | m | LCV01D:downq50 | m | LIT01:upq80 | 79 | 1.704 | unresolved (13.0 / 17.0) | unresolved (0.054 / 0.053) | False |
| B4005:downq50 | l | B4022:upq50 | s | B4005:upq20 | 12 | 1.689 | X reacts (76.0 / 1.5) | unresolved (0.039 / 0.032) | False |
| TIT02:downq50 | m | PIT02:upq90 | l | TIT02:upq50 | 25 | 1.686 | Y reacts (17.5 / 103.0) | Y reacts (0.035 / 0.007) | False |
| HILout:upq50 | m | SIT02:peak | m | HILout:downq50 | 19 | 1.673 | unresolved (7.0 / 10.0) | unresolved (0.054 / 0.041) | False |
| LCV01Z:downq20 | m | LCV01D:upq20 | s | LCV01Z:upq20 | 14 | 1.664 | X reacts (17.0 / 1.0) | Y reacts (0.062 / 0.035) | False |
| LIT01:upq50 | m | LCV01D:upq20 | m | LIT01:downq50 | 71 | 1.654 | unresolved (16.0 / 14.0) | unresolved (0.043 / 0.056) | False |
| HILout:upq80 | l | SIT01:trough | l | HILout:downq80 | 34 | 1.654 | unresolved (38.0 / 56.0) | Y reacts (0.060 / 0.024) | False |
| LCP01D:downq80 | m | LIT01:upq80 | l | LCP01D:upq20 | 19 | 1.651 | Y reacts (22.0 / 41.0) | Y reacts (0.098 / 0.022) | False |
| LIT01:upq80 | m | LCV01D:upq20 | m | LIT01:downq50 | 55 | 1.644 | unresolved (14.0 / 15.0) | unresolved (0.048 / 0.056) | False |
| TIT02:downq50 | m | PIT02:upq90 | l | TIT02:upq80 | 25 | 1.643 | Y reacts (17.5 / 105.0) | Y reacts (0.035 / 0.007) | False |
| SIT01:trough | m | VXT03:downq50 | m | SIT01:peak | 10 | 1.623 | unresolved (16.0 / 13.0) | X reacts (0.020 / 0.033) | False |
| B4022:downq50 | m | B2016:trough | m | B4022:upq50 | 51 | 1.619 | unresolved (12.0 / 13.0) | unresolved (0.030 / 0.042) | False |
| LCV01Z:downq20 | l | FT01:upq20 | s | LCV01Z:upq50 | 7 | 1.617 | X reacts (64.0 / 3.0) | X reacts (0.008 / 0.073) | False |
| LIT01:downq50 | m | LCV01D:downq50 | m | LIT01:upq50 | 82 | 1.616 | unresolved (16.0 / 15.0) | unresolved (0.043 / 0.063) | False |
| HILout:upq50 | m | SIT01:peak | m | HILout:downq50 | 20 | 1.61 | unresolved (7.0 / 10.0) | unresolved (0.054 / 0.041) | False |
| HILout:upq80 | m | SIT01:peak | m | HILout:downq50 | 9 | 1.606 | unresolved (16.0 / 12.0) | Y reacts (0.092 / 0.041) | False |
| LCP01D:upq50 | m | LIT01:upq20 | l | LCP01D:downq50 | 47 | 1.581 | Y reacts (10.5 / 41.5) | unresolved (0.053 / 0.047) | False |
| LIT01:upq50 | m | LCV01D:upq20 | m | LIT01:downq80 | 54 | 1.56 | X reacts (16.0 / 10.0) | unresolved (0.043 / 0.044) | False |
| FCV01Z:trough | l | PIT02:downq90 | m | FCV01Z:peak | 13 | 1.558 | X reacts (76.0 / 20.0) | unresolved (0.013 / 0.018) | False |
| B400B:upq20 | l | PIT02:downq90 | l | B400B:downq50 | 27 | 1.55 | Y reacts (63.0 / 96.0) | Y reacts (0.017 / 0.008) | False |
| FT02:upq20 | l | PIT02:downq90 | l | FT02:downq50 | 27 | 1.55 | Y reacts (63.0 / 96.0) | Y reacts (0.016 / 0.008) | False |
| FT02Z:upq20 | l | PIT02:downq90 | l | FT02Z:downq50 | 27 | 1.55 | Y reacts (63.0 / 96.0) | Y reacts (0.016 / 0.008) | False |
| LCV01Z:downq20 | m | FT01:upq20 | l | LCV01Z:upq20 | 15 | 1.527 | Y reacts (8.0 / 50.0) | unresolved (0.018 / 0.018) | False |
| CO_rpm:trough | m | VXT03:upq80 | m | CO_rpm:peak | 15 | 1.52 | Y reacts (8.5 / 15.0) | unresolved (0.037 / 0.037) | False |
| HILout:downq50 | l | CO_rpm:peak | l | HILout:upq50 | 59 | 1.518 | unresolved (73.0 / 54.0) | Y reacts (0.056 / 0.027) | False |
| FCV02Z:upq50 | l | PIT02:upq90 | l | FCV02Z:downq50 | 28 | 1.512 | X reacts (117.0 / 39.0) | unresolved (0.010 / 0.011) | False |
| HILout:upq50 | m | CO_rpm:peak | m | HILout:downq50 | 17 | 1.511 | unresolved (14.0 / 10.0) | unresolved (0.054 / 0.043) | False |
| LIT01:downq20 | m | LCV01D:downq80 | m | LIT01:upq50 | 58 | 1.509 | unresolved (14.0 / 17.0) | unresolved (0.044 / 0.052) | False |

Chains (non-return): 1319.

## Absences

- silent roles: ['FCV02D', 'PCV02D', 'Emerg', 'OnOff', 'FIT01', 'HT_FD', 'ST_FD']
- roles never a target: ['24Vdc', 'B4002', 'HT_LD', 'HT_PO', 'HT_PS', 'LD', 'PCV02Z', 'ST_GOV', 'ST_LD', 'ST_PO', 'ST_PS', 'ST_PT01', 'ST_TT01']
- keyed pairs not found: FCV02D → FCV02Z; PP01AD → PP01AR; PP02D → PP02R; LCV01Z → LIT01; B4005 → FCV03D; FCV03Z → TIT01; LCP01D → FIT01; FIT01 → LIT01
- signal floor: 12 (absence is informative only for pairs whose support would exceed the signal floor)

## Regimes

50 annotations

## Matrix row

Cells in (this system as receiver):

| source | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tennessee_eastman | 8.74 | 13.73 | 39.92 | 31.18 | 26.19 | marginal | — | 142/168 | short, damage |
| nasa_battery | 0.17 | 0.17 | 29.73 | 29.50 | 29.56 | derangement | — | 10/168 | short |
| physionet_slp | 0.99 | 5.02 | 37.84 | 36.84 | 32.82 | marginal | — | 4/168 | short, damage |
| building_59 | 17.27 | 26.26 | 49.52 | 32.25 | 23.26 | marginal | — | 95/168 | short, damage |
| fingrid | 1.30 | 1.30 | 34.39 | 30.34 | 33.09 | derangement | — | 10/168 | short, damage |
| alibaba_2018 | 4.71 | 6.37 | 36.46 | 31.76 | 30.09 | marginal | — | 30/168 | short, damage |

Cells out (this system as source):

| receiver | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tennessee_eastman | -21.37 | 48.61 | 89.49 | 110.86 | 40.88 | marginal | -0.12 | 34/40 | damage |
| nasa_battery | 0.07 | 0.11 | -0.28 | -0.35 | -0.39 | marginal | 0.03 | 12/12 | short |
| physionet_slp | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | marginal | — | 10/10 |  |
| building_59 | 4.37 | 8.01 | 129.67 | 125.30 | 121.65 | marginal | 0.04 | 85/89 | damage |
| fingrid | 5.93 | 5.93 | 21.72 | 12.43 | 15.79 | derangement | 0.04 | 16/16 |  |
| alibaba_2018 | 2.08 | 2.62 | 2.89 | 0.81 | 0.26 | marginal | — | 25/27 | damage |

Nearest taxa by distance: shape_jaccard: building_59 0.886, tennessee_eastman 0.89, fingrid 0.967; shape_bray_curtis: building_59 0.841, tennessee_eastman 0.849, fingrid 0.964; transfer_net: building_59 0.085, fingrid 0.216, physionet_slp 0.669
