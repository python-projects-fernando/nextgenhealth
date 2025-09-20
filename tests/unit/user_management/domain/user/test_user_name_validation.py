"""
Test suite for first_name and last_name validation in the User entity.

This module verifies that the User class enforces strict validation of personal names,
ensuring they conform to domain rules:
- Must be non-empty strings
- Must contain only ASCII letters (A-Z, a-z)
- Must not include special characters, numbers, or accents
- Must not have consecutive spaces

The tests use create_valid_user() from test helpers to minimize boilerplate
and focus on validation logic. Aligned with DDD (fail-fast) and TDD principles.
"""

import pytest

from src.user_management.domain.exceptions import InvalidNameError
from tests.helpers import create_valid_user


def test_user_creation_fails_when_first_name_is_not_valid():
    """
    Verifies User instantiation fails when first_name is invalid.

    The domain requires first_name to be a non-empty string containing only
    ASCII letters and single spaces between words. Inputs such as empty strings,
    whitespace-only values, accented characters (e.g., 'ã', 'é'), special symbols,
    or multiple consecutive spaces should raise InvalidNameError.

    This test ensures consistent rejection of malformed first_name values.
    """
    invalid_names = [
        "",               # empty string
        "   ",            # whitespace only
        "João",           # contains accent
        "Mary  Jane",     # multiple consecutive spaces
        "Carlos$",        # contains special character
        "Ana@"            # contains symbol
    ]

    for name in invalid_names:
        with pytest.raises(InvalidNameError):
            create_valid_user(first_name=name)


def test_user_creation_succeeds_with_valid_first_name():
    """
    Verifies User can be created with a valid first_name.

    Confirms that providing a properly formatted first_name results in successful
    instantiation and that the value is correctly assigned and preserved.

    This test covers the happy path for first_name validation.
    """
    valid_name = "Lili"
    user = create_valid_user(first_name=valid_name)
    assert user.first_name == valid_name


def test_user_creation_fails_when_last_name_is_not_valid():
    """
    Verifies User instantiation fails when last_name is invalid.

    Similar to first_name, last_name must be a non-empty string with only
    ASCII letters and single spaces. Invalid inputs (empty, accented, symbolic)
    should trigger InvalidNameError.

    Ensures consistent validation across both name fields.
    """
    invalid_names = [
        "",             # empty string
        "   ",          # whitespace only
        "João",         # contains accent
        "Carlos$",      # contains special character
        "Ana@"          # contains symbol
    ]

    for name in invalid_names:
        with pytest.raises(InvalidNameError):
            create_valid_user(last_name=name)


def test_user_creation_succeeds_with_valid_last_name():
    """
    Verifies User can be created with a valid last_name.

    Confirms that a syntactically correct last_name is accepted and stored
    without modification during object creation.

    Covers the happy path for last_name validation.
    """
    valid_name = "Magalhaes"
    user = create_valid_user(last_name=valid_name)
    assert user.last_name == valid_name