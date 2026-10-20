# Transfer matrix — method v3, profile v1, seed 0 (2026-10-19)

Cells are **net bit-days**: the area between the receiver's own learning curve and the curve of its model
mixed with the translated source model, minus the same area for the source model sent through a permuted
mapping (3.12, v3). The control removes what any smooth foreign model gives a data-starved receiver —
regularisation — and leaves what the correspondence gives.

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

## What this says about the thesis

Type-level alignment of lift matrices (3.12) finds correspondences between systems of the same kind and does
not find them across kinds, with 40 vs 168 types and two signature anchors. It does not yet say whether the
cross-kind correspondence is absent or merely not findable this way. The structures that should be shared
between a chemical plant and a boiler — level control, pressure control, actuator → measurement loops — are
a handful of motifs among hundreds of types; the type-level Hungarian match has no way to privilege them. The
candidate route is the one Experiment C pointed to: align at the level of *shapes* (type-free fragment
topology: "actuator rises → measurement falls at lag s, then actuator falls") and transfer the shape prior,
not the lexicon. That is the next method question, and it is a v4 question, not a tuning one.

## Open items raised

1. Shape-level (syntax) alignment and transfer as the cross-kind route (3.12 alternative).
2. Pooled lag classes for the pair before alignment (each dataset's own bands reduce comparability).
3. The learning curve's λ is chosen by 2-fold on the receiver's training days and then reused for the control;
   a control-specific λ would be fairer to the control, i.e. more conservative.
4. A within-kind real pair (TEP ↔ a second chemical process, HAI ↔ SWaT) is the missing test between the
   synthetic same-kind result and the cross-kind null.
