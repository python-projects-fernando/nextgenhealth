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
from user_management.domain.validation.user import UserValidator


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


        UserValidator.validate(uuid, email, first_name, last_name,
                               phone, date_of_birth, user_role, user_status, "created_at", updated_at)

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
