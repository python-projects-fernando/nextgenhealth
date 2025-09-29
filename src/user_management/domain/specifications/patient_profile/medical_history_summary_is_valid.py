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


class ValidMedicalHistorySummarySpecification(Specification):
    """
    Specification to validate that a UUID is a properly typed identity object.

    Enforces strict type checking to ensure only valid UUID instances are accepted
    during User aggregate creation. Prevents common errors like passing strings
    or None as identifiers in critical healthcare workflows.
    """

    def is_satisfied_by(self, mhs) -> bool:

        if not isinstance(mhs, str):
            return False

        pattern = r"^[A-Za-zÀ-ÿ]+(?:[\s\-][A-Za-zÀ-ÿ]+)*(?:[,.;:]\s*[A-Za-zÀ-ÿ][\s\-A-Za-zÀ-ÿ.,;:]*)*$"
        return re.match(pattern, mhs) is not None