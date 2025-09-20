"""
        Aggregate Root representing a user in the NextGenHealth system.

        Central entity for identity management, enforcing validation,
        security, and auditability.
"""

import re
from uuid import UUID
from user_management.domain.exceptions import InvalidUUIDError, InvalidEmailError
from user_management.domain.exceptions import InvalidNameError
from user_management.domain.exceptions import InvalidPhoneNumberError


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



        self.uuid = uuid
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

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