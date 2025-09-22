"""
Specification that validates whether a given value is a valid personal name.

A valid name must:
- Be a string
- Not be None, empty, or consist only of whitespace
- Contain only alphabetic characters (a-z, A-Z)
- Allow single spaces between words (e.g., "John Doe")
- Not include numbers, special characters, accents, or symbols (e.g., @, $, ', -)

This rule ensures data consistency, supports international compliance,
and prevents injection risks in user identity management.
"""

import re
from .. import Specification


class ValidNameSpecification(Specification):
    """
    Specification to validate that a first or last name conforms to allowed format rules.

    Enforces clean, readable names within the User aggregate.
    Used during creation and updates to maintain data integrity in healthcare workflows.
    """

    def is_satisfied_by(self, name) -> bool:
        """
        Checks if the provided value is a valid name.

        Args:
            name: The value to validate. Expected to be a string.

        Returns:
            bool: True if the name is valid; False otherwise.
        """
        if not isinstance(name, str):
            return False

        if not name or not name.strip():
            return False

        # Matches one or more words, each starting with a letter, separated by single spaces
        # Example: "John", "Mary Jane", but not "Mary  Jane" (double space) or "O'Connor"
        pattern = r"^[A-Za-z]+(?: [A-Za-z]+)*$"
        return re.match(pattern, name) is not None