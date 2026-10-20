# Transfer matrix — methods v3 to v5, profile v1 (2026-10-19; v5 seeds 0–4 added 2026-10-20)

Cells are **net bit-days**: the area between the receiver's own learning curve and the curve of its model
mixed with the translated source model, minus the same area for the source model sent through a permuted
mapping (3.12, v3). The control removes what any smooth foreign model gives a data-starved receiver —
regularisation — and leaves what the correspondence gives.

## v5: place prefix and dimension suffix (alignment hard on kind and dimension, graded on clock and place; control permuted within clock class × dimension)

| source → receiver | zero-shot (learned) | zero-shot (permuted) | raw cell | control cell | **net cell** | v4 net | v3 net | types mapped |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tennessee Eastman → HAI | 7.682 (shared 7.176) | 8.697 | 0.86 | 0.03 | **0.83** | 1.67 | 0.37 | 120/168 |
| HAI → Tennessee Eastman | 6.607 (shared 5.884) | 7.647 | 21.65 | 8.29 | **13.37** | 10.52 | 0.06 | 34/40 |

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

The seed enters the pipeline's null draws and the alignment; the control's three permutations are drawn from a
fixed generator (`transfer()` is called without an rng), so the seed reaches the control only through the mapping
it permutes. Each seed is a full re-run of both pipelines followed by both transfer directions.

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
- **Open items:** (a) the control's permutations should take the run's seed, not a fixed one, so that a seed
  sweep also samples the control; (b) three permutations is a thin control, and the control's spread (sd 0.89)
  is now the matrix's largest uncertainty — more permutations per seed would narrow it at low cost.

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
