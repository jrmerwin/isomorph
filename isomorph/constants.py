"""
Fixed constants of the method (METHOD.md section 7). Nothing here is tuned per
dataset. Two profiles exist: "v1" is the method; "legacy" reproduces the
session runs recorded in docs/RESULTS_session_2026-10-18.md (fixed lag classes
in minutes, a 30/30 train/test split with a 20/10 proposal/confirmation split
inside the training days) and exists only to prove the reorganised code is
faithful to those numbers.
"""
METHOD_VERSION = 1

LIFT_MIN = 1.5                 # proposal and confirmation
N_NULL_DRAWS = 19              # per null; pass = observed count exceeds every draw
CONFIRM_MIN_COUNT = 3
DEBOUNCE = 3                   # samples
LOGISTIC_C = 0.5
ALIGN_RESTARTS = 20
ALIGN_ITERS = 30
N_ANCHORS = 2
LEARNING_CURVE_DAYS = (1, 2, 3, 5, 10, 20, None)   # None = all training days
CLAIM_MIN_GAIN_BITS = 0.10
SUPERFAMILY_RATIO = 2.0
SUPERFAMILY_MIN_MEMBERS = 3
PERIOD_ACF_THRESHOLD = 0.2
HORIZON_QUANTILE = 0.95
FLOOR_PAIRS = 50
CALIBRATION_TOLERANCE_BITS = 0.02

PROFILES = {
    "v1": dict(
        splits=(0.50, 0.25, 0.25),      # proposal / confirmation / test, chronological
        lag_mode="terciles",            # lag classes from the proposal split's gap distribution
        min_count_mode="floor",         # candidate admission by the signal floor
        min_count=5,                    # used only until the floor is implemented for a dataset
    ),
    "legacy": dict(
        splits=(20 / 60, 10 / 60, 30 / 60),
        lag_mode="fixed_minutes",       # s < 5, m < 30, l < 90 (horizon 90)
        lag_edges=(5.0, 30.0, 90.0),
        min_count_mode="fixed",
        min_count=5,
    ),
}
