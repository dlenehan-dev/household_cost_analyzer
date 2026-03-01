# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog.
This project follows semantic versioning.

[Unreleased]

---

## [0.2.1] – 2026-03-01
### Added
- CLI option `--month` to filter expenses by YYYY-MM
- Unit test for month filtering
- CLI test for no matching expenses

### Fixed
- Config loading error (NameError: Config not defined)
- CLI exit code consistency when CSV file not found
- Path handling in CLI tests

### Improved
- Logging behavior for no-result scenarios
- General CLI polish and stability

---

## [0.2.0] – 2026-02-15
### Added
- CLI option `--category` to filter expenses by category
- Unit test for category filtering

---

## [0.1.1] – 2026-02-07
### Added
- CHANGELOG.md

### Changed
- Improved .gitignore to exclude build artifacts and logs
- Minor documentation polish

---

## [0.1.0] – 2026-02-01
### Added
- Initial household cost analyzer implementation
- CSV loading and validation
- Expense aggregation by category and month
- Command-line interface
- Pytest test suite