"""
Test suite for updated_at validation in the User entity.

Verifies that the User class enforces strict rules for the updated_at timestamp:
- Must be a timezone-aware datetime (UTC)
- Cannot be in the future
- Rejects invalid types (None, strings, naive datetimes, etc.)
"""

from datetime import datetime, timezone, date, timedelta
import pytest

from user_management.domain.exceptions import InvalidUpdatedAtError
from tests.helpers import create_valid_user


def test_user_creation_fails_when_updated_at_is_not_a_datetime():
    """
    Verifies User instantiation fails when updated_at is not a datetime object.

    The domain requires updated_at to be a datetime instance.
    Inputs such as None, strings, integers, or other types should raise InvalidUpdatedAtError.
    """
    invalid_values = [None, "", "2024-01-01", 123, {}, [], True, b"raw"]

    for value in invalid_values:
        with pytest.raises(InvalidUpdatedAtError):
            create_valid_user(updated_at=value)


def test_user_creation_fails_when_updated_at_has_no_timezone():
    """
    Verifies User instantiation fails when updated_at is a naive datetime.

    The domain requires all timestamps to be timezone-aware.
    A datetime without tzinfo should raise InvalidUpdatedAtError.
    """
    naive_dt = datetime(2024, 1, 1, 10, 0, 0)  # No timezone
    with pytest.raises(InvalidUpdatedAtError):
        create_valid_user(updated_at=naive_dt)


def test_user_creation_fails_when_updated_at_is_not_in_utc():
    """
    Verifies User instantiation fails when updated_at uses a non-UTC timezone.

    The system standardizes on UTC for consistency and auditability.
    Any datetime with a non-UTC timezone should be rejected.
    """
    non_utc = datetime(2024, 1, 1, 10, 0, 0, tzinfo=timezone(timedelta(hours=-3)))  # UTC-3
    with pytest.raises(InvalidUpdatedAtError):
        create_valid_user(updated_at=non_utc)


def test_user_creation_fails_when_updated_at_is_in_the_future():
    """
    Verifies User instantiation fails when updated_at is in the future.

    Timestamps must represent real-world time. Future dates are invalid
    and should raise InvalidUpdatedAtError.
    """
    future_dt = datetime(3000, 1, 1, tzinfo=timezone.utc)
    with pytest.raises(InvalidUpdatedAtError):
        create_valid_user(updated_at=future_dt)


def test_user_creation_succeeds_with_valid_updated_at():
    """
    Verifies User can be created with a valid UTC-aware datetime.

    Confirms that a properly formatted, realistic updated_at value is accepted
    and correctly assigned to the User instance.
    """
    valid_dt = datetime(2024, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
    user = create_valid_user(updated_at=valid_dt)
    assert user.updated_at == valid_dt