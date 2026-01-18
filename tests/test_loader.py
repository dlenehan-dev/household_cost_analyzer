# tests/test_loader.py

from pathlib import Path
from household_cost_analyzer.loader import load_expenses_from_csv

def test_loader_runs():
    result = load_expenses_from_csv(Path("dummy.csv"))
    assert result == []
