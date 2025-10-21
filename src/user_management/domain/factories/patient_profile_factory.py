from user_management.domain.entities import PatientProfile
from datetime import datetime, timezone

class PatientProfileFactory:

    @staticmethod
    def create_from_command(command) -> PatientProfile:
        now = datetime.now(timezone.utc)

        try:
            patient = PatientProfile(
                user_uuid=command.user_uuid,
                emergency_contact_name=command.emergency_contact_name,
                emergency_contact_phone=command.emergency_contact_phone,
                insurance_info=command.insurance_info,
                preferred_language=command.preferred_language,
                medical_history_summary=command.medical_history_summary,
                created_at=now,
                updated_at=now,
            )
        except Exception as e:
            raise

        return patient