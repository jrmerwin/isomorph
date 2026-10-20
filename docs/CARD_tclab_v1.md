# Benchmark card — TCLab (dataset 5), method v5, profile v1, seed 0

Run 2026-10-20. Source: nine public recordings of the Arduino Temperature Control Lab (Hedengren, Park, Martin et
al., BYU; https://apmonitor.com/heat.htm) — a real kit with two transistor heaters (Q1, Q2, 0–100 % power) and a
thermistor on each (T1, T2, °C), 1-second samples. Seven are APMonitor course uploads (open-loop step tests, 10 min
to 4 h), one is a 90-min closed-loop PID run with its setpoint (BYU PRISM), one is a 13-min step test (Kantor, Notre
Dame). The thermal member of the Rosetta set: heater (actuator, dimensionless power) → sensor temperature ⟨Θ⟩.

**Not admitted.** 7.6 h of events, and the period rule finds no cycle, so neither the 20-day line nor the
natural-period clause is met. The card is recorded for the record and every cell that uses it is flagged.

## Declarations

- **Resolution: 5-second means** of the 1-second source. The sensor LSB is 0.1 °C and the heater-to-sensor time
  constant 1–3 min, so at 1 s successive readings differ by less than an LSB (quantisation texture, not structure).
- **Time axis compressed**: the recordings have no common clock (different boards, rooms, years), so they are
  concatenated longest first (the rule; ties by name) with each of the 8 boundaries a gap for every entity, and
  the two stretches in which sensor 2 was absent (the 4-h and the 90-min runs) are gaps for h2.
- **Columns constant within a recording are absent** for it (an unplugged sensor reads 0; an unused heater 0).
- Ambient temperature is not recorded; there are no system-wide roles.

## Identity and scale

| | |
| --- | --- |
| Entity | **heater** (h1, h2 — each heater with its own sensor), chosen by 3.1: 4.300 vs 5.251 bits/event Markov-only for a single system |
| Symbolization (3.2) | Q: q20/50/80 — the only faithful scheme — at 10 / 43 / 60 % on heater 1 (heater 2 is 0 or 100 in the few runs that use it: 10 / 10 / 100, degenerate); T: turning points (the 5-s means need no further denoising, window 1); Tsp: q10/90 at 41 / 67 °C, 7 events |
| Events | 469 in 7.6 h (1,471/day); h1 437, h2 32 |
| Types | 12 |
| Lag classes (3.3) | 0.52 / 3.28 / 20.54 min (recurrence horizon 20.5 min) |
| Period (3.4) | none |
| Signal floor (3.5) | 5 (descriptive) |
| Nulls (3.8) | circular (gate) survival 0.46; rewire 0.0 (two entities, one of them nearly eventless) |
| Discovery | 48 candidates → **2 validated fragments**, 0 compositions; chatty share 1.00 |
| Dropped for gaps | **210 of 469 events** (45%): the horizon is 20.5 min and six of the nine recordings are 10–14 min, so every event in them, and the first 20 min of each longer one, has a look-back window that spans a boundary |
| Test split | 282 events (last 115 min: the 1-h step sequence and the five short runs), evaluated once |

## Headline (bits per event on the test split)

| model | all |
| --- | --- |
| unigram | 3.069 |
| markov-1 | 2.909 |
| markov-2 | 3.176 |
| markov-3 | 3.345 |
| hawkes-like decay features | 3.031 |
| logistic markov features | **2.775** |
| logistic triviality library (3.11) | 2.855 |
| logistic library | 2.747 |
| logistic unselected contexts | 2.781 |

Gain over triviality 0.107 bits; over the best baseline (logistic Markov, 2.775) 0.027 → claim: **no gain**.

## Reading the result

The two fragments are a heater step passing through two thresholds in one move — `Q:upq50 -s-> Q:upq80`,
`Q:downq50 -s-> Q:downq20` — the staircase of a step test, not the thermal loop. The keyed mechanism, heater →
its own sensor, is **not found (recovery 0/3)**: at 5-second means a heating ramp has a turning point only when
the heater steps, so T emits 89 events in 7.6 h, and the gap rule removes the short recordings in which both
heaters act. The triviality baseline finds the four same-role re-crossings and nothing else.

This is a card about the public recordings, not about the loop. The TCLab is the right Rosetta member — the
simplest first-order loop with a dimensionless actuator and a ⟨Θ⟩ measurement — but no public recording of it
is long enough: the longest is 4 h on one heater. The kit itself is inexpensive; a 24–48 h recording of both
heaters under a setpoint schedule or a PRBS would meet the natural-period clause on its own schedule and
replace this card.

## Open items raised by this dataset (not rules)

1. **The gap rule against short recordings.** A target is dropped when its whole look-back window overlaps a
   gap; with a 20-min horizon and 10-min recordings that is every event. Same item as the battery card's, from
   the other side: the collection needs a stated rule for observation fragmented at or below the horizon.
2. **A recording to collect.** The dataset's own fault is span; the fix is data, not method.
3. The step-test staircase (one actuator move crossing several quantiles within one lag class) is the one motif
   short open-loop recordings have; 3.11 does not absorb it because the crossings are not alternations.
