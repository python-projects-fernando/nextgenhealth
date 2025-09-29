import re
from datetime import datetime, timezone, timedelta
from uuid import UUID

from user_management.domain.exceptions import InvalidPatientProfileUserUUIDError, \
    InvalidPatientProfileEmergencyContactNameError, InvalidPatientProfileEmergencyContactPhoneError, \
    InvalidPatientProfileInsuranceInfoError, InvalidPatientProfilePreferredLanguageError, \
    InvalidPatientProfileMedicalHistorySummaryError, InvalidPatientProfileCreatedAtError, \
    InvalidPatientProfileUpdatedAtError
from user_management.domain.specifications.patient_profile import ValidEmergencyContactNameSpecification, \
    ValidEmergencyContactPhoneSpecification, ValidInsuranceInfoSpecification, ValidPreferredLanguageSpecification, \
    ValidMedicalHistorySummarySpecification
from user_management.domain.validation.patient_profile import PatientProfileValidator


class PatientProfile:
    def __init__(self,
                 user_uuid: UUID,
                 emergency_contact_name: str,
                 emergency_contact_phone: str,
                 insurance_info: str,
                 preferred_language: str,
                 medical_history_summary: str,
                 created_at: datetime,
                 updated_at: datetime,
                 ):

        PatientProfileValidator.validate(user_uuid, emergency_contact_name, emergency_contact_phone, insurance_info,
                                         preferred_language,medical_history_summary,created_at,updated_at)



        self.user_uuid = user_uuid
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone
        self.insurance_info = insurance_info
        self.preferred_language = preferred_language
        self.medical_history_summary = medical_history_summary
        self.created_at = created_at
        self.updated_at = updated_at


    def update_medical_info(self,
                            emergency_contact_name: str,
                            emergency_contact_phone:str,
                            insurance_info: str,
                            preferred_language: str,
                            medical_history_summary: str):

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


        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone
        self.insurance_info = insurance_info
        self.preferred_language = preferred_language
        self.medical_history_summary = medical_history_summary
        self.updated_at = datetime.now(timezone.utc)