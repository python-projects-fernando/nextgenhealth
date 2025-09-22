"""
Specification that validates whether a given value is a valid email address.

A valid email must:
- Be a string
- Not be empty, None, or whitespace-only
- Follow the format local-part@domain.tld
- Contain exactly one '@' symbol
- Have non-empty local and domain parts
- Not start/end with dots or contain consecutive dots
- Domain part must contain at least one '.'

This rule enforces data integrity during user registration, profile updates,
and authentication workflows in compliance with common RFC-like formatting standards.
"""

from .. import Specification


class ValidEmailSpecification(Specification):
    """
    Specification to validate that an email address conforms to structural rules.

    Ensures only properly formatted emails are accepted in the domain layer.
    Used within the User aggregate to enforce fail-fast validation and prevent invalid identities.
    """

    def is_satisfied_by(self, email) -> bool:
        """
        Checks if the provided value is a valid email address.

        Args:
            email: The value to validate. Must be a string to pass.

        Returns:
            bool: True if the email is valid; False otherwise.
        """
        if not isinstance(email, str):
            return False

        if not email or not email.strip():
            return False

        # Basic structural checks
        if " " in email or ".." in email:
            return False
        if email.startswith(".") or email.endswith("."):
            return False
        if "@@" in email:
            return False
        if email.count("@") != 1:
            return False

        try:
            local, domain = email.split("@")
        except ValueError:
            return False

        if not local or not domain:
            return False
        if local.startswith(".") or local.endswith("."):
            return False
        if domain.startswith(".") or domain.endswith("."):
            return False
        if "." not in domain:
            return False

        return True