"""
Defines domain-level exceptions for the User Management module.

These exceptions represent business rule violations and validation failures
that occur during user-related operations. They are raised in the domain layer
and handled appropriately by higher layers (application, interface).
"""


class InvalidEmailError(Exception):
    """
    Raised when an email address does not meet the required format or is invalid.

    This includes malformed syntax, missing components, or incorrect structure.
    Used during user creation, profile updates, and authentication processes.
    """
    pass


class InvalidUserError(Exception):
    """
    Raised when required user data is missing, empty, or contains invalid content.

    Covers fields such as names, role assignments, and status values.
    Indicates a violation of core user entity invariants.
    """
    pass


class InvalidPhoneNumberError(Exception):
    """
    Raised when a phone number does not conform to the E.164 format standard.

    The expected format is '+CountryCodeNumber' without spaces or special characters.
    Applies to both creation and update operations involving contact information.
    """
    pass