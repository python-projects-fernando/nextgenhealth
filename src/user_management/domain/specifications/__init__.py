"""
Public API for the Specification pattern in the domain layer.

This module provides the foundational building blocks for expressing and composing
business rules as reusable, testable objects. It enables logical composition via
and_, or_, and not_ methods, supporting complex validation workflows in a clean,
readable way.

Import specification base classes directly using:
from .specification import Specification
from .and_specification import AndSpecification
from .or_specification import OrSpecification
from .not_specification import NotSpecification
)
"""

from .specification import Specification
from .and_specification import AndSpecification
from .or_specification import OrSpecification
from .not_specification import NotSpecification

__all__ = [
    "Specification",
    "AndSpecification",
    "OrSpecification",
    "NotSpecification",
]