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
