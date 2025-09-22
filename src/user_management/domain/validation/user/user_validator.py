from datetime import date, datetime
from uuid import UUID

from ...enums.user_role import UserRole
from ...enums.user_status import UserStatus
from ...exceptions import InvalidUUIDError, InvalidNameError, InvalidDateOfBirthError, InvalidUserRoleError, \
    InvalidCreatedAtError, InvalidUpdatedAtError
from ...exceptions.user import InvalidEmailError, InvalidUserError, InvalidPhoneNumberError, InvalidUserStatusError
from ...specifications.user import ValidUserStatusSpecification, ValidCreatedAtSpecification, \
    ValidUpdatedAtSpecification
from ...specifications.user.user_role_is_valid import ValidUserRoleSpecification
from ...specifications.user.uuid_is_valid import ValidUUIDSpecification

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
        status: UserStatus,
        created_at: datetime,
        updated_at: datetime
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

        if not ValidUUIDSpecification().is_satisfied_by(uuid):
            raise InvalidUUIDError("Invalid uuid")

        if not ValidEmailSpecification().is_satisfied_by(email):
            raise InvalidEmailError("Invalid email format")

        if not ValidNameSpecification().is_satisfied_by(first_name):
            raise InvalidNameError("Name must contain only letters and spaces")

        if not ValidNameSpecification().is_satisfied_by(last_name):
            raise InvalidNameError("Name must contain only letters and spaces")

        if not ValidPhoneE164Specification().is_satisfied_by(phone):
            raise InvalidPhoneNumberError("Phone must be in E.164 format")

        if not ValidDateOfBirthSpecification().is_satisfied_by(date_of_birth):
            raise InvalidDateOfBirthError("Invalid date of birth")

        if not ValidUserRoleSpecification().is_satisfied_by(role):
            raise InvalidUserRoleError("Invalid user role")

        if not ValidUserStatusSpecification().is_satisfied_by(status):
            raise InvalidUserStatusError("Invalid user role")

        if not ValidCreatedAtSpecification().is_satisfied_by(created_at):
            raise InvalidCreatedAtError("Invalid created at date")

        if not ValidUpdatedAtSpecification().is_satisfied_by(updated_at):
            raise InvalidUpdatedAtError("Invalid update at date")