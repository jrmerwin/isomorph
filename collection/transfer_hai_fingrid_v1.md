# Transfer cells — hai ↔ fingrid (method v8, profile v1, seed 0)

Own libraries: hai 3.714 bits (triviality 3.675); fingrid 1.615 bits (triviality 1.603)

Cells in bit-horizons (bits × the receiver's recurrence horizon H) on observed training time to 200 H (3.12, v8); the control is the median of ten derangements, moved share at widths (clock, dimension) / clock / all.

| direction | zero-shot (all) | zero-shot (shared) | zero-shot, derangement | cell (bit-H) | control cell | net cell | types moved by width | receiver types mapped | mapping accuracy | flags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hai → fingrid | 4.537 | 4.537 | 4.855 | 21.72 | 15.79 | **5.93** | 1.00 / 1.00 / 1.00 | 16/16 | not measured (no mapping key) |  |
| fingrid → hai | 8.238 | 5.483 | 8.505 | 34.37 | 33.05 | **1.31** | 1.00 / 1.00 / 1.00 | 10/168 | not measured (no mapping key) | short, damage |
