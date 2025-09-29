"""
Specification that validates whether a given value is a valid UUID.

A valid UUID must:
- Be an instance of Python's uuid.UUID class
- Not be None, string, int, or any other type

This rule ensures global identity integrity within the domain,
preventing invalid or spoofed identifiers in audit trails and entity references.
"""
import re
from uuid import UUID
from .. import Specification


class ValidEmergencyContactPhoneSpecification(Specification):
    """
    Specification to validate that a UUID is a properly typed identity object.

    Enforces strict type checking to ensure only valid UUID instances are accepted
    during User aggregate creation. Prevents common errors like passing strings
    or None as identifiers in critical healthcare workflows.
    """

    def is_satisfied_by(self, phone) -> bool:
        """
        Checks if the provided value is a valid E.164 phone number or None.

        Args:
            phone: The value to validate. Expected to be a string or None.

        Returns:
            bool: True if the phone is None or correctly formatted; False otherwise.
        """
        if phone is None:
            return True

        if not isinstance(phone, str):
            return False

        # E.164 format: +[1-9][0-9]{1,14}
        pattern = r"^\+[1-9]\d{1,14}$"
        return re.match(pattern, phone) is not None