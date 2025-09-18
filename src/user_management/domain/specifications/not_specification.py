from .specification import Specification
from typing import Generic, TypeVar

T = TypeVar('T')


class NotSpecification(Specification[T]):
    """
    Composes a specification with logical negation (NOT).

    This specification is satisfied if the wrapped specification is NOT satisfied.
    Useful for expressing rules like "user must not be locked" or "email must not be blacklisted".

    Example:
        active_user_spec = NotSpecification(IsLockedSpecification())
        if active_user_spec.is_satisfied_by(user):
            grant_access()
    """

    def __init__(self, spec: Specification[T]):
        """
        Initializes the negated specification with a child specification.

        Args:
            spec (Specification[T]): The specification to negate.
        """
        self.spec = spec

    def is_satisfied_by(self, candidate: T) -> bool:
        """
        Evaluates whether the candidate does NOT satisfy the wrapped specification.

        Args:
            candidate (T): The object to validate against the negated rule.

        Returns:
            bool: True if the original specification fails; False otherwise.
        """
        return not self.spec.is_satisfied_by(candidate)