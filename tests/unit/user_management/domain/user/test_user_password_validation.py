"""
Test suite for password validation in the User entity.

Verifies that the User class correctly validates passwords using is_password_valid().
Now uses UserCredentials VO for secure credential handling.
Follows TDD: RED → GREEN → REFACTOR.
"""

import pytest

from tests.helpers import create_valid_user
from user_management.domain.exceptions import InvalidPasswordError
from user_management.domain.value_objects import UserCredentials


def test_is_password_valid_returns_true_when_password_is_correct():
    """Should return True when correct password is provided."""
    # Arrange: Create credentials with known password
    valid_password = "SecurePass123!"
    credentials = UserCredentials.create(valid_password)

    # Act: Create user with these credentials
    user = create_valid_user(credentials=credentials)

    # Assert: Should accept correct password
    assert user.is_password_valid(valid_password) is True


def test_is_password_valid_returns_false_when_password_is_incorrect():
    """Should return False when incorrect password is provided."""
    # Arrange
    valid_password = "SecurePass123!"
    wrong_password = "WrongPass!"
    credentials = UserCredentials.create(valid_password)

    # Act
    user = create_valid_user(credentials=credentials)

    # Assert
    assert user.is_password_valid(wrong_password) is False


def test_is_password_valid_returns_false_when_password_is_empty_string():
    """Should reject empty string as password."""
    credentials = UserCredentials.create("SecurePass123!")
    user = create_valid_user(credentials=credentials)
    assert user.is_password_valid("") is False


def test_is_password_valid_returns_false_when_password_is_none():
    """Should reject None as password."""
    credentials = UserCredentials.create("SecurePass123!")
    user = create_valid_user(credentials=credentials)
    assert user.is_password_valid(None) is False



#------------------
def test_change_password_succeeds_when_current_password_is_correct():
    """Should update password when current password is valid."""
    credentials = UserCredentials.create("OldPass123!")
    user = create_valid_user(credentials=credentials)

    user.change_password("OldPass123!", "NewPass456!")

    assert user.is_password_valid("NewPass456!") is True
    assert user.is_password_valid("OldPass123!") is False
    assert user.updated_at >= user.created_at

def test_change_password_fails_when_current_password_is_incorrect():
    """Should raise error if current password is wrong."""
    credentials = UserCredentials.create("ValidPass123!")
    user = create_valid_user(credentials=credentials)

    with pytest.raises(InvalidPasswordError):
        user.change_password("WrongPass!", "NewPass123!")

def test_change_password_fails_when_new_password_is_invalid():
    """Should reject empty or weak passwords."""
    credentials = UserCredentials.create("ValidPass123!")
    user = create_valid_user(credentials=credentials)

    with pytest.raises(InvalidPasswordError):
        user.change_password("ValidPass123!", "")

def test_change_password_fails_when_new_password_is_same_as_old():
    """Should prevent reusing the same password."""
    credentials = UserCredentials.create("SamePass123!")
    user = create_valid_user(credentials=credentials)

    with pytest.raises(InvalidPasswordError):
        user.change_password("SamePass123!", "SamePass123!")