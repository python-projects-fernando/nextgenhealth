from datetime import date
import pytest
from uuid import UUID
from src.user_management.domain.enums.user_role import UserRole
from src.user_management.domain.enums.user_status import UserStatus
from src.user_management.domain.entities.user import User
from src.user_management.domain.exceptions.user import InvalidPhoneNumberError


def test_should_accept_valid_phone_in_e164_format():
    """
    Verifies that a phone number in correct E.164 format is accepted during user creation.

    Confirms the system allows valid international phone numbers with country code,
    formatted as '+CountryCodeNumber' without spaces or special characters.
    """
    # Arrange
    user_id = UUID('123e4567-e89b-12d3-a456-426614174000')

    # Act
    user = User(
        uuid=user_id,
        email="john@patient.com",
        first_name="Maria Clara",
        last_name="Silva",
        phone="+5511987654321",
        date_of_birth=date(1982, 3, 18),
        role=UserRole.PATIENT,
        status=UserStatus.ACTIVE
    )

    # Assert
    assert user.phone == "+5511987654321"


def test_should_raise_exception_for_missing_plus_sign():
    """
    Ensures that a phone number without the '+' prefix is rejected.

    The E.164 format requires a leading '+' to indicate the country code.
    This test confirms validation enforces this rule strictly.
    """
    # Arrange
    user_id = UUID('123e4567-e89b-12d3-a456-426614174000')

    # Act & Assert
    with pytest.raises(InvalidPhoneNumberError, match="Phone must be in E.164 format"):
        User(
            uuid=user_id,
            email="john@patient.com",
            first_name="Maria Clara",
            last_name="Silva",
            phone="5511987654321",
            date_of_birth=date(1982, 3, 18),
            role=UserRole.PATIENT,
            status=UserStatus.ACTIVE
        )


def test_should_raise_exception_for_spaces_in_phone():
    """
    Ensures that a phone number containing spaces is rejected.

    The E.164 format does not allow whitespace. This test validates that
    even if digits and '+' are present, spaces invalidate the format.
    """
    # Arrange
    user_id = UUID('123e4567-e89b-12d3-a456-426614174000')

    # Act & Assert
    with pytest.raises(InvalidPhoneNumberError, match="Phone must be in E.164 format"):
        User(
            uuid=user_id,
            email="john@patient.com",
            first_name="Maria Clara",
            last_name="Silva",
            phone="+55 11 98765 4321",
            date_of_birth=date(1982, 3, 18),
            role=UserRole.PATIENT,
            status=UserStatus.ACTIVE
        )


def test_should_raise_exception_for_invalid_characters():
    """
    Ensures that a phone number with invalid characters (e.g., parentheses) is rejected.

    The E.164 format only permits '+' followed by digits. Special characters like
    parentheses or dashes are not allowed and must trigger a validation error.
    """
    # Arrange
    user_id = UUID('123e4567-e89b-12d3-a456-426614174000')

    # Act & Assert
    with pytest.raises(InvalidPhoneNumberError, match="Phone must be in E.164 format"):
        User(
            uuid=user_id,
            email="john@patient.com",
            first_name="Maria Clara",
            last_name="Silva",
            phone="+55(11)987654321",
            date_of_birth=date(1982, 3, 18),
            role=UserRole.PATIENT,
            status=UserStatus.ACTIVE
        )


def test_phone_is_optional():
    """
    Verifies that the phone number field can be omitted or set to None.

    Confirms the system accepts user creation when no phone number is provided,
    reflecting the optional nature of this contact information.
    """
    # Arrange
    user_id = UUID('123e4567-e89b-12d3-a456-426614174000')

    # Act
    user = User(
        uuid=user_id,
        email="john@patient.com",
        first_name="Maria Clara",
        last_name="Silva",
        phone=None,
        date_of_birth=date(1982, 3, 18),
        role=UserRole.PATIENT,
        status=UserStatus.ACTIVE
    )

    # Assert
    assert user.phone is None