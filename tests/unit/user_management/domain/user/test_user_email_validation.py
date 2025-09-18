from datetime import date
import pytest
from uuid import UUID
from src.user_management.domain.enums.user_role import UserRole
from src.user_management.domain.enums.user_status import UserStatus
from src.user_management.domain.entities.user import User
from src.user_management.domain.exceptions.user import InvalidEmailError


def test_should_raise_exception_for_invalid_email():
    """
    Ensures that an invalid email format triggers a validation error during user creation.

    The system must reject malformed email addresses (e.g., missing '@', invalid domain).
    This test confirms the enforcement of standard email syntax rules.
    """
    # Arrange
    user_id = UUID('123e4567-e89b-12d3-a456-426614174000')

    # Act & Assert
    with pytest.raises(InvalidEmailError, match="Invalid email format"):
        User(
            uuid=user_id,
            email="invalid-email",
            first_name="John",
            last_name="Doe",
            phone="+5511987654321",
            date_of_birth=date(1982, 3, 18),
            role=UserRole.PATIENT,
            status=UserStatus.ACTIVE
        )


def test_should_accept_valid_email():
    """
    Verifies that a correctly formatted email address is accepted during user creation.

    Confirms the system allows valid email addresses following the standard format.
    This test validates the positive path for email validation.
    """
    # Arrange
    user_id = UUID('123e4567-e89b-12d3-a456-426614174000')

    # Act
    user = User(
        uuid=user_id,
        email="john@patient.com",
        first_name="John",
        last_name="Doe",
        phone="+5511987654321",
        date_of_birth=date(1982, 3, 18),
        role=UserRole.PATIENT,
        status=UserStatus.ACTIVE
    )

    # Assert
    assert user.email == "john@patient.com"