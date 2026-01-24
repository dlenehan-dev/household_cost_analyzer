from datetime import date

from household_cost_analyzer.models import Expense
from household_cost_analyzer.processor import (
    total_spend,
    spend_by_category,
    spend_by_month,
)


def test_total_spend():
    expenses = [
        Expense(date(2025, 1, 1), "Food", "Lunch", 10),
        Expense(date(2025, 1, 2), "Food", "Dinner", 15),
        Expense(date(2025, 1, 3), "Utilities", "Gas", 30),
    ]

    assert total_spend(expenses) == 55


def test_spend_by_category():
    expenses = [
        Expense(date(2025, 1, 1), "Food", "Lunch", 10),
        Expense(date(2025, 1, 2), "Food", "Dinner", 15),
        Expense(date(2025, 1, 3), "Utilities", "Gas", 30),
    ]

    result = spend_by_category(expenses)

    assert result == {
        "Food": 25,
        "Utilities": 30,
    }

def test_spend_by_month():
    expenses = [
        Expense(date(2025, 1, 15), "Food", "Lunch", 10),
        Expense(date(2025, 1, 20), "Food", "Dinner", 15),
        Expense(date(2025, 2, 1), "Utilities", "Gas", 30),
    ]

    result = spend_by_month(expenses)

    assert result == {
        "2025-01": 25,
        "2025-02": 30,
    }
