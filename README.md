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

Method **v5** (integer versions; amendments are logged in `CHANGELOG.md`; cards valid from v2, the last change to per-dataset rules):

| # | dataset | library vs triviality / best baseline (bits per event, test split) | claim |
| --- | --- | --- | --- |
| 1 | building A (synthetic, calibration) | 2.167 vs 2.169 / 2.562 | no gain |
| 2 | building B′ (synthetic, calibration) | 1.365 vs 1.530 / 1.860 | beats baselines |
| 3 | Tennessee Eastman, first 120 days ([card](docs/CARD_tennessee_eastman_v1.md)) | 3.033 vs 3.171 / 3.410 | beats baselines |
| 4 | HAI 21.03, 1-minute means, 15.3 days ([card](docs/CARD_hai_v2.md); provisional: below the 20-day line) | 3.851 vs 3.826 / 3.905 | no gain (recovery 7/15: the physics is found but the alternation baseline already carries it) |

Transfer matrix (net bit-days after the permuted-mapping control; [full table and reading](docs/MATRIX.md)):

| source → receiver | net cell | |
| --- | --- | --- |
| building A → B′ | 0.74 | same kind: alignment real (zero-shot 4.6 vs 7.9 permuted) |
| building B′ → A | 5.53 | the richer system teaches more |
| Tennessee Eastman → HAI | **0.83** (v4: 1.67, v3: 0.37) | cross kind; v5 control is stricter (within dimension) and the dimension constraint maps fewer types |
| HAI → Tennessee Eastman | **13.37** (v4: 10.52, v3: 0.06) | cross kind; mixed curve beats TEP's own model by 0.3–0.6 bits to 20 days |

Implemented: canonical contract; compression-driven entity (3.1) and symbolization (3.2, with noise and
faithfulness floors); lag classes; period estimation and the cycle null; circular null (gate) and rewire
null (attribute); signal floor (descriptive); fixed baselines incl. Markov-3 and Hawkes-like decay features;
name-free triviality library; alignment and transfer with a global mixing weight and a permuted-mapping control; the transfer matrix (`isomorph transfer`); calibration gates.

Not yet: per-fragment transfer weights; the collection matrix and lineage files (`collect/matrix.py`,
`collect/lineage.py`); pooled lag classes for alignment; a horizon tied to system time scales (open item
from dataset 3). Syntax motifs (chains, the feedback-return motif) are the next grammar step (docs/MATRIX.md).

## Layout

```
isomorph/
  constants.py        fixed constants and the two profiles (v1, legacy)
  canon/              the data contract: ingest adapters, validation
  mine/               entity streams, lagged contexts, gap handling, discovery, nulls, compositions
  score/              logistic model over contexts; baselines; triviality library
  transfer/           alignment of two vocabularies from structure; zero-shot and learning-curve transfer
  collect/            calibration gates (matrix and lineage to come)
  pipeline.py         one deterministic pass over one dataset -> benchmark card
  cli.py              isomorph run / calibrate
datasets/<name>/      raw/ (generator or source), events.csv, observation.csv, gaps.csv, sidecar.json, answer_key.json, out/
collection/           calibration_reference.json (matrix and lineage to come)
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
