"""
Specification that validates whether a given date of birth is valid.

A valid date of birth must:
- Be a date object (not string or datetime)
- Not be None
- Not be in the future
- Represent a realistic human lifespan (e.g., not before 1900 or older than ~150 years)

This rule ensures data integrity, compliance with personal data standards,
and consistency across healthcare workflows (e.g., patient registration).
"""

from datetime import date, timedelta
from .. import Specification


class ValidDateOfBirthSpecification(Specification):
    """
    Specification to validate that a date of birth is realistic and properly formatted.

    Enforces domain invariants for user age during creation and updates.
    Used within the User aggregate to prevent invalid or impossible dates.
    """

    def is_satisfied_by(self, dob) -> bool:
        """
        Checks if the provided value is a valid date of birth.

        Args:
            dob: The value to validate. Expected to be a `datetime.date` object.

        Returns:
            bool: True if the date is valid; False otherwise.
        """
        if dob is None:
            return False

        if not isinstance(dob, date):
            return False

        today = date.today()
        if dob > today:
            return False

        # Minimum allowed date: ~150 years back (accounts for leap years)
        min_allowed_date = today - timedelta(days=150 * 365.25)
        return dob >= min_allowed_date