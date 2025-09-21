"""
Test suite for created_at validation in the User entity.

Verifies that the User class enforces strict rules for the created_at timestamp:
- Must be a timezone-aware datetime (UTC)
- Cannot be in the future
- Rejects invalid types (None, strings, naive datetimes, etc.)
"""

from datetime import datetime, timezone, date, timedelta
import pytest

from user_management.domain.exceptions import InvalidCreatedAtError
from tests.helpers import create_valid_user


def test_user_creation_fails_when_created_at_is_not_a_datetime():
    """Should reject non-datetime values."""
    invalid_values = [None, "", "2024-01-01", 123, {}, [], True, b"raw"]

    for value in invalid_values:
        with pytest.raises(InvalidCreatedAtError):
            create_valid_user(created_at=value)


def test_user_creation_fails_when_created_at_has_no_timezone():
    """Should reject naive datetime (no tzinfo)."""
    naive_dt = datetime(2024, 1, 1, 10, 0, 0)  # No timezone
    with pytest.raises(InvalidCreatedAtError):
        create_valid_user(created_at=naive_dt)


def test_user_creation_fails_when_created_at_is_not_in_utc():
    """Should reject datetime with non-UTC timezone."""
    non_utc = datetime(2024, 1, 1, 10, 0, 0, tzinfo=timezone(timedelta(hours=-3)))  # UTC-3
    with pytest.raises(InvalidCreatedAtError):
        create_valid_user(created_at=non_utc)


def test_user_creation_fails_when_created_at_is_in_the_future():
    """Should reject future dates."""
    future_dt = datetime(3000, 1, 1, tzinfo=timezone.utc)
    with pytest.raises(InvalidCreatedAtError):
        create_valid_user(created_at=future_dt)


def test_user_creation_succeeds_with_valid_created_at():
    """Should accept a valid UTC-aware datetime in the past or present."""
    valid_dt = datetime(2024, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
    user = create_valid_user(created_at=valid_dt)
    assert user.created_at == valid_dt