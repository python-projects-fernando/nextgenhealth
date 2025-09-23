"""
Test suite for UserStatus validation in the User entity.

This module verifies that the User class enforces strict validation of the 'user_status' field,
ensuring it conforms to domain rules:
- Must be a valid UserStatus enum member (e.g., ACTIVE, INACTIVE, LOCKED)
- Rejects invalid types (None, strings, ints, etc.)
- Rejects incorrect values or malformed status names

The tests use create_valid_user() from test helpers to minimize boilerplate.
Aligned with DDD (fail-fast) and TDD principles.
"""

import pytest

from user_management.domain.enums import UserStatus
from user_management.domain.exceptions import InvalidUserStatusError
from tests.helpers import create_valid_user


def test_user_creation_fails_when_user_status_is_not_a_valid_user_status_instance():
    """
    Verifies User instantiation fails when user_status is not a valid UserStatus enum member.

    The domain requires user_status to be one of the predefined enum values.
    Inputs such as None, strings, integers, or invalid status names should raise InvalidUserStatusError.

    This test ensures consistent rejection of unauthorized or malformed statuses.
    """
    invalid_status = [
        None,
        "",
        "   ",
        "Active",           # string instead of enum
        "ACTIVE",           # wrong case
        "Locked",           # string
        "invalid_status",   # not in enum
        "user",
        123,
        {},
        [],
        True,
        b"raw-bytes",
        0,
        -1,
    ]

    for status in invalid_status:
        with pytest.raises(InvalidUserStatusError):
            create_valid_user(user_status=status)


def test_user_creation_succeeded_when_user_status_is_a_valid_user_status_instance():
    """
    Verifies User can be created with a valid UserStatus enum instance.

    Confirms that providing a correct UserStatus value results in successful instantiation
    and that the status is correctly assigned and preserved.

    This test covers the happy path for user_status validation.
    """
    user = create_valid_user(user_status=UserStatus.INACTIVE)
    assert user.user_status == UserStatus.INACTIVE



def test_change_user_status_succeeds_with_valid_status():
    user = create_valid_user(user_status=UserStatus.ACTIVE)

    user.change_user_status(UserStatus.LOCKED)

    assert user.user_status == UserStatus.LOCKED
    assert user.updated_at > user.created_at


def test_change_user_status_fails_when_invalid_status():
    invalid_status = [
        None,
        "",
        "   ",
        "Active",  # string instead of enum
        "ACTIVE",  # wrong case
        "Locked",  # string
        "invalid_status",  # not in enum
        "user",
        123,
        {},
        [],
        True,
        b"raw-bytes",
        0,
        -1,
    ]

    user = create_valid_user(user_status=UserStatus.ACTIVE)

    for status in invalid_status:
        with pytest.raises(InvalidUserStatusError):
            user.change_user_status(status)


