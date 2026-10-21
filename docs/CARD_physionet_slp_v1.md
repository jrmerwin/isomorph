# Benchmark card — MIT-BIH Polysomnographic Database (dataset 7), method v6, profile v1, seed 0

Run 2026-10-21. Source: PhysioNet slpdb 1.0.0 (Ichimaru & Moody 1999), https://physionet.org/content/slpdb/1.0.0/ —
18 overnight records of 16 men under evaluation for sleep apnea, 250 Hz: ECG with beat annotations, invasive
radial-artery blood pressure, one or two respiration channels (nasal thermistor, chest or abdominal effort),
EEG, and in five records SO2; sleep stages and apnea events annotated every 30 s. 85.6 h in all. The
physiological member of the Rosetta set: the baroreflex — pressure → heart rate → pressure — as a return in flesh.

**Not admitted under the rule as written.** 3.6 days, and the period rule finds no cycle. Carried as a
*provisional* leaf of the lineage, flagged, so that the four-leaf tree can be looked at; the decision to keep it
there is a human one (see the reading below on why the period rule is blind here).

## Declarations

- **Resolution: 1-second samples.** Heart rate from the beat annotations (60 / RR), systolic and diastolic
  pressure as the maximum and minimum of the arterial waveform between successive beats, all interpolated
  linearly to the 1-s grid (beat-to-beat resampling; a grid point more than 2 s from a beat is missing);
  respiration is the 1-s mean of the first available waveform (nasal preferred; uncalibrated, dimensionless);
  SO2 the 1-s mean where recorded. Implausible beats (RR outside 0.3–2 s) and pressures (outside 40–250 mmHg)
  are missing. EEG, EOG, EMG and SV are left out: not cardiorespiratory regulator quantities.
- **Time axis compressed**: the 18 records (different nights) concatenated with each of the 17 boundaries a gap;
  each record observed on its own stretch only.
- **Sleep stages and apnea / arousal events** (3,624 runs) are regime annotations in the sidecar, not events.
- Fetched from PhysioNet's S3 mirror (the web host throttles to ~5 KB/s); read with `wfdb`.

## Identity and scale

| | |
| --- | --- |
| Entity | **record** (18 nights as units with roles HR, SBP, DBP, RESP, SO2 where recorded), chosen by 3.1: 2.559 vs 26.107 bits/event Markov-only for a single system |
| Symbolization (3.2) | HR, SBP, DBP, SO2: turning points (noise windows 1–3 s: the beat-level series are not oversmoothed); RESP: q20/50/80, the only faithful scheme — with noise windows of 8–91 s, because a 4-s breathing wave sampled at 1 s has acf(1) ≈ 0 and the noise floor (3.2) reads it as white noise and averages it away; three records' respiration has no signal at all under the rule |
| Events | 78,687 in 85.6 h (22,053/day); 14 types; test split 24,196 events |
| Lag classes (3.3) | 3.0 s / 8.6 s / 25.4 s (recurrence horizon 25 s) |
| Period (3.4) | none — the rule's resolution is 0.1% of the span (5 min here); the data's cycles are 4 s (breathing, ~77,000 of them), ~10 s (Mayer waves) and ~90 min (sleep), none visible at 5-min bins |
| Signal floor (3.5) | 322 (descriptive) |
| Nulls (3.8) | circular (gate) survival 0.66; rewire 1.00 (every fragment binds: 18 subjects, nothing system-wide) |
| Discovery | 396 candidates → **37 validated fragments** (27 used), 42 compositions kept; chatty share 0.16 |
| Syntax (3.15) | 114 chain candidates → 9 with conditional lift → 9 above the null → 1 admitted (a RESP staircase), 0 used; **0 returns** |

## Headline (bits per event on the test split)

| model | all |
| --- | --- |
| unigram | **4.799** |
| markov-1 | 5.475 |
| markov-2 | 6.181 |
| markov-3 | 6.775 |
| hawkes-like decay features | 5.284 |
| logistic markov features | 5.362 |
| logistic triviality library (3.11) | 4.813 |
| logistic library | 4.931 |
| logistic unselected contexts | 4.813 |

Gain over triviality **−0.118** bits; over the best baseline (the unigram, 4.799) −0.132 → claim: **no gain**.

## Reading the result

**What is found is the slow-wave coupling, not the baroreflex.** Recovery 2/5: HR → SBP (5 fragments) and
SBP → HR (3) are in the library, as `HR:peak -s-> DBP:peak` (n 1,472, lift 4.2), `DBP:peak -s-> SBP:peak`
(n 1,107, lift 4.9) and their troughs — the heart-rate wave leads the pressure wave by a few seconds. These are
turning points of series denoised over their correlation time, so they are the ~10-s Mayer waves and slower
drifts, about one peak every 35 s per role. The baroreflex itself closes within one or two beats, below the
first lag class (3 s), and the respiratory couplings are not found because respiration was averaged away.
No return: the path `SBP:peak → HR:trough → SBP:trough` does not pass the conditional-lift gate.

**Every sequence model is worse than the unigram.** Markov-1 to -3 lose 0.7–2.0 bits to the unigram: at this
symbolization the event stream of 18 subjects is nearly memoryless, and the Markov features overfit the record
they were trained on. The library and the triviality baseline sit at the unigram.

**This is a card about the instrument's time scales, not about the physiology.** Three rules meet a signal
faster than anything the collection has seen: the period rule's resolution floor hides a 4-s cycle; the noise
floor treats a 4-s oscillation at 1-s sampling as noise; the recurrence horizon (25 s) and the first lag class
(3 s) sit above the reflex's one or two beats. Each is a stated rule applied unchanged — which is the point of
the method — and each is now an open item with a number attached.

## Open items raised by this dataset (not rules)

1. **The period rule's resolution floor** (3.4): bins of 0.1% of the span cannot see a cycle shorter than 0.1%
   of the span. A multi-scale search (bins at the sampling interval up to the span) would find breathing here
   and the daily cycle in the buildings alike; the admission clause depends on it.
2. **Envelope symbolization for fast oscillations** (3.2): the HAI item again, now decisive — respiration is the
   driver of both reflexes and the noise floor erased it. Breath-by-breath (rate, amplitude) is the envelope.
3. **Sub-sample mechanisms**: the baroreflex acts within 1–2 beats; a beat-indexed declaration (events on the
   beat grid, time in beats) would put it inside the first lag class — a per-dataset declaration, like HAI's
   1-minute means, and so a card choice, not a rule.
4. The 18 subjects give a rewire survival of 1.0: nothing is system-wide, so `COMMON` never occurs and every
   role is `LOCAL`; a subject-level population is a different shape of dataset from a plant, and the place prefix
   says so.
