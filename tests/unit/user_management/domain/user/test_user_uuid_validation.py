"""
Test suite for UUID validation in the User entity.

This module verifies that the User class correctly validates the 'uuid' field
during instantiation, rejecting invalid types and accepting valid UUID instances.
The tests enforce domain-level validation aligned with DDD and fail-fast principles.

Tests include:
- Ensuring InvalidUUIDError is raised for non-UUID inputs (None, str, int, etc.)
- Confirming successful instantiation with a valid UUID object

The tests use create_valid_user() from test helpers to minimize boilerplate,
ensuring clarity and maintainability.

Follows TDD and supports automated documentation via Sphinx.
"""

from uuid import UUID
import pytest

from src.user_management.domain.entities import User
from user_management.domain.exceptions import InvalidUUIDError
from tests.helpers.domain import create_valid_user


def test_user_creation_fails_when_uuid_is_not_a_valid_uuid_instance():
    """
    Verifies that User instantiation fails when uuid is not a UUID instance.

    The domain requires that the uuid parameter be a valid UUID object.
    Passing any other type (e.g., None, str, int) should raise InvalidUUIDError.

    This test checks a variety of invalid inputs to ensure consistent validation.
    """
    invalid_values = [
        None,
        "",
        "not-a-uuid",
        123,
        {},
        [],
        True,
        b"raw-bytes"
    ]

    for value in invalid_values:
        with pytest.raises(InvalidUUIDError):
            create_valid_user(uuid=value)


def test_user_creation_succeeded_when_uuid_is_a_valid_uuid_instance():
    """
    Verifies that User can be instantiated with a valid UUID.

    Confirms that providing a correct UUID object results in successful creation
    and that the uuid value is correctly assigned and preserved in the instance.

    This test covers the happy path and ensures data integrity during construction.
    """
    valid_uuid = UUID("12345678-1234-5678-1234-567812345678")

    user = create_valid_user(uuid=valid_uuid)
    assert user.uuid == valid_uuid