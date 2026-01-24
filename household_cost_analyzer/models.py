# household_cost_analyzer/models.py

from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Expense:
    """
    Represents a single household expense record.
    """

    date: date
    category: str
    description: str
    amount: float

    def is_valid(self) -> bool:
        """
        Returns True if the expense is valid:
        - category and description are not empty
        - amount is positive
        - date is not in the future
        """
        if not self.category.strip() or not self.description.strip():
            return False
        if self.amount <= 0:
            return False
        if self.date > date.today():
            return False
        return True
