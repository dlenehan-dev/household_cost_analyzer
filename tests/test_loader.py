from pathlib import Path
from datetime import date, timedelta

import pytest

from household_cost_analyzer.loader import load_expenses_from_csv
from household_cost_analyzer.models import Expense


def write_csv(path: Path, content: str) -> None:
    """Helper function to write CSV content to a file."""
    path.write_text(content, encoding="utf-8")


def test_load_expenses_from_csv_valid_row(tmp_path: Path):
    past_date = date.today() - timedelta(days=1)

    csv_file = tmp_path / "expenses.csv"
    write_csv(
        csv_file,
        f"""date,category,description,amount
{past_date},Food,Lunch,12.50
"""
    )

    expenses = load_expenses_from_csv(csv_file)

    assert expenses == [
        Expense(
            date=past_date,
            category="Food",
            description="Lunch",
            amount=12.50,
        )
    ]


def test_load_expenses_from_csv_ignores_future_dates(tmp_path: Path):
    future_date = date.today() + timedelta(days=1)

    csv_file = tmp_path / "expenses.csv"
    write_csv(
        csv_file,
        f"""date,category,description,amount
{future_date},Utilities,Future bill,100
"""
    )

    expenses = load_expenses_from_csv(csv_file)

    assert expenses == []


def test_load_expenses_from_csv_negative_amount(tmp_path: Path):
    past_date = date.today() - timedelta(days=1)

    csv_file = tmp_path / "expenses.csv"
    write_csv(
        csv_file,
        f"""date,category,description,amount
{past_date},Food,Lunch,-5
"""
    )

    expenses = load_expenses_from_csv(csv_file)

    assert expenses == []


def test_load_expenses_from_csv_empty_fields(tmp_path: Path):
    past_date = date.today() - timedelta(days=1)

    csv_file = tmp_path / "expenses.csv"
    write_csv(
        csv_file,
        f"""date,category,description,amount
{past_date},,Lunch,10
{past_date},Food,,10
"""
    )

    expenses = load_expenses_from_csv(csv_file)

    assert expenses == []


def test_load_expenses_from_csv_invalid_date_format(tmp_path: Path):
    csv_file = tmp_path / "expenses.csv"
    write_csv(
        csv_file,
        """date,category,description,amount
01-01-2024,Food,Lunch,10
"""
    )

    expenses = load_expenses_from_csv(csv_file)

    assert expenses == []


def test_load_expenses_from_csv_mixed_valid_and_invalid(tmp_path: Path):
    past_date = date.today() - timedelta(days=1)
    future_date = date.today() + timedelta(days=1)

    csv_file = tmp_path / "expenses.csv"
    write_csv(
        csv_file,
        f"""date,category,description,amount
{future_date},Utilities,Future bill,100
{past_date},Food,Lunch,10
{past_date},Travel,,20
"""
    )

    expenses = load_expenses_from_csv(csv_file)

    assert expenses == [
        Expense(
            date=past_date,
            category="Food",
            description="Lunch",
            amount=10.0,
        )
    ]


def test_load_expenses_from_csv_missing_file(tmp_path: Path):
    missing_file = tmp_path / "does_not_exist.csv"

    with pytest.raises(FileNotFoundError):
        load_expenses_from_csv(missing_file)
