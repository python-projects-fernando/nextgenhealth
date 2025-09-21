"""
Test factories for User entity.
Provides reusable functions to create valid User instances with minimal boilerplate.
"""
from datetime import date, datetime, timezone, timedelta
from uuid import UUID

from user_management.domain.enums import UserRole, UserStatus
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

    now = datetime.now(tz=timezone.utc)
    one_month_ago = now - timedelta(days=30)

    defaults = {
        "uuid": UUID("12345678-1234-5678-1234-567812345678"),
        "email": "validexample.com",
        "first_name": "Fernando",
        "last_name": "Magalhaes",
        "phone": "+81312345678",
        "date_of_birth": date(1982, 3, 18),
        "user_role": UserRole.ADMINISTRATOR,
        "user_status": UserStatus.ACTIVE,
        "created_at": one_month_ago,
        "updated_at": now,
    }

    defaults.update(kwargs)
    return User(**defaults)