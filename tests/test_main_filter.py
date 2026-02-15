# tests/test_main_filter.py

import sys
from pathlib import Path
from datetime import date

# Add the package root to sys.path (ensures imports work on Windows)
repo_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo_root))

from household_cost_analyzer.models import Expense
from household_cost_analyzer.processor import total_spend
import pytest

def test_category_filtering():
    # Sample expenses
    expenses = [
        Expense(date(2026, 1, 1), "Food", "Lunch", 10),
        Expense(date(2026, 1, 2), "Food", "Dinner", 15),
        Expense(date(2026, 1, 3), "Utilities", "Gas", 30),
    ]

    # Filter for Food
    filtered = [e for e in expenses if e.category == "Food"]

    # Assert only Food expenses remain
    assert len(filtered) == 2
    assert total_spend(filtered) == 25
