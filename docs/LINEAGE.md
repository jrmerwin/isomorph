# Lineage — the collection step (METHOD 3.13), method v6

Characters are tagged shapes (3.14, 3.15); taxa are the admitted datasets whose libraries carry them: TEP, HAI, battery, PhysioNet.
The buildings are synthetic and untagged (3.14) and TCLab is withdrawn; both are inventoried for the record and are not taxa. A leaf marked provisional is below the admission line and flagged in every view.

## 1. Returns, the characters that matter most

| dataset | returns | distinct return shapes | the strongest return | shape |
| --- | --- | --- | --- | --- |
| TEP | 106 | 101 | `underflow_valve:downq20 -s-> P:downq80 -s-> underflow_valve:upq20` (n 29, cond. lift 8.35) | `MID·RELAY.down.q20 -s-> MID·FOLLOW.down.q80 -s-> MID·RELAY.up.q20 [return]` |
| HAI | 118 | 99 | `LIT01:upq80 -s-> LCV01D:upq20 -s-> LIT01:downq80` (n 15, cond. lift 9.01) | `MID·RELAY.up.q80 -s-> MID·RELAY.up.q20 -s-> MID·RELAY.down.q80 [return]` |
| battery | 1 | 1 | `I:downq10 -s-> V:downq20 -s-> I:upq10` (n 27, cond. lift 2.10) | `MID-S·RELAY.down.q10 -s-> MID·RELAY.down.q20 -s-> MID-S·RELAY.up.q10 [return]` |
| PhysioNet | 0 | 0 | — | — |

Return shapes shared between datasets:

- `MID·RELAY.up.q80 -m-> MID·RELAY.up.q20 -m-> MID·RELAY.down.q80 [return]` — TEP × 1, HAI × 1

Return place signatures (end → middle → end, from the place prefix):

- TEP: RELAY → RELAY → RELAY (47); RELAY → FOLLOW → RELAY (31); FOLLOW → RELAY → FOLLOW (24); FOLLOW → FOLLOW → FOLLOW (4)
- HAI: RELAY → RELAY → RELAY (113); LEAD → RELAY → LEAD (3); RELAY → LEAD → RELAY (2)
- battery: RELAY → RELAY → RELAY (1)
- PhysioNet: 

## 2. Inventory

| dataset | standing | method | fragments (tagged) | fragment shapes | chains | chain shapes | returns | return shapes | library bits |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| building A | synthetic | v6 | 78 (0) | 0 | 15 | 0 | 1 | 0 | 2.164 |
| building B′ | synthetic | v6 | 131 (0) | 0 | 32 | 0 | 0 | 0 | 1.341 |
| TEP | admitted | v6 | 567 (567) | 295 | 525 | 380 | 106 | 101 | 3.033 |
| HAI | admitted (provisional) | v6 | 2165 (2165) | 1098 | 1437 | 803 | 118 | 99 | 3.714 |
| TCLab | withdrawn | v6 | 3 (3) | 3 | 0 | 0 | 0 | 0 | 1.949 |
| battery | admitted | v6 | 47 (47) | 47 | 13 | 12 | 1 | 1 | 0.838 |
| PhysioNet | provisional (not admitted as the rule stands: 3.6 days, no period found; flagged) | v6 | 37 (37) | 31 | 1 | 1 | 0 | 0 | 4.931 |

## 3. The character matrix (shape × dataset)

| pair | fragment shapes shared | chain shapes shared | return shapes shared |
| --- | --- | --- | --- |
| TEP ↔ HAI | 138 | 4 | 1 |
| TEP ↔ battery | 7 | 0 | 0 |
| TEP ↔ PhysioNet | 22 | 1 | 0 |
| HAI ↔ battery | 9 | 0 | 0 |
| HAI ↔ PhysioNet | 26 | 1 | 0 |
| battery ↔ PhysioNet | 3 | 0 | 0 |

Shapes present in every taxon: **3**.

| shape | TEP | HAI | battery | PhysioNet |
| --- | --- | --- | --- | --- |
| `MID.up.q50 -s-> MID.up.q80 [same role]` | 5 | 5 | 1 | 1 |
| `MID.up.q80 -m-> MID.down.q80 [same role]` | 5 | 4 | 1 | 1 |
| `MID.down.q80 -s-> MID.down.q50 [same role]` | 5 | 3 | 1 | 1 |

Fragment shapes shared by TEP and battery (7):

- `MID.down.q50 -s-> MID.up.q50 [same role]` (TEP × 1, battery × 1)
- `MID.down.q80 -s-> MID.down.q50 [same role]` (TEP × 5, battery × 1)
- `MID.up.q50 -l-> MID.down.q80 [same role]` (TEP × 1, battery × 1)
- `MID.up.q50 -s-> MID.up.q80 [same role]` (TEP × 5, battery × 1)
- `MID.up.q80 -m-> MID.down.q50 [same role]` (TEP × 2, battery × 1)
- `MID.up.q80 -m-> MID.down.q80 [same role]` (TEP × 5, battery × 1)
- `MID.up.q80 -s-> MID.down.q80 [same role]` (TEP × 5, battery × 1)

Fragment shapes shared by HAI and battery (9):

- `MID-S.down.q10 -m-> MID-S.up.q10 [same role]` (HAI × 1, battery × 1)
- `MID.down.q50 -s-> MID.up.q50 [same role]` (HAI × 4, battery × 1)
- `MID.down.q80 -s-> MID.down.q50 [same role]` (HAI × 3, battery × 1)
- `MID.down.q80 -s-> MID.up.q80 [same role]` (HAI × 2, battery × 1)
- `MID.up.q50 -l-> MID.down.q50 [same role]` (HAI × 1, battery × 1)
- `MID.up.q50 -s-> MID.up.q80 [same role]` (HAI × 5, battery × 1)
- `MID.up.q80 -m-> MID.down.q50 [same role]` (HAI × 1, battery × 1)
- `MID.up.q80 -m-> MID.down.q80 [same role]` (HAI × 4, battery × 1)
- `MID.up.q80 -s-> MID.down.q80 [same role]` (HAI × 3, battery × 1)

Fragment shapes shared by battery and PhysioNet (3):

- `MID.down.q80 -s-> MID.down.q50 [same role]` (battery × 1, PhysioNet × 1)
- `MID.up.q50 -s-> MID.up.q80 [same role]` (battery × 1, PhysioNet × 1)
- `MID.up.q80 -m-> MID.down.q80 [same role]` (battery × 1, PhysioNet × 1)

## 4. Similarity trees

**shape_jaccard** — `(nasa_battery:0.489,(physionet_slp:0.476,(tennessee_eastman:0.445,hai:0.445):0.476):0.489);`

| | TEP | HAI | battery | PhysioNet |
| --- | --- | --- | --- | --- |
| TEP | 0.000 | 0.890 | 0.979 | 0.928 |
| HAI | 0.890 | 0.000 | 0.992 | 0.976 |
| battery | 0.979 | 0.992 | 0.000 | 0.960 |
| PhysioNet | 0.928 | 0.976 | 0.960 | 0.000 |

**shape_bray_curtis** — `((tennessee_eastman:0.424,hai:0.424):0.483,(nasa_battery:0.464,physionet_slp:0.464):0.483);`

| | TEP | HAI | battery | PhysioNet |
| --- | --- | --- | --- | --- |
| TEP | 0.000 | 0.849 | 0.977 | 0.927 |
| HAI | 0.849 | 0.000 | 0.992 | 0.971 |
| battery | 0.977 | 0.992 | 0.000 | 0.929 |
| PhysioNet | 0.927 | 0.971 | 0.929 | 0.000 |

**transfer_net** — `(nasa_battery:0.394,(physionet_slp:0.313,(tennessee_eastman:0.061,hai:0.061):0.313):0.394);`

| | TEP | HAI | battery | PhysioNet |
| --- | --- | --- | --- | --- |
| TEP | 0.000 | 0.122 | 0.512 | 0.336 |
| HAI | 0.122 | 0.000 | 0.934 | 0.915 |
| battery | 0.512 | 0.934 | 0.000 | 0.920 |
| PhysioNet | 0.336 | 0.915 | 0.920 | 0.000 |

Shape distances: Jaccard over fragment shapes (1 − shared / union), Bray–Curtis over shape counts. Transfer distance: 1 / (1 + symmetrised net cell) of the current version; a pair without a cell is at 1.

## 5. Inheritance graph

| from → to | shapes recurred (inherited) | of them returns | fragments tested through the mapping | confirmed | failed |
| --- | --- | --- | --- | --- | --- |
| TEP → HAI | 143 | 1 | 377 | 81 | 296 |
| TEP → PhysioNet | 23 | 0 | 35 | 15 | 20 |
| TEP → battery | 7 | 0 | 39 | 10 | 29 |
| HAI → battery | 3 | 0 | 15 | 4 | 11 |
| HAI → PhysioNet | 6 | 0 | 22 | 6 | 16 |
| HAI → TEP | 0 | 0 | 1849 | 89 | 1760 |
| battery → TEP | 0 | 0 | 47 | 5 | 42 |
| battery → HAI | 0 | 0 | 34 | 3 | 31 |
| PhysioNet → TEP | 0 | 0 | 37 | 15 | 22 |
| PhysioNet → HAI | 0 | 0 | 37 | 15 | 22 |
| battery → PhysioNet | 0 | 0 | 18 | 3 | 15 |
| PhysioNet → battery | 0 | 0 | 21 | 3 | 18 |

Shapes by the dataset that first validated them (running order): TEP 776, HAI 1857, battery 50, PhysioNet 3.

Inherited shapes (validated again in a later dataset): **155**, of them returns 1, chains 4.

Shapes confirmed through a mapping in another dataset: 117; tested and failed: 1068.

Lineage of the return shapes present in more than one dataset, or tested through a mapping:

- `MID·RELAY.up.q80 -m-> MID·RELAY.up.q20 -m-> MID·RELAY.down.q80 [return]`: first TEP; recurred HAI; confirmed via mapping —; failed —
