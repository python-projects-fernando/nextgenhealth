"""
Test suite for update_basic_profile method in User entity.

Verifies that the user can safely update their basic profile information,
including date of birth, using domain specifications for validation.
Follows TDD: RED → GREEN → REFACTOR.
"""

import pytest
from datetime import datetime, timezone, date, timedelta

from tests.helpers import create_valid_user
from user_management.domain.exceptions import (
    InvalidNameError,
    InvalidEmailError,
    InvalidPhoneNumberError,
    InvalidDateOfBirthError,
)


def test_update_basic_profile_succeeds_with_valid_data():
    """Should update all fields when data is valid."""
    user = create_valid_user(
        first_name="Fernando",
        last_name="Magalhaes",
        email="old@example.com",
        phone="+8123456789",
        date_of_birth=date(1982, 3, 18)
    )
    old_updated_at = user.updated_at

    user.update_basic_profile(
        first_name="Lili",
        last_name="Doe",
        email="lili@fmbyteshiftsoftware.com",
        phone="+1987654321",
        date_of_birth=date(2005, 4, 25)
    )

    assert user.first_name == "Lili"
    assert user.last_name == "Doe"
    assert user.email == "lili@fmbyteshiftsoftware.com"
    assert user.phone == "+1987654321"
    assert user.date_of_birth == date(2005, 4, 25)
    assert user.updated_at > old_updated_at


def test_update_basic_profile_fails_when_first_name_is_invalid():
    """Should reject empty or invalid first name."""
    user = create_valid_user()
    with pytest.raises(InvalidNameError):
        user.update_basic_profile(
            first_name="",
            last_name="Valid",
            email="valid@example.com",
            phone="+1234567890",
            date_of_birth=date(1990, 1, 1)
        )


def test_update_basic_profile_fails_when_last_name_is_invalid():
    """Should reject empty or invalid last name."""
    user = create_valid_user()
    with pytest.raises(InvalidNameError):
        user.update_basic_profile(
            first_name="Valid",
            last_name="   ",
            email="valid@example.com",
            phone="+1234567890",
            date_of_birth=date(1990, 1, 1)
        )


def test_update_basic_profile_fails_when_email_is_invalid():
    """Should reject malformed email address."""
    user = create_valid_user()
    with pytest.raises(InvalidEmailError):
        user.update_basic_profile(
            first_name="Valid",
            last_name="Name",
            email="not-an-email",
            phone="+1234567890",
            date_of_birth=date(1990, 1, 1)
        )


def test_update_basic_profile_fails_when_phone_is_invalid():
    """Should reject phone number not in E.164 format."""
    user = create_valid_user()
    with pytest.raises(InvalidPhoneNumberError):
        user.update_basic_profile(
            first_name="Valid",
            last_name="Name",
            email="valid@example.com",
            phone="12345",  # missing '+'
            date_of_birth=date(1990, 1, 1)
        )


def test_update_basic_profile_fails_when_date_of_birth_is_in_future():
    """Should reject future date of birth."""
    user = create_valid_user()
    future_dob = date.today() + timedelta(days=1)
    with pytest.raises(InvalidDateOfBirthError):
        user.update_basic_profile(
            first_name="Valid",
            last_name="Name",
            email="valid@example.com",
            phone="+1234567890",
            date_of_birth=future_dob
        )


def test_update_basic_profile_fails_when_date_of_birth_is_too_old():
    """Should reject unreasonably old date of birth."""
    user = create_valid_user()
    too_old = date(1800, 1, 1)  # unrealistic
    with pytest.raises(InvalidDateOfBirthError):
        user.update_basic_profile(
            first_name="Valid",
            last_name="Name",
            email="valid@example.com",
            phone="+1234567890",
            date_of_birth=too_old
        )