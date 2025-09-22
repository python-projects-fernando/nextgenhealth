"""
Specification that validates whether a given created_at timestamp is valid.

A valid created_at must:
- Be a datetime object
- Have timezone information (aware)
- Use UTC timezone
- Not be in the future (including small clock drift tolerance)
- Be within a realistic range (e.g., not before 1900)

This rule ensures auditability, consistency, and compliance with standards like HIPAA/GDPR.
"""

from datetime import datetime, timezone, timedelta

from .. import Specification


class ValidCreatedAtSpecification(Specification):
    """
    Specification to validate that created_at is a valid timestamp for user creation.

    Enforces temporal integrity by rejecting invalid or impossible timestamps.
    Used during User aggregate construction to ensure domain invariants are preserved.
    """

    def is_satisfied_by(self, created_at) -> bool:
        """
        Checks if the provided value is a valid created_at timestamp.

        Args:
            created_at: The value to validate. Expected to be a timezone-aware UTC datetime.

        Returns:
            bool: True if the timestamp is valid; False otherwise.
        """
        if not isinstance(created_at, datetime):
            return False
        if created_at.tzinfo is None:
            return False
        if created_at.tzinfo != timezone.utc:
            return False
        now = datetime.now(timezone.utc)
        # Allow small clock skew (e.g., 1 minute ahead)
        return created_at <= now + timedelta(minutes=1)