"""
Public API for User-related business rule specifications.

This module provides ready-to-use specifications for validating core user data
during registration, profile updates, and authentication workflows.

Import specifications directly using:
from src.user_management.domain.specifications.user import (
    ValidEmailSpecification,
    ValidNameSpecification,
    ValidPhoneE164Specification,
    ValidDateOfBirthSpecification
)
"""

from .email import ValidEmailSpecification
from .name import ValidNameSpecification
from .phone import ValidPhoneE164Specification
from .date_of_birth import ValidDateOfBirthSpecification

__all__ = [
    "ValidEmailSpecification",
    "ValidNameSpecification",
    "ValidPhoneE164Specification",
    "ValidDateOfBirthSpecification",
]