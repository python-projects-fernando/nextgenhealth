"""
Base Specification pattern implementation.

Defines an abstract interface for business rule specifications,
enabling validation and composition of domain rules through logical operations
such as AND, OR, and NOT. Supports the creation of complex, reusable, and testable
business logic in a clean and expressive way.
"""
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, TYPE_CHECKING

if TYPE_CHECKING:
    from .and_specification import AndSpecification
    from .or_specification import OrSpecification
    from .not_specification import NotSpecification

T = TypeVar('T')


class Specification(Generic[T], ABC):
    """
    Abstract base class for domain rule specifications.

    Represents a business rule that evaluates whether a candidate object
    satisfies a given condition. Specifications can be composed using logical
    operators (and_, or_, not_) to build more complex validation logic.

    This pattern promotes high cohesion, reusability, and clarity in enforcing
    domain invariants across different use cases.
    """

    @abstractmethod
    def is_satisfied_by(self, candidate: T) -> bool:
        """
        Determines whether the candidate satisfies this specification.

        Args:
            candidate (T): The object to evaluate against the rule.

        Returns:
            bool: True if the rule is satisfied; False otherwise.
        """
        pass

    def and_(self, other: 'Specification[T]') -> 'AndSpecification[T]':
        """
        Composes this specification with another using logical AND.

        The resulting specification is satisfied only if both this and the
        provided specification are satisfied.

        Args:
            other (Specification[T]): Another specification to combine.

        Returns:
            AndSpecification[T]: A new composite specification.
        """
        from .and_specification import AndSpecification
        return AndSpecification(self, other)

    def or_(self, other: 'Specification[T]') -> 'OrSpecification[T]':
        """
        Composes this specification with another using logical OR.

        The resulting specification is satisfied if at least one of the
        two specifications is satisfied.

        Args:
            other (Specification[T]): Another specification to combine.

        Returns:
            OrSpecification[T]: A new composite specification.
        """
        from .or_specification import OrSpecification
        return OrSpecification(self, other)

    def not_(self) -> 'NotSpecification[T]':
        """
        Negates this specification using logical NOT.

        The resulting specification is satisfied if this specification
        is NOT satisfied by the candidate.

        Returns:
            NotSpecification[T]: A new negated specification.
        """
        from .not_specification import NotSpecification
        return NotSpecification(self)