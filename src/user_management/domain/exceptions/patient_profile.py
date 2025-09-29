from user_management.domain.exceptions import DomainError


class InvalidPatientProfileError(DomainError):
    pass

class InvalidPatientProfileUserUUIDError(InvalidPatientProfileError):
    pass

class InvalidPatientProfileEmergencyContactNameError(InvalidPatientProfileError):
    pass

class InvalidPatientProfileEmergencyContactPhoneError(InvalidPatientProfileError):
    pass

class InvalidPatientProfileInsuranceInfoError(InvalidPatientProfileError):
    pass

class InvalidPatientProfilePreferredLanguageError(InvalidPatientProfileError):
    pass

class InvalidPatientProfileMedicalHistorySummaryError(InvalidPatientProfileError):
    pass

class InvalidPatientProfileCreatedAtError(InvalidPatientProfileError):
    pass

class InvalidPatientProfileUpdatedAtError(InvalidPatientProfileError):
    pass