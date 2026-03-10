import json
from household_cost_analyzer.main import main


def test_json_output(capsys):
    result = main([
        "--csv", "tests/fixtures/sample.csv",
        "--json"
    ])

    captured = capsys.readouterr()

    # CLI should succeed
    assert result == 0

    # Output should be valid JSON
    output = json.loads(captured.out.strip())

    assert "total" in output
    assert isinstance(output["total"], (int, float))