from datetime import date
from uuid import UUID

from ...enums.user_role import UserRole
from ...enums.user_status import UserStatus
from ...exceptions.user import InvalidEmailError, InvalidUserError, InvalidPhoneNumberError

from ....domain.specifications.user import (
    ValidEmailSpecification,
    ValidNameSpecification,
    ValidPhoneE164Specification,
    ValidDateOfBirthSpecification,
)


class UserValidator:
    """
    Centralized validator for User entity creation and updates.

    Applies domain rules through reusable Specification objects to ensure data integrity.
    This class encapsulates all validation logic, enabling clean separation from the User entity
    and promoting testability, reuse, and maintainability.

    Validation includes:
    - UUID format
    - Email validity
    - Name character constraints
    - Phone number in E.164 format
    - Realistic and non-future date of birth
    - Valid role and status enums
    """

    @staticmethod
    def validate(
        uuid: UUID,
        email: str,
        first_name: str,
        last_name: str,
        phone,
        date_of_birth,
        role: UserRole,
        status: UserStatus
    ) -> None:
        """
        Validates user data against domain rules before entity creation.

        Executes a series of checks using Specifications. Raises specific domain exceptions
        if any validation fails. All validations are executed sequentially.

        Args:
            uuid (UUID): Unique identifier; must be a valid UUID instance.
            email (str): Email address; must be properly formatted.
            first_name (str): First name; must contain only letters and spaces.
            last_name (str): Last name; must contain only letters and spaces.
            phone (str, optional): Phone number in E.164 format (e.g., +1234567890).
                                   May be None.
            date_of_birth (date): Date of birth; must not be in the future or unrealistic.
            role (UserRole): Assigned role; must be a valid UserRole enum member.
            status (UserStatus): Account status; must be a valid UserStatus enum member.

        Raises:
            InvalidUserError: If UUID, names, role, status, or date of birth are invalid.
            InvalidEmailError: If email format is invalid.
            InvalidPhoneNumberError: If phone is provided but not in E.164 format.
        """
        if not isinstance(uuid, UUID):
            raise InvalidUserError("User ID must be a valid UUID")

        if not ValidEmailSpecification().is_satisfied_by(email):
            raise InvalidEmailError("Invalid email format")

        if not ValidNameSpecification().is_satisfied_by(first_name):
            raise InvalidUserError("Name must contain only letters and spaces")

        if not ValidNameSpecification().is_satisfied_by(last_name):
            raise InvalidUserError("Name must contain only letters and spaces")

        if not ValidPhoneE164Specification().is_satisfied_by(phone):
            raise InvalidPhoneNumberError("Phone must be in E.164 format")

        if not ValidDateOfBirthSpecification().is_satisfied_by(date_of_birth):
            if date_of_birth is None:
                raise InvalidUserError("Date of birth is required")
            if date_of_birth > date.today():
                raise InvalidUserError("Date of birth cannot be in the future")
            raise InvalidUserError("Unrealistic age detected")

        if not isinstance(role, UserRole):
            raise InvalidUserError("Invalid user role")

        if not isinstance(status, UserStatus):
            raise InvalidUserError("Invalid user status")