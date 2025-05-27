"""Income and Expense Ledger Module."""

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable
from uuid import uuid4


@dataclass(frozen=True)
class Entry:
    id: str  # Unique identifier for the entry
    amount: float  # Positive for income, negative for expenses
    category: str  # Category of the entry (e.g., "Food", "Transport")
    dt: date  # Date of the entry


@dataclass
class Ledger:
    """A ledger to track income and expenses."""

    entries: list[Entry] = field(default_factory=list)

    def add(self, amount: float, category: str, dt: date | None = None) -> Entry:
        """Add a new entry to the ledger."""
        if amount == 0:
            raise ValueError("Amount cannot be zero.")
        e = Entry(
            id=str(uuid4()), amount=amount, category=category, dt=dt or date.today()
        )
        self.entries.append(e)
        return e

    def by_category(self, cat: str) -> Iterable[Entry]:
        """Get all entries in a specific category."""
        return (e for e in self.entries if e.category == cat)

    def net_balance(self) -> float:
        """Calculate the net balance of all entries."""
        return sum(e.amount for e in self.entries)
