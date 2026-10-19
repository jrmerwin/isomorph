# isomorph

*Validated motif libraries from event streams, and how much they transfer between systems.*

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

Version 1.0.0 — reorganised and calibrated. Both calibration datasets (two simulated buildings with
answer keys) run end to end under the v1 profile and a legacy profile that reproduces the recorded
session results; reference cards are in `collection/calibration_reference.json`.

Not yet implemented from METHOD.md (each reported as `not measured` on cards until it is): the
compression-driven choice of entity (3.1) and symbolization (3.2); the signal floor (3.5); period
estimation (3.4) and the cycle null; the rewire null; the Hawkes and Markov-3 baselines; per-fragment
transfer weights; the collection matrix and lineage files. See `CHANGELOG.md`.

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
