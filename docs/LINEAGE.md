# Lineage — the collection step (METHOD 3.13), method v9

Characters are tagged shapes (3.14, 3.15); taxa are the admitted datasets whose libraries carry them: TEP, HAI, battery, PhysioNet, building_59, Fingrid.
The buildings are synthetic and untagged (3.14) and TCLab is withdrawn; both are inventoried for the record and are not taxa. A leaf marked provisional is below the admission line and flagged in every view.

## 1. Returns, the characters that matter most

| dataset | returns | distinct return shapes | the strongest return | shape |
| --- | --- | --- | --- | --- |
| TEP | 106 | 101 | `underflow_valve:downq20 -s-> P:downq80 -s-> underflow_valve:upq20` (n 29, cond. lift 8.35) | `MID·RELAY.down.q20 -s-> MID·FOLLOW.down.q80 -s-> MID·RELAY.up.q20 [return]` |
| HAI | 118 | 99 | `LIT01:upq80 -s-> LCV01D:upq20 -s-> LIT01:downq80` (n 15, cond. lift 9.01) | `MID·RELAY.up.q80 -s-> MID·RELAY.up.q20 -s-> MID·RELAY.down.q80 [return]` |
| battery | 1 | 1 | `I:downq10 -s-> V:downq20 -s-> I:upq10` (n 27, cond. lift 2.10) | `MID-S·RELAY.down.q10 -s-> MID·RELAY.down.q20 -s-> MID-S·RELAY.up.q10 [return]` |
| PhysioNet | 0 | 0 | — | — |
| building_59 | 299 | 209 | `oa_damper:downq90 -s-> ma_t:peak -s-> oa_damper:upq90` (n 13, cond. lift 12.14) | `MID-S·RELAY.down.q90 -s-> MID·RELAY.peak -s-> MID-S·RELAY.up.q90 [return]` |
| Fingrid | 3 | 3 | `afrr_up:upq80 -s-> f:trough -m-> afrr_up:downq80` (n 202, cond. lift 2.46) | `MID-S·RELAY.up.q80 -s-> MID·RELAY.trough -m-> MID-S·RELAY.down.q80 [return]` |

Return shapes shared between datasets:

- `MID·RELAY.up.q80 -m-> MID·RELAY.up.q20 -m-> MID·RELAY.down.q80 [return]` — TEP × 1, HAI × 1
- `SLOW·RELAY.down.q20 -s-> MID·RELAY.up.q20 -m-> SLOW·RELAY.up.q20 [return]` — TEP × 1, building_59 × 3
- `MID·RELAY.down.q50 -m-> MID·RELAY.down.q80 -m-> MID·RELAY.up.q50 [return]` — HAI × 1, building_59 × 1
- `MID-S·RELAY.down.q10 -s-> MID·RELAY.down.q20 -s-> MID-S·RELAY.up.q10 [return]` — battery × 1, building_59 × 1

Return place signatures (end → middle → end, from the place prefix):

- TEP: RELAY → RELAY → RELAY (47); RELAY → FOLLOW → RELAY (31); FOLLOW → RELAY → FOLLOW (24); FOLLOW → FOLLOW → FOLLOW (4)
- HAI: RELAY → RELAY → RELAY (113); LEAD → RELAY → LEAD (3); RELAY → LEAD → RELAY (2)
- battery: RELAY → RELAY → RELAY (1)
- PhysioNet: 
- building_59: RELAY → RELAY → RELAY (297); RELAY → LEAD → RELAY (2)
- Fingrid: RELAY → RELAY → RELAY (3)

## 2. Inventory

| dataset | standing | method | fragments (tagged) | fragment shapes | chains | chain shapes | returns | return shapes | library bits |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| building A | synthetic | v8 | 78 (0) | 0 | 15 | 0 | 1 | 0 | 2.164 |
| building B′ | synthetic | v8 | 131 (0) | 0 | 32 | 0 | 0 | 0 | 1.341 |
| TEP | admitted | v8 | 567 (567) | 295 | 525 | 380 | 106 | 101 | 3.033 |
| HAI | admitted (provisional: 15.3 days, 178 H; standing decision, section 6) | v8 | 2165 (2165) | 1098 | 1437 | 803 | 118 | 99 | 3.714 |
| TCLab | withdrawn | v8 | 3 (3) | 3 | 0 | 0 | 0 | 0 | 1.949 |
| battery | admitted | v8 | 47 (47) | 47 | 13 | 12 | 1 | 1 | 0.838 |
| PhysioNet | admitted (v7: by horizons, 19,419 H) | v8 | 22 (22) | 12 | 3 | 3 | 0 | 0 | 3.136 |
| building_59 | admitted (365 days) | v8 | 1285 (1285) | 720 | 1044 | 589 | 299 | 209 | 2.760 |
| Fingrid | admitted (365 days) | v8 | 71 (71) | 62 | 15 | 12 | 3 | 3 | 1.615 |
| Alibaba (neg. control) | negative control (admitted by horizons if so; flagged as a negative control in every view) | v9 | 86 (86) | 48 | 18 | 5 | 13 | 12 | 2.635 |

## 3. The character matrix (shape × dataset)

Same-role shapes (`[same role]`: a variable re-crossing its own thresholds, the function words of any bounded series) are counted apart from cross-role shapes; only a cross-role shape can be a finding about two systems.

| pair | fragment shapes shared: cross-role | same-role | chain shapes shared | return shapes shared |
| --- | --- | --- | --- | --- |
| TEP ↔ HAI | **79** | 59 | 4 | 1 |
| TEP ↔ battery | **0** | 7 | 0 | 0 |
| TEP ↔ PhysioNet | **2** | 2 | 0 | 0 |
| TEP ↔ building_59 | **104** | 42 | 5 | 1 |
| TEP ↔ Fingrid | **0** | 0 | 0 | 0 |
| HAI ↔ battery | **0** | 9 | 0 | 0 |
| HAI ↔ PhysioNet | **2** | 2 | 0 | 0 |
| HAI ↔ building_59 | **128** | 58 | 3 | 1 |
| HAI ↔ Fingrid | **22** | 15 | 0 | 0 |
| battery ↔ PhysioNet | **0** | 0 | 0 | 0 |
| battery ↔ building_59 | **12** | 13 | 2 | 1 |
| battery ↔ Fingrid | **0** | 0 | 0 | 0 |
| PhysioNet ↔ building_59 | **3** | 2 | 0 | 0 |
| PhysioNet ↔ Fingrid | **0** | 0 | 0 | 0 |
| building_59 ↔ Fingrid | **0** | 0 | 0 | 0 |

Shapes present in every taxon: **0** (0 cross-role, 0 same-role).

Cross-role fragment shapes shared by TEP and PhysioNet (2):

- `MID.peak -s-> MID.peak` (TEP × 1, PhysioNet × 3)
- `MID.trough -s-> MID.trough` (TEP × 1, PhysioNet × 2)

Cross-role fragment shapes shared by HAI and PhysioNet (2):

- `MID.peak -s-> MID.peak` (HAI × 14, PhysioNet × 3)
- `MID.trough -s-> MID.trough` (HAI × 18, PhysioNet × 2)

Cross-role fragment shapes shared by HAI and Fingrid (22):

- `MID-S.down.q20 -l-> MID-S.peak` (HAI × 1, Fingrid × 1)
- `MID-S.down.q80 -s-> MID.peak` (HAI × 2, Fingrid × 1)
- `MID-S.peak -m-> MID-S.down.q50` (HAI × 3, Fingrid × 1)
- `MID-S.peak -m-> MID-S.up.q50` (HAI × 1, Fingrid × 1)
- `MID-S.peak -m-> MID-S.up.q80` (HAI × 1, Fingrid × 2)
- `MID-S.peak -m-> MID.peak` (HAI × 1, Fingrid × 1)
- `MID-S.peak -m-> MID.trough` (HAI × 1, Fingrid × 2)
- `MID-S.trough -l-> MID-S.peak` (HAI × 2, Fingrid × 1)
- `MID-S.trough -m-> MID-S.up.q20` (HAI × 6, Fingrid × 2)
- `MID-S.trough -m-> MID.peak` (HAI × 1, Fingrid × 1)
- `MID-S.trough -m-> MID.trough` (HAI × 1, Fingrid × 1)
- `MID-S.trough -s-> MID.peak` (HAI × 4, Fingrid × 2)
- `MID-S.up.q50 -m-> MID-S.peak` (HAI × 4, Fingrid × 1)
- `MID.peak -m-> MID-S.peak` (HAI × 2, Fingrid × 1)
- `MID.peak -m-> MID-S.up.q20` (HAI × 1, Fingrid × 1)
- `MID.peak -s-> MID-S.down.q20` (HAI × 1, Fingrid × 1)
- `MID.peak -s-> MID-S.down.q50` (HAI × 1, Fingrid × 1)
- `MID.peak -s-> MID-S.peak` (HAI × 1, Fingrid × 1)
- `MID.trough -m-> MID-S.down.q80` (HAI × 3, Fingrid × 1)
- `MID.trough -m-> MID-S.trough` (HAI × 2, Fingrid × 2)
- `MID.trough -s-> MID-S.trough` (HAI × 3, Fingrid × 1)
- `MID.trough -s-> MID-S.up.q80` (HAI × 2, Fingrid × 1)

Cross-role fragment shapes shared by battery and building_59 (12):

- `MID-S.down.q10 -s-> MID.down.q20` (battery × 1, building_59 × 2)
- `MID-S.down.q90 -l-> MID.down.q50` (battery × 1, building_59 × 2)
- `MID-S.down.q90 -m-> MID.down.q80` (battery × 1, building_59 × 1)
- `MID-S.down.q90 -s-> MID.up.q50` (battery × 1, building_59 × 1)
- `MID-S.up.q90 -l-> MID.down.q50` (battery × 1, building_59 × 2)
- `MID-S.up.q90 -l-> MID.down.q80` (battery × 1, building_59 × 1)
- `MID-S.up.q90 -m-> MID.up.q50` (battery × 1, building_59 × 1)
- `MID.down.q20 -m-> MID-S.up.q10` (battery × 1, building_59 × 2)
- `MID.down.q20 -s-> MID-S.down.q10` (battery × 1, building_59 × 1)
- `MID.down.q20 -s-> MID-S.up.q10` (battery × 1, building_59 × 1)
- `MID.up.q20 -m-> MID-S.up.q90` (battery × 1, building_59 × 2)
- `MID.up.q20 -s-> MID-S.up.q90` (battery × 1, building_59 × 1)

Cross-role fragment shapes shared by PhysioNet and building_59 (3):

- `MID.peak -m-> MID.peak` (PhysioNet × 3, building_59 × 2)
- `MID.peak -s-> MID.peak` (PhysioNet × 3, building_59 × 5)
- `MID.trough -s-> MID.trough` (PhysioNet × 2, building_59 × 2)

## 4. Similarity trees

**shape_jaccard** — `(physionet_slp:0.498,(fingrid:0.496,(nasa_battery:0.490,(hai:0.444,(tennessee_eastman:0.416,building_59:0.416):0.444):0.490):0.496):0.498);`

| | TEP | HAI | battery | PhysioNet | building_59 | Fingrid |
| --- | --- | --- | --- | --- | --- | --- |
| TEP | 0.000 | 0.890 | 0.979 | 0.987 | 0.832 | 1.000 |
| HAI | 0.890 | 0.000 | 0.992 | 0.996 | 0.886 | 0.967 |
| battery | 0.979 | 0.992 | 0.000 | 1.000 | 0.966 | 1.000 |
| PhysioNet | 0.987 | 0.996 | 1.000 | 0.000 | 0.993 | 1.000 |
| building_59 | 0.832 | 0.886 | 0.966 | 0.993 | 0.000 | 1.000 |
| Fingrid | 1.000 | 0.967 | 1.000 | 1.000 | 1.000 | 0.000 |

**shape_bray_curtis** — `(fingrid:0.496,(physionet_slp:0.495,(nasa_battery:0.489,(hai:0.422,(tennessee_eastman:0.388,building_59:0.388):0.422):0.489):0.495):0.496);`

| | TEP | HAI | battery | PhysioNet | building_59 | Fingrid |
| --- | --- | --- | --- | --- | --- | --- |
| TEP | 0.000 | 0.849 | 0.977 | 0.986 | 0.775 | 1.000 |
| HAI | 0.849 | 0.000 | 0.992 | 0.993 | 0.841 | 0.964 |
| battery | 0.977 | 0.992 | 0.000 | 1.000 | 0.963 | 1.000 |
| PhysioNet | 0.986 | 0.993 | 1.000 | 0.000 | 0.985 | 1.000 |
| building_59 | 0.775 | 0.841 | 0.963 | 0.985 | 0.000 | 1.000 |
| Fingrid | 1.000 | 0.964 | 1.000 | 1.000 | 1.000 | 0.000 |

**transfer_net** — `(nasa_battery:0.488,((tennessee_eastman:0.016,physionet_slp:0.016):0.395,(fingrid:0.176,(hai:0.042,building_59:0.042):0.176):0.395):0.488);`

| | TEP | HAI | battery | PhysioNet | building_59 | Fingrid |
| --- | --- | --- | --- | --- | --- | --- |
| TEP | 0.000 | 1.000 | 1.000 | 0.031 | 0.075 | 1.000 |
| HAI | 1.000 | 0.000 | 0.893 | 0.669 | 0.085 | 0.216 |
| battery | 1.000 | 0.893 | 0.000 | 0.987 | 1.000 | 1.000 |
| PhysioNet | 0.031 | 0.669 | 0.987 | 0.000 | 1.000 | 1.000 |
| building_59 | 0.075 | 0.085 | 1.000 | 1.000 | 0.000 | 0.489 |
| Fingrid | 1.000 | 0.216 | 1.000 | 1.000 | 0.489 | 0.000 |

Shape distances: Jaccard over fragment shapes (1 − shared / union), Bray–Curtis over shape counts. Transfer distance: 1 / (1 + symmetrised net cell in bit-horizons) of the current version; a pair without a controlled cell is at 1.

## 5. Inheritance graph

Inheritance is directed by **running order**: a shape belongs to the dataset that validated it first and is inherited by every later dataset that validates it again, so a zero in the reverse direction is the order, not the physics; the symmetric view is the character matrix above. Confirmation through a mapping is directed by the transfer cell and runs both ways.

| from → to | shapes recurred (inherited) | of them returns | fragments tested through the mapping | confirmed | failed |
| --- | --- | --- | --- | --- | --- |
| TEP → building_59 | 152 | 1 | 428 | 79 | 349 |
| TEP → HAI | 143 | 1 | 377 | 81 | 296 |
| TEP → battery | 7 | 0 | 39 | 10 | 29 |
| TEP → PhysioNet | 4 | 0 | 0 | 0 | 0 |
| HAI → Fingrid | 37 | 0 | 33 | 10 | 23 |
| HAI → building_59 | 119 | 1 | 966 | 112 | 854 |
| HAI → battery | 3 | 0 | 15 | 4 | 11 |
| battery → building_59 | 20 | 1 | 0 | 0 | 0 |
| PhysioNet → building_59 | 1 | 0 | 0 | 0 | 0 |
| HAI → TEP | 0 | 0 | 1849 | 89 | 1760 |
| battery → TEP | 0 | 0 | 47 | 5 | 42 |
| battery → HAI | 0 | 0 | 34 | 3 | 31 |
| PhysioNet → TEP | 0 | 0 | 22 | 0 | 22 |
| HAI → PhysioNet | 0 | 0 | 8 | 1 | 7 |
| PhysioNet → HAI | 0 | 0 | 22 | 0 | 22 |
| battery → PhysioNet | 0 | 0 | 0 | 0 | 0 |
| PhysioNet → battery | 0 | 0 | 2 | 0 | 2 |
| building_59 → TEP | 0 | 0 | 1218 | 83 | 1135 |
| building_59 → HAI | 0 | 0 | 1255 | 102 | 1153 |
| TEP → Fingrid | 0 | 0 | 0 | 0 | 0 |
| Fingrid → TEP | 0 | 0 | 71 | 13 | 58 |
| Fingrid → HAI | 0 | 0 | 71 | 10 | 61 |
| battery → Fingrid | 0 | 0 | 18 | 4 | 14 |
| Fingrid → battery | 0 | 0 | 11 | 3 | 8 |
| building_59 → Fingrid | 0 | 0 | 34 | 8 | 26 |
| Fingrid → building_59 | 0 | 0 | 25 | 6 | 19 |

Shapes by the dataset that first validated them (running order): TEP 776, HAI 1857, battery 50, PhysioNet 11, building_59 1226, Fingrid 40.

Inherited shapes (validated again in a later dataset): **402**, of them returns 4, chains 12.

Shapes confirmed through a mapping in another dataset: 300; tested and failed: 1653.

Lineage of the return shapes present in more than one dataset, or tested through a mapping:

- `MID·RELAY.up.q80 -m-> MID·RELAY.up.q20 -m-> MID·RELAY.down.q80 [return]`: first TEP; recurred HAI; confirmed via mapping —; failed —
- `SLOW·RELAY.down.q20 -s-> MID·RELAY.up.q20 -m-> SLOW·RELAY.up.q20 [return]`: first TEP; recurred building_59; confirmed via mapping —; failed —
- `MID·RELAY.down.q50 -m-> MID·RELAY.down.q80 -m-> MID·RELAY.up.q50 [return]`: first HAI; recurred building_59; confirmed via mapping —; failed —
- `MID-S·RELAY.down.q10 -s-> MID·RELAY.down.q20 -s-> MID-S·RELAY.up.q10 [return]`: first battery; recurred building_59; confirmed via mapping —; failed —
