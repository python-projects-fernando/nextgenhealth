import pytest

from tests.helpers import create_valid_user
from user_management.domain.enums import UserRole
from user_management.domain.exceptions import InvalidUserRoleError


def test_user_creation_fails_when_user_role_is_not_a_valid_user_role_instance():
    invalid_roles = [
        None,
        "",
        "   ",
        "Patient",
        "PATIENT",
        "patient123",
        "invalid_role",
        "user",
        123,
        {},
        [],
        True,
        b"raw-bytes",
        0,
        -1,
        "doctor ",
        " nurse",
        "do..ctor",
        "👨‍⚕️",
    ]

    for role in invalid_roles:
        with pytest.raises(InvalidUserRoleError):
            create_valid_user(user_role=role)

def test_user_creation_succeeded_when_user_role_is_a_valid_user_role_instance():
    user = create_valid_user(user_role = UserRole.DOCTOR)
    assert user.user_role == UserRole.DOCTOR
