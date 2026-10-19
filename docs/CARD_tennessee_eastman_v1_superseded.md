# Benchmark card — Tennessee Eastman (dataset 3), method v1, profile v1, seed 0

Run 2026-10-19. Source: Souza, de Souza & da Silva (2023) 1-year continuous run of the Tennessee Eastman
process (Ricker's revised model), https://github.com/anasouzac/new_tep_datasets, `matlab_data_1year.csv`.
Declared span: the first 120 days (57,600 samples at 3 min). Days 120–365 untouched (continuation).

## Identity and scale

| | |
| --- | --- |
| Kind | simulated plant, random fault episodes (IDV 1–20) with normal operation between; fault label excluded from events, kept as 82 regime annotations in the sidecar |
| Entity | **vessel** (reactor, separator, stripper), chosen over a single plant entity by 3.1: 4.280 vs 5.329 bits/event, Markov features only |
| Symbolization (3.2) | 40 roles; 26 quantile crossings (q20/50/80, per-unit thresholds), 13 turning points (product analysers, D/E feeds, levels, purge, purge valve), 1 silent (stripper steam: no detectable signal at the sampling scale). Noise windows 1–136 samples. |
| Events | 280,002 in 120 days (2,333/day); 78,562 vessel targets (reactor 30,427; separator 26,513; stripper 21,622), 201,440 system-wide |
| Types | 186 in all; 40 target types |
| Lag classes (3.3) | edges 3.0 / 9.0 / 21.0 min — the horizon is the 95th-percentile inter-event gap, set here by event density, not plant dynamics; gaps are multiples of the 3-min sample, so class `s` (gap < 3) is empty |
| Period (3.4) | none (the acf of the event rate decays slowly with regime switching; no prominent peak with ≥ 8 repetitions) |
| Signal floor (3.5) | 66 events (descriptive) |
| Nulls run (3.8) | circular (gate), rewire (attribute); survival 0.75 / 0.24 |
| Discovery | 14,271 candidates → 606 validated fragments (179 distinct contexts), 0 compositions kept |
| Test split | 19,784 events (days 90–120), evaluated once |

## Headline (bits per event on the test split; no deterministic types)

| model | bits |
| --- | --- |
| unigram | 5.087 |
| markov-1 | 4.524 |
| markov-2 | 4.606 |
| markov-3 | 5.188 |
| hawkes-like decay features | 3.978 |
| logistic markov features | 4.196 |
| logistic triviality library (3.11) | 3.569 |
| **logistic library** | **3.387** |
| logistic unselected contexts | 3.477 |

Gain over triviality **0.183** bits; over the best baseline (Hawkes-like, 3.978) **0.592** bits → claim: **beats baselines**.
The validated library also beats the unselected contexts by 0.090 bits, the first dataset where validation
pays on the headline (on the buildings the unselected set was as good or better).

Trivial pairs found (3.11): threshold re-crossings of every quantile role (P, T, cw_flow, cw_out, feed,
underflow_valve: downqX ↔ upqX) and L:peak ↔ L:trough. The 0.183 is what the library adds beyond those.

## What the library contains

- 606 fragments, lag classes m 321 / l 285; 52% have a vessel-role context, 48% a system-wide one
  (compressor, feed valves, A feed, purge composition C most common); binding evidence (rewire) 35%.
- Highest lifts are same-role re-crossings (cw_flow:upq80 →l cw_flow:downq80, lift 26; underflow_valve
  downq20 →l upq20, 23; feed downq20 →l upq20, 18): the control loops returning a variable to its band.
- **Cooling-water mechanism recovered** with the right sign: cw_flow:up → cw_out:down (more cooling water,
  cooler outlet) and cw_flow:down → cw_out:up, at lags m and l, 22 fragments, lift 1.7–8.3, bound to the
  entity (reactor and separator each). Not recovered: cw_flow → T (vessel temperature), steam → T,
  underflow → L.
- Target roles: P 141, T 140, cw_out 107, cw_flow 103, underflow_valve 66, feed 42, underflow 7, L 0.

## Recovery (answer key: flowsheet actuator → measurement, role prefix, any lag)

recall 1/10, precision 0.036. Five of the ten keyed pairs (feed valves → feed flows, purge valve → purge)
are between system-wide roles, which are contexts and never targets under the vessel entity, so they are
unrecoverable by construction here; the key should list only pairs whose effect is an entity role. Of the
five recoverable pairs, one (cw_flow → cw_out) is found; cw_flow → T and steam → T plausibly need a
horizon longer than 21 min (thermal response); underflow → L finds no fragments at all.

## Open items raised by this dataset (not rules)

1. The horizon follows event density (3.3). On a busy system it is 21 min, shorter than the plant's thermal
   time scales (correlation times 1–7 h), so slow mechanisms cannot be seen. A horizon tied to the system's
   correlation time rather than to its event rate is the candidate fix.
2. Lag edges below the sampling interval are degenerate (class `s` empty). Edges should respect the sampling
   interval, or be computed on gaps > one sample.
3. Answer keys should name only pairs whose effect is a target role under the chosen entity.
4. Vessel level (L, turning points) is never predicted by anything; whether that is the symbolization or the
   plant is open.
5. Bits per event are high (3.4) because the streams are busy and the vocabulary is 40 types; absolute
   levels are not comparable across datasets, gains are.
