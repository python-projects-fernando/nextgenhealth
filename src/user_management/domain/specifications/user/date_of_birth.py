from datetime import date, timedelta
from .. import Specification


class ValidDateOfBirthSpecification(Specification[date]):
    """
    Specification that validates whether a given date of birth is valid.

    A valid date of birth must:
    - Not be None
    - Not be in the future (after today)
    - Represent a realistic human age (not older than 150 years)

    This rule is enforced during user creation and profile updates to ensure data integrity.
    """

    def is_satisfied_by(self, dob: date) -> bool:
        """
        Checks if the provided date of birth satisfies all validation rules.

        Args:
            dob (date): The date of birth to validate. Can be None.

        Returns:
            bool: True if the date is valid; False otherwise.
        """
        if dob is None:
            return False

        today = date.today()
        if dob > today:
            return False

        min_allowed_date = today - timedelta(days=150 * 365.25)
        return dob >= min_allowed_date