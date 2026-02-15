from pathlib import Path
from household_cost_analyzer.main import main

def test_no_matching_expenses_logs_warning(caplog):
    caplog.set_level("WARNING")

    csv_path = Path(__file__).parent / "fixtures" / "sample.csv"

    result = main([
        "--csv", str(csv_path),
        "--category", "Nonexistent"
    ])

    assert result == 0
    assert "No expenses matched the given filters" in caplog.text
