"""
Specification that validates whether a given value is a valid UUID.

A valid UUID must:
- Be an instance of Python's uuid.UUID class
- Not be None, string, int, or any other type

This rule ensures global identity integrity within the domain,
preventing invalid or spoofed identifiers in audit trails and entity references.
"""

from uuid import UUID
from .. import Specification


class ValidUserUUIDSpecification(Specification):
    """
    Specification to validate that a UUID is a properly typed identity object.

    Enforces strict type checking to ensure only valid UUID instances are accepted
    during User aggregate creation. Prevents common errors like passing strings
    or None as identifiers in critical healthcare workflows.
    """

    def is_satisfied_by(self, uuid) -> bool:
        """
        Checks if the provided value is a valid UUID instance.

        Args:
            uuid: The value to validate. Expected to be a uuid.UUID object.

        Returns:
            bool: True if the value is a valid UUID; False otherwise.
        """
        return isinstance(uuid, UUID)