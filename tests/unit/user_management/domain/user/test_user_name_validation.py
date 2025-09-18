from datetime import date
import pytest
from uuid import UUID
from src.user_management.domain.enums.user_role import UserRole
from src.user_management.domain.enums.user_status import UserStatus
from src.user_management.domain.entities.user import User
from src.user_management.domain.exceptions.user import InvalidUserError


def test_should_raise_exception_when_first_name_is_empty():
    """
    Ensures that an empty first name triggers a validation error during user creation.

    The system must enforce non-empty names to maintain data completeness.
    This test confirms rejection when the first name is an empty string.
    """
    user_id = UUID('123e4567-e89b-12d3-a456-426614174000')

    with pytest.raises(InvalidUserError, match="must contain only letters and spaces"):
        User(
            uuid=user_id,
            email="john@patient.com",
            first_name="",
            last_name="Doe",
            phone="+5511987654321",
            date_of_birth=date(1982, 3, 18),
            role=UserRole.PATIENT,
            status=UserStatus.ACTIVE
        )


def test_should_raise_exception_when_last_name_is_empty():
    """
    Ensures that an empty last name triggers a validation error during user creation.

    The system must enforce non-empty names to maintain data completeness.
    This test confirms rejection when the last name is an empty string.
    """
    user_id = UUID('123e4567-e89b-12d3-a456-426614174000')

    with pytest.raises(InvalidUserError, match="must contain only letters and spaces"):
        User(
            uuid=user_id,
            email="john@patient.com",
            first_name="John",
            last_name="",
            phone="+5511987654321",
            date_of_birth=date(1982, 3, 18),
            role=UserRole.PATIENT,
            status=UserStatus.ACTIVE
        )


def test_should_accept_names_with_letters_and_spaces_only():
    """
    Verifies that names containing only letters and spaces are accepted.

    Confirms the system allows valid personal names with standard formatting.
    This test validates the positive path for name validation.
    """
    user_id = UUID('123e4567-e89b-12d3-a456-426614174000')

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

    assert user.first_name == "Maria Clara"
    assert user.last_name == "Silva"


def test_should_raise_exception_for_names_with_numbers():
    """
    Ensures that names containing numbers are rejected during user creation.

    Prevents invalid or potentially malicious input by enforcing character restrictions.
    Only alphabetic characters and spaces are allowed in name fields.
    """
    user_id = UUID('123e4567-e89b-12d3-a456-426614174000')

    with pytest.raises(InvalidUserError, match="must contain only letters and spaces"):
        User(
            uuid=user_id,
            email="john@patient.com",
            first_name="John123",
            last_name="Doe",
            phone="+5511987654321",
            date_of_birth=date(1982, 3, 18),
            role=UserRole.PATIENT,
            status=UserStatus.ACTIVE
        )