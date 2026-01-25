"""
Reporting utilities for the Household Cost Analyzer.
"""

def report_total_spend(total):
    return f"Total spend: £{total:.2f}"


def report_grouped_spend(title, grouped_data):
    lines = [title]

    for key, amount in grouped_data.items():
        lines.append(f"- {key}: £{amount:.2f}")

    return "\n".join(lines)
