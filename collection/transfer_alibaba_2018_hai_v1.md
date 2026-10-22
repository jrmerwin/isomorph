# Transfer cells — alibaba_2018 ↔ hai (method v9, profile v1, seed 0)

Own libraries: alibaba_2018 2.635 bits (triviality 2.481); hai 3.714 bits (triviality 3.675)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alibaba_2018 → hai | 8.732 | 9.587 | 8.851 | 36.46 | 30.09 | 31.76 | 6.37 | **4.71** (marginal) | — | 30/168 | not measured (no mapping key) | short, damage |
| hai → alibaba_2018 | 5.127 | 5.851 | 5.216 | 2.89 | 0.26 | 0.81 | 2.62 | **2.08** (marginal) | — | 25/27 | not measured (no mapping key) | damage |
