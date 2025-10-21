from sqlalchemy.ext.asyncio import AsyncSession

from user_management.application.repositories import UserRepository
from user_management.application.repositories.patient_profile_repository import PatientProfileRepository
from user_management.domain.entities import PatientProfile
from user_management.infrastructure.models.patient_profile_model import PatientProfileModel


class PostgresPatientProfileRepository(PatientProfileRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, patient_profile: PatientProfile) -> None:
        patient_profile_model = PatientProfileModel(
            user_uuid=str(patient_profile.user_uuid),
            emergency_contact_name=patient_profile.emergency_contact_name,
            emergency_contact_phone=patient_profile.emergency_contact_phone,
            insurance_info=patient_profile.insurance_info,
            preferred_language=patient_profile.preferred_language,
            medical_history_summary=patient_profile.medical_history_summary,
            created_at=patient_profile.created_at,
            updated_at=patient_profile.updated_at,
        )

        self.session.add(patient_profile_model)
        await self.session.commit()