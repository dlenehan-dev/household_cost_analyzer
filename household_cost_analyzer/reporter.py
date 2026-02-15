"""
Reporting utilities for the Household Cost Analyzer.
"""

def report_total_spend(total,currency_symbol="£"):
    return f"Total spend: {currency_symbol}{total:.2f}"


def report_grouped_spend(title, grouped_data, currency_symbol="£"):
    lines = [title]

    for key, amount in grouped_data.items():
        lines.append(f"- {key}: {currency_symbol}{amount:.2f}")

    return "\n".join(lines)
