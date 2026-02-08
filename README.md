# Household Cost Analyzer

A command-line Python application that analyzes household expenses from a CSV file and produces summary reports.

This project was built as part of a structured learning journey from COBOL to Python, with a focus on:
- clean code
- testability
- packaging best practices
- real-world CLI usage

---

## Features

- Load expenses from a CSV file
- Validate input data (dates, amounts, required fields)
- Calculate:
  - total spend
  - spend by category
  - spend by month
- Configurable logging via TOML configuration
- Fully tested with pytest
- Installable as a command-line tool

---

## Example CSV Format

```csv
date,category,description,amount
2025-01-15,Food,Lunch,12.50
2025-01-20,Utilities,Electricity,45.00

Installation (local development)
python -m venv venv
venv\Scripts\activate
pip install -e .

Usage
household-cost-analyzer --csv data/expenses.csv

Project Structure
household_cost_analyzer/
├── household_cost_analyzer/
│   ├── loader.py
│   ├── processor.py
│   ├── reporter.py
│   ├── models.py
│   ├── config.py
│   └── main.py
├── tests/
├── pyproject.toml
├── config.toml
└── README.md

Learning Goals

This project demonstrates:

Python packaging with pyproject.toml

Command-line interfaces with argparse

Data validation and error handling

Logging configuration

Automated testing with pytest

Author

Deirdre Lenehan