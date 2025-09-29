"""
Test suite for UserRole validation in the User entity.

This module verifies that the User class enforces strict validation of the 'user_role' field,
ensuring it conforms to domain rules:
- Must be a valid UserRole enum member (e.g., DOCTOR, PATIENT)
- Rejects invalid types (None, strings, ints, etc.)
- Rejects incorrect values or malformed role names

The tests use create_valid_user() from test helpers to minimize boilerplate.
Aligned with DDD (fail-fast) and TDD principles.
"""

import pytest

from tests.helpers.domain import create_valid_user
from user_management.domain.enums import UserRole
from user_management.domain.exceptions import InvalidUserRoleError


def test_user_creation_fails_when_user_role_is_not_a_valid_user_role_instance():
    """
    Verifies User instantiation fails when user_role is not a valid UserRole enum member.

    The domain requires user_role to be one of the predefined enum values.
    Inputs such as None, strings, integers, or invalid role names should raise InvalidUserRoleError.

    This test ensures consistent rejection of unauthorized or malformed roles.
    """
    invalid_roles = [
        None,
        "",
        "   ",
        "Patient",           # wrong case
        "PATIENT",           # uppercase
        "patient123",        # with suffix
        "invalid_role",      # not in enum
        "user",              # not a valid role
        123,                 # integer
        {},                  # dict
        [],                  # list
        True,                # boolean
        b"raw-bytes",        # bytes
        0,                   # int
        -1,                  # negative int
        "doctor ",           # trailing space
        " nurse",            # leading space
        "do..ctor",          # malformed
        "👨‍⚕️",               # emoji
    ]

    for role in invalid_roles:
        with pytest.raises(InvalidUserRoleError):
            create_valid_user(user_role=role)


def test_user_creation_succeeded_when_user_role_is_a_valid_user_role_instance():
    """
    Verifies User can be created with a valid UserRole enum instance.

    Confirms that providing a correct UserRole value results in successful instantiation
    and that the role is correctly assigned and preserved.

    This test covers the happy path for user_role validation.
    """
    user = create_valid_user(user_role=UserRole.DOCTOR)
    assert user.user_role == UserRole.DOCTOR


def test_change_user_role_succeeds_with_valid_role():
    """Should update role when new role is valid."""
    user = create_valid_user(user_role=UserRole.NURSE)

    user.change_user_role(UserRole.DOCTOR)

    assert user.user_role == UserRole.DOCTOR
    assert user.updated_at > user.created_at


def test_change_user_role_fails_when_invalid_role():
    """Should raise error when invalid role is provided."""
    user = create_valid_user()

    invalid_values = [None, "", "Doctor", 123, {}, [], True, b"raw"]

    for value in invalid_values:
        with pytest.raises(InvalidUserRoleError):
            user.change_user_role(value)