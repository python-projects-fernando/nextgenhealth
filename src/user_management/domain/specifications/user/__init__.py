"""
Public API for User-related business rule specifications.

This module provides composable, reusable specification objects that encapsulate
domain validation rules for the User entity. These specifications are used to enforce
business invariants during user creation, profile updates, and system audits.

Each specification implements the `is_satisfied_by(value) -> bool` interface,
enabling clean, testable, and readable validation logic within the domain layer.

Specifications support:
- Fail-fast validation
- Reusability across use cases
- Composability (e.g., AND/OR rules)
- Clear separation of concerns

They are central to enforcing data integrity, security, and compliance (e.g., HIPAA/GDPR).

Import specifications directly using:

.. code-block:: python

    from src.user_management.domain.specifications.user import (
        ValidEmailSpecification,
        ValidNameSpecification,
        ValidPhoneE164Specification,
        ValidDateOfBirthSpecification,
        ValidUserRoleSpecification,
        ValidUserStatusSpecification,
        ValidCreatedAtSpecification,
        ValidUpdatedAtSpecification
    )
"""

from .uuid_is_valid import ValidUUIDSpecification
from .email_is_valid import ValidEmailSpecification
from .name_is_valid import ValidNameSpecification
from .phone_is_valid import ValidPhoneE164Specification
from .date_of_birth_is_valid import ValidDateOfBirthSpecification
from .user_role_is_valid import ValidUserRoleSpecification
from .user_status_is_valid import ValidUserStatusSpecification
from .created_at_is_valid import ValidCreatedAtSpecification
from .updated_at_is_valid import ValidUpdatedAtSpecification


__all__ = [
    "ValidUUIDSpecification",
    "ValidEmailSpecification",
    "ValidNameSpecification",
    "ValidPhoneE164Specification",
    "ValidDateOfBirthSpecification",
    "ValidUserRoleSpecification",
    "ValidUserStatusSpecification",
    "ValidCreatedAtSpecification",
    "ValidUpdatedAtSpecification"
]