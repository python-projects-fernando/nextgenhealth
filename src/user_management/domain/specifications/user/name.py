import re
from .. import Specification


class ValidNameSpecification(Specification[str]):
    """
    Specification that validates whether a given string is a valid name.

    A valid name must:
    - Not be empty or consist only of whitespace
    - Contain only alphabetic characters (a-z, A-Z) and spaces
    - Not include numbers, special characters, or symbols

    This rule is enforced during user creation and profile updates to ensure data consistency.
    """

    def is_satisfied_by(self, name: str) -> bool:
        """
        Checks if the provided string satisfies the name format requirements.

        Args:
            name (str): The name to validate. Can be None or empty.

        Returns:
            bool: True if the name is valid; False otherwise.
        """
        if not name or not name.strip():
            return False
        pattern = r"^[A-Za-z\s]+$"
        return re.match(pattern, name) is not None