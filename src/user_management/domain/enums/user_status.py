"""
Defines the possible operational states of a user account within the system.

These statuses control access and determine whether a user can authenticate
and interact with the application. Used for security, compliance, and workflow management.
"""

from enum import Enum


class UserStatus(Enum):
    """
    Enumeration of user account statuses.

    Represents the current lifecycle state of a user account,
    influencing authentication, permissions, and system behavior.
    """
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    LOCKED = "Locked"