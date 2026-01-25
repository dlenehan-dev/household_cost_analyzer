from household_cost_analyzer.reporter import (
    report_total_spend,
    report_grouped_spend,
)

def test_report_total_spend():
    result = report_total_spend(123.456)
    assert result == "Total spend: £123.46"


def test_report_grouped_spend():
    data = {
        "Food": 25.0,
        "Utilities": 30.0,
    }

    result = report_grouped_spend("Spend by category", data)

    expected = (
        "Spend by category\n"
        "- Food: £25.00\n"
        "- Utilities: £30.00"
    )

    assert result == expected
