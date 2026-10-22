# Brief — physionet_slp (method v8, a view)

*Lifts are odds ratios on the proposal split (3.6-3.8), confirmed on the confirmation split; absence is informative only above the signal floor (3.5); `no gain` means found but already carried by the trivial alternation model (3.11); loop-rule verdicts are recorded, not promoted (3.16); cells are bit-horizons net of the larger of two controls, with share of the receiver's ceiling where a diagonal exists (3.12).*

## Identity

- kind: real physiological records (MIT-BIH polysomnographic, 18 nights); standing: admitted (v7: by horizons, 19,419 H)
- entity: record (18 units); H = 0.3 min; lag edges [0.02, 0.07, 0.26] min
- periods: slow —, fast —; admission: {'days': 3.57, 'slow_periods': None, 'horizons': 19419.1, 'test_horizons': 4854.8, 'admitted': True, 'by': 'horizons'}
- claim: **beats baselines** — library 3.136 bits, triviality 3.328, best baseline 3.373; gain over triviality 0.192
- events 221062, types 10, signal floor 1039

## Vocabulary

| role | full tag | quantity | scheme | loop tags (timing / determinism) |
| --- | --- | --- | --- | --- |
| DBP | MID·LOCAL·RELAY ⟨M L⁻¹ T⁻²⟩ | pressure | dsign | — / — |
| HR | MID·LEAD ⟨T⁻¹⟩ | frequency | dsign | — / — |
| RESP | FAST·LOCAL·RELAY | — | dsign | — / — |
| SBP | MID·LOCAL·FOLLOW ⟨M L⁻¹ T⁻²⟩ | pressure | dsign | — / — |
| SO2 | MID·ISOLATED | — | dsign | — / — |

## Couplings (validated fragments)

| prior | lag | target | lift | conf. lift | n | binding | shape | confirmed in | failed in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DBP:peak | s | SBP:peak | 6.348 | 10.967 | 711 | True | `MID.peak -s-> MID.peak` | — | tennessee_eastman, hai |
| DBP:trough | s | SBP:trough | 5.031 | 5.692 | 600 | True | `MID.trough -s-> MID.trough` | — | tennessee_eastman, hai |
| RESP:peak | s | DBP:trough | 4.532 | 3.798 | 1963 | True | `FAST.peak -s-> MID.trough` | — | tennessee_eastman, hai |
| RESP:peak | s | SBP:trough | 4.527 | 5.251 | 1638 | True | `FAST.peak -s-> MID.trough` | — | tennessee_eastman, hai |
| RESP:trough | s | SBP:peak | 4.084 | 4.277 | 1436 | True | `FAST.trough -s-> MID.peak` | — | tennessee_eastman, hai |
| RESP:trough | s | DBP:peak | 3.69 | 3.983 | 1553 | True | `FAST.trough -s-> MID.peak` | — | tennessee_eastman, hai |
| HR:peak | m | SBP:peak | 2.533 | 3.915 | 1860 | True | `MID.peak -m-> MID.peak` | — | tennessee_eastman, hai |
| SBP:trough | s | DBP:trough | 2.405 | 3.976 | 263 | True | `MID.trough -s-> MID.trough` | — | tennessee_eastman, hai |
| HR:peak | s | DBP:peak | 2.4 | 3.214 | 509 | True | `MID.peak -s-> MID.peak` | — | tennessee_eastman, hai |
| DBP:peak | m | SBP:peak | 2.345 | 3.229 | 1029 | True | `MID.peak -m-> MID.peak` | — | tennessee_eastman, hai |
| SBP:peak | s | DBP:peak | 2.272 | 3.561 | 226 | True | `MID.peak -s-> MID.peak` | — | tennessee_eastman, hai |
| HR:peak | m | DBP:peak | 2.236 | 2.967 | 1965 | True | `MID.peak -m-> MID.peak` | — | tennessee_eastman, hai |
| HR:trough | m | SBP:trough | 2.186 | 2.535 | 1571 | True | `MID.trough -m-> MID.trough` | — | tennessee_eastman, hai |
| SBP:trough | l | SBP:peak | 2.106 | 2.028 | 3059 | True | `MID.trough -l-> MID.peak [same role]` | — | tennessee_eastman, hai |
| RESP:peak | l | RESP:peak | 2.092 | 1.974 | 17596 | True | `FAST.peak -l-> FAST.peak [same role]` | — | tennessee_eastman, hai, nasa_battery |
| HR:trough | m | DBP:trough | 2.072 | 2.95 | 1783 | True | `MID.trough -m-> MID.trough` | — | tennessee_eastman, hai |
| HR:trough | s | RESP:peak | 2.007 | 1.637 | 2628 | True | `MID.trough -s-> FAST.peak` | — | tennessee_eastman, hai |
| RESP:trough | l | RESP:trough | 1.998 | 2.208 | 17588 | True | `FAST.trough -l-> FAST.trough [same role]` | — | tennessee_eastman, hai, nasa_battery |
| HR:peak | s | RESP:trough | 1.935 | 1.584 | 3233 | True | `MID.peak -s-> FAST.trough` | — | tennessee_eastman, hai |
| DBP:peak | l | DBP:trough | 1.858 | 1.802 | 3480 | True | `MID.peak -l-> MID.trough [same role]` | — | tennessee_eastman, hai |
| DBP:trough | l | DBP:peak | 1.841 | 1.692 | 3692 | True | `MID.trough -l-> MID.peak [same role]` | — | tennessee_eastman, hai |
| SBP:peak | l | SBP:trough | 1.817 | 1.993 | 2468 | True | `MID.peak -l-> MID.trough [same role]` | — | tennessee_eastman, hai |

## Loops (returns; verdicts recorded, not promoted)

| X | l1 | Y | l2 | X′ | n | cond. lift | timing (g1 / g2) | determinism (p1 / p2) | used |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Chains (non-return): 3.

## Absences

- silent roles: none
- roles never a target: ['HR', 'SO2']
- keyed pairs not found: SBP → HR; RESP → HR; RESP → SO2
- signal floor: 1039 (absence is informative only for pairs whose support would exceed the signal floor)

## Regimes

3624 annotations

## Matrix row

Cells in (this system as receiver):

| source | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tennessee_eastman | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | marginal | — | 10/10 |  |
| hai | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | marginal | — | 10/10 |  |
| nasa_battery | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | marginal | — | 2/10 |  |
| alibaba_2018 | 0.00 | — | 0.00 | 0.00 | 0.00 | marginal | — | 0/10 | uncontrolled |

Cells out (this system as source):

| receiver | structure | net (derangement) | raw | marginal | derangement | larger control | share of ceiling | types | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tennessee_eastman | 62.39 | 62.39 | 81.83 | 7.13 | 19.44 | derangement | 0.35 | 4/40 | damage |
| hai | 0.99 | 5.02 | 37.84 | 36.84 | 32.82 | marginal | — | 4/168 | short, damage |
| nasa_battery | 0.03 | 0.03 | -0.27 | -0.32 | -0.29 | derangement | 0.01 | 2/12 | short, damage |
| alibaba_2018 | 0.00 | — | 1.25 | 1.25 | 1.25 | marginal | — | 0/27 | uncontrolled |

Nearest taxa by distance: shape_jaccard: tennessee_eastman 0.987, building_59 0.993, hai 0.996; shape_bray_curtis: building_59 0.985, tennessee_eastman 0.986, hai 0.993; transfer_net: tennessee_eastman 0.031, hai 0.669, nasa_battery 0.987
