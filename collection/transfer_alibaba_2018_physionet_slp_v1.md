# Transfer cells — alibaba_2018 ↔ physionet_slp (method v9, profile v1, seed 0)

Own libraries: alibaba_2018 2.635 bits (triviality 2.481); physionet_slp 3.136 bits (triviality 3.328)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8). Controls: the median of ten derangements and the marginal control (the source's type frequencies through the mapping, v9); **structure** = learned cell net of the larger control; share = structure / the receiver's diagonal structure (its ceiling), where a diagonal exists.

| direction | zero-shot (learned) | zero-shot, derangement | zero-shot, marginal | cell (bit-H) | derangement cell | marginal cell | net (derangement) | structure | share of ceiling | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alibaba_2018 → physionet_slp | 3.322 | 3.322 | 3.322 | 0.00 | 0.00 | 0.00 | — (raw is an upper bound) | **0.00** (marginal) | — | 0/10 | not measured (no mapping key) | uncontrolled |
| physionet_slp → alibaba_2018 | 4.755 | 4.755 | 4.755 | 1.25 | 1.25 | 1.25 | — (raw is an upper bound) | **0.00** (marginal) | — | 0/27 | not measured (no mapping key) | uncontrolled |
