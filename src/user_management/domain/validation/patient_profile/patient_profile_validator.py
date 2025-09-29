from datetime import datetime
from uuid import UUID

from user_management.domain.exceptions import InvalidPatientProfileUserUUIDError, \
    InvalidPatientProfileEmergencyContactNameError, InvalidPatientProfileEmergencyContactPhoneError, \
    InvalidPatientProfileInsuranceInfoError, InvalidPatientProfilePreferredLanguageError, \
    InvalidPatientProfileMedicalHistorySummaryError, InvalidPatientProfileCreatedAtError, \
    InvalidPatientProfileUpdatedAtError

from user_management.domain.specifications.patient_profile import ValidUserUUIDSpecification, \
    ValidEmergencyContactNameSpecification, ValidEmergencyContactPhoneSpecification, ValidInsuranceInfoSpecification, \
    ValidPreferredLanguageSpecification, ValidMedicalHistorySummarySpecification, ValidCreatedAtSpecification, \
    ValidUpdatedAtSpecification, ValidUpdatedAtRelativeToCreatedAtSpecification


class PatientProfileValidator:

    @staticmethod
    def validate(
            user_uuid: UUID,
            emergency_contact_name: str,
            emergency_contact_phone: str,
            insurance_info: str,
            preferred_language: str,
            medical_history_summary: str,
            created_at: datetime,
            updated_at: datetime,
    ) -> None:

        if not ValidUserUUIDSpecification().is_satisfied_by(user_uuid):
            raise InvalidPatientProfileUserUUIDError("Invalid user uuid")

        if not ValidEmergencyContactNameSpecification().is_satisfied_by(emergency_contact_name):
            raise InvalidPatientProfileEmergencyContactNameError("Invalid emergency contact name")

        if not ValidEmergencyContactPhoneSpecification().is_satisfied_by(emergency_contact_phone):
            raise InvalidPatientProfileEmergencyContactPhoneError("Invalid emergency contact phone")

        if not ValidInsuranceInfoSpecification().is_satisfied_by(insurance_info):
            raise InvalidPatientProfileInsuranceInfoError("Invalid insurance info")

        if not ValidPreferredLanguageSpecification().is_satisfied_by(preferred_language):
            raise InvalidPatientProfilePreferredLanguageError("Invalid preferred language")

        if not ValidMedicalHistorySummarySpecification().is_satisfied_by(medical_history_summary):
            raise InvalidPatientProfileMedicalHistorySummaryError("Invalid medical history summary")

        if not ValidCreatedAtSpecification().is_satisfied_by(created_at):
            raise InvalidPatientProfileCreatedAtError("Invalid created at date")

        if not ValidUpdatedAtSpecification().is_satisfied_by(updated_at):
            raise InvalidPatientProfileUpdatedAtError("Invalid updated at date")

        if not ValidUpdatedAtRelativeToCreatedAtSpecification(created_at).is_satisfied_by(updated_at):
            raise InvalidPatientProfileUpdatedAtError("updated_at cannot be earlier than created_at")
