"""
Public API for User validation services.

This module provides the UserValidator class for enforcing domain rules
during user creation and updates. It encapsulates all validation logic,
including email format, name validity, phone number (E.164), date of birth,
and role/status integrity.

Import directly from this package:
from src.user_management.domain.validation.user import UserValidator
"""

from .user_validator import UserValidator

__all__ = ["UserValidator"]