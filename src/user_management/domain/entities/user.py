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
                                               InvalidUpdatedAtError)

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
                 ):

        if not isinstance(uuid, UUID):
            raise InvalidUUIDError("Invalid UUID")

        if not isinstance(email, str):
            raise InvalidEmailError("Email must be a string.")

        if not self._is_valid_email(email):
            raise InvalidEmailError("Invalid email")

        if not self._is_valid_name(first_name):
            raise InvalidNameError("Invalid first name")

        if not self._is_valid_name(last_name):
            raise InvalidNameError("Invalid last name")

        if not self._is_valid_phone(phone):
            raise InvalidPhoneNumberError("Invalid phone number")

        if not self._is_valid_date_of_birth(date_of_birth):
            raise InvalidDateOfBirthError("Invalid date of birth")

        if not self._is_valid_user_role(user_role):
            raise InvalidUserRoleError("Invalid user role")

        if not self._is_valid_user_status(user_status):
            raise InvalidUserStatusError("Invalid user status")

        if not self._is_valid_created_at(created_at):
            raise InvalidCreatedAtError("created_at must be a valid UTC datetime, not in the future")

        if not self._is_valid_updated_at(updated_at):
            raise InvalidUpdatedAtError("updated_at must be a valid UTC datetime, not in the future")
        self.updated_at = updated_at



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

    @staticmethod
    def _is_valid_updated_at(dt: datetime) -> bool:
        if not isinstance(dt, datetime):
            return False
        if dt.tzinfo is None:
            return False
        if dt.tzinfo != timezone.utc:
            return False
        now = datetime.now(timezone.utc)
        return dt <= now  # Not in the future

    @staticmethod
    def _is_valid_created_at(dt: datetime) -> bool:
        if not isinstance(dt, datetime):
            return False
        if dt.tzinfo is None:
            return False
        if dt.tzinfo != timezone.utc:
            return False
        now = datetime.now(timezone.utc)
        return dt <= now  # Not in the future

    @staticmethod
    def _is_valid_user_status(user_status: UserStatus) -> bool:
        return isinstance(user_status, UserStatus)

    @staticmethod
    def _is_valid_user_role(user_role: UserRole) -> bool:
        return isinstance(user_role, UserRole)

    @staticmethod
    def _is_valid_date_of_birth(dob: date) -> bool:
        if dob is None:
            return False

        if not isinstance(dob, date):
            return False

        today = date.today()
        if dob > today:
            return False

        min_allowed_date = today - timedelta(days=150 * 365.25)
        return dob >= min_allowed_date

    @staticmethod
    def _is_valid_phone(phone: str) -> bool:
        if phone is None:
            return True
        pattern = r"^\+[1-9]\d{1,14}$"
        return re.match(pattern, phone) is not None

    @staticmethod
    def _is_valid_name(name:str) -> bool:
        if not name or not name.strip():
            return False
        # pattern = r"^[A-Za-z\s]+$"
        pattern = r"^[A-Za-z]+(?: [A-Za-z]+)*$"
        return re.match(pattern, name) is not None

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        if not email or len(email.strip()) == 0:
            return False
        if " " in email or ".." in email:
            return False
        if email.startswith(".") or email.endswith("."):
            return False
        if "@@" in email:
            return False
        if email.count("@") != 1:
            return False

        try:
            local, domain = email.split("@")
        except ValueError:
            return False

        if not local or not domain:
            return False
        if local.startswith(".") or local.endswith("."):
            return False
        if domain.startswith(".") or domain.endswith("."):
            return False
        if "." not in domain:
            return False

        return True