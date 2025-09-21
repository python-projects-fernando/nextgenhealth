"""
Exceptions related to User entity validation and business rules.
"""

from .base import DomainError



class InvalidUserError(DomainError):
    """
    Raised when a User violates core identity rules.

    Examples:
        - Invalid UUID format
        - Malformed email
        - Name with invalid characters
        - Future date of birth
    """
    pass


class InvalidUUIDError(InvalidUserError):
    """
    Raised when the provided UUID is not a valid UUID instance.

    This includes:
        - None
        - Empty string
        - Malformed string
        - Wrong type (e.g., int, dict)

    The User entity requires a valid UUID object for identity integrity.
    """
    pass

class InvalidEmailError(InvalidUserError):
    """
    Raised when an email does not conform to RFC-like formatting rules.

    Example: 'invalid-email', 'user@', '@domain.com'
    """
    pass


class InvalidNameError(InvalidUserError):
    """
    Raised when first_name or last_name contains non-alphabetic characters.

    Only letters and spaces are allowed.
    """
    pass


class InvalidPhoneNumberError(InvalidUserError):
    """
    Raised when phone number is provided but not in E.164 format.

    Example: '+1234567890' is valid; '123-456-7890' is invalid.
    """
    pass


class InvalidDateOfBirthError(InvalidUserError):
    """
    Raised when date of birth is in the future or unrealistically old.

    Example: born in 2050 or 1800.
    """
    pass

class InvalidUserRoleError(InvalidUserError):

    pass

class InvalidUserStatusError(InvalidUserError):

    pass

class InvalidCreatedAtError(InvalidUserError):

    pass

class InvalidUpdatedAtError(InvalidUserError):

    pass