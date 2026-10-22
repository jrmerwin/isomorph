# Transfer cells — nasa_battery ↔ nasa_battery (method v9, profile v1, seed 0)

Own libraries: nasa_battery 1.042 bits (triviality 0.916); nasa_battery 0.838 bits (triviality 0.827)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nasa_battery_stretch → nasa_battery (diagonal, identity) | 2.543 | 4.729 | 3.598 | 0.82 | -2.08 | -1.78 | 2.90 | **2.60** (marginal) | — | 12/12 | identity | short |
