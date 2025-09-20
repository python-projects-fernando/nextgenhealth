"""
Test suite for phone number validation in the User entity.

This module verifies that the User class correctly validates the 'phone' field
according to the E.164 international format standard. The phone number is optional,
but if provided, it must conform to strict syntax rules.

Validation rules:
- Must be None (allowed) or a string in E.164 format (e.g., '+33142948800')
- Must start with '+'
- First digit after '+' must be 1–9 (not zero)
- Maximum of 15 digits total (1 + up to 14 digits)
- No spaces, hyphens, parentheses, or other formatting characters

The tests use create_valid_user() from test helpers to minimize boilerplate.
Aligned with DDD (fail-fast) and TDD principles.
"""

import pytest

from user_management.domain.exceptions import InvalidPhoneNumberError
from tests.helpers import create_valid_user


def test_user_creation_fails_when_phone_is_not_valid():
    """
    Verifies User instantiation fails when phone is invalid.

    The domain requires that if a phone number is provided, it must be a valid
    E.164 formatted string. Inputs such as empty strings, whitespace-only values,
    malformed formats, or non-conforming patterns should raise InvalidPhoneNumberError.

    This test ensures consistent rejection of invalid phone inputs.
    """
    invalid_phones = [
        "",
        "   ",
        "+",
        "(+123) 456-7890",
    ]

    for phone in invalid_phones:
        with pytest.raises(InvalidPhoneNumberError):
            create_valid_user(phone=phone)


def test_user_creation_succeeds_with_valid_phone():
    """
    Verifies User can be created with a valid E.164 phone number.

    Confirms that providing a properly formatted phone number results in successful
    instantiation and that the value is correctly assigned and preserved.

    This test covers the happy path for optional phone field validation.
    """
    valid_phone = "+33142948800"
    user = create_valid_user(phone=valid_phone)
    assert user.phone == valid_phone