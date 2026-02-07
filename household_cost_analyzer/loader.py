# household_cost_analyzer/loader.py

import csv
import logging
from pathlib import Path
from datetime import datetime
from typing import List

from household_cost_analyzer.models import Expense


def load_expenses_from_csv(file_path: Path) -> List[Expense]:
    """
    Load expenses from a CSV file.
    Each row is expected to have: date, category, description, amount.
    Returns a list of valid Expense objects.
    """
    expenses: List[Expense] = []

    with file_path.open(mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        # Start at 2 because line 1 is the header
        for line_number, row in enumerate(reader, start=2):
            try:
                expense_date = datetime.strptime(
                    row["date"], "%Y-%m-%d"
                ).date()
                amount = float(row["amount"])

                expense = Expense(
                    date=expense_date,
                    category=row["category"],
                    description=row["description"],
                    amount=amount,
                )

                if expense.is_valid():
                    expenses.append(expense)
                else:
                    logging.warning(
                        "Line %d: invalid expense data (failed validation): %s",
                        line_number,
                        row,
                    )

            except KeyError as exc:
                logging.warning(
                    "Line %d: missing column %s (%s)",
                    line_number,
                    exc,
                    row,
                )

            except ValueError as exc:
                logging.warning(
                    "Line %d: invalid data format (%s): %s",
                    line_number,
                    exc,
                    row,
                )

    return expenses
