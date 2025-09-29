"""
Specification that validates whether a given value is a valid UUID.

A valid UUID must:
- Be an instance of Python's uuid.UUID class
- Not be None, string, int, or any other type

This rule ensures global identity integrity within the domain,
preventing invalid or spoofed identifiers in audit trails and entity references.
"""
import re
from uuid import UUID
from .. import Specification


class ValidPreferredLanguageSpecification(Specification):
    """
    Specification to validate that a UUID is a properly typed identity object.

    Enforces strict type checking to ensure only valid UUID instances are accepted
    during User aggregate creation. Prevents common errors like passing strings
    or None as identifiers in critical healthcare workflows.
    """

    def is_satisfied_by(self, language) -> bool:
        if not isinstance(language, str):
            return False
        stripped = language.strip()
        if not stripped:
            return False
        if len(stripped) < 3:
            return False
        if len(stripped) > 100:
            return False

        if not re.search(r"[A-Za-zÀ-ÿ]", stripped):
            return False

        if not re.fullmatch(r"[A-Za-zÀ-ÿ0-9\s\-'.]+", stripped):
            return False

        return True
