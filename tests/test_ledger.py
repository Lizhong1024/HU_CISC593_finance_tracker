"""Unit tests for the ledger module."""

from datetime import date

import pytest

from pftracker.ledger import Ledger


def test_add_positive_amount():
    """Test adding an entry with a positive amount."""
    ledger = Ledger()
    entry = ledger.add(amount=100.0, category="Salary")
    assert entry.amount == 100.0
    assert entry.category == "Salary"
    assert entry.dt == date.today()
    assert len(ledger.entries) == 1
    assert ledger.entries[0] == entry


def test_add_negative_amount():
    """Test adding an entry with a negative amount."""
    ledger = Ledger()
    entry = ledger.add(amount=-50.0, category="Food")
    assert entry.amount == -50.0
    assert entry.category == "Food"
    assert entry.dt == date.today()
    assert len(ledger.entries) == 1
    assert ledger.entries[0] == entry


def test_add_with_custom_date():
    """Test adding an entry with a custom date."""
    ledger = Ledger()
    custom_date = date(2025, 5, 27)
    entry = ledger.add(amount=200.0, category="Bonus", dt=custom_date)
    assert entry.amount == 200.0
    assert entry.category == "Bonus"
    assert entry.dt == custom_date
    assert len(ledger.entries) == 1
    assert ledger.entries[0] == entry


def test_add_zero_amount():
    """Test adding an entry with a zero amount raises ValueError."""
    ledger = Ledger()
    with pytest.raises(ValueError, match="Amount cannot be zero."):
        ledger.add(amount=0.0, category="Invalid")
