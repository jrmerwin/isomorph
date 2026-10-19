# Benchmark card — HAI 21.03 (dataset 4), method v2, profile v1, seed 0

Run 2026-10-19. Source: HAI (HIL-based Augmented ICS) security dataset 21.03, https://github.com/icsdataset/hai —
a real testbed: Emerson boiler (P1), GE turbine rotor kit (P2), FESTO water treatment (P3), coupled through a
dSPACE hardware-in-the-loop simulator of steam-turbine and pumped-storage generation (P4). In place of SWaT, which
iTrust distributes on request only.

## Declarations

- **Resolution: 1-minute means** of the 1-second source (booleans: last value; attack flags: max). At 1 s the
  turbine's vibration and rpm channels (correlation times 7–40 s) emit ~1.5 million crossings in 15 days — the
  texture of a rotating machine, not structure — while the boiler and water-treatment dynamics act over 15–70 min.
- **Time axis compressed**: the eight time-continuous files (3 normal, 5 with attacks, Jul 7 – Aug 10 2020) are
  concatenated in chronological order with the unobserved stretches between them removed; each of the 7 boundaries
  is a missing-data gap for every entity, so no context spans one (1,234 contexts dropped).
- **Attack labels excluded** from the events; the 50 attack episodes are regime annotations in the sidecar.
- **Span 15.3 days — below the 20-day admission line**, and the period rule finds no cycle, so the natural-period
  clause does not apply. Admitted provisionally; the card is flagged.

## Identity and scale

| | |
| --- | --- |
| Entity | **process** (P1 boiler, P2 turbine, P3 water treatment), chosen by 3.1: 5.033 vs 6.220 bits/event Markov-only for a single system; P4 (HIL schedule, demand, output power) is system-wide |
| Symbolization (3.2) | 57 roles: 22 q20/50/80, 5 q10/90 (the first dataset where the coarse quantile scheme wins anywhere), 23 turning points, 7 silent (two 0/100 valve commands, P3 inflow — pump cycling that averages out at 1-min means — the two frequency deviations, two constant setpoints) |
| Events | 34,298 in 15.3 days (2,238/day); targets P1 13,829, P3 8,264, P2 6,489; system-wide 5,716 |
| Types | 190 in all; 168 target types |
| Lag classes (3.3) | 5.0 / 24.9 / 124.0 min (recurrence horizon 2.1 h) |
| Period (3.4) | none |
| Signal floor (3.5) | 12 (descriptive) |
| Nulls (3.8) | circular (gate) survival 0.20; rewire (attribute) 0.03 — roles are process-specific, so almost nothing is "bound" in the rewire sense |
| Discovery | 30,982 candidates → 2,096 validated fragments (431 distinct contexts), 0 compositions |
| Deterministic types | 7 (FT02Z crossings, FT03Z and SIT02 turning points) reported separately |
| Test split | 7,454 events (last 3.8 days), evaluated once |

## Headline (bits per event on the test split)

| model | all | non-deterministic | deterministic |
| --- | --- | --- | --- |
| unigram | 6.859 | 6.837 | 7.39 |
| markov-1 | 5.276 | 5.475 | 0.392 |
| markov-2 | 5.771 | 5.990 | 0.441 |
| markov-3 | 6.188 | 6.423 | 0.462 |
| hawkes-like decay features | 3.876 | 3.905 | 3.153 |
| logistic markov features | 4.937 | 5.118 | 0.518 |
| logistic triviality library (3.11) | 3.696 | **3.826** | 0.509 |
| logistic library | 3.721 | 3.851 | 0.545 |
| logistic unselected contexts | 3.736 | 3.865 | 0.575 |

Gain over triviality **−0.024** bits; over the best baseline (Hawkes-like, 3.905) 0.055 → claim: **no gain**.

## Reading the result

The triviality baseline (3.11, name-free alternating pairs) found **188 pairs**: 89 are same-role re-crossings
(downqX ↔ upqX, peak ↔ trough), **99 are cross-role** — a valve command and its position crossing the same
quantile in strict alternation, setpoints that step together under the HIL schedule (B2004 ↔ B3004), and the
like. Those cross-role pairs are deterministic couplings of the plant, and the "trivial" model carries them:
with 188 × 3 lag classes it is a 1,128-context model that scores 3.826. The validated library (431 contexts)
scores 3.851 and the unselected contexts 3.865 — the library adds nothing the alternation model does not have.

That is consistent with the recovery: **7 of 15** keyed mechanisms are in the library (level-control valve →
return-tank level, 19 fragments at lag m, lift up to 2.6; speed-controller output → turbine rpm, lift 27 at lag
s; pressure valve → HX outlet pressure; FCV03, FCV01, PCV01 and LCV01 command → position), the best recovery of
any dataset so far — and most of them are exactly the deterministic couplings that 3.11 absorbs. The method
finds the physics and then, correctly under its own rules, declines to claim it as non-trivial structure.

Not found: FCV03 position → HX outlet temperature, pump start → running (constant in this span), the P3 pump →
inflow → level chain (inflow silent at 1-min means), and the P4 load → gate → output chain (system-wide roles are
contexts, not targets).

## Open items raised by this dataset (not rules)

1. **3.11 absorbs deterministic cross-variable couplings.** The name-free alternation test was introduced for
   symmetric re-crossings of one variable; on HAI 99 of 188 pairs join different roles. Whether a command →
   position coupling is "trivial" is a definitional choice to settle (and version) before dataset 5, not after a
   result. The card reports both counts so the choice can be made with the evidence in view.
2. Fast-oscillation channels (vibration, rpm at 1 s) need an envelope symbolization; the 1-minute declaration is a
   workaround.
3. The P3 inflow is silent at 1-min means although its pump cycles are the water-treatment mechanism: the resolution
   declaration costs a known mechanism.
4. 15.3 days is short; the test split is 3.8 days. SWaT (11 days) would face the same shortfall.
