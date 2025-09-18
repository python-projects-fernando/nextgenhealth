# src/user_management/domain/specifications/or_specification.py
from .specification import Specification
from typing import Generic, TypeVar

T = TypeVar('T')


class OrSpecification(Specification[T]):
    """
    Composes multiple specifications using logical OR.

    This specification is satisfied if at least one of the composed specifications
    is satisfied by the candidate object. Useful for defining alternative valid states
    or flexible business rules during validation workflows.

    Example:
        eligible_role = IsDoctorSpecification().or_(IsNurseSpecification())
        if eligible_role.is_satisfied_by(user):
            assign_to_unit()
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
        Evaluates whether the candidate satisfies at least one of the composed specifications.

        Args:
            candidate (T): The object to validate against the specifications.

        Returns:
            bool: True if any specification is satisfied; False otherwise.
        """
        return any(spec.is_satisfied_by(candidate) for spec in self.specs)