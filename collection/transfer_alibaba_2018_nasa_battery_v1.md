# Transfer cells — alibaba_2018 ↔ nasa_battery (method v9, profile v1, seed 0)

Own libraries: alibaba_2018 2.635 bits (triviality 2.481); nasa_battery 0.838 bits (triviality 0.827)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alibaba_2018 → nasa_battery | 3.809 | 6.442 | 4.608 | 0.16 | -0.38 | -0.28 | 0.54 | **0.44** (marginal) | — | 10/12 | not measured (no mapping key) | short, damage |
| nasa_battery → alibaba_2018 | 7.490 | 7.652 | 7.126 | 0.90 | 0.88 | 1.63 | 0.01 | **-0.74** (marginal) | — | 9/27 | not measured (no mapping key) | damage |
