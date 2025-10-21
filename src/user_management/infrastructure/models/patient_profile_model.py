from sqlalchemy import String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
import uuid
from user_management.infrastructure.models.base import Base

class PatientProfileModel(Base):
    __tablename__ = "patient_profiles"

    user_uuid: Mapped[uuid.UUID] = mapped_column(
        String(36),
        ForeignKey("users.uuid"),
        primary_key=True,
        nullable=False
    )

    emergency_contact_name: Mapped[str] = mapped_column(String(255), nullable=False)
    emergency_contact_phone: Mapped[str] = mapped_column(String(20), nullable=False)
    insurance_info: Mapped[str] = mapped_column(Text, nullable=False)
    preferred_language: Mapped[str] = mapped_column(String(10), nullable=False)
    medical_history_summary: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    def __repr__(self) -> str:
        return (f"<PatientProfileModel(user_uuid={self.user_uuid}, "
                f"emergency_contact_name='{self.emergency_contact_name}')>")
