"""
Public API for domain exceptions.
Import these directly from:
from src.user_management.domain.exceptions.user import {ExceptionName}
"""

from .user_exceptions import (
    InvalidEmailError,
    InvalidUserError,
    InvalidPhoneNumberError,
)