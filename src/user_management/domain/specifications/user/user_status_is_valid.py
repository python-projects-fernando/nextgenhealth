"""
Specification that validates whether a given value is a valid UserStatus.

A valid user status must:
- Be an instance of the UserStatus enum
- Match one of the predefined statuses (e.g., ACTIVE, INACTIVE, LOCKED)

This rule ensures consistent account lifecycle management, supports security workflows,
and prevents invalid state transitions in compliance-sensitive healthcare systems.
"""

from .. import Specification
from ...enums import UserStatus


class ValidUserStatusSpecification(Specification):
    """
    Specification to validate that a user status is a valid enum member.

    Enforces domain integrity by rejecting strings, None, or invalid types
    during User creation or status updates. Ensures only approved states are assigned.
    """

    def is_satisfied_by(self, user_status) -> bool:
        """
        Checks if the provided value is a valid UserStatus enum member.

        Args:
            user_status: The value to validate. Expected to be a UserStatus instance.

        Returns:
            bool: True if the status is a valid enum member; False otherwise.
        """
        return isinstance(user_status, UserStatus)