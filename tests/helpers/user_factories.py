"""
Test factories for User entity.
Provides reusable functions to create valid User instances with minimal boilerplate.
"""

from uuid import UUID
from src.user_management.domain.entities.user import User

def create_valid_user(**kwargs):
    """
        Factory function to create a User instance with valid default values.

        All parameters can be overridden via keyword arguments.

        Args:
            **kwargs: Override any field (e.g., email="", first_name="Custom")

        Returns:
            User: A fully initialized User instance.
    """

    defaults = {
        "uuid": UUID("12345678-1234-5678-1234-567812345678"),
        "email": "valid@example.com",
        "first_name": "Fernando",
        "last_name": "Magalhaes",
        "phone": "+81312345678",
    }

    defaults.update(kwargs)
    return User(**defaults)