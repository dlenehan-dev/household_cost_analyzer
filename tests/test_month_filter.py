# tests/test_month_filter.py

import sys
from pathlib import Path
from datetime import date

# Ensure package root is importable (Windows-safe)
repo_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo_root))

from household_cost_analyzer.models import Expense
from household_cost_analyzer.processor import total_spend


def test_month_filtering():
    expenses = [
        Expense(date(2026, 1, 5), "Food", "Lunch", 10),
        Expense(date(2026, 1, 20), "Food", "Dinner", 15),
        Expense(date(2026, 2, 1), "Utilities", "Gas", 30),
    ]

    january_expenses = [
        e for e in expenses if e.date.strftime("%Y-%m") == "2026-01"
    ]

    assert len(january_expenses) == 2
    assert total_spend(january_expenses) == 25
