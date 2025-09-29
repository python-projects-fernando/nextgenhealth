"""
Test suite for date_of_birth validation in the User entity.

This module verifies that the User class enforces strict validation of the 'date_of_birth' field,
ensuring it conforms to domain rules:
- Must be a date object (not string, int, etc.)
- Must not be in the future
- Must not be unrealistically far in the past (e.g., before 1800)
- Only valid date instances are accepted

The tests use create_valid_user() from test helpers to minimize boilerplate.
Aligned with DDD (fail-fast) and TDD principles.
"""

from datetime import date
import pytest

from tests.helpers.domain import create_valid_user
from user_management.domain.exceptions import InvalidDateOfBirthError


def test_user_creation_fails_when_date_of_birth_is_not_valid():
    """
    Verifies User instantiation fails when date_of_birth is invalid.

    The domain requires date_of_birth to be a valid date object, not in the future,
    and not unreasonably old. Inputs such as None, strings, integers, or future dates
    should raise InvalidDateOfBirthError.

    This test ensures consistent rejection of malformed or impossible birth dates.
    """
    invalid_dates_of_birth = [
        date(2050, 1, 1),           # Future date
        date(1800, 1, 1),           # Too far in the past
        None,
        "",
        "not-a-date",
        123,
        {},
        [],
        True,
        b"raw-bytes"
    ]

    for dob in invalid_dates_of_birth:
        with pytest.raises(InvalidDateOfBirthError):
            create_valid_user(date_of_birth=dob)


def test_user_creation_succeeds_with_valid_date_of_birth():
    """
    Verifies User can be created with a valid date_of_birth.

    Confirms that providing a realistic and correctly typed date object results
    in successful instantiation and that the value is correctly assigned and preserved.

    This test covers the happy path for date_of_birth validation.
    """
    valid_dob = date(1970, 3, 25)
    user = create_valid_user(date_of_birth=valid_dob)
    assert user.date_of_birth == valid_dob