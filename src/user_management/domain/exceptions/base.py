"""
Base domain exceptions for the NextGenHealth system.
All other domain-specific errors inherit from these.
"""

class DomainError(Exception):
    """
    Base exception class for all business rule violations in the domain.

    This is not raised directly, but serves as the parent for all domain exceptions.
    Helps with broad exception handling at higher layers.
    """
    pass