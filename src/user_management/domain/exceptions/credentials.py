"""
Exceptions related to user credentials (password, authentication).
"""

from .base import DomainError


class InvalidCredentialsError(DomainError):
    """
    Base exception for credential-related validation failures.

    Examples:
        - Weak password
        - Password reuse
        - Failed verification attempts
    """
    pass


class InvalidPasswordError(InvalidCredentialsError):
    """
    Raised when a password does not meet security requirements.

    Rules:
        - At least 8 characters
        - Not commonly used (e.g., '123456')
        - Not empty or whitespace-only
    """
    pass