from household_cost_analyzer.reporter import report_total_spend, report_grouped_spend


def test_report_total_spend(capsys):
    report_total_spend(123.456)

    captured = capsys.readouterr()

    assert captured.out.strip() == "Total spend: £123.46"


def test_report_grouped_spend(capsys):
    data = {
        "Food": 25.0,
        "Utilities": 30.0,
    }

    report_grouped_spend("Spend by category", data)

    captured = capsys.readouterr()

    expected = (
        "Spend by category\n"
        "- Food: £25.00\n"
        "- Utilities: £30.00"
    )

    assert captured.out.strip() == expected