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


class ValidEmergencyContactNameSpecification(Specification):
    """
    Specification to validate that a UUID is a properly typed identity object.

    Enforces strict type checking to ensure only valid UUID instances are accepted
    during User aggregate creation. Prevents common errors like passing strings
    or None as identifiers in critical healthcare workflows.
    """

    def is_satisfied_by(self, name) -> bool:
        """
        Checks if the provided value is a valid name.

        Args:
            name: The value to validate. Expected to be a string.

        Returns:
            bool: True if the name is valid; False otherwise.
        """
        if not isinstance(name, str):
            return False

        if not name or not name.strip():
            return False

        # Matches one or more words, each starting with a letter, separated by single spaces
        # Example: "John", "Mary Jane", but not "Mary  Jane" (double space) or "O'Connor"
        pattern = r"^[A-Za-z]+(?: [A-Za-z]+)*$"
        return re.match(pattern, name) is not None