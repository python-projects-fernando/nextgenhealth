# src/user_management/infrastructure/models/user_credentials_model.py
"""
ORM model for the UserCredentials value object.

Stores sensitive authentication data (hashed password) separately from User.
Linked via foreign key to ensure data integrity and security.

This model maps the domain UserCredentials to a PostgreSQL table,
keeping persistence concerns separate from business logic.
"""

from uuid import UUID
from sqlalchemy import String, LargeBinary, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .user_model import Base


class UserCredentialsModel(Base):
    """
    ORM model representing user authentication credentials.

    Maps to the 'user_credentials' table in PostgreSQL.
    Ensures secure storage of hashed passwords with referential integrity to 'users'.
    """

    __tablename__ = "user_credentials"

    user_uuid: Mapped[UUID] = mapped_column(String(36), ForeignKey("users.uuid"), primary_key=True)
    hashed_password: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)

    def __repr__(self):
        return f"<UserCredentialsModel(user_uuid={self.user_uuid})>"