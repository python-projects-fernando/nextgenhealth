import pytest
from datetime import date, timedelta
from uuid import UUID
from src.user_management.domain.enums.user_role import UserRole
from src.user_management.domain.enums.user_status import UserStatus
from src.user_management.domain.entities.user import User
from src.user_management.domain.exceptions.user import InvalidUserError


def test_should_accept_valid_date_of_birth():
    """
    Verifies that a user can be created with a valid and realistic date of birth.

    Ensures the system accepts historical dates that represent plausible human ages.
    This test confirms the correct behavior under normal, expected conditions.
    """
    # Arrange
    user_id = UUID('123e4567-e89b-12d3-a456-426614174000')
    valid_dob = date(1990, 5, 15)

    # Act
    user = User(
        uuid=user_id,
        email="john@patient.com",
        first_name="John",
        last_name="Doe",
        phone="+5511987654321",
        date_of_birth=valid_dob,
        role=UserRole.PATIENT,
        status=UserStatus.ACTIVE
    )

    # Assert
    assert user.date_of_birth == valid_dob


def test_should_raise_exception_when_date_of_birth_is_in_future():
    """
    Ensures that a future date of birth is rejected during user creation.

    Prevents data entry errors or malicious input by validating against the current date.
    The system must not allow dates after today.
    """
    # Arrange
    user_id = UUID('123e4567-e89b-12d3-a456-426614174000')
    future_date = date.today() + timedelta(days=1)

    # Act & Assert
    with pytest.raises(InvalidUserError, match="Date of birth cannot be in the future"):
        User(
            uuid=user_id,
            email="john@patient.com",
            first_name="John",
            last_name="Doe",
            phone="+5511987654321",
            date_of_birth=future_date,
            role=UserRole.PATIENT,
            status=UserStatus.ACTIVE
        )


def test_should_raise_exception_when_date_of_birth_is_too_old():
    """
    Ensures that extremely old (unrealistic) dates are rejected.

    Prevents invalid demographic data by enforcing a reasonable lower bound on age.
    Assumes no person older than ~150 years should be registered.
    """
    # Arrange
    user_id = UUID('123e4567-e89b-12d3-a456-426614174000')
    too_old = date(1800, 1, 1)

    # Act & Assert
    with pytest.raises(InvalidUserError, match="Unrealistic age detected"):
        User(
            uuid=user_id,
            email="john@patient.com",
            first_name="John",
            last_name="Doe",
            phone="+5511987654321",
            date_of_birth=too_old,
            role=UserRole.PATIENT,
            status=UserStatus.ACTIVE
        )


def test_should_raise_exception_when_date_of_birth_is_missing():
    """
    Ensures that a null or missing date of birth is not allowed.

    Validates that date of birth is a required field for all users.
    The system must enforce completeness of core personal data.
    """
    # Arrange
    user_id = UUID('123e4567-e89b-12d3-a456-426614174000')

    # Act & Assert
    with pytest.raises(InvalidUserError, match="Date of birth is required"):
        User(
            uuid=user_id,
            email="john@patient.com",
            first_name="John",
            last_name="Doe",
            phone="+5511987654321",
            date_of_birth=None,
            role=UserRole.PATIENT,
            status=UserStatus.ACTIVE
        )