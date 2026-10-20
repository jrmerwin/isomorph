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

The choice stage is embarrassingly parallel across the two or three scheme trials of a role, which is not yet
exploited; it is the first thing to parallelise on a multi-core machine.
