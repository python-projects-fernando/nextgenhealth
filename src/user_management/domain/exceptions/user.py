"""
Exceptions related to User entity validation and business rules.

Each exception represents a specific violation of domain invariants,
enabling precise error handling and meaningful feedback during user management operations.
"""

from .base import DomainError


class InvalidUserError(DomainError):
    """
    Base exception raised when a User violates identity or business rules.

    Serves as the parent class for all user-related validation errors.
    Helps enable broad exception handling at higher layers while preserving specificity.

    Examples:
        - Invalid UUID format
        - Malformed email address
        - Name containing invalid characters
        - Date of birth in the future
    """
    pass


class InvalidUUIDError(InvalidUserError):
    """
    Raised when the provided UUID is not a valid UUID instance.

    This includes:
        - None
        - Empty string
        - Malformed string (e.g., 'not-a-uuid')
        - Wrong type (e.g., int, dict, list)

    The User entity requires a valid UUID object for identity integrity and auditability.
    """
    pass


class InvalidEmailError(InvalidUserError):
    """
    Raised when an email does not conform to RFC-like formatting rules.

    Valid emails must:
        - Be a non-empty string
        - Contain exactly one '@'
        - Have valid local-part and domain structure

    Example invalid values: 'invalid-email', 'user@', '@domain.com'
    """
    pass


class InvalidNameError(InvalidUserError):
    """
    Raised when first_name or last_name contains invalid characters.

    Names must:
        - Be non-empty strings
        - Contain only alphabetic characters (A-Z, a-z) and single spaces
        - Not include numbers, symbols, accents, or consecutive spaces

    Ensures consistency and compliance in personal data representation.
    """
    pass


class InvalidPhoneNumberError(InvalidUserError):
    """
    Raised when phone number is provided but not in E.164 format.

    Valid format: '+' followed by 1–15 digits (e.g., '+1234567890').

    Example invalid values:
        - '123-456-7890' (formatted)
        - '1234567890' (missing +)
        - '+12' (too short)

    Aligns with international telephony standards for global systems.
    """
    pass


class InvalidDateOfBirthError(InvalidUserError):
    """
    Raised when date of birth is in the future or unrealistically far in the past.

    Business rule: date of birth must be:
        - A valid date object
        - Not in the future
        - Not before 1900 (or configurable minimum)

    Example violations: born in 2050 or 1800.
    """
    pass


class InvalidUserRoleError(InvalidUserError):
    """
    Raised when the assigned role is not a valid UserRole enum member.

    The system only accepts predefined roles like PATIENT, DOCTOR, NURSE, ADMINISTRATOR.

    Prevents unauthorized access levels due to invalid or malformed roles.
    """
    pass


class InvalidUserStatusError(InvalidUserError):
    """
    Raised when the user status is not a valid UserStatus enum member.

    Only ACTIVE, INACTIVE, and LOCKED are allowed.

    Ensures account lifecycle state is always consistent and auditable.
    """
    pass


class InvalidCreatedAtError(InvalidUserError):
    """
    Raised when created_at timestamp is invalid.

    A valid created_at must:
        - Be a timezone-aware datetime object
        - Use UTC timezone
        - Not be in the future
        - Not be unrealistically old

    Critical for audit trails and compliance (e.g., HIPAA/GDPR).
    """
    pass


class InvalidUpdatedAtError(InvalidUserError):
    """
    Raised when updated_at timestamp is invalid.

    A valid updated_at must:
        - Be a timezone-aware datetime object
        - Use UTC timezone
        - Not be in the future
        - Not be earlier than created_at

    Enforces chronological consistency in user record history.
    """
    pass

