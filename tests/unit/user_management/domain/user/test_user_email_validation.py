"""
Test suite for email validation in the User entity.

This module verifies that the User class enforces strict validation of the 'email' field
during instantiation, rejecting malformed or invalid values and only allowing properly
formatted email addresses.

Tests include:
- Rejection of non-string types (None, int, dict, bytes, etc.)
- Rejection of syntactically invalid strings (missing '@', domain issues, etc.)
- Acceptance of valid email strings

The tests use create_valid_user() from test helpers to minimize boilerplate
and focus on the validation logic. Aligned with TDD and DDD (fail-fast) principles.
"""

from uuid import UUID
import pytest

from src.user_management.domain.entities import User
from src.user_management.domain.exceptions import InvalidEmailError
from tests.helpers import create_valid_user


def test_user_creation_fails_when_email_is_not_valid():
    """
    Verifies that User instantiation fails when email is invalid.

    The domain requires that the email field be a non-empty string conforming to
    basic email syntax (e.g., contains '@' and valid domain). Inputs such as None,
    empty strings, invalid formats, or non-string types should raise InvalidEmailError.

    This test checks a comprehensive list of invalid values to ensure robust validation.
    """
    invalid_emails = [
        None,
        "",
        "   ",
        "not-an-email",
        "xpto@",
        "@domain.com",
        "user@",
        "user@@domain.com",
        "user@domain",
        "user@.com",
        "user..name@domain.com",
        123,
        {},
        [],
        True,
        b"raw-bytes"
    ]

    for email in invalid_emails:
        with pytest.raises(InvalidEmailError):
            create_valid_user(email=email)


def test_user_creation_succeeds_with_valid_email():
    """
    Verifies that User can be instantiated with a valid email address.

    Confirms that providing a syntactically correct email results in successful creation
    and that the email value is correctly assigned and preserved in the instance.

    This test covers the happy path and ensures data integrity during construction.
    """
    email = "contact@fmbyteshiftsoftware.com"
    user = create_valid_user(email=email)
    assert user.email == email