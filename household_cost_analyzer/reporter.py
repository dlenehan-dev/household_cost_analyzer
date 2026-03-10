# household_cost_analyzer/reporter.py
import json
from typing import Dict


def report_total_spend(total: float, currency_symbol: str = "£", as_json: bool = False) -> None:
    """
    Print total spend to console or output JSON if as_json is True.

    Args:
        total: total spend amount
        currency_symbol: symbol to display in human-readable output
        as_json: if True, print JSON {"total": ...}
    """
    if as_json:
        print(json.dumps({"total": total}))
    else:
        print(f"Total spend: {currency_symbol}{total:.2f}")


def report_grouped_spend(title: str, grouped_data: Dict[str, float], currency_symbol: str = "£", as_json: bool = False) -> None:
    """
    Print grouped spend to console or JSON if as_json is True.
    
    Args:
        title: heading for human-readable report
        grouped_data: dictionary of key -> amount
        currency_symbol: symbol for human-readable output
        as_json: if True, print JSON
    """
    if as_json:
        print(json.dumps(grouped_data))
    else:
        print(title)
        for key, amount in grouped_data.items():
            print(f"- {key}: {currency_symbol}{amount:.2f}")