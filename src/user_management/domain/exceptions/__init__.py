"""
Public API for domain exceptions.
Allows clean imports across the project.
"""

# Base
from .base import DomainError


from .user import (
    InvalidUserError,
    InvalidUUIDError,
    InvalidEmailError,
    InvalidNameError,
    InvalidPhoneNumberError,
    InvalidDateOfBirthError,
    InvalidUserRoleError,
    InvalidUserStatusError,
    InvalidCreatedAtError,
    InvalidUpdatedAtError,
)


from .credentials import (
    InvalidCredentialsError,
    InvalidPasswordError,
)

__all__ = [
    "DomainError",
    "InvalidUserError",
    "InvalidUUIDError",
    "InvalidEmailError",
    "InvalidNameError",
    "InvalidPhoneNumberError",
    "InvalidDateOfBirthError",
    "InvalidUserRoleError",
    "InvalidUserStatusError",
    "InvalidCreatedAtError",
    "InvalidUpdatedAtError",
    "InvalidCredentialsError",
    "InvalidPasswordError",
]