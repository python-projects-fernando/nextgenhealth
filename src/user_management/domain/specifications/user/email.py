import re
from .. import Specification


class ValidEmailSpecification(Specification[str]):
    """
    Specification that validates whether a given string is a valid email address.

    A valid email must:
    - Not be empty or None
    - Follow the general format local-part@domain.tld
    - Contain valid characters and proper domain structure

    This rule is enforced during user creation and profile updates to ensure data integrity.
    """

    def is_satisfied_by(self, email: str) -> bool:
        """
        Checks if the provided string satisfies the email format requirements.

        Args:
            email (str): The email address to validate. Can be None or empty.

        Returns:
            bool: True if the email is valid; False otherwise.
        """
        if not email:
            return False
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None