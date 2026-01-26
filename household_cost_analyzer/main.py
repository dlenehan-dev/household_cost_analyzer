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


def main() -> None:
    csv_path = Path("data/expenses.csv")

    expenses = load_expenses_from_csv(csv_path)

    if not expenses:
        print("No valid expenses found.")
        return

    total = total_spend(expenses)
    by_category = spend_by_category(expenses)
    by_month = spend_by_month(expenses)

    print(report_total_spend(total))
    print()
    print(report_grouped_spend("Spend by category", by_category))
    print()
    print(report_grouped_spend("Spend by month", by_month))


if __name__ == "__main__":
    main()
