"""
Specification that validates whether a given value is a valid UserRole.

A valid user role must:
- Be an instance of the UserRole enum
- Match one of the predefined roles in the system (e.g., PATIENT, DOCTOR, ADMINISTRATOR)

This rule ensures consistent role management, supports role-based access control (RBAC),
and prevents unauthorized privilege assignment in healthcare workflows.
"""

from .. import Specification
from ...enums import UserRole


class ValidUserRoleSpecification(Specification):
    """
    Specification to validate that a user role is a valid enum member.

    Enforces domain integrity by rejecting strings, None, or invalid types
    during User creation or role updates. Ensures only approved roles are assigned.
    """

    def is_satisfied_by(self, user_role) -> bool:
        """
        Checks if the provided value is a valid UserRole enum member.

        Args:
            user_role: The value to validate. Expected to be a UserRole instance.

        Returns:
            bool: True if the role is a valid enum member; False otherwise.
        """
        return isinstance(user_role, UserRole)