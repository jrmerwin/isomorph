# Lineage — the collection step (METHOD 3.13), method v7

Characters are tagged shapes (3.14, 3.15); taxa are the admitted datasets whose libraries carry them: TEP, HAI, battery, PhysioNet, building_59.
The buildings are synthetic and untagged (3.14) and TCLab is withdrawn; both are inventoried for the record and are not taxa. A leaf marked provisional is below the admission line and flagged in every view.

## 1. Returns, the characters that matter most

| dataset | returns | distinct return shapes | the strongest return | shape |
| --- | --- | --- | --- | --- |
| TEP | 106 | 103 | `underflow_valve:downq20 -s-> P:downq80 -s-> underflow_valve:upq20` (n 29, cond. lift 8.35) | `MID·REACTS.down.q20 -s-> MID·FOLLOW.down.q80 -s-> MID·REACTS.up.q20 [return]` |
| HAI | 118 | 106 | `LIT01:upq80 -s-> LCV01D:upq20 -s-> LIT01:downq80` (n 15, cond. lift 9.01) | `MID·REACTS.up.q80 -s-> MID·RESPONDS.up.q20 -s-> MID·REACTS.down.q80 [return]` |
| battery | 1 | 1 | `I:downq10 -s-> V:downq20 -s-> I:upq10` (n 27, cond. lift 2.10) | `MID-S·REACTS.down.q10 -s-> MID·RESPONDS.down.q20 -s-> MID-S·REACTS.up.q10 [return]` |
| PhysioNet | 0 | 0 | — | — |
| building_59 | 299 | 268 | `oa_damper:downq90 -s-> ma_t:peak -s-> oa_damper:upq90` (n 13, cond. lift 12.14) | `MID-S·REACTS.down.q90 -s-> MID·RESPONDS.peak -s-> MID-S·REACTS.up.q90 [return]` |

No return shape is shared between any two taxa.

Return place signatures (end → middle → end, from the place prefix):

- TEP: RESPONDS → RESPONDS → RESPONDS (29); RESPONDS → FOLLOW → RESPONDS (18); REACTS → FOLLOW → REACTS (13); FOLLOW → RESPONDS → FOLLOW (13); FOLLOW → REACTS → FOLLOW (11)
- HAI: RESPONDS → REACTS → RESPONDS (42); REACTS → RESPONDS → REACTS (33); RESPONDS → RESPONDS → RESPONDS (12); REACTS → REACTS → REACTS (8); RELAY → REACTS → RELAY (7)
- battery: REACTS → RESPONDS → REACTS (1)
- PhysioNet: 
- building_59: REACTS → RESPONDS → REACTS (87); REACTS → REACTS → REACTS (55); RESPONDS → REACTS → RESPONDS (44); RESPONDS → RESPONDS → RESPONDS (33); REACTS → RELAY → REACTS (31)

## 2. Inventory

| dataset | standing | method | fragments (tagged) | fragment shapes | chains | chain shapes | returns | return shapes | library bits |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| building A | synthetic | v7 | 78 (0) | 0 | 15 | 0 | 1 | 0 | 2.164 |
| building B′ | synthetic | v7 | 131 (0) | 0 | 32 | 0 | 0 | 0 | 1.341 |
| TEP | admitted | v7 | 567 (567) | 295 | 525 | 388 | 106 | 103 | 3.033 |
| HAI | admitted (provisional: 15.3 days, 178 H; standing decision, section 6) | v7 | 2165 (2165) | 1098 | 1437 | 1039 | 118 | 106 | 3.714 |
| TCLab | withdrawn | v7 | 3 (3) | 3 | 0 | 0 | 0 | 0 | 1.949 |
| battery | admitted | v7 | 47 (47) | 47 | 13 | 12 | 1 | 1 | 0.838 |
| PhysioNet | admitted (v7: by horizons, 19,419 H) | v7 | 22 (22) | 12 | 3 | 3 | 0 | 0 | 3.136 |
| building_59 | admitted (365 days) | v7 | 1285 (1285) | 720 | 1044 | 697 | 299 | 268 | 2.760 |

## 3. The character matrix (shape × dataset)

Same-role shapes (`[same role]`: a variable re-crossing its own thresholds, the function words of any bounded series) are counted apart from cross-role shapes; only a cross-role shape can be a finding about two systems.

| pair | fragment shapes shared: cross-role | same-role | chain shapes shared | return shapes shared |
| --- | --- | --- | --- | --- |
| TEP ↔ HAI | **79** | 59 | 0 | 0 |
| TEP ↔ battery | **0** | 7 | 0 | 0 |
| TEP ↔ PhysioNet | **2** | 2 | 0 | 0 |
| TEP ↔ building_59 | **104** | 42 | 2 | 0 |
| HAI ↔ battery | **0** | 9 | 0 | 0 |
| HAI ↔ PhysioNet | **2** | 2 | 0 | 0 |
| HAI ↔ building_59 | **128** | 58 | 0 | 0 |
| battery ↔ PhysioNet | **0** | 0 | 0 | 0 |
| battery ↔ building_59 | **12** | 13 | 0 | 0 |
| PhysioNet ↔ building_59 | **3** | 2 | 0 | 0 |

Shapes present in every taxon: **0** (0 cross-role, 0 same-role).

Cross-role fragment shapes shared by TEP and PhysioNet (2):

- `MID.peak -s-> MID.peak` (TEP × 1, PhysioNet × 3)
- `MID.trough -s-> MID.trough` (TEP × 1, PhysioNet × 2)

Cross-role fragment shapes shared by HAI and PhysioNet (2):

- `MID.peak -s-> MID.peak` (HAI × 14, PhysioNet × 3)
- `MID.trough -s-> MID.trough` (HAI × 18, PhysioNet × 2)

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

**shape_jaccard** — `(physionet_slp:0.497,(nasa_battery:0.490,(hai:0.444,(tennessee_eastman:0.416,building_59:0.416):0.444):0.490):0.497);`

| | TEP | HAI | battery | PhysioNet | building_59 |
| --- | --- | --- | --- | --- | --- |
| TEP | 0.000 | 0.890 | 0.979 | 0.987 | 0.832 |
| HAI | 0.890 | 0.000 | 0.992 | 0.996 | 0.886 |
| battery | 0.979 | 0.992 | 0.000 | 1.000 | 0.966 |
| PhysioNet | 0.987 | 0.996 | 1.000 | 0.000 | 0.993 |
| building_59 | 0.832 | 0.886 | 0.966 | 0.993 | 0.000 |

**shape_bray_curtis** — `(physionet_slp:0.495,(nasa_battery:0.489,(hai:0.422,(tennessee_eastman:0.388,building_59:0.388):0.422):0.489):0.495);`

| | TEP | HAI | battery | PhysioNet | building_59 |
| --- | --- | --- | --- | --- | --- |
| TEP | 0.000 | 0.849 | 0.977 | 0.986 | 0.775 |
| HAI | 0.849 | 0.000 | 0.992 | 0.993 | 0.841 |
| battery | 0.977 | 0.992 | 0.000 | 1.000 | 0.963 |
| PhysioNet | 0.986 | 0.993 | 1.000 | 0.000 | 0.985 |
| building_59 | 0.775 | 0.841 | 0.963 | 0.985 | 0.000 |

**transfer_net** — `(nasa_battery:0.435,(physionet_slp:0.324,(hai:0.061,(tennessee_eastman:0.008,building_59:0.008):0.061):0.324):0.435);`

| | TEP | HAI | battery | PhysioNet | building_59 |
| --- | --- | --- | --- | --- | --- |
| TEP | 0.000 | 0.184 | 0.513 | 0.100 | 0.016 |
| HAI | 0.184 | 0.000 | 0.970 | 0.843 | 0.059 |
| battery | 0.513 | 0.970 | 0.000 | 1.000 | 1.000 |
| PhysioNet | 0.100 | 0.843 | 1.000 | 0.000 | 1.000 |
| building_59 | 0.016 | 0.059 | 1.000 | 1.000 | 0.000 |

Shape distances: Jaccard over fragment shapes (1 − shared / union), Bray–Curtis over shape counts. Transfer distance: 1 / (1 + symmetrised net cell) of the current version; a pair without a cell is at 1.

## 5. Inheritance graph

Inheritance is directed by **running order**: a shape belongs to the dataset that validated it first and is inherited by every later dataset that validates it again, so a zero in the reverse direction is the order, not the physics; the symmetric view is the character matrix above. Confirmation through a mapping is directed by the transfer cell and runs both ways.

| from → to | shapes recurred (inherited) | of them returns | fragments tested through the mapping | confirmed | failed |
| --- | --- | --- | --- | --- | --- |
| TEP → HAI | 138 | 0 | 377 | 81 | 296 |
| TEP → building_59 | 148 | 0 | 428 | 79 | 349 |
| TEP → battery | 7 | 0 | 39 | 10 | 29 |
| TEP → PhysioNet | 4 | 0 | 0 | 0 | 0 |
| HAI → building_59 | 116 | 0 | 951 | 96 | 855 |
| HAI → battery | 3 | 0 | 23 | 2 | 21 |
| battery → building_59 | 17 | 0 | 0 | 0 | 0 |
| PhysioNet → building_59 | 1 | 0 | 0 | 0 | 0 |
| HAI → TEP | 0 | 0 | 1737 | 80 | 1657 |
| battery → TEP | 0 | 0 | 47 | 5 | 42 |
| battery → HAI | 0 | 0 | 34 | 3 | 31 |
| PhysioNet → TEP | 0 | 0 | 22 | 0 | 22 |
| HAI → PhysioNet | 0 | 0 | 8 | 1 | 7 |
| PhysioNet → HAI | 0 | 0 | 22 | 0 | 22 |
| battery → PhysioNet | 0 | 0 | 0 | 0 | 0 |
| PhysioNet → battery | 0 | 0 | 2 | 0 | 2 |
| building_59 → TEP | 0 | 0 | 1218 | 83 | 1135 |
| building_59 → HAI | 0 | 0 | 1154 | 114 | 1040 |

Shapes by the dataset that first validated them (running order): TEP 786, HAI 2105, battery 50, PhysioNet 11, building_59 1403.

Inherited shapes (validated again in a later dataset): **351**, of them returns 0, chains 2.

Shapes confirmed through a mapping in another dataset: 278; tested and failed: 1557.

Lineage of the return shapes present in more than one dataset, or tested through a mapping:

- none yet: returns do not cross datasets under the mappings of this version.
