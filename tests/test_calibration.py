"""Calibration gate: both buildings under both profiles must match the reference within tolerance.
Run: python -m pytest tests  (about 90 s)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from isomorph.collect.calibrate import calibrate


def test_calibration_gates():
    assert calibrate(record=False, log=lambda *a, **k: None)
