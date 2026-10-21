# Benchmark card — MIT-BIH Polysomnographic Database (dataset 7), v2: 0.25-second samples, method v7, profile v1, seed 0

Run 2026-10-21. Same source and layout as [v1](CARD_physionet_slp_v1.md) (PhysioNet slpdb 1.0.0: 18 nights, 16 men;
beat-annotated ECG, invasive radial-artery pressure, respiration, SO2 in five records; sleep stages and apnea as
regimes). One per-dataset declaration changed, no rule: **0.25-second samples** in place of 1 s. At 1 s a 4-s
breathing wave had acf(1) ≈ 0 and the noise floor (3.2) averaged it away over 8–91 s; at 0.25 s the wave has
acf(1) ≈ 0.7 and every role keeps a noise window of 1–5 samples. The choice stage was remade from scratch.

**Admitted under v7** (section 6): 3.6 days but **19,419 recurrence horizons**, test split 4,855 — the
first dataset admitted on the horizon clause. The period rule finds no cycle on either grid: on the fine grid the
pooled event rate's autocorrelation peaks at 1.5, 3.75 and 4.5 s reach 0.13–0.15 against the 0.2 threshold, 18
subjects breathing at 18 rates (see open item 1).

## Identity and scale

| | v1 (1 s) | v2 (0.25 s) |
| --- | --- | --- |
| Entity | record (2.56 vs 26.1 bits) | **record** (1.50 vs 25.94 bits) |
| Symbolization | HR, SBP, DBP, SO2 turning points; RESP q20/50/80 with 8–91 s noise windows | **all five roles turning points**; noise windows 1 (HR, SBP, DBP, SO2) and 1–5 (RESP) |
| Events / types | 78,687 / 14 | **221,062 / 10** (RESP 149,427: one peak every 4.1 s — the breaths) |
| Lag classes (3.3) | 3.0 / 8.6 / 25.4 s | **1.0 / 4.0 / 15.9 s** (horizon 15.9 s) |
| Candidates → fragments | 396 → 37 (27 used) | 177 → **22 (17 used)**, 32 compositions |
| Nulls (3.8) | circular 0.66, rewire 1.00 | circular 0.85, rewire 1.00 |
| Chains / returns (3.15) | 1 / 0 | **3 / 0** |
| Recovery | 2/5 (HR → SBP, SBP → HR) | 2/5 (**RESP → SBP**, HR → SBP) |

## Headline (bits per event on the test split)

| model | v1 | v2 |
| --- | --- | --- |
| unigram | 4.799 | 3.434 |
| markov-1 / -2 / -3 | 5.475 / 6.181 / 6.775 | 3.718 / 4.068 / 4.435 |
| hawkes-like decay features | 5.284 | 3.559 |
| logistic markov features | 5.362 | 3.373 |
| logistic triviality library (3.11) | 4.813 | 3.328 |
| logistic library | 4.931 | **3.136** |
| logistic unselected contexts | 4.813 | 3.325 |

Gain over triviality **+0.192** bits (v1: −0.118); over the best baseline (logistic Markov, 3.373) +0.237 → claim:
**beats baselines** — the first real dataset outside TEP to do so, and on a library of 22 fragments.

## Reading the result

**The respiratory couplings appear, as physiology says.** `RESP:peak -s-> DBP:trough` (n 1,963, lift 4.5) and
`RESP:peak -s-> SBP:trough` (n 1,638, 4.5): the pressures fall within a second of peak inspiration; the troughs
precede the pressure peaks. `HR:trough -s-> RESP:peak` and `HR:peak -s-> RESP:trough` (n 2,628 / 3,233): the heart
slows into inspiration's peak and speeds into expiration's — respiratory sinus arrhythmia, written with HR as the
*prior*: at 0.25 s the heart's turning point leads the breath's by under a second, so the library spells it
HR → RESP while the key spells it RESP → HR, and recovery counts it as not found. The pressure-wave couplings
of v1 are still there at the medium lag (`HR:peak -m-> SBP:peak`, `DBP:peak -s-> SBP:peak`).

**No baroreflex return.** SBP → HR is not in the library at any lag, so no `SBP → HR → SBP` chain can form; the
three chains admitted are `HR → RESP → DBP/SBP`, the breath between the heart and the pressure. The reflex's
own time scale (one to two beats, 0.8–2 s) now sits inside the first lag class (≤ 1.0 s) and the second — it is
not hidden by the clock any more; it is not found as a pair. Two readings, both for the open items: the sleeping
baroreflex of apnea patients is weak, and a beat-indexed declaration (time in beats) would test the reflex in
its own clock.

**Every Markov model is still worse than the unigram**, and the library beats both: the structure is in the
cross-role couplings at specific lags, not in the sequence of symbols.

## Open items raised by this card (not rules)

1. **The fine-grid period on a population.** The pooled rate of 18 subjects has no autocorrelation peak above
   0.2 at any lag although each subject breathes regularly; a per-entity autocorrelation (the median period over
   entities) would see it. The admission clause did not need it here (horizons carried), but the cycle null did.
2. **Direction by sub-second lead.** HR → RESP at lag s where physiology writes RESP → HR: when two coupled
   oscillators are sampled finely, the one whose turning point comes first is the prior. The answer key's
   direction is the causal one; the library's is the temporal one. Recovery should perhaps count either.
3. **The baroreflex as a pair is absent**, not hidden: the next check is a beat-indexed declaration.

## v8 regeneration (2026-10-21)

Unchanged (22 fragments, 3 chains, 0 returns; 3.136, beats baselines; admitted by horizons). No returns, so no
loop rule has anything to resolve. As a receiver the dataset is `short` (2.7 observed days ≈ 10 H of training
against the 200 H the curve wants) and its cells are so flagged.
