"""
Defines the roles that a user can have within the system.

Each role determines the user's permissions and access level across application features.
This enumeration supports consistent role management and enables role-based access control (RBAC).
"""

from enum import Enum


class UserRole(Enum):
    """
    Enumeration of user roles in the system.

    These roles define the scope of actions and data access for each authenticated user.
    Used throughout the domain to enforce authorization rules and tailor workflows.
    """
    PATIENT = "PATIENT"
    NURSE = "NURSE"
    DOCTOR = "DOCTOR"
    ADMINISTRATOR = "ADMINISTRATOR"