# src/user_management/infrastructure/models/user_model.py
"""
ORM model for the User entity.

Maps the domain User to a PostgreSQL table using SQLAlchemy.
Keeps persistence concerns separate from domain logic.
"""

from sqlalchemy import Column, String, Date, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID
import uuid

from user_management.domain.enums import UserRole, UserStatus
from user_management.infrastructure.models.base import Base


class UserModel(Base):
    __tablename__ = "users"

    uuid: Mapped[UUID] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    date_of_birth: Mapped[Date] = mapped_column(Date, nullable=False)
    user_role: Mapped[str] = mapped_column(Enum(UserRole), nullable=False)
    user_status: Mapped[UserStatus] = mapped_column(Enum(UserStatus), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)

    def __repr__(self):
        return f"<UserModel(uuid={self.uuid}, email={self.email})>"