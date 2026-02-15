# household_cost_analyzer/main.py

import argparse
import logging
from pathlib import Path

from household_cost_analyzer.loader import load_expenses_from_csv
from household_cost_analyzer.processor import (
    total_spend,
    spend_by_category,
    spend_by_month,
)
from household_cost_analyzer.reporter import (
    report_total_spend,
    report_grouped_spend,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Household Cost Analyzer"
    )

    parser.add_argument(
        "--csv",
        type=Path,
        required=True,
        help="Path to expenses CSV file",
    )

    # NEW: Optional category filter
    parser.add_argument(
        "--category",
        type=str,
        help="Filter expenses by category (optional)",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    csv_path = args.csv

    expenses = load_expenses_from_csv(csv_path)

    if not expenses:
        logging.warning("No valid expenses found.")
        return

    # NEW: Apply category filter if provided
    if args.category:
        filtered_expenses = [e for e in expenses if e.category == args.category]
        if not filtered_expenses:
            logging.warning(f"No expenses found for category '{args.category}'.")
            return
        expenses = filtered_expenses

    total = total_spend(expenses)
    by_category = spend_by_category(expenses)
    by_month = spend_by_month(expenses)

    logging.info(report_total_spend(total))
    logging.info("")
    logging.info(report_grouped_spend("Spend by category", by_category))
    logging.info("")
    logging.info(report_grouped_spend("Spend by month", by_month))


if __name__ == "__main__":
    main()
