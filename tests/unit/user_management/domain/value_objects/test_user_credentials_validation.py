"""
Test suite for UserCredentials Value Object.

Verifies that UserCredentials correctly handles password hashing and validation.
Follows TDD: RED → GREEN → REFACTOR.
"""

import pytest
from user_management.domain.value_objects import UserCredentials
from user_management.domain.exceptions import InvalidPasswordError


def test_user_credentials_creation_fails_when_password_is_none():
    """Should raise InvalidPasswordError if password is None."""
    with pytest.raises(InvalidPasswordError):
        UserCredentials.create(None)


def test_user_credentials_creation_fails_when_password_is_empty():
    """Should raise InvalidPasswordError if password is empty string."""
    with pytest.raises(InvalidPasswordError):
        UserCredentials.create("")


def test_user_credentials_creation_fails_when_password_is_whitespace_only():
    """Should raise InvalidPasswordError if password is only whitespace."""
    with pytest.raises(InvalidPasswordError):
        UserCredentials.create("   ")


def test_user_credentials_creation_succeeds_with_valid_password():
    """Should create instance with valid password."""
    credentials = UserCredentials.create("SecurePass123!")
    assert isinstance(credentials, UserCredentials)


def test_user_credentials_can_validate_correct_password():
    """Should return True when provided password matches."""
    credentials = UserCredentials.create("SecurePass123!")
    assert credentials.is_valid("SecurePass123!") is True


def test_user_credentials_rejects_incorrect_password():
    """Should return False when provided password does not match."""
    credentials = UserCredentials.create("SecurePass123!")
    assert credentials.is_valid("WrongPass!") is False


def test_user_credentials_rejects_none_and_non_string_inputs():
    """Should reject None or non-string inputs as invalid passwords."""
    credentials = UserCredentials.create("SecurePass123!")

    assert credentials.is_valid(None) is False
    assert credentials.is_valid(123) is False
    assert credentials.is_valid([]) is False
    assert credentials.is_valid({}) is False