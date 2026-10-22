# Benchmark card — Alibaba cluster-trace-v2018 machine usage (dataset 10, negative control one), method v8 card / v9 collection

Run 2026-10-21. Source: Alibaba Open Cluster Trace Program, cluster-trace-v2018 `machine_usage` (github.com/alibaba/clusterdata;
public OSS mirror, 1.77 GB archive, 9 GB csv, 247 M rows): ~4,000 machines over 8 days. A deterministic subsample
of 200 machines (every 20th id; 198 with data) as units with roles cpu, mem, net_in, net_out, disk_io — percentages
and normalised rates, all dimensionless, so no role carries a suffix and the dimension constraint of 3.12 maps
nothing hard. **The collection's first negative control** (section 6): a scheduler places jobs on these machines
and nothing in these columns closes a loop on another column. The prediction declared before it ran: as a source
into TEP, structure ≈ 0 (below 5 bit-H).

## Declarations

- **1-minute means** over the 8-day trace (the native step; 12.1 M rows in the subsample); no gaps declared.
- **Entity: machine**, the only candidate run — a single-system layout of 990 roles (~6,000 types) is beyond the
  Markov-only comparison, as for Building 59.
- No answer key; recovery `not measured`.

## Identity and scale

| | |
| --- | --- |
| Entity | **machine**, 198 units, five roles each |
| Symbolization (3.2) | q20/50/80 for every role (the only faithful scheme throughout) |
| Events | 475,385 in 8 days (59,439/day); 27 target types |
| Lag classes (3.3) | 3.3 / 10.8 / 35.5 min (recurrence horizon 35.5 min) |
| Period (3.4) | slow 121 min (a two-hour cadence of the cluster); no fast period |
| Admission (section 6) | 8.0 days · **324 H** (test 81 H) · 95 slow periods → admitted (by slow periods) |
| Nulls (3.8) | circular 0.75; cycle 0.78; rewire 0.83 |
| Discovery | 1,140 candidates → **86 validated fragments** (40 used), 151 compositions; chatty share 0.21 |
| Syntax (3.15) | 417 chain candidates → 22 → 22 → **18 admitted, 13 returns**, all used |
| Tags (3.14) | every role SLOW; cpu, mem, disk_io `LOCAL·RELAY`; net_in, net_out `ISOLATED` |

## Headline (bits per event on the test split)

| model | all |
| --- | --- |
| unigram | 4.168 |
| markov-1 / -2 / -3 | 3.555 / 3.028 / **2.761** |
| hawkes-like decay features | 2.963 |
| logistic markov features | 2.991 |
| logistic triviality library (3.11) | 2.481 |
| logistic library | 2.635 |
| logistic unselected contexts | 2.482 |

Gain over triviality **−0.154**; over the best baseline (Markov-3) +0.126 → claim: **no gain**.

## Reading the result

A machine's utilisation re-crosses its own quantiles, and the alternation model carries that; the 86 fragments are
mostly a role's own re-crossings and cpu ↔ mem ↔ disk_io co-movements within a machine. Thirteen returns on cpu and
disk_io (cpu RESPONDS, disk_io REACTS by timing; the reverse by determinism, 11 of 13 unresolved) — a job's
I/O and CPU rising and falling together is not a loop, and the loop rules, recorded, cannot tell that from one.

**As a source.** Into TEP: **structure 51.2 bit-H** (raw 124.4; derangement 43.8; marginal 73.2), 30 of 40 TEP
types through five roles — P ↔ cpu, cw_flow ↔ net_in, cw_out ↔ mem, feed ↔ net_out, underflow_valve ↔ disk_io —
and 29% of TEP's own ceiling. The declared prediction fails by an order of magnitude. Into Building 59 4.3, HAI
4.7 (short), Fingrid −1.5, the battery 0.4, PhysioNet uncontrolled (no type shared), the buildings ≈ 0. **As a
receiver:** TEP 4.6, Building 59 2.6, HAI 2.1, Fingrid 1.9, the rest ≤ 0 — small, as a system without a loop
should receive.

**What the TEP cell says.** It is the measurement section 6 asked for: TEP's own learning model sits above TEP's
own unigram at eight of nine curve points (5.2–5.4 bits against 5.09), so any smooth prior over TEP's 40 classes
improves it, a cluster trace's five mapped roles included; the deranged and the flattened versions of that prior
remove part of the effect and not all of it. The cells into TEP, and into Building 59 (own model above its unigram
at every point), are receiver-side regularisation. The control did its job; the collection stops here until the
receiver's own baseline is repaired (docs/MATRIX.md, v9).

## Open items raised by this dataset (not rules)

1. **The receiver's own curve as the baseline** (3.12): it must be no worse than the receiver's own unigram at every
   point; TEP's and Building 59's are not. The fix is a method question and the stop condition of this round.
2. Single-system candidates at 990 roles: the Building 59 item again.
3. Returns on co-moving utilisations: a return needs a different role in the middle, and cpu → disk_io → cpu
   qualifies; whether a return should require evidence of opposition (the far end reversing *because of* the
   middle) is a 3.15 question the negative control raises.
