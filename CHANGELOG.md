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
