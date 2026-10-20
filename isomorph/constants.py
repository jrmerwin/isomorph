"""
Fixed constants of the method (METHOD.md section 7). Nothing here is tuned per
dataset. Two profiles exist: "v1" is the method; "legacy" reproduces the
session runs recorded in docs/RESULTS_session_2026-10-18.md (fixed lag classes
in minutes, a 30/30 train/test split with a 20/10 proposal/confirmation split
inside the training days) and exists only to prove the reorganised code is
faithful to those numbers.
"""
CARD_RULES_VERSION = 2   # the version at which the per-dataset rules (3.1-3.11) last changed; cards and cached state from it stay valid
METHOD_VERSION = 5   # v5: structural prefix (place) and dimension suffix in alignment and control (3.14, 3.12); v4: grammar — parts of speech, tagged shapes, tag-constrained alignment (3.14, 3.12); v3: transfer cells net of the random-mapping control (3.12); v2: horizon by recurrence time, geometric lag bands (3.3)

LIFT_MIN = 1.5                 # proposal and confirmation
N_NULL_DRAWS = 19              # per null; pass = observed count exceeds every draw
CONFIRM_MIN_COUNT = 3
DEBOUNCE = 3                   # samples
LOGISTIC_C = 0.5
ALIGN_RESTARTS = 20
ALIGN_ITERS = 30
N_ANCHORS = 2
ALIGN_UNMATCHED_PENALTY = 3.0     # role-level alignment (v5): penalty, in units of the typical signature distance, for leaving a role unmatched
LEARNING_CURVE_DAYS = (1, 2, 3, 5, 10, 20, None)   # None = all training days
N_CONTROL_MAPPINGS = 3                              # permuted-mapping controls per cell (3.12, v3)

# parts of speech (3.14, v4): dimensionless, relative to the system's horizon
POS_CONST_FRAC = 0.9      # share of zero increments at or above which a series is a schedule/setpoint (SET)
POS_FAST = 0.1            # correlation time / horizon below which a series is FAST
POS_SLOW = 1.0            # ... above which it is SLOW
POS_SAT_SHARE = 0.05      # share of samples at the min or max (1% of range) at or above which a series saturates (S)
CLAIM_MIN_GAIN_BITS = 0.10
SUPERFAMILY_RATIO = 2.0
SUPERFAMILY_MIN_MEMBERS = 3
PERIOD_ACF_THRESHOLD = 0.2
PERIOD_MIN_PROMINENCE = 0.1       # a period peak must rise this far above the acf minimum before it (3.4)
PERIOD_HARMONIC_RATIO = 0.8       # the period is the shortest prominent peak within this ratio of the strongest (3.4)
HORIZON_QUANTILE = 0.95           # v1 rule only (profile lag_mode 'terciles')
FLOOR_PAIRS = 50
FAITHFULNESS_MAX_RESIDUAL = 0.5   # a symbolization must reconstruct the (denoised) series to within half its std
NOISE_FRACTION = 0.05             # white noise left after denoising <= 5% of the signal variance (3.2 noise floor)
CALIBRATION_TOLERANCE_BITS = 0.02

PROFILES = {
    "v1": dict(
        splits=(0.50, 0.25, 0.25),      # proposal / confirmation / test, chronological
        lag_mode="recurrence",          # v2: horizon = median type recurrence time; classes = context-gap terciles (3.3)
        min_count_mode="fixed",         # admission is per pair, by the nulls; the floor is reported, not applied (changelog v1)
        min_count=3,
    ),
    "legacy": dict(
        splits=(20 / 60, 10 / 60, 30 / 60),
        lag_mode="fixed_minutes",       # s < 5, m < 30, l < 90 (horizon 90)
        lag_edges=(5.0, 30.0, 90.0),
        min_count_mode="fixed",
        min_count=5,
    ),
}
