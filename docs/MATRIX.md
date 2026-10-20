# Transfer matrix — methods v3 to v6, profile v1 (2026-10-19; v5 seeds 0–4, the Rosetta pair and v6 added 2026-10-20)

Cells are **net bit-days**: the area between the receiver's own learning curve and the curve of its model
mixed with the translated source model, minus the same area for the source model sent through a permuted
mapping (3.12, v3). The control removes what any smooth foreign model gives a data-starved receiver —
regularisation — and leaves what the correspondence gives.

## v6 (2026-10-20): gap clipping, cross-scheme spelling, chains and returns — seed 0, ten seeded permutations

Cards regenerated under v6 (3.6 clips a gap instead of dropping the target; 3.15 admits chains and returns);
alignment under 3.12's cross-scheme spelling (a quantile symbol crosses to the source role's symbol of the same
direction and nearest quantile). TCLab is withdrawn from the running order; the battery set is Rosetta member one.

| source → receiver | zero-shot (learned) | zero-shot (permuted) | raw cell | control cell | **net cell** | v5 net | types mapped | roles mapped |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tennessee Eastman → HAI | 7.632 (shared 7.262) | 8.917 | 0.86 | −0.05 | **0.90** | 0.98 | 142/168 (v5: 120) | 37/52 |
| HAI → Tennessee Eastman | 6.629 (shared 6.381) | 8.410 | 17.91 | 4.38 | **13.53** | 14.45 | 34/40 | 36/39 |
| Tennessee Eastman → battery | 3.676 (shared 3.676) | 6.346 | 0.04 | −0.21 | **0.25** | 0.00 | 12/12 (v5: 8) | 3/3: I ↔ cw_flow, T ↔ purge_D, V ↔ underflow_valve |
| battery → Tennessee Eastman | 8.772 (shared 3.504) | 9.006 | 5.59 | 3.94 | **1.65** | 0.00 | 6/40 (v5: 0) | 3/39: AC_valve ↔ V, cw_flow ↔ I, underflow ↔ T |
| HAI → battery | 4.721 (shared 4.721) | 5.359 | −0.22 | −0.28 | **0.05** | −0.00 | 12/12 (v5: 2) | 3/3: I ↔ LCP01D, T ↔ TIT01, V ↔ FCV01D |
| battery → HAI | 9.466 (shared 4.201) | 9.514 | −0.13 | −0.22 | **0.09** | −0.00 | 10/168 (v5: 6) | 3/52: B4002 ↔ V, FT03Z ↔ T, LIT01 ↔ I |

- **TEP ↔ HAI holds.** 0.90 and 13.53 against 0.98 and 14.45 under v5, inside the seed spread of the control,
  with a changed HAI library (2,165 fragments after clipping) and 22 more HAI types carried across by the
  spelling rule. The result does not depend on which v5-or-v6 instrument measured it.
- **The spelling rule did what it was for.** Every battery cell now carries types (12/12 as receiver against 2
  or 8), and TEP → battery is the first cross-kind cell where the learned mapping beats the permuted one by more
  than two bits of zero-shot (3.68 against 6.35) on a receiver whose own model is near its floor. The net cell
  is small (0.25) because a 12-type protocol is learned by the receiver's own model within its first day; the
  zero-shot gap is the evidence, the cell is not. Battery → TEP nets 1.65 through three roles — current ↔
  cooling-water flow, voltage ↔ the A/C feed valve, temperature ↔ separator underflow — a plausible pairing of
  an actuator, a setpoint-held quantity and a slow measurement, and too few roles to claim.
- **HAI ↔ battery stays at zero** (0.05, 0.09): the learned mapping beats the permuted by 0.6 bits as HAI → battery,
  the mixed curves do not move.

### Returns (3.15) — the loop signature across datasets

| dataset | chains admitted (used) | returns | the loop, as a return | spelled |
| --- | --- | --- | --- | --- |
| Tennessee Eastman | 525 (0) | 106 | `cw_flow:downq20 -s-> P:downq20 -m-> cw_flow:upq20` (n 46, cond. lift 3.52, null 11) | SLOW·RELAY → MID·FOLLOW → SLOW·RELAY |
| HAI | 1,437 (0) | 118 | `LIT01:upq80 -s-> LCV01D:upq20 -s-> LIT01:downq80` (n 15, cond. lift 9.01, null 5) | MID·RELAY → MID·RELAY → MID·RELAY |
| NASA battery | 13 (13) | 1 | `I:downq10 -s-> V:downq20 -s-> I:upq10` (n 27, cond. lift 2.10, null 4) | MID-S·RELAY → MID·RELAY → MID-S·RELAY |
| building A | 15 (15) | 1 | `T:down20 -m-> vent:off -s-> T:up20` (n 6, cond. lift 2.65, null 1) | untagged |
| building B′ | 32 (32) | 0 | — | — |

TEP's cooling-water loop and HAI's level loop both appear as returns, the strongest of their datasets' return
inventories (cw_flow ↔ cw_out and cw_flow → P → cw_flow: 31 returns; LIT01 ↔ LCV01D: 20). The thesis line
holds with one correction to its spelling: **neither is LEAD → FOLLOW → LEAD, and no return anywhere is.** An
actuator inside a closed loop is a context *and* a target — it moves the measurement and is moved by it — so the
degree rule of 3.14 tags it RELAY by construction. LEAD belongs to open drivers (feeds, schedules, the HIL load:
chains LEAD → RELAY → RELAY, 76 in TEP and 206 in HAI). A loop closing reads RELAY → FOLLOW → RELAY where the
measurement only follows (TEP's vessels) and RELAY → RELAY → RELAY where it also drives (HAI's level, the
battery's voltage). Whether 3.14 should carry a loop-aware place tag is the next method question, not a tuning.

## v5: place prefix and dimension suffix (alignment hard on kind and dimension, graded on clock and place; control permuted within clock class × dimension)

| source → receiver | zero-shot (learned) | zero-shot (permuted) | raw cell | control cell | **net cell** | v4 net | v3 net | types mapped |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tennessee Eastman → HAI | 7.683 (shared 7.177) | 8.986 | 0.86 | −0.12 | **0.98** | 1.67 | 0.37 | 120/168 |
| HAI → Tennessee Eastman | 6.622 (shared 5.887) | 7.944 | 21.57 | 7.11 | **14.45** | 10.52 | 0.06 | 34/40 |

Seed 0, re-run 2026-10-20 under the current control (ten permutations drawn from the run's seed; the 2026-10-19
cells, 0.83 and 13.37, were under three permutations from a fixed generator). The learned side is unchanged to the
third decimal; the control moved (−0.12 against 0.03; 7.11 against 8.29) and both nets moved with it.

Mixed picture, reported as such. HAI → TEP improved: more TEP roles found a dimensionally and dynamically
compatible HAI counterpart (34 of 40 types mapped against 22), and the mixed curve beats TEP's own model by
0.29–0.64 bits from 1 to 20 receiver days against a stricter control. TEP → HAI fell: the zero-shot is unchanged
(7.68 vs 7.65) but the control is now permuted within (clock class, dimension) and so is 0.9 bits better than
v4's, and the dimension constraint rules out pairs that v4 had used (120 types mapped against 134), so the net
halves. Two caveats on the comparison: v5 also fixed a scale bug that had made the "forbidden" penalty only
partly effective in v3 and v4 (distances were not normalised), so v4's constraints were looser than written;
and the stricter control is the right control, which means part of v4's 1.67 was credit the grammar had not
earned. Five seeds (below), one pair.

### v5 across seeds 0–4 (2026-10-20)

Seeds 1–4 were run under the control as it then was: three permutations from a fixed generator, so the seed
reached the control only through the mapping it permutes (the control has since been seeded and raised to ten
permutations; seed 0 above is under the new one, seeds 1–4 are not yet). Each seed is a full re-run of both
pipelines followed by both transfer directions.

| seed | TEP → HAI net | HAI → TEP net | HAI → TEP raw | HAI → TEP control | HAI → TEP zero-shot (learned / permuted) | HAI roles mapped |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.83 | 13.37 | 21.65 | 8.29 | 6.607 / 7.647 | 37/39 |
| 1 | 0.83 | 15.24 | 21.60 | 6.36 | 6.619 / 7.767 | 36/39 |
| 2 | 0.83 | 15.16 | 21.63 | 6.47 | 6.621 / 7.778 | 36/39 |
| 3 | 0.83 | 13.87 | 21.66 | 7.79 | 6.607 / 7.715 | 37/39 |
| 4 | 0.83 | 15.12 | 21.61 | 6.49 | 6.623 / 7.747 | 36/39 |
| **mean ± sd** | **0.83 ± 0.00** | **14.55 ± 0.87** | 21.63 ± 0.03 | 7.08 ± 0.89 | | |

- **TEP → HAI is seed-free.** All five seeds give the same role map, the same anchors (B4022 ↔ cw_out,
  PIT02 ↔ underflow_valve), 120/168 types mapped, and the same cells to two decimals (raw 0.86, control 0.03,
  net 0.83). The small cell is a property of the pair under v5, not of one draw.
- **HAI → TEP transfers on every seed; the spread is the control's, and it follows one pairing.** The raw cell is
  stable (21.60–21.66) and the learned zero-shot moves by 0.02 bits at most, while the control cell ranges
  6.36–8.29 and the net cell inherits it: 13.37–15.24, mean 14.55 ± 0.87. The split is clean: the two seeds that
  map E_feed ↔ CO_rpm (0 and 3) have controls 8.29 and 7.79; the three that leave E_feed unmapped have 6.36–6.49.
  That pairing adds ~1.5 bit-days of regularisation to the control and nothing to the raw cell, so it carries no
  structure and the net is more honest without it. The lowest seed is still 1.3× the v4 cell (10.52).
- **The role pairings rotate within a dynamical class.** Seeds 1–4 differ from seed 0 on four or five of the
  39 HAI roles, all among HAI's purge and feed roles and TEP's valve roles VXT02/VXT03/VYT02/VYT03 (the same
  tag class, exchanged among themselves), plus E_feed ↔ CO_rpm dropped in three seeds. The alignment is stable
  where it is confident and indifferent where the candidates are interchangeable, which is what a graded
  distance should do.
- **Open item (done the same day):** the control now takes the run's seed and ten permutations; seeds 1–4 are
  to be regenerated under it at the next sweep, and the mean ± sd above will then sample the control as well.

## v5, the Rosetta set's first two members (2026-10-20): TCLab (5) and the NASA battery cells (6)

Seed 0, the seeded ten-permutation control. TCLab is **not admitted** (7.6 h, no period; its card is for the
record) and has less than one training day, so it cannot carry a learning curve as a receiver: those cells are
"not measurable" and only the zero-shot is reported. The battery set is admitted (47.5 observed days) but its
library is 12 fragments built from the 7% of events that survive the gap rule (its card).

| source → receiver | zero-shot (learned) | zero-shot (permuted) | raw cell | control cell | **net cell** | roles mapped | types mapped | role pairings |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TCLab → battery | 6.236 (shared 1.105) | 6.232 | −0.18 | −0.18 | **−0.00** | 2/3 | 2/12 | T ↔ T, Q ↔ I |
| battery → TCLab | 6.654 (shared 0.901) | 6.715 | — | — | not measurable | 3/3 | 2/12 | Q ↔ I, T ↔ T, Tsp ↔ V |
| TEP → battery | 3.585 (shared 3.585) | 3.585 | 0.19 | 0.19 | **0.00** | 3/3 | 8/12 | I ↔ cw_flow, T ↔ purge_D, V ↔ purge_B |
| battery → TEP | 5.322 (shared —) | 5.322 | 25.97 | 25.97 | **0.00** | 3/39 | 0/40 | AC_valve ↔ V, feed ↔ I, prod_H ↔ T |
| HAI → battery | 3.926 (shared 1.854) | 3.917 | −0.01 | −0.01 | **−0.00** | 3/3 | 2/12 | I ↔ FCV02Z, T ↔ TIT01, V ↔ FCV01D |
| battery → HAI | 9.063 (shared 2.715) | 9.073 | 0.03 | 0.04 | **−0.00** | 3/52 | 6/168 | B4005 ↔ V, SIT01 ↔ T, VXT03 ↔ I |
| TEP → TCLab | 3.876 (shared 3.876) | 4.072 | — | — | not measurable | 3/3 | 8/12 | Q ↔ feed, T ↔ purge_D, Tsp ↔ cw_flow |
| TCLab → TEP | 7.435 (shared 1.240) | 7.443 | 8.79 | 8.82 | **−0.04** | 3/39 | 2/40 | cw_flow ↔ Tsp, feed_C ↔ Q, underflow ↔ T |
| HAI → TCLab | 3.484 (shared 3.484) | 3.682 | — | — | not measurable | 3/3 | 12/12 | Q ↔ FT01, T ↔ FCV03D, Tsp ↔ B4002 |
| TCLab → HAI | 9.491 (shared 3.431) | 9.504 | 0.17 | 0.14 | **0.03** | 3/52 | 12/168 | B2016 ↔ T, B4002 ↔ Tsp, B4022 ↔ Q |

**Nothing transfers, and the table says why.** Every net cell is zero to two decimals and every learned zero-shot
is within 0.2 bits of its permuted control. Three instrument facts sit upstream of the physics:

- **The pair's libraries are too small to carry anything.** TCLab has two fragments (a step-test staircase);
  the battery set twelve, from one-twentieth of its events. A source with no motifs has nothing to send, and a
  receiver with 282 test events cannot register what arrives.
- **Role pairings cross, symbol spellings do not.** Battery → TCLab pairs Q ↔ I, T ↔ T, Tsp ↔ V — the physical
  correspondence (actuator ↔ actuator, temperature ↔ temperature) — but T ↔ T is forced by the ⟨Θ⟩ suffix and
  Q, being dimensionless, is free, so with three roles a side this is a coin toss, not evidence. More to the
  point, Q is spelled q20/50/80 and I is spelled q10/90, so the role match carries no types (2 of 12 mapped, both
  of them T's peak and trough); the same happens to battery → TEP (3 roles matched, 0 of 40 types). Symbols cross
  by spelling (3.12), and the symbolization rule chose different spellings for the two actuators.
- **The regulariser is large and the control takes all of it.** Battery → TEP's raw cell is 25.97 bit-days,
  the largest raw number in the collection, and the control is 25.97: a three-role model through any mapping
  smooths TEP's 40-class receiver. The v3 lesson again, at scale, and the control does its job.

What the Rosetta pair tests — whether the thermal and the electrochemical first-order loop share a grammar — is
not yet tested. The order of repair is the one the cards give: a gap rule for fragmented observation (the
battery would then mine ~12,000 events instead of 838); a long TCLab recording (24–48 h, both heaters, a setpoint
schedule); and a decision on whether actuators spelled by different quantile schemes should be allowed to cross
(a spelling rule, 3.12 — not a tuning). Until then the cells stand as the first all-zero row of the matrix,
with the control confirming that zero is zero.

## v4: grammar (parts of speech, role-level alignment, symbols by spelling, control permuted within class)

| source → receiver | zero-shot (learned) | zero-shot (permuted, within class) | raw cell | control cell | **net cell** | v3 net | kind |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Tennessee Eastman → HAI | 7.646 (shared 7.220) | 9.627 | 1.21 | −0.45 | **1.67** | 0.37 | cross kind |
| HAI → Tennessee Eastman | 6.390 (shared 4.700) | 7.435 | 18.42 | 7.90 | **10.52** | 0.06 | cross kind |
| building A → B′ | — | — | — | — | 0.74 | 0.74 | same kind; B′ has scrambled type names, so v4's role-level alignment does not apply and the cell is v3's |
| building B′ → A | — | — | — | — | 5.53 | 5.53 | as above |

Under v4 the mixed curve beats the receiver's own model at **every** point of both cross-kind curves (TEP → HAI:
−1.07 bits at 1 receiver-day, −0.24 at 2, −0.08 at 3–5, −0.01 to −0.02 at 10–11; HAI → TEP: −0.18 to −0.57
bits from 1 to 20 days, mixing weight 0.25), and the within-class permuted control is worse than the learned
mapping at every point (by 0.1–0.6 bits). In v3 the same two cells were at chance. What changed is only the
spelling of the motifs: a part-of-speech prefix on each role, roles aligned to roles of the same part of speech
and symbol kind, and symbols carried across by their spelling, so `up` stays `up` and `q80` stays `q80`.

The role pairings are not physical identities (TEP cooling-water flow ↔ HAI temperature demand; TEP level ↔
HAI pressure; TEP vessel temperature ↔ HAI speed-controller output). They are dynamical: a mid-speed
controlled variable in one plant stands in for a mid-speed controlled variable in the other. That is the
thesis as stated — the same form in different substance — and the net cells say the pairing predicts. One
seed, one pair: the result stands as a first positive, not a universal.

## v3 (type-level alignment, for the record)

| source → receiver | zero-shot (learned mapping) | zero-shot (permuted mapping) | raw cell | control cell | **net cell** | kind |
| --- | --- | --- | --- | --- | --- | --- |
| building A → building B′ | 4.600 | 7.934 | 0.20 | −0.54 | **0.74** | same kind (synthetic buildings) |
| building B′ → building A | 3.075 | 7.780 | 1.73 | −3.80 | **5.53** | same kind |
| Tennessee Eastman → HAI | 8.855 | 9.646 | 0.25 | −0.12 | **0.37** | cross kind (chemical process → boiler/turbine testbed) |
| HAI → Tennessee Eastman | 8.426 | 8.510 | 8.22 | 8.16 | **0.06** | cross kind |

Receivers' own libraries, bits/event on the test split: A 2.167, B′ 1.365, TEP 3.033, HAI 3.721.
Mapping accuracy is measured only where a key exists: A → B′ 0.60 (30 scorable types). Cells for the
pairs 1,2 ↔ 3,4 are not run: a building and a plant are different kinds, and the matrix needs the
within-kind cells first.

## Reading

- **Same kind, same mechanisms: the alignment is real.** Between the two buildings the learned mapping's
  zero-shot beats the permuted mapping's by 3.3–4.7 bits, and the permuted model *hurts* the receiver
  (control cells −0.54 and −3.80), so the learned mapping's modest raw gains are large net gains. B′ (four
  zones, a dehumidifier loop) teaches A far more than A teaches B′ — the richer system is the better source.
- **Cross kind: nothing at the type level.** TEP ↔ HAI mappings are at chance (learned vs permuted zero-shot
  within 0.1–0.8 bits; the anchors pair a purge-gas analyser with a boiler temperature demand). HAI → TEP's
  raw 8.22 bit-days is entirely regularisation: a 10% share of *any* smooth distribution helps TEP's
  over-parameterised 40-class model from 2 to 20 training days, and the permuted mapping does it just as
  well. TEP → HAI's 0.37 is small and confined to the first two receiver days.
- **The control was necessary.** Under v2 the HAI → TEP cell would have entered the matrix as 8.2 bit-days —
  the largest in the collection — and been false. This is the collection's first negative-control result,
  arriving before the datasets designated as negative controls.

## What v3 said about the thesis (superseded by v4 above)

Type-level alignment of lift matrices (3.12) finds correspondences between systems of the same kind and does
not find them across kinds, with 40 vs 168 types and two signature anchors. It does not yet say whether the
cross-kind correspondence is absent or merely not findable this way. The structures that should be shared
between a chemical plant and a boiler — level control, pressure control, actuator → measurement loops — are
a handful of motifs among hundreds of types; the type-level Hungarian match has no way to privilege them. The
candidate route is the one Experiment C pointed to: align at the level of *shapes* (type-free fragment
topology: "actuator rises → measurement falls at lag s, then actuator falls") and transfer the shape prior,
not the lexicon. That is the next method question, and it is a v4 question, not a tuning one.

## Open items raised

1. (v4 did the first half) Parts of speech and role-level alignment lifted the cross-kind cells; syntax motifs — chains and the feedback-return motif — are the second half, not yet built.
2. Pooled lag classes for the pair before alignment (each dataset's own bands reduce comparability).
3. The learning curve's λ is chosen by 2-fold on the receiver's training days and then reused for the control;
   a control-specific λ would be fairer to the control, i.e. more conservative.
4. A within-kind real pair (TEP ↔ a second chemical process, HAI ↔ SWaT) is the missing test between the
   synthetic same-kind result and the cross-kind null.
