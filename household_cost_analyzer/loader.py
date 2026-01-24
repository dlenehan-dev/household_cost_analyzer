# household_cost_analyzer/loader.py

import csv
from pathlib import Path
from datetime import datetime
from typing import List

from household_cost_analyzer.models import Expense

def load_expenses_from_csv(file_path: Path) -> List[Expense]:
    """
    Load expenses from a CSV file.
    Each row is expected to have: date, category, description, amount
    Returns a list of valid Expense objects.
    """
    expenses: List[Expense] = []

    with file_path.open(mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                expense_date = datetime.strptime(row["date"], "%Y-%m-%d").date()
                amount = float(row["amount"])
                expense = Expense(
                    date=expense_date,
                    category=row["category"],
                    description=row["description"],
                    amount=amount
                )
                if expense.is_valid():
                    expenses.append(expense)
            except Exception:
                # Skip rows with invalid format
                continue

    return expenses
