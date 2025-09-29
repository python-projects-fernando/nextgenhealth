"""
Specification that validates whether updated_at is consistent with created_at.

A valid relation requires:
- updated_at must be greater than or equal to created_at

Used to enforce chronological integrity in the User aggregate.
"""

from datetime import datetime
from .. import Specification


class ValidUpdatedAtRelativeToCreatedAtSpecification(Specification):
    """
    Specification to validate that updated_at is not earlier than created_at.

    Enforces chronological consistency in audit timestamps.
    """

    def __init__(self, created_at: datetime):
        self.created_at = created_at

    def is_satisfied_by(self, updated_at: datetime) -> bool:
        """
        Checks if updated_at is not earlier than created_at.

        Args:
            updated_at: The updated_at timestamp to validate.

        Returns:
            bool: True if updated_at >= created_at; False otherwise.
        """
        if not isinstance(updated_at, datetime):
            return False
        return updated_at >= self.created_at  # ✅ Corrigido