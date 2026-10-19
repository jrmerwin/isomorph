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
