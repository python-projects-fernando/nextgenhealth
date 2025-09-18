from datetime import date
from uuid import UUID
from src.user_management.domain.enums.user_role import UserRole
from src.user_management.domain.enums.user_status import UserStatus
from src.user_management.domain.entities.user import User


def test_should_create_user_with_valid_data():
    """
    Verifies that a User can be successfully created with valid and complete data.

    Ensures all provided attributes are correctly assigned to the User instance
    without modification or validation failure. This test confirms the basic
    instantiation contract of the User entity under valid conditions.
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
    assert user.uuid == user_id
    assert user.email == "john@patient.com"
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.phone == "+5511987654321"
    assert user.date_of_birth == date(1982, 3, 18)
    assert user.role == UserRole.PATIENT
    assert user.status == UserStatus.ACTIVE