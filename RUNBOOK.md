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


## The v9 round (October 2026) — the brief for the Mac

Collection-only: METHOD.md 3.12 (v9 paragraph) and section 6 rows 9–10. No card changes, no bump of
CARD_RULES_VERSION; METHOD_VERSION to 9 and the matrix regenerated. The question the round answers is whether
the cells into TEP (PhysioNet → TEP 61.9, Building 59 → TEP 71.1, HAI → TEP 48.6 bit-H) are motif structure.

1. **Marginal control (3.12).** In `transfer/apply.py`, beside the derangements: the source model reduced to its
   type marginals through the learned mapping — per mapped receiver type, the translated source frequency and
   nothing lagged — mixed with the receiver's own model by the same per-fragment procedure (one feature per mapped
   type). `cell_marginal_bit_horizons`; the **structure** cell = learned − max(derangement, marginal); MATRIX.md
   gains the two columns. Prediction, declared: PhysioNet → TEP's structure cell falls below 10 bit-H; TEP ↔ HAI
   and TEP ↔ Building 59 keep most of theirs.
2. **The diagonal (3.12).** `isomorph transfer --self datasets/<name> --source-stretch <spec>`: fit the source
   pipeline on the disjoint stretch (TEP: days 120–240 of the 1-year file — days 240–365 remain untouched and the
   card says so; Building 59: 2018; Fingrid: the adjacent year; buildings: generator seed 1; battery: the other
   FY08Q4-era cells, B0029–B0032 or whichever the archive holds) and apply it to the receiver through the identity
   mapping, controls as for any cell. `collection/matrix.json` gets the diagonal entries; every off-diagonal cell
   also reports `share_of_ceiling = structure / diagonal_structure`. HAI and PhysioNet `not measured`.
3. **Dataset 10, negative control one.** Alibaba cluster-trace-v2018 `machine_usage.csv` (public on GitHub /
   Aliyun OSS; ~2 GB): 1-minute means over a subsample of ~200 machines as units, roles cpu_util, mem_util,
   net_in, net_out, disk_io — all dimensionless, so every role is unsuffixed and the dimension constraint maps
   nothing hard. Fallback: Google clusterdata-2011-2 machine-level usage at 5 min (`gsutil`, large). Admission by
   horizons. Run it as a source into every receiver and as a receiver from every source. **Declared:** structure
   into TEP ≈ 0 (below 5 bit-H). If it is not, stop and report; nothing else gets added until the cell is
   understood.
4. **`isomorph brief datasets/<name>`** — a view, not a rule: the system's structural map for a machine reader.
   One JSON and one markdown per dataset: identity (entity, H, periods, admission, claim with its numbers);
   vocabulary (every role with `full_tag`); couplings (validated fragments as prior → target with lag class,
   lift, confirmation n, binding evidence, used/unused); loops (returns with both loop-rule verdicts, unpromoted);
   absences (silent roles, roles never a target, keyed pairs not found, all above the signal floor); regimes;
   and the matrix row (cells in, cells out, share of ceiling where measured, nearest taxa by shape). A short
   epistemics header once: lifts are odds, absence is informative only above the floor, `no gain` means found but
   already carried by the trivial model. No prose beyond that header.
5. CHANGELOG `## v9 implemented`; MATRIX.md v9 table with structure and share-of-ceiling columns; LINEAGE.md
   regenerated with the seventh taxon and the negative control marked as such in every view.
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


## The v8 round — status (Mac, 2026-10-21)

1. **Derangement controls** — built; every type moved at width 0 in all but three cells (B′ → 59 0.91 → 1.00 at
   full width; TEP → 59 and HAI → 59 0.99 → 1.00; Building 59 → HAI 0.97: three HAI types share one source
   counterpart through nearest-quantile crossing and cannot be deranged among themselves — *dev.* at full width
   each leftover is swapped with a moved type, and that cell was re-run). No cell is uncontrolled in the final matrix.
   The cells that moved most are the receiver-TEP ones, as expected, but not to zero: PhysioNet → TEP stays large
   with every type moved (61.9 bit-H), so the v7 reading "its own control" was not the whole story.
2. **Curve in receiver horizons** — built on observed time (per entity, windows and gaps); `obs` added to the
   state cache. HAI (126 H), the battery (161 H) and PhysioNet (10 H) are `short` as receivers; Building 59's
   first-week gap no longer makes empty curve points. TEP's 200 H = 20.0 days as the brief said.
3. **Loop rules recorded** — timing withdrawn from the prefix and alignment, determinism added; predictions and
   outcomes on each card and in CHANGELOG. Neither rule reaches 0.75 anywhere; the determinism rule gets HAI's
   level loop right (LCV01D REACTS 12:2) and TEP's valve and Building 59's valves wrong. Promotion: none.
4. **Bump to 8** — buildings reproduce v7's headline exactly (only control zero-shots moved); cards, matrix (14
   pairs both ways), lineage, tags regenerated.
5. **Dataset 9, Fingrid** — fetched with the user's key through the environment (never stored; rotate it, it was
   pasted in chat), one year at 3 min with 15-min reserves held; 71 fragments, recovery 6/7, 3 returns on the
   reserve side; admitted. *dev.* the imbalance series (1 min) begins 2025-06-25 and is left out; the API caps
   queries at 40,000 rows, so the fetch runs month by month. Open: the 15-min hold fixes the timing rule's verdict
   (f REACTS by construction); the honest loop declaration is the reserves' own 15 min.

## The v8 round (October 2026) — the brief for the Mac

Three repairs, each from a number v7 produced. METHOD.md 3.12 (v8 paragraph) and 3.16 (v8 paragraph) are the spec.
No new dataset until these are in: every `X → TEP` cell of v7 is suspect for the first reason below.

1. **Controls as derangements (3.12).** `transfer/apply.permuted_mappings`: each control mapping must give every
   mapped type a counterpart other than its learned one. Widen the group only as far as needed — within
   (clock class, dimension) first, then within the clock class across dimensions, then across all mapped types —
   and record the share of types moved at each width in the transfer json and in `cell_markdown`. A cell with a
   single mapped type is `uncontrolled`: raw area reported as an upper bound, net `None`, excluded from the transfer
   tree. Expect the receiver-TEP cells (PhysioNet → TEP 18.08, Building 59 → TEP 19.26, battery → TEP 1.65,
   HAI → TEP) to move most; TEP → HAI (142 types through 37 roles) least.
2. **The curve on observed time, to 200 receiver horizons, in bit-horizons (3.12).** `transfer/apply.transfer`:
   training time measured with gaps excluded (the battery's compressed axis already does this; Building 59 does not);
   curve points at 1, 2, 3, 5, 10, 20, 50, 100, 200 H of the receiver (`H` from the receiver's state, 3.3); last point
   min(200 H, training end); drop `all`; areas in bits × H. Rename the fields (`cell_bit_horizons`, etc.) and keep the
   v7 bit-day cells in MATRIX.md's v7 table for the record. TEP's 200 H is 20.0 days, so HAI → TEP under v8 should
   read ≈ 10 × its truncated bit-day value before the control change moves it; a receiver below 200 H of training
   (HAI 11 d ≈ 126 H; PhysioNet) is flagged `short`.
3. **Loop roles withdrawn from the prefix; the determinism candidate recorded (3.16).** `pos._part` / `full_tag`
   spell the degree tag again (RELAY); `align.py` drops the loop +1; the sidecar keeps `loop_tags` per rule. In
   `mine/syntax.py` add the determinism verdict beside the timing one: precision of the leg into Y on the
   confirmation split, P(Y | X within l₁), against P(X′ | Y within l₂), ratio 1.5, else unresolved; role tags by
   majority as before. The card's Loop roles block becomes a table with one row per rule: resolved, roles by tag,
   dimension check, flowsheet check. The declared predictions are in 3.16; write down what came out next to them,
   whatever it is. Promotion is by the criterion in 3.16 (flowsheet ≥ 0.75 on every keyed dataset with ≥ 10
   resolved actuator–measurement returns); if the determinism rule meets it, it enters the prefix and alignment in
   the *next* version, not this one.
4. **Bump** to 8 (CARD_RULES_VERSION too: the Loop roles block changes). Buildings first; regenerate cards, the whole
   matrix (both directions for every pair that has one), lineage, `tag_datasets.py`. CHANGELOG `## v8 implemented`.
5. **Then dataset 9: grid frequency** (Fingrid open data — frequency at 1-min or 10-Hz, activated FCR / aFRR
   reserve; check what is downloadable without a key). Roles: frequency ⟨T⁻¹⟩, activated reserve ⟨M L² T⁻³⟩,
   net transfer / imbalance ⟨M L² T⁻³⟩; the whole synchronous area is one entity, so 3.1 has one candidate and the
   card says so. The loop to look for: frequency drops → reserve activates → frequency recovers, a return whose
   REACTS side is the only actuator in the system.
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
3. **The loop-aware place tag — specified 2026-10-21 as METHOD 3.16 (v7).** See the round below.

## The v7 round — status (Mac, 2026-10-21)

Done in work order; deviations from the brief are marked *dev.*

1. **Loop roles (3.16)** — built in `mine/syntax.py` (`leg_gaps`, `loop_verdict`, `loop_tags`), the tag replaces
   `RELAY` in `pos.place_of` / `full_tag` / chain shapes, +1 graded in `align_roles`, cards carry a **Loop roles**
   block with both checks. Expected vs found: TEP's `underflow_valve` lands on REACTS (9 votes to 7) but `cw_flow` on
   RESPONDS (25 to 16); HAI's `LCV01D` on RESPONDS and `LIT01` on REACTS — both expectations inverted at the role
   level. The flowsheet check is at chance on TEP (24/44) and inverted on HAI (7/21); the dimension check is below
   chance on both (REACTS dimensionless 0.25 / 0.27). On TEP the gaps are multiples of the 3-min sample, so medians
   tie and 19 returns are unresolved. **The checks pass on Building 59** (flowsheet 35/56 = 0.63; RESPONDS
   dimensioned 4/5), where the economizer loop reads `REACTS → RESPONDS → REACTS`. Nothing fixed by hand.
2. **Fine-grid period (3.4)** — `nulls.period_estimate_fine` (FFT acf at δ out to 1,000 δ), `period_fast` /
   `period_slow` on cards and sidecars, the cycle null at each. Buildings, TEP, HAI, battery, Building 59: `none`
   on the fine grid, as expected. *dev.* PhysioNet also `none`: the pooled rate of 18 subjects breathing at 18
   rates has acf peaks of 0.13–0.15 at 1.5–4.5 s against the 0.2 threshold; a per-entity period is the open item.
3. **Admission in horizons (section 6)** — `pipeline.run` computes days / slow periods / H / test H and the card
   states the clause. PhysioNet admitted (19,419 H at 0.25 s); HAI **not admitted under the rule** (178 H, 15.3 d),
   kept as the standing provisional member and so flagged; TCLab out (22 H); Building 59 admitted (365 d, 641 H).
4. **PhysioNet at 0.25 s** — `CARD_physionet_slp_v2.md`: 22 fragments, **beats baselines** (+0.19 over triviality),
   respiration spelled breath by breath, RESP → SBP/DBP and HR → SBP found, RSA spelled HR → RESP by lead; **no
   baroreflex return** (SBP → HR absent as a pair, not hidden by the clock any more).
5. **Bump to 7** — buildings reproduce the v6 reference exactly (calibration passed, then re-recorded); every card
   regenerated, `tag_datasets.py` with loop tags, matrix v7 seed 0 (docs/MATRIX.md), `isomorph lineage`.
6. **Lineage checks** — (a) the two PhysioNet rows were two mappings (HR ↔ purge_valve vs HR ↔ SIT02) whose confirmed
   sets differ by one fragment each way: equal counts by coincidence. (b) LINEAGE.md now states the running-order
   direction and counts same-role and cross-role shapes apart; of the shapes present in every taxon under v6 all
   three were same-role, and under v7 (five taxa) none is present in every taxon.
7. **Dataset 8, Building 59** — fetched from the Zenodo mirror (Dryad's file streams refuse unauthenticated
   downloads; CC0), year 2019 at 5-min means, entity `unit` by 3.1 (55 units) over `zone`; *dev.* no `sys` candidate
   (299 roles → ~1,800 types, the Markov-only comparison segfaults on the vocabulary-squared feature map: open item).
   1,285 fragments, 1,044 chains, 299 returns, recovery 9/11, no gain over triviality (50 thermostatic zones are 50
   alternations). Shares 104 cross-role shapes with TEP and 128 with HAI; the shape tree pairs it with TEP.
   Cells A → 59, B′ → 59, 59 ↔ TEP, 59 ↔ HAI in docs/MATRIX.md. Next: Fingrid grid frequency (⟨T⁻¹⟩).

## The v7 round (October 2026) — the brief for the Mac

Read METHOD.md 3.16, the v7 note in 3.4, and section 6 before touching code; they are the spec, this is the order of work.

1. **Loop roles (3.16).** In `mine/syntax.py` (or beside it) record, for every admitted return, the median realised
   gap of each leg over its confirmed triples (`g1`, `g2`), the verdict (`Y reacts` / `X reacts` / `unresolved`,
   ratio 1.5), and per role the majority loop tag over resolved returns, as end or middle. The loop tag replaces
   `RELAY` in the place prefix only (`pos.full_tag`, `_part` for chain shapes); LEAD / FOLLOW / ISOLATED stay.
   Alignment (`transfer/align.py`): graded +1 when the loop tags differ, like clock and place; nothing hard.
   Cards get a **Loop roles** block: resolved / unresolved returns, roles by tag, the dimension check (share of
   REACTS roles dimensionless, of RESPONDS roles dimensioned, against 0.5) and, where the answer key names
   actuators (TEP flowsheet, HAI point descriptions, battery protocol), the flowsheet check (share of
   actuator–measurement returns with the actuator on the REACTS side). Expected if the reading holds: TEP's
   `underflow_valve → P → underflow_valve` and `cw_flow → P → cw_flow` put the valve and the flow on REACTS;
   HAI's `LIT01 → LCV01D → LIT01` puts LCV01D on REACTS. If it comes out inverted, the card says so and nobody
   fixes it by hand.
2. **Fine-grid period (3.4).** `mine/nulls.period_estimate` runs twice: the coarse grid as now and a fine grid at
   δ out to 1,000 δ; `period_fast`, `period_slow` in the card and sidecar; the cycle null gate at each period
   found. Buildings and TEP should report `period_fast: none`; PhysioNet should find ~4 s (and perhaps ~10 s).
3. **Admission in horizons (section 6).** `pipeline.py` computes span / H and the card's admission line reads it;
   nothing else changes. Statuses expected: PhysioNet admitted (12,300 H), HAI still provisional (175 H),
   TCLab still out (22 H).
4. **PhysioNet at 0.25 s (per-dataset, no rule change).** The noise floor reads a 4-s wave at 1-s sampling as white
   noise (acf(1) ≈ 0), and the baroreflex (1–2 beats) closes below the first lag class (3 s). Re-ingest at
   δ = 0.25 s (beat-interpolated HR and pressures are smooth at that step; respiration keeps acf(1) ≈ 0.7),
   re-run, and write CARD_physionet_slp_v2.md. The recovery line to watch: does SBP ↔ HR close as a return.
5. **Bump** METHOD_VERSION and CARD_RULES_VERSION to 7; buildings first (within 0.02 bits); regenerate every card,
   the matrix (seed 0 both directions for TEP ↔ HAI, TEP ↔ battery, HAI ↔ battery, and PhysioNet against each),
   `isomorph lineage`; `scripts/tag_datasets.py` so the shapes carry the loop tag. Record in CHANGELOG under
   `## v7 implemented`. Deviations from the spec go in the commit message and here, as before.
6. **Two checks on the v6 lineage while you are there.** (a) `PhysioNet → TEP` and `PhysioNet → HAI` report the
   same row (37 tested, 15 confirmed, 22 failed) — confirm this is two mappings giving the same count and not one
   result written twice. (b) LINEAGE.md should say in one line that inheritance direction is running order, and the
   character matrix should separate same-role shapes (function words) from cross-role shapes before counting what
   is shared; the three shapes present in every taxon are all same-role.
7. **Dataset 8, the real building** (running order 8; `building_59_layout.py`, `ingest_building_59.py`). Candidate:
   LBNL Building 59, Berkeley — Luo et al. 2022, *Scientific Data*, "A three-year dataset supporting research on
   building energy management and occupancy analytics" (2018–2020, HVAC and zone data at 1-min and 15-min; check
   the host — Dryad or LBNL — and the licence before fetching). Entity by 3.1 between zone and AHU; roles zone
   temperature ⟨Θ⟩, supply air temperature ⟨Θ⟩, damper / valve position (dimensionless), airflow ⟨L³ T⁻¹⟩, outdoor
   temperature system-wide; schedules and setpoints as SET. The point: the calibration buildings are synthetic;
   this is the same kind of system in the real world, so the A/B′ → 59 cells say whether the synthetic generator
   taught anything, and 59 ↔ TEP / HAI is the third regulator in the matrix. If Building 59 is unreachable, the
   fallback with the same role is the ASHRAE Great Energy Predictor III meter data (hourly only — coarser than
   anything admitted so far; say so on the card). After 8: grid frequency regulation (Fingrid open data, 10-Hz or
   1-min frequency with activated reserve) as a Rosetta member whose dimension is ⟨T⁻¹⟩ and whose loop is the
   whole Nordic grid.

