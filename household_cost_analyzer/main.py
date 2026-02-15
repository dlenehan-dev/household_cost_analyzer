import argparse
import logging
from pathlib import Path
from typing import List, Optional

from household_cost_analyzer.config import load_config
from household_cost_analyzer.loader import load_expenses_from_csv
from household_cost_analyzer.processor import total_spend
from household_cost_analyzer.reporter import report_total_spend


logger = logging.getLogger(__name__)


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="household-cost-analyzer",
        description="Analyze household expenses from a CSV file and report totals.",
    )

    parser.add_argument(
        "--csv",
        required=True,
        help="Path to expenses CSV file (columns: date, category, description, amount)",
    )

    parser.add_argument(
        "--category",
        help="Filter expenses by category (e.g. Food, Utilities)",
    )

    parser.add_argument(
        "--month",
        type=int,
        choices=range(1, 13),
        metavar="1-12",
        help="Filter expenses by month number (1=Jan, 12=Dec)",
    )

    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    # Load config (logging, currency, etc.)
    config = load_config()
    logger.debug("Configuration loaded")

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

    # Apply filters
    if args.category:
        expenses = [e for e in expenses if e.category == args.category]

    if args.month:
        expenses = [e for e in expenses if e.date.month == args.month]

    if not expenses:
        logger.warning("No expenses matched the given filters.")
        return 0

    total = total_spend(expenses)

    report_total_spend(
        total,
        currency_symbol=config.currency_symbol,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
