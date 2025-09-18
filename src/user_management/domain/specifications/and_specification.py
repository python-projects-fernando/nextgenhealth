from .specification import Specification
from typing import Generic, TypeVar

T = TypeVar('T')


class AndSpecification(Specification[T]):
    """
    Composes multiple specifications using logical AND.

    This specification is satisfied only if all composed specifications
    are satisfied by the candidate object. Useful for enforcing multiple
    business rules simultaneously during validation workflows.

    Example:
        combined = ValidEmailSpecification().and_(ValidNameSpecification())
        combined.is_satisfied_by(user_data)  # True only if both pass
    """

    def __init__(self, *specs: Specification[T]):
        """
        Initializes the composite specification with one or more child specifications.

        Args:
            *specs (Specification[T]): One or more specifications to combine.
        """
        self.specs = specs

    def is_satisfied_by(self, candidate: T) -> bool:
        """
        Evaluates whether the candidate satisfies all composed specifications.

        Args:
            candidate (T): The object to validate against all specifications.

        Returns:
            bool: True if all specifications are satisfied; False otherwise.
        """
        return all(spec.is_satisfied_by(candidate) for spec in self.specs)