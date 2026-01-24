from collections import defaultdict
from typing import List, Dict

from household_cost_analyzer.models import Expense


def total_spend(expenses: List[Expense]) -> float:
    """Return the total amount spent."""
    return sum(expense.amount for expense in expenses)


def spend_by_category(expenses: List[Expense]) -> Dict[str, float]:
    """Return total spend grouped by category."""
    totals: Dict[str, float] = defaultdict(float)

    for expense in expenses:
        totals[expense.category] += expense.amount

    return dict(totals)


def spend_by_month(expenses: List[Expense]) -> Dict[str, float]:
    """Return total spend grouped by YYYY-MM."""
    totals: Dict[str, float] = defaultdict(float)

    for expense in expenses:
        month_key = expense.date.strftime("%Y-%m")
        totals[month_key] += expense.amount

    return dict(totals)
