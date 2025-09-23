"""
        Aggregate Root representing a user in the NextGenHealth system.

        Central entity for identity management, enforcing validation,
        security, and auditability.
"""
from datetime import date, timedelta, datetime, timezone
import re
from uuid import UUID

from user_management.domain.enums import UserRole, UserStatus
from user_management.domain.exceptions import (InvalidUUIDError,
                                               InvalidEmailError,
                                               InvalidNameError,
                                               InvalidPhoneNumberError,
                                               InvalidDateOfBirthError,
                                               InvalidUserRoleError,
                                               InvalidUserStatusError,
                                               InvalidCreatedAtError,
                                               InvalidUpdatedAtError, InvalidPasswordError)
from user_management.domain.validation.user import UserValidator
from user_management.domain.value_objects import UserCredentials

from user_management.domain.specifications.user import (
    ValidNameSpecification,
    ValidEmailSpecification,
    ValidPhoneE164Specification,
    ValidDateOfBirthSpecification
)


class User:
    """
        Aggregate Root representing a user in the NextGenHealth system.

        Central entity for identity management, enforcing validation,
        security, and auditability.
    """

    def __init__(self,
                 uuid: UUID,
                 email: str,
                 first_name: str,
                 last_name: str,
                 phone: str,
                 date_of_birth: date,
                 user_role: UserRole,
                 user_status: UserStatus,
                 created_at: datetime,
                 updated_at: datetime,
                 credentials: UserCredentials
                 ):


        UserValidator.validate(uuid, email, first_name, last_name,
                               phone, date_of_birth, user_role, user_status, created_at, updated_at)


        self.uuid = uuid
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.user_role = user_role
        self.user_status = user_status
        self.created_at = created_at
        self.updated_at = updated_at
        self._credentials = credentials


    def is_password_valid(self, provided: str) -> bool:
        return self._credentials.is_valid(provided)

    def change_password(self, current_password: str, new_password: str):
        """
        Changes the user's password if the current password is correct
        and the new password is valid and different.

        Args:
            current_password (str): The user's current password
            new_password (str): The desired new password

        Raises:
            InvalidPasswordError: If current password is wrong or new password is invalid
        """
        if not self.is_password_valid(current_password):
            raise InvalidPasswordError("Current password is incorrect")


        new_credentials = UserCredentials.with_new_password(current_password, new_password)


        self._credentials = new_credentials
        self.updated_at = datetime.now(timezone.utc)

    def change_user_role(self, new_role: UserRole):
        """
        Changes the user's role to a new valid role.

        This method ensures the new role is a valid UserRole enum member.
        The decision of *who* can perform this action belongs to the Use Case layer.

        Args:
            new_role (UserRole): The new role to assign

        Raises:
            InvalidUserRoleError: If the role is invalid
        """
        if not isinstance(new_role, UserRole):
            raise InvalidUserRoleError("Invalid user role")

        self.user_role = new_role
        self.updated_at = datetime.now(timezone.utc)

    def change_user_status(self, new_status: UserStatus):
        if not isinstance(new_status, UserStatus):
            raise InvalidUserStatusError("Invalid user status")

        self.user_status = new_status
        self.updated_at = datetime.now(timezone.utc)

    def update_basic_profile(self, first_name: str, last_name: str, email: str, phone: str, date_of_birth: date):
        """
        Updates the user's basic profile information using domain specifications.

        Validates inputs via Specification Pattern before applying changes.
        Updates updated_at timestamp on success.

        Args:
            first_name (str): New first name
            last_name (str): New last name
            email (str): New email address
            phone (str): New phone number in E.164 format
            date_of_birth (date): New date of birth

        Raises:
            InvalidNameError: If first or last name fails specification
            InvalidEmailError: If email fails specification
            InvalidPhoneNumberError: If phone fails specification
            InvalidDateOfBirthError: If date_of_birth fails specification
        """
        # Validate using specifications
        if not ValidNameSpecification().is_satisfied_by(first_name):
            raise InvalidNameError("First name does not satisfy naming rules")

        if not ValidNameSpecification().is_satisfied_by(last_name):
            raise InvalidNameError("Last name does not satisfy naming rules")

        if not ValidEmailSpecification().is_satisfied_by(email):
            raise InvalidEmailError("Email does not satisfy format rules")

        if not ValidPhoneE164Specification().is_satisfied_by(phone):
            raise InvalidPhoneNumberError("Phone number does not follow E.164 format")

        if not ValidDateOfBirthSpecification().is_satisfied_by(date_of_birth):
            raise InvalidDateOfBirthError("Date of birth is not valid")

        # Apply changes
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.updated_at = datetime.now(timezone.utc)
