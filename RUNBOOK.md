# Running isomorph locally

Everything below runs from the repository root. Python 3.11+; the dependencies are numpy, pandas, scipy,
scikit-learn. A full dataset (choice stage + pipeline) wants ~4 GB of memory; the transfer cells ~4 GB each.

## Setup (once)

    git clone https://github.com/jrmerwin/isomorph.git && cd isomorph
    python3 -m venv .venv && source .venv/bin/activate
    pip install -e .

## Reproduce the collection as it stands

    isomorph calibrate                       # buildings must match collection/calibration_reference.json
    bash scripts/fetch_tep.sh && bash scripts/fetch_hai.sh      # raw data (not committed): ~72 MB + ~190 MB
    isomorph run datasets/tennessee_eastman  # cards reproduce; writes the state cache the transfer step reuses
    isomorph run datasets/hai
    isomorph transfer datasets/tennessee_eastman datasets/hai    # both directions; ~1 h here, much less on a Mac

The choice stage (entity + symbolization) is already made for all four datasets and is never revisited
(METHOD 3.1–3.2); `scripts/ingest_tep.py` and `scripts/ingest_hai.py` load the recorded choices and only
rewrite the canonical files. To re-run a choice from scratch, delete `datasets/<name>/out/choices_*.json`
and `choice_checkpoint.json` first — expect 3–4 hours for TEP; the stage checkpoints after every role and
resumes if interrupted.

## Adding a dataset (the running order is in METHOD.md section 6)

1. `scripts/<name>_layout.py`: columns → entities and roles, kinds, the dimension table (v5 suffix), the
   answer key if one exists, regime annotations if labels exist. Look at `hai_layout.py` for a real one.
2. `scripts/ingest_<name>.py`: load, declare resolution/span, run `choose_symbolization` (checkpointed) and
   `choose_entity`, write the canonical dataset. Copy `ingest_hai.py`.
3. `isomorph run datasets/<name>`; then `python3 scripts/tag_datasets.py` (add the dataset there) for the
   parts of speech, place tags and dimension suffix; then `isomorph transfer` against each dataset already in
   the collection (one direction per invocation if memory is tight: `--direction ab` / `ba`).
4. Write `docs/CARD_<name>_v<version>.md` from `datasets/<name>/out/card_v1.md` and the library, and add a row
   to the README table and `docs/MATRIX.md`.

## Returning results

Everything worth returning is tracked by git (cards, libraries, sidecars, choices, matrix, cell cards,
calibration, choice logs). Raw data and `out/state_*.pkl` caches are ignored on purpose.

    git add -A && git commit -m "<dataset>: card and cells" && git push

If you would rather hand over a file: `isomorph bundle` writes `results_<date>.zip` with the same set.

## What takes time

| step | TEP (120 d, 3 min) | HAI (15 d, 1 min) |
| --- | --- | --- |
| choice stage (once per dataset) | 3–4 h | 2–3 h |
| pipeline (`isomorph run`) | ~40 min | ~5 min |
| one transfer direction | ~35 min | ~30 min |

The choice stage runs the two or three scheme trials of a role in forked workers (`n_jobs`, default
min(3, cores)); expect roughly a 2–3× speed-up over the figures above. Pipeline and transfer steps are
single-process apart from numpy's own threading.

## The next round (October 2026)

1. **Robustness of the cross-kind cells — done 2026-10-20.** Seeds 0–4 of TEP ↔ HAI under v5 are in the matrix:
   TEP → HAI 0.83 ± 0.00, HAI → TEP 14.55 ± 0.87 (docs/MATRIX.md, seeds table). Each seed is ~25 min on a 24-core Mac Pro:
   both pipelines (~11 min), TEP → HAI (~11 min), HAI → TEP (~3 min). Two things to know before committing after a sweep:
   a seeded transfer rewrites `out/benchmark_v1.json` and `out/library_v1.json` for that seed, and every `run`
   writes the library *without* the tagged shapes — so either re-run `scripts/tag_datasets.py` or restore the
   seed-0 files with `git checkout -- datasets/*/out collection/transfer_*.md` before `git add -A`.
2. **A Rosetta set** — the NASA battery cells (6) are Rosetta member one (admitted, 47.5 days; recovery 3/3
   under v6). TCLab (5) is withdrawn from the running order: no public recording is long enough (7.6 h, no
   period); it re-enters with a 24–48 h recording of both heaters under a setpoint schedule, made on a kit.
   Of the three repairs the pair asked for, two are in v6 (gap clipping 3.6, cross-scheme spelling 3.12); the
   recording is the third. Next members: a tank rig, a DC motor, a PhysioNet regulator — each a `*_layout.py`
   and an `ingest_*.py` (copy `battery_layout.py` for a cycled protocol). The negative controls move down the
   running order, not off it.
3. **Syntax motifs — v6, implemented 2026-10-20** (3.15: `isomorph/mine/syntax.py`). Chains of two validated
   fragments and returns are admitted on every card; TEP 525 chains / 106 returns, HAI 1,437 / 118, battery
   13 / 1, building A 15 / 1. On the Mac a chain search costs about as much as the pair nulls (TEP ~3 min).
   Open: the place prefix tags both ends of a closed loop RELAY (an actuator in a loop is context and target),
   so a loop closing reads RELAY → FOLLOW → RELAY or RELAY → RELAY → RELAY, never LEAD → FOLLOW → LEAD; whether
   3.14 should carry a loop-aware tag is the next method question.

## The round after v6 (October 2026)

1. **The collection step, 3.13.** Build `isomorph/collect/lineage.py`: for every admitted dataset the tagged shape
   inventory (fragments, chains, returns) with counts and lifts; a shape × dataset character matrix; the similarity
   tree (hierarchical clustering of a shared-shape distance, with the transfer matrix's net cells as a second
   distance for comparison); and the inheritance graph — a shape first validated in one dataset and later validated
   in another is `inherited`, and the lineage records where each shape first appeared, where it recurred, where it
   was tested and failed (its alignment counterpart's absence under a role match). `isomorph lineage` writes
   `collection/lineage.json` and `docs/LINEAGE.md`. Returns are the characters that matter most; report them first.
2. **One more Rosetta member — done 2026-10-21, with a caveat.** PhysioNet slpdb (dataset 7: 18 nights, beat-to-beat
   HR, invasive pressure, respiration, SO2; `scripts/fetch_physionet_slp.sh` from the S3 mirror, `ingest_physionet_slp.py`,
   needs `pip install wfdb`). 37 fragments, recovery 2/5 (the slow-wave HR → DBP → SBP coupling), 0 returns, no
   gain; **not admitted as the rule stands** (3.6 days; the period rule's 0.1%-of-span bins cannot see a 4-s
   breathing cycle) and carried as a provisional leaf, flagged, so the four-leaf tree can be seen. The card lists
   three instrument limits with numbers: the period rule's resolution floor, the noise floor erasing a 4-s
   oscillation at 1-s sampling, and a reflex that closes below the first lag class. A beat-indexed declaration
   (time in beats) is the per-dataset route; the other two are method items. Keeping or withdrawing the leaf is a
   human call.
3. **The loop-aware place tag** (METHOD open items, v7 candidate) — specified after the return inventories of
   all datasets are in view; the timing asymmetry inside returns (REACTS / RESPONDS) is the candidate rule.
