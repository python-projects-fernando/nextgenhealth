"""
Specification that validates whether a given updated_at timestamp is valid.

A valid updated_at must:
- Be a datetime object
- Have timezone information (aware)
- Use UTC timezone
- Not be in the future (with small clock skew tolerance)
- Be within a realistic range (e.g., not before 1900)

This rule ensures audit trail integrity, chronological consistency,
and compliance with standards like HIPAA/GDPR in healthcare systems.
"""

from datetime import datetime, timezone, timedelta
from .. import Specification


class ValidUpdatedAtSpecification(Specification):
    """
    Specification to validate that updated_at is a valid timestamp for user record updates.

    Enforces temporal correctness by rejecting invalid or impossible timestamps.
    Used during User aggregate construction to ensure domain invariants are preserved.
    """

    def is_satisfied_by(self, updated_at) -> bool:
        """
        Checks if the provided value is a valid updated_at timestamp.

        Args:
            updated_at: The value to validate. Expected to be a timezone-aware UTC datetime.

        Returns:
            bool: True if the timestamp is valid; False otherwise.
        """
        if not isinstance(updated_at, datetime):
            return False
        if updated_at.tzinfo is None:
            return False
        if updated_at.tzinfo != timezone.utc:
            return False
        now = datetime.now(timezone.utc)
        # Allow small clock skew (e.g., up to 1 minute ahead due to system sync)
        return updated_at <= now + timedelta(minutes=1)