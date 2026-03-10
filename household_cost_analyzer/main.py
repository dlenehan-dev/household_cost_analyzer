import argparse
import logging
from pathlib import Path
from typing import List, Optional

from household_cost_analyzer.config import load_config
from household_cost_analyzer.loader import load_expenses_from_csv
from household_cost_analyzer.processor import total_spend, spend_by_category, spend_by_month
from household_cost_analyzer.reporter import report_total_spend, report_grouped_spend

logger = logging.getLogger(__name__)


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="household-cost-analyzer",
        description="Analyze household expenses from a CSV file and report totals.",
    )

    parser.add_argument("--csv", required=True, help="Path to expenses CSV file")
    parser.add_argument("--category", help="Filter expenses by category (e.g. Food, Utilities)")
    parser.add_argument("--month", type=int, choices=range(1, 13), metavar="1-12", help="Filter by month number")
    parser.add_argument("--json", action="store_true", help="Output total as JSON")

    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    config = load_config()

    logging.basicConfig(
        level=getattr(logging, config.logging.get("level", "INFO")),
        format="%(levelname)s: %(message)s",
    )

    args = parse_args(argv)
    csv_path = Path(args.csv)

    try:
        expenses = load_expenses_from_csv(csv_path)
    except FileNotFoundError:
        logger.error("CSV file not found: %s", csv_path)
        return 1
    except ValueError as exc:
        logger.error("Failed to parse CSV: %s", exc)
        return 1

    # Apply category filter
    if args.category:
        expenses = [e for e in expenses if e.category == args.category]

    # Apply month filter
    if args.month:
        expenses = [e for e in expenses if e.date.month == args.month]

    if not expenses:
        logger.warning("No expenses matched the given filters.")
        return 0

    # Compute totals
    total = total_spend(expenses)
    by_category = spend_by_category(expenses)
    by_month = spend_by_month(expenses)

    # Report
    report_total_spend(total, currency_symbol=config.currency_symbol, as_json=args.json)
    if not args.json:
        print()
        report_grouped_spend("Spend by category", by_category, currency_symbol=config.currency_symbol)
        print()
        report_grouped_spend("Spend by month", by_month, currency_symbol=config.currency_symbol)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())