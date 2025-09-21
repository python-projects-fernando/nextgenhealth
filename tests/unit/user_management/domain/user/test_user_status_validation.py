import pytest

from user_management.domain.enums import UserStatus
from tests.helpers import create_valid_user
from user_management.domain.exceptions import InvalidUserRoleError, InvalidUserStatusError


def test_user_creation_fails_when_user_status_is_not_a_valid_user_status_instance():
    invalid_status = [
        None,
        "",
        "   ",
        # "Active",
        # "ACTIVE",
        # "Locked",
        "invalid_sratus",
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
        user = create_valid_user(user_status = UserStatus.INACTIVE)
        assert user.user_status == UserStatus.INACTIVE
