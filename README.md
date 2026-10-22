# isomorph

*Validated motif libraries from event streams, and how much they transfer between systems.*

Complex physical and informational systems may instantiate recurring, substrate-independent logical
structures. These structures can potentially be inferred from observational data as compositional motifs,
organized into families, and studied to discover the conditions governing their recurrence,
transformation, and transfer.

A system — a building, a plant, a cluster, an organism — leaves a stream of events. isomorph turns that
stream into a library of validated motifs (lagged, entity-bound fragments of structure), scores the
library against fixed baselines in bits per event, and measures how much the library helps on every
other system in the collection. The collection's outputs are a directed **transfer matrix** (which
systems can teach which) and the **lineage** of a shared library grown across datasets: where each
motif first appeared, where it was inherited, where it failed.

The thesis is the one the name states: the same form can appear in different substance. Whether it does,
and what shared structure says about the processes that produced it, is the research question. The
method is built so that the answer is read off the data, not argued — one ruler, applied unchanged to
every dataset, with every claim carrying its control and its sign.

The method is specified in [docs/METHOD.md](docs/METHOD.md). The experiments that set its constants are
recorded in [docs/RESULTS_session_2026-10-18.md](docs/RESULTS_session_2026-10-18.md).

## Status

Method **v8** implemented, **v9** specified (collection-only) (integer versions; amendments are logged in `CHANGELOG.md`; cards valid from v6). The collection's lineage — returns, the character matrix, similarity trees and the inheritance graph over four taxa — is in [docs/LINEAGE.md](docs/LINEAGE.md).

| # | dataset | library vs triviality / best baseline (bits per event, test split) | claim |
| --- | --- | --- | --- |
| 1 | building A (synthetic, calibration) | 2.167 vs 2.169 / 2.562 | no gain |
| 2 | building B′ (synthetic, calibration) | 1.365 vs 1.530 / 1.860 | beats baselines |
| 3 | Tennessee Eastman, first 120 days ([card](docs/CARD_tennessee_eastman_v1.md)) | 3.033 vs 3.171 / 3.410 | beats baselines (v6: 525 chains, 106 returns; the cooling-water loop closes as RELAY → FOLLOW → RELAY) |
| 4 | HAI 21.03, 1-minute means, 15.3 days ([card](docs/CARD_hai_v2.md); provisional: 15.3 days, 178 H — below every v7 admission clause, kept by the standing decision in section 6) | 3.844 vs 3.805 / 3.892 (v6) | no gain (recovery 7/15: the physics is found but the alternation baseline already carries it; v6: 1,437 chains, 118 returns, the level loop LIT01 ↔ LCV01D the strongest) |
| 5 | TCLab ([card](docs/CARD_tclab_v1.md)) — **withdrawn from the running order 2026-10-20**: no public recording is long enough (7.6 h, no period); re-enters with a 24–48 h recording of both heaters | 1.949 vs 1.779 / 1.714 (v6) | not admitted |
| 6 | NASA PCoE battery set FY08Q4, four cells, 1-minute means, 47.5 observed days ([card](docs/CARD_nasa_battery_v1.md)) — Rosetta member one | 0.838 vs 0.827 / 1.087 (v6) | no gain (recovery 3/3 under v6 gap clipping, 47 fragments from 12; 13 chains used, 1 return: the discharge cutoff loop) |
| 7 | MIT-BIH Polysomnographic (PhysioNet slpdb), 18 nights, **0.25-second samples** ([card v2](docs/CARD_physionet_slp_v2.md); [v1 at 1 s](docs/CARD_physionet_slp_v1.md)); **admitted under v7 by horizons** (19,419 H in 3.6 days) | 3.136 vs 3.328 / 3.373 (v7) | **beats baselines** (+0.19 over triviality; recovery 2/5: respiration → pressures and HR → SBP found, respiratory sinus arrhythmia spelled HR → RESP by lead; no baroreflex return) |
| 8 | LBNL Building 59, four rooftop units and 51 underfloor zones, calendar year 2019 at 5-minute means ([card](docs/CARD_building_59_v1.md)); admitted (365 days, 641 H) | 2.760 vs 2.638 / 3.235 (v7) | no gain (recovery **9/11**, the best in the collection; 1,285 fragments, 1,044 chains, 299 returns; the economizer loop reads REACTS → RESPONDS → REACTS and the loop-role checks pass for the first time: flowsheet 0.63, dimension 0.50 / 0.80) |
| 9 | Fingrid, Nordic grid frequency regulation, one year at 3-minute samples ([card](docs/CARD_fingrid_v1.md)); admitted (365 days, 5,840 H); fetched with a key that is never stored | 1.615 vs 1.603 / 2.588 (v8) | no gain (recovery **6/7**: the frequency containment loop is the top of the library; 3 returns on the reserve side; +0.97 over every sequence baseline) |
| 10 | **Negative control one**: Alibaba cluster-trace-v2018 machine usage, 200-machine subsample, 8 days at 1-minute means ([card](docs/CARD_alibaba_2018_v1.md)); admitted by slow periods (324 H) | 2.635 vs 2.481 / 2.761 (v8 card) | no gain; **as a source into TEP its structure cell is 51.2 bit-H against a declared ≈ 0 — the stop condition of section 6: the cells into TEP are receiver-side regularisation (TEP's own curve sits above its own unigram), and the collection pauses until the receiver baseline is repaired** |

Transfer matrix — **paused at v9** (docs/MATRIX.md): the negative control's cell into TEP (51.2 bit-H structure, 29% of TEP's ceiling) shows the cells into TEP and Building 59 to be regularisation of a receiver whose own learning curve is worse than its unigram. The v8 rows below stand for the record; the v9 table with structure cells, both controls and shares of ceiling is in MATRIX.md.

| source → receiver | net cell | |
| --- | --- | --- |
| building A → B′ | 0.74 | same kind: alignment real (zero-shot 4.6 vs 7.9 permuted) |
| building B′ → A | 5.53 | the richer system teaches more |
| Tennessee Eastman → HAI | **0.90** (v6, seed 0; v5: 0.98, 0.83 ± 0.00 over seeds 0–4 under the earlier control; v4: 1.67, v3: 0.37) | cross kind; identical role map and cells on every seed; v5 control is stricter (within dimension) and the dimension constraint maps fewer types |
| HAI → Tennessee Eastman | **13.53** (v6, seed 0; v5: 14.45, 14.55 ± 0.87 over seeds 0–4 under the earlier control; v4: 10.52, v3: 0.06) | cross kind; raw cell stable to 0.03 across seeds, the spread is the control's; mixed curve beats TEP's own model by 0.3–0.6 bits to 20 days |
| Tennessee Eastman ↔ battery (6) | **0.25** / **1.65** (v6; v5: 0.00 / 0.00) | the spelling rule carries all 12 battery types; TEP → battery's learned zero-shot beats the permuted by 2.7 bits (3.68 vs 6.35), the first cross-kind alignment to do so; the cell is small because a 12-type protocol is learned in a day |
| HAI ↔ battery (6) | **0.05** / **0.09** (v6) | at zero both ways |
| TCLab (5) | withdrawn | no public recording long enough; the v5 cells (all zero) stand in the matrix for the record |

Implemented: canonical contract; compression-driven entity (3.1) and symbolization (3.2, with noise and
faithfulness floors); lag classes; period estimation and the cycle null; circular null (gate) and rewire
null (attribute); signal floor (descriptive); fixed baselines incl. Markov-3 and Hawkes-like decay features;
name-free triviality library; alignment and transfer with a global mixing weight and a permuted-mapping control; the transfer matrix (`isomorph transfer`); calibration gates.

Also implemented: the grammar (parts of speech, place prefix, dimension suffix; 3.14), syntax motifs (chains
and returns; 3.15), the collection matrix and lineage (`collect/matrix.py`, `collect/lineage.py`; `isomorph
transfer`, `isomorph lineage`). Also: loop roles recorded with their checks, the fine-grid period, admission in horizons (v7). Not yet: derangement
controls and the cell in bit-horizons to 200 receiver horizons (v8, specified in METHOD.md 3.12 / 3.16); per-fragment
transfer weights; pooled lag classes for alignment.

## Layout

```
isomorph/
  constants.py        fixed constants and the two profiles (v1, legacy)
  canon/              the data contract: ingest adapters, validation
  mine/               entity streams, lagged contexts, gap handling, discovery, nulls, compositions
  score/              logistic model over contexts; baselines; triviality library
  transfer/           alignment of two vocabularies from structure; zero-shot and learning-curve transfer
  collect/            calibration gates, the transfer matrix, the lineage
  pipeline.py         one deterministic pass over one dataset -> benchmark card
  cli.py              isomorph run / calibrate / transfer / lineage / bundle
datasets/<name>/      raw/ (generator or source), events.csv, observation.csv, gaps.csv, sidecar.json, answer_key.json, out/
collection/           calibration_reference.json, matrix.json, lineage.json, transfer_*.md
docs/                 METHOD.md, session results
scripts/              ingest_buildings.py
```

## Quickstart

```
pip install -e .
python scripts/ingest_buildings.py            # builds datasets/building_a and datasets/building_b
isomorph run datasets/building_a              # one pass, v1 profile -> datasets/building_a/out/card_v1.md
isomorph run datasets/building_a --profile legacy
isomorph calibrate                            # both datasets, both profiles, A->B transfer, compared to the reference
```

## Adding a dataset

1. Write an adapter that produces the contract: `events.csv` (event_id, t, entity, type, value, tie_rank),
   `observation.csv`, `gaps.csv`, `sidecar.json`, and `answer_key.json` if ground truth exists. See
   `isomorph/canon/ingest.py` and `scripts/ingest_buildings.py`.
2. `isomorph run datasets/<name>` — the card is written by the pipeline; prose about the dataset goes
   after the card and may interpret but not restate it.
3. Admission rules and the running order of the first collection are in METHOD.md section 6. Negative
   controls are not optional.

## Research programme

Once the collection has several members, the questions are:

- **Transfer.** Which systems can teach which, and how much (the matrix, in bit-days)? Does transfer
  follow domain boundaries, or cut across them?
- **Superfamilies.** Does clustering the matrix recover families of systems that share a grammar — and
  are they the families an engineer would have named?
- **Lineage.** When a motif validated in one system is inherited by another, what does the shared
  structure say about the processes that produced it? This is the phylogenetic question, and the
  inheritance graph is the only object the word phylogeny is used for.
- **Function.** Is there a type-free shape (pattern plus lag classes) that is inherited across more than
  one family and beats the triviality baseline in each? That would be the strongest claim the framework
  can make, and the only route to anything resembling a universal.

Every one of these is answered by a number with a control, or not at all.
