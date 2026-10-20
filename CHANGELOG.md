# Changelog

Method version is an integer (METHOD.md section 7); every card states the version it was produced under.

## v1 — 2026-10-18

- Method specification v1 adopted (docs/METHOD.md): canonical contract with event ids, tie ranks,
  observation and gap intervals; chronological 50/25/25 splits with distinct roles.
- Contract clarification: `gaps.csv` carries an optional `type` column so a single sensor's dropout is
  recorded against that sensor's event types rather than widened to the whole entity.
- Reorganised the session code into the `isomorph` package. Legacy profile (fixed lag classes, 30/30
  split) reproduces the recorded building-A card within 0.02 bits once the one contract change
  (unobserved zone-C events excluded) is applied on both sides: Markov-2 2.601 vs 2.602; Markov-features
  logistic 2.318 vs 2.318; library 1.818 vs 1.837; unselected contexts 1.800 vs 1.800.
- Transfer A->B' under the legacy profile with rule-chosen anchors: mapping accuracy 0.60 (recorded 0.61
  with hand-chosen anchors); zero-shot through the true mapping 3.097 / 2.631 (recorded 3.126 / 2.661).
- First finding from the triviality baseline: on building A the library's gain over the trivial library
  of symmetric pairs is 0.06 bits (legacy) and -0.005 bits (v1); the claim rule returns "no gain". Most
  of the 0.5-bit advantage over Markov on this building is on/off and up/down alternation.
- v1 profile observations: data-driven lag edges on building A come out at 5 / 21 / 72 minutes (the
  session used 5 / 30 / 90 by hand). Alignment accuracy A->B' under v1 is 0.40 vs 0.60 under legacy;
  per-dataset lag terciles reduce the comparability of lift matrices across systems with different time
  constants. Open item: align on lag-pooled lift with an ordinal lag signature.
- Not yet implemented (cards say `not measured`): entity and symbolization by compression, signal floor,
  period and cycle null, rewire null, Hawkes and Markov-3 baselines, per-fragment transfer weights,
  collection matrix and lineage.

### v1, stage 2 — floor, period, cycle and rewire nulls (2026-10-18)

- Period estimation (3.4) from the autocorrelation of the whole-system event rate; building A: 1440 min.
- Cycle null (3.8): whole-period offsets per type, DISTINCT across types and drawn from both
  directions. The first version drew offsets independently and in some draws gave two types the
  same offset, preserving their alignment; the null maximum then equalled the observed count and
  rejected every core mechanism. Caught by the answer key (recall fell to 0.33); fixed (0.75).
- Rewire null (entity labels permuted within type) is recorded per fragment as `binding_evidence`,
  not used as a gate: it is blind by construction to system-wide causes (setpoint -> heater) and
  uninformative when units run on a synchronized schedule (occupancy -> CO2 in all zones at once).
  Gates are circular + cycle. METHOD.md 3.8 to be amended accordingly.
- Signal floor (3.5) is reported on the card but not applied as a minimum count: as an absolute
  number it is dominated by high-rate pairs (building A: 16) and would discard real low-rate
  mechanisms; admission is per pair through the nulls, with the fixed minimum count 3. METHOD.md
  3.5/3.6 to be amended.
- Known limitation: one period only. Weekly structure survives a daily cycle null (building A:
  "T:up20 (long) -> occ:arrive" remains, a weekday-schedule confound); nested periods need spans
  long enough for distinct whole-week offsets.
- Building A, v1 profile after this stage: 90 validated fragments, recovery 9/12 (misses: the two
  rare window mechanisms and setpoint:down -> T:down20, whose lag exceeds the data-driven horizon of
  72 min). Library 2.214 bits vs triviality 2.210: no gain over trivial structure on this building.

### v1, stage 3 — compression-driven choices, remaining baselines (2026-10-18)

- Entity by compression (3.1) implemented over candidate layouts of the raw frame; building A chooses
  `zone` (1.80 bits vs 8.10 for a single-entity layout).
- Symbolization by compression (3.2) implemented per role (a role is one variable shared across
  entities, so every unit gets the same symbols): schemes q20/50/80, q10/90, smoothed-derivative
  extrema with the smoothing window = the series' own correlation time (first lag at which its
  autocorrelation drops below 0.5). Criterion = TOTAL confirmation bits of the whole event table with
  system-wide events scored as targets, subject to a faithfulness floor: the scheme must reconstruct
  the series to within FAITHFULNESS_MAX_RESIDUAL = 0.5 of its std (band means for quantile schemes,
  linear interpolation between extrema for dsign). Two earlier criteria were rejected: per-event bits
  on other roles ignored chatter in system-wide channels; total bits without the floor drifted to the
  coarsest symbolization (CO2 as daily extrema). PELT change-points are not in v1.0.
  Building A result: T on q20/50/80 at 16.8 / 18.0 / 21.4 C (the control bands); CO2 and RH as smoothed
  extrema (3.6 h and 5.9 h windows); T_out as daily extrema; vibration (pure noise) forced to a fine
  quantile scheme because only fine schemes are faithful to noise — the library then ignores it
  (chatty share 0.07). Open item: a "no events" option for roles whose symbols inform nothing.
  The auto-symbolized building (`datasets/building_a_auto`) scores library 1.897 vs triviality 1.947:
  gain 0.05 bits, still "no gain" under the 0.10 rule.
- Period estimation moved to 0.1% resolution on entity-level events (1% bins could not see a daily
  cycle; system-wide chatter diluted the autocorrelation): building A 1436 min.
- Markov-3 (third-order backoff) and a Hawkes-like baseline (exponentially decaying excitation per
  type, tau = the middle lag edge, same logistic model) are on the card. Building A v1: Markov-3
  3.329 (worse than Markov-2, as in the session), decay features 2.737.
- Calibration reference re-recorded for v1; legacy reproduces its reference exactly.
- METHOD.md amendments pending from stages 2-3: 3.5/3.6 (floor descriptive, admission per pair),
  3.8 (rewire as attribute), 3.2 (criterion and faithfulness floor as implemented), 3.4 (resolution).
- Triviality baseline made name-free (3.11): a trivial pair is two types within an entity whose merged
  subsequence strictly alternates (>= 0.9 over >= 20 transitions). The first version matched on/off and
  up/down by NAME and found nothing on the name-scrambled building B', which then "beat baselines" for free
  (legacy B' triviality 2.220 -> 1.694). Now: building A finds its 8 switch and threshold pairs (v1 gain over
  triviality 0.04, "no gain"); B' finds 10 pairs from opaque names (gain 0.15, "beats baselines" — the
  four-zone building with the dehumidifier loop carries cross-variable structure A does not). Reference
  re-recorded for both profiles; only the triviality rows changed.
- METHOD.md amended to what is implemented (3.2, 3.4, 3.5, 3.6, 3.8, 3.9, 3.11, constants table, open items).
- Noise floor added to symbolization (3.2), found on Tennessee Eastman: measurements carry white noise at the
  3-min sampling scale, so quantile crossings toggled at the debounce limit (812k events a year under the
  all-fine start) and the extrema scheme tracked every wiggle (240k events for one role); the faithfulness
  test, measured against the raw series, demanded that the symbols reconstruct the noise and admitted only
  the extrema scheme. Now each series is denoised by a centred moving average over w = ceil(f/(0.05(1-f)))
  samples, f = 1 - acf(1), leaving <= 5% white noise; a series needing w > 1% of its length has no signal and
  emits no events (the "none" option, from the data); schemes and faithfulness run on the denoised series; a
  role with exactly one faithful scheme takes it without the criterion. Buildings: acf(1) > 0.999 on every
  real signal, w = 1, unchanged; the vibration noise channel (acf(1) = 0.60) is denoised over 14 samples and
  now takes dsign instead of forced q20/50/80; building_a_auto's CO2 flips to q20/50/80 (8.6 vs 8.8 kb).
  Calibration datasets (fixed symbolization) unaffected. New constant NOISE_FRACTION = 0.05.
- Recovery check accepts answer keys that name roles (match = "role_prefix") for datasets whose mechanisms are
  actuator -> measurement in any direction.
- Dataset 3 declared: Tennessee Eastman, first 120 days of the Souza et al. (2023) 1-year continuous run
  (Ricker model), entity candidates vessel / sys, STATUS excluded from events and kept as regimes, answer key =
  flowsheet actuator -> measurement pairs. scripts/fetch_tep.sh, scripts/tep_layout.py, scripts/ingest_tep.py.
- Symbolization search starts from each role's coarsest faithful scheme instead of q20/50/80 everywhere: on
  Tennessee Eastman the all-fine start made every trial table chatter-heavy (4 GB and climbing on the first
  criterion). Building A auto re-run to confirm the same choice is reached.
- dsign scheme re-implemented as persistent turning points (3.2): a peak is the maximum of the denoised series
  within +/- one correlation time (trough likewise), alternation enforced. The v1.0 implementation took sign
  changes of the derivative of a moving average, and the derivative of a moving average is the difference of
  two samples one window apart — as noisy as the raw series — so on Tennessee Eastman it emitted an extremum
  every ~5 samples whatever the window (reactor pressure: 11k per column in 120 days; now 2.9k, and dsign
  is no longer trivially faithful: reactor pressure 0.51, reactor temperature 0.57). Building A auto re-run.
- Faithfulness test made robust (3.2): residual MAD / series MAD with band-median reconstruction, floor unchanged
  at 0.5. On Tennessee Eastman a few 10-sigma fault excursions dominated the std, so every scheme scored 0.9+
  on reactor pressure/temperature and the method would have discarded them; band means were also pulled by
  the excursions. On Gaussian and AR(1) series the MAD and std ratios coincide (0.36 for q20/50/80, 0.65 for
  q10/90), so the buildings' admissibility is unchanged. Under the robust test q20/50/80 is faithful on every
  TEP role (0.34-0.45) and turning points only where the series really swings (0.03-0.4) — elsewhere 0.9-3.
- Symbolization search stops after a pass that changes nothing (converged); identical result, saves a full pass.
- Thresholds and windows per unit (3.2): quantile thresholds were pooled across the units sharing a role. On
  Tennessee Eastman the reactor, separator and stripper pressures run at 2800, 2700 and 3300 kPa, so pooled
  20/50/80 quantiles put each vessel in one band and no scheme was faithful for any vessel role (P, L, T,
  cooling water, underflow all silent). Now each unit's own quantiles and correlation time; types carry the
  quantile label (P:upq80) rather than the threshold value, so they remain shared across units. Building
  zones share a scale, so this never showed; building_a_auto regenerated (type names change).
- Choice stage checkpoints after every role decision and resumes; ingest_tep.py is resumable. The first full
  TEP choice run was lost to a 2-hour job limit mid pass 1 (its log is kept in datasets/tennessee_eastman/out/).
- Period rule (3.4) corrected on Tennessee Eastman, which has no cycle: the estimator returned 9.4 h (a 0.49-vs-0.47
  bump on a slowly decaying acf) and, with a prominence test, a 10.7-day hump of acf 0.22 seen 5.5 times. Now a
  qualifying peak needs prominence >= 0.1 above the preceding acf minimum and at least 8 repetitions in the span
  (was 4), and the period is the fundamental (shortest qualifying peak within 80% of the strongest) rather than
  the first peak — on building A the first peak is a 5-hour component (0.33) and the strongest is the weekly cycle
  (0.48), neither the one the cycle null must respect. Buildings: 1436-1438 min from the data (sidecars declare
  1440, which the pipeline uses); TEP: none. The first TEP pipeline run was restarted under this rule.
- Dataset 3 carded (docs/CARD_tennessee_eastman_v1.md): library 3.387 vs triviality 3.569 vs best baseline
  3.978 -> beats baselines; unselected contexts 3.477 (validation pays here); 606 fragments; cooling-water
  mechanism recovered with the right sign; recall 1/10 against a key half of which is unrecoverable by
  construction (system-wide effects). Open items: horizon follows event density (21 min here), lag class `s`
  empty under 3-min sampling, keys must name target roles only, L never predicted.

## v2 (2026-10-19)
- 3.3 horizon and lag classes: horizon = median over target types of the median recurrence gap (time until
  the same symbol recurs); lag classes = three geometric bands between the data's time resolution and the
  horizon, closed on the right. v1's 95th-percentile-gap horizon was 21 min on Tennessee Eastman (2,300
  events/day) against thermal mechanisms acting over hours, and its first tercile sat at the 3-min sampling
  interval (class s empty). Context-gap terciles were tried first and rejected: under a 5-hour horizon they
  put every gap under 52 min in one class (building B'). New edges: A 5.6/31.6/178, B' 6.9/47/322,
  TEP 10.9/39.5/143 min (v1: 5/21/72, 5/21/65, 3/9/21). Rule change -> version 2; calibration reference
  re-recorded; all cards regenerated. Symbolization and entity choices (upper row) are not revisited.
- Speed: FFT autocorrelation for the correlation time; run-length crossings (identical to the per-sample scan
  except that the scan confirmed a crossing in the last two samples without the full debounce); interned
  context keys; gaps dict built only where the decay baseline needs it. Needed for 1-second HAI data.
- Dataset 4: HAI 21.03 in place of SWaT (SWaT is distributed by iTrust on request only, not reachable here;
  Jason can request it and it joins as 4b). scripts/fetch_hai.sh, hai_layout.py, ingest_hai.py.
- Dataset 3 re-carded under v2: library 3.033 vs triviality 3.171 vs best baseline 3.410 (beats baselines);
  unselected 3.176; 567 fragments; recovery 2/10 (underflow valve -> underflow now visible); classes s/m/l all
  populated. Buildings under v2: A 2.167 vs 2.169 (no gain), B' 1.365 vs 1.530 (beats baselines); A->B'
  mapping accuracy 0.60 (v1 profile), zero-shot through the learned mapping 4.60 — the longer horizon gives the
  source model many more context features and wrong mappings do more damage — cell 0.20 bit-days; B'->A cell
  1.73 bit-days. `isomorph transfer A B` writes collection/matrix.json and a cell card.
- Symbolization search: a tie between schemes keeps the current choice (a tie is not evidence to change, and a
  flip forces another pass). Prompted by HAI B4005, which on inspection was not a tie (31,395 vs 31,438 bits);
  its switch stands and pass 1 ran.
- Tie tolerance made relative (1e-4 of the total bits): HAI HT_PS and ST_PS emit identical events under two schemes
  (all thresholds equal) and differed by 0.003 bits of solver noise, which would have forced a third pass. The
  pass-1 HT_PS entry was set to what the rule yields (unchanged).
- Dataset 4 carded (docs/CARD_hai_v2.md): HAI 21.03 at 1-minute means, entity process (5.033 vs 6.220), 57 roles
  (22 q20/50/80, 5 q10/90, 23 turning points, 7 silent), 2,096 fragments; library 3.851 vs triviality 3.826 vs best
  baseline 3.905 -> no gain; recovery 7/15. The alternation baseline found 188 pairs, 99 cross-role (command ->
  position, co-stepping setpoints): it carries the plant's deterministic couplings, so the library adds nothing
  beyond them. Admitted provisionally (15.3 days, no period). Open item: whether 3.11 should absorb cross-variable
  couplings — to settle before dataset 5.
- Pipeline state cached (out/state_<profile>_<seed>.pkl, not committed, keyed by method version); `isomorph transfer`
  loads it and takes --direction ab|ba|both, so each cell runs as its own job. The first TEP<->HAI transfer job
  re-ran both pipelines and spent over an hour on the TEP->HAI learning curve (168 receiver classes) before the
  2-hour job limit; nothing was recorded.

## v3 (2026-10-19)
- 3.12: transfer cells reported net of a permuted-mapping control (3 permutations, same mixing weights, median).
  Prompted by the first cross-kind cell, TEP -> HAI: zero-shot 8.86 bits (receiver unigram 6.86; the anchors were
  nonsense pairs) yet "help" at 1-2 receiver days (-0.72, -0.10 bits) — regularisation of a data-starved receiver
  by any smooth model, which the raw cell cannot distinguish from shared structure. Collection-step change:
  version incremented, matrix regenerated, cards unchanged (CARD_RULES_VERSION = 2 marks their validity).
- Matrix v3 (docs/MATRIX_v3.md): A->B' 0.74, B'->A 5.53 (same kind; learned mapping 3-5 bits better than permuted
  in zero-shot, permuted model hurts the receiver); TEP->HAI 0.37, HAI->TEP 0.06 (cross kind; mappings at chance;
  HAI->TEP raw 8.22 was entirely regularisation). First negative-control result of the collection.

## v4 (2026-10-19)
- 3.14 grammar: parts of speech per role from the series alone, relative to H (SET, TEX, FAST/MID/SLOW, -S);
  tag-prefixed shapes in every library (TEP 295 distinct shapes over 567 fragments, HAI 1,064 over 2,096,
  134 shared). Jason's framing: the motifs were written in six grunts, so every system's motifs sounded alike;
  a prefix on the identity of the data keeps unlike motifs from aligning.
- 3.12 role-level alignment: roles to roles of the same symbol kind and part of speech, symbols by spelling;
  control permutes within tag class. Collection-step change; cards unchanged.
- scripts/tag_datasets.py writes tags into sidecars and shapes into libraries. Buildings untagged for now
  (B' has scrambled type names and the same-kind pair already aligns).
- Matrix v4: TEP -> HAI net 1.67 bit-days (v3 0.37), HAI -> TEP net 10.52 (v3 0.06); learned mapping 1.0-2.0 bits
  better than the within-class permuted control in zero-shot; mixed curve beats the receiver's own model at every
  point of both curves. The grammar (3.14 + role-level 3.12) moved the cross-kind cells off the floor. Buildings
  unchanged (B' scrambled names -> type-level). docs/MATRIX.md.

## v5 (2026-10-19)
- 3.14 second prefix (place): LOCAL/COMMON from binding evidence, LEAD/FOLLOW/RELAY/ISOLATED from library degrees;
  suffix: SI dimension vector from each dataset's unit table (TEP: Downs & Vogel; HAI: technical details).
  A role reads `P: MID·COMMON·FOLLOW ⟨M L⁻¹ T⁻²⟩`. Jason: not units but the vector behind them, combinations of
  the same fundamental measurements; a strict language also filters the data to what it can describe.
- 3.12 alignment: kind and dimension hard; clock class and place graded; both sides padded; unmatched costs 3.
  Bug found on the way: distances were not normalised, so the 10^6 "forbidden" penalty was smaller than typical
  signature distances once both sides were padded and forbidden pairs (and even anchors) were taken; distances
  are now in units of their median before penalties. Earlier versions' constraints were only partly effective.
- RUNBOOK.md for local runs; `isomorph bundle` packages everything worth returning (58 files, 0.4 MB).
- Matrix v5: TEP -> HAI net 0.83 (v4 1.67), HAI -> TEP net 13.37 (v4 10.52). The within-dimension control is
  stricter and the dimension constraint maps fewer TEP->HAI types; HAI->TEP maps more (34/40 vs 22/40) and gains.
- Choice stage: scheme trials of a role run in forked workers (n_jobs, default min(3, cores)); identical results
  to the sequential run on building A. RUNBOOK: the next round (seeds sweep, Rosetta set, syntax motifs).

### v5, seeds 0–4 (2026-10-20)
- TEP <-> HAI under v5 on seeds 1–4 (one direction per invocation; seed 0 from 2026-10-19). TEP -> HAI net 0.83 on
  every seed, with the same role map, anchors and 120/168 types mapped. HAI -> TEP net 15.24 / 15.16 / 13.87 / 15.12
  (seed 0: 13.37): mean 14.55 ± 0.87. The raw cell is stable (21.60–21.66, zero-shot within 0.02 bits); the spread is
  the permuted-mapping control (6.36–8.29) and follows one pairing: seeds that map E_feed <-> CO_rpm (0, 3) have
  controls 8.29 / 7.79, seeds that leave E_feed unmapped (1, 2, 4) have 6.36–6.49. Other role-map differences are
  rotations among purge/feed <-> VXT/VYT. Found on the way: `_cell` calls `transfer()` without an rng, so the three
  control permutations come from a fixed generator and the seed reaches the control only through the mapping.
  Seeds table and reading in docs/MATRIX.md; README rows carry mean ± sd. Open items: seed the control; more permutations.
- Reproducibility: the seed-0 pipelines re-run under the v5 code reproduce both libraries fragment for fragment
  (TEP 567, HAI 2,096; lifts and counts identical) and the headline bits within 2e-4 (the descriptive signal floor
  moved, 180 -> 151 and 13 -> 12, from a changed rng draw order).
- Operational, found on the way: a seeded `isomorph transfer` re-runs both pipelines (the state cache is keyed by
  seed through the card) and every `run` rewrites `out/benchmark_v1.json` and `out/library_v1.json` — the library
  without the tagged shapes that `scripts/tag_datasets.py` adds. The tracked seed-0 files and the seed-0 cell card
  were restored from git after the sweep; `matrix.json` is keyed by seed and holds all five. RUNBOOK amended.
- After the seeds sweep (Mac, 0ee5cba): control permutations now take the run's seed (they came from a fixed
  generator, so a seed sweep sampled the control only through the mapping); permutations 3 -> 10, since the
  control's spread (sd 0.89 bit-days) had become the matrix's largest uncertainty — the control's definition is
  unchanged, only its sample; cells shift slightly and are regenerated at the next sweep. `isomorph run` now
  writes tag-prefixed shapes into the library when the sidecar has tags, so a re-run no longer strips them.

### v5, seed 0 re-run and the Rosetta set's first two members (2026-10-20, Mac)
- TEP <-> HAI seed 0 re-run under the seeded ten-permutation control: TEP -> HAI net 0.98 (control -0.12; was 0.83
  with control 0.03), HAI -> TEP net 14.45 (control 7.11; was 13.37 with 8.29). Learned side unchanged to 1e-3; the
  headline rows in docs/MATRIX.md and the README are under the new control, seeds 1-4 remain under the old one.
- Dataset 5, TCLab: nine public recordings of the two-heater kit (APMonitor course uploads, BYU-PRISM, Kantor),
  5-second means, concatenated longest first with boundaries as gaps; 7.6 h, no period -> NOT admitted; card
  recorded (docs/CARD_tclab_v1.md): 469 events, 12 types, 2 fragments (a step-test staircase), recovery 0/3, 45%
  of events dropped at recording boundaries. One candidate file (BYU MIMO_240min) was an emulator record and is not
  used. scripts/tclab_layout.py, ingest_tclab.py, fetch_tclab.sh.
- Dataset 6, NASA PCoE battery set FY08Q4 (B0005-7, B0018): charge/discharge cycles at 1-minute means on a compressed
  axis, 469 unobserved stretches as gaps; 47.5 observed days, admitted; period 239.5 min (the cycle), cycle null
  active; entity = cell by 13.7 bits over one system; 12,274 events, 12 types, 12 fragments, recovery 2/3 (current
  -> temperature, voltage -> current), no gain over triviality (-0.07: a cycling protocol is an alternation).
  93% of events dropped at cycle boundaries: the horizon (recurrence, 196 min) is one cycle and the gap rule drops
  any target whose window spans a boundary. Open item (v6): a gap rule for observation fragmented at the horizon.
  docs/CARD_nasa_battery_v1.md; scripts/battery_layout.py, ingest_battery.py, fetch_battery.sh.
- Matrix: ten cells among {TCLab, battery} x {each other, TEP, HAI}, all net 0.00 where measurable; TCLab has
  under one training day and cannot carry a curve as a receiver ("not measurable", zero-shot only). Role pairings
  cross the way physics says (battery -> TCLab: Q <-> I, T <-> T, Tsp <-> V) but the two actuators are spelled by
  different quantile schemes (q20/50/80 vs q10/90) so the role match carries no types; battery -> TEP raw 25.97 =
  control 25.97. docs/MATRIX.md, Rosetta section. METHOD running order: 5 TCLab, 6 battery, negative controls moved down.
- Code, found on the way: `contexts_for_stream` returns no rows for an entity with no events in a split (it
  crashed the circular null on TCLab's h2); `transfer()` returns zero-shot only, cells None, when the receiver has
  under one training day; the cell log line and cell card tolerate that; `DIMENSIONS` gains `current` <I>;
  `tag_datasets.py` tags the two new datasets. No rule changed; cards and cached state of datasets 1-4 unchanged.
- Reproducibility note kept: the tagging re-run on TEP and HAI left their sidecars and libraries byte-identical.

## v6 (2026-10-20) — specified here, implemented on the Mac
- 3.6 gap clipping: a gap clips the look-back window instead of dropping the target (NASA battery: 93% of
  events dropped under v5). Per-dataset rule -> cards regenerated (CARD_RULES_VERSION = 6).
- 3.12 symbols cross between quantile schemes by direction and nearest quantile; never across kinds.
- 3.15 chains (compositions of two validated fragments with conditional lift >= 1.5, circular null, confirmation
  count >= 3; admitted as features by confirmation bits) and returns (same role at both ends, opposite
  direction, a different role in the middle; [return] in the shape); three nodes.
- Decisions behind 3.15: a chain is admitted as a composition of two admitted fragments (library-driven search,
  provenance of links) and must beat its last link by conditional lift; a return requires the same role at both
  ends — a path ending elsewhere is a chain.

### v6 implemented (2026-10-20, Mac)
- 3.6 gap clipping: `contexts_for_stream` gap mode "clip" (profile v1; legacy ignores gaps as before): the window is
  [max(t − H, end of the last gap before t), t), Markov history on the far side of a gap is dropped with the
  contexts, a target is dropped only when a gap covers it. Battery: events dropped 11,436 → 1,120, fragments 12 →
  47, recovery 2/3 → 3/3, every model about two bits lower (Markov contexts now exist on every row). HAI: 1,234 →
  133 dropped, fragments 2,096 → 2,165, library 3.844 / triviality 3.805 (non-det.), still no gain. TEP (no gaps)
  unchanged. Calibration reference re-recorded (buildings: library A 2.164, B′ 1.341); both tests pass.
- 3.12 cross-scheme spelling: `align.cross_scheme` — same direction, nearest quantile, a tie crosses to nothing
  (q50 against q10/q90). TEP → HAI maps 142/168 types (was 120); every battery cell carries types (12/12 as receiver).
- 3.15 chains and returns: `isomorph/mine/syntax.py`. Candidates are pairs of validated fragments sharing the middle
  type; an instance is B as the target's most recent context at l2 and A's most recent occurrence within l1 of that
  B with no entity gap between; conditional lift ≥ LIFT_MIN on proposal, triple count above the circular null over
  N_NULL_DRAWS, confirmation count ≥ CONFIRM_MIN_COUNT at the same lift; indicator features kept only if they reduce
  confirmation bits. Returns: same role at both ends, opposite direction, different middle role; `[return]` in the
  shape. Shapes of chains carry the place prefix (`SLOW·RELAY.down.q20 -s-> MID·FOLLOW.down.q20 -m-> SLOW·RELAY.up.q20
  [return]`); `library_v1.json` gains `chains`; cards gain `library.chains / chains_used / returns / chain_search`.
  Results: TEP 5,733 candidates → 525 admitted, 106 returns, none used; HAI 38,955 → 1,437, 118 returns, none used;
  battery 155 → 13, 1 return, all 13 used; building A 15 / 1 return (used), B′ 32 / 0 (used).
- The returns: TEP's cooling-water loop (`cw_flow:downq20 -s-> P:downq20 -m-> cw_flow:upq20`, n 46, cond. lift 3.52;
  cw_flow ↔ cw_out and → P → 31 returns) and HAI's level loop (`LIT01:upq80 -s-> LCV01D:upq20 -s-> LIT01:downq80`,
  n 15, cond. lift 9.01, the strongest of 118) both appear. Neither is LEAD → FOLLOW → LEAD, and no return is: an
  actuator in a closed loop is context and target, so 3.14's degree rule tags it RELAY; loops read RELAY → FOLLOW →
  RELAY (TEP) or RELAY → RELAY → RELAY (HAI, battery). LEAD opens chains (LEAD → RELAY → RELAY: TEP 76, HAI 206).
  Open: a loop-aware place tag (3.14) — a method question.
- Matrix v6, seed 0, ten seeded permutations: TEP → HAI 0.90, HAI → TEP 13.53 (v5: 0.98, 14.45); TEP → battery 0.25
  with learned zero-shot 3.68 against permuted 6.35 (the first cross-kind alignment to beat its control by > 2
  bits), battery → TEP 1.65 through three roles (I ↔ cw_flow, V ↔ AC_valve, T ↔ underflow); HAI ↔ battery 0.05 /
  0.09. docs/MATRIX.md v6 section and returns table.
- TCLab withdrawn from the running order (no public recording long enough; re-enters with a 24–48 h recording);
  the battery set is Rosetta member one. README, METHOD running order, RUNBOOK, cards (v6 sections) updated.
- After v6 (Mac, b1a888f): returns found in every admitted dataset — TEP cooling water (31) and HAI level (20) the
  strongest families; no LEAD->FOLLOW->LEAD exists because loop members are RELAY by the degree rule. Loop-aware
  place tag logged as the v7 candidate (timing asymmetry inside returns). Collection step 3.13 scheduled next;
  138 tagged shapes shared TEP/HAI, 7-9 with the battery.
