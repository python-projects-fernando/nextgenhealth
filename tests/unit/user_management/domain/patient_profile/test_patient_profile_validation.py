from uuid import UUID

import pytest

from datetime import datetime, timezone, date, timedelta

from tests.helpers.domain import create_valid_patient_profile
from user_management.domain.exceptions import (InvalidPatientProfileUserUUIDError,
                                               InvalidPatientProfileEmergencyContactNameError,
                                               InvalidPatientProfileEmergencyContactPhoneError,
                                               InvalidPatientProfileInsuranceInfoError,
                                               InvalidPatientProfilePreferredLanguageError,
                                               InvalidPatientProfileMedicalHistorySummaryError,
                                               InvalidPatientProfileCreatedAtError,
                                               InvalidPatientProfileUpdatedAtError)



def test_patient_profile_creation_fails_when_uuid_is_not_a_valid_uuid_instance():
    invalid_values = [
        None,
        "",
        "not-a-uuid",
        123,
        {},
        [],
        True,
        b"raw-bytes"
    ]

    for value in invalid_values:
        with pytest.raises(InvalidPatientProfileUserUUIDError):
            create_valid_patient_profile(user_uuid=value)


def test_patient_profile_creation_succeeded_when_uuid_is_a_valid_uuid_instance():
    valid_uuid = UUID("12345678-1234-5678-1234-567812345678")

    patient = create_valid_patient_profile(user_uuid=valid_uuid)

    assert isinstance(patient.user_uuid, UUID)


def test_patient_profile_creation_fails_when_emergency_contact_name_is_not_valid():
    invalid_emergency_contact_names = [
        "",  # empty string
        "   ",  # whitespace only
        "João",  # contains accent
        "Mary  Jane",  # multiple consecutive spaces
        "Carlos$",  # contains special character
        "Ana@"  # contains symbol
    ]

    for name in invalid_emergency_contact_names:
        with pytest.raises(InvalidPatientProfileEmergencyContactNameError):
            create_valid_patient_profile(emergency_contact_name=name)


def test_patient_profile_creation_succeeds_with_valid_emergency_contact_name():

    valid_name = "Will Magalhaes"

    patient = create_valid_patient_profile(emergency_contact_name = valid_name)

    assert patient.emergency_contact_name == valid_name


def test_patient_profile_creation_fails_when_emergency_contact_phone_is_not_valid():
    invalid_phones = [
        "",
        "   ",
        "+",
        "(+123) 456-7890",
    ]

    for phone in invalid_phones:
        with pytest.raises(InvalidPatientProfileEmergencyContactPhoneError):
            create_valid_patient_profile(emergency_contact_phone=phone)


def test_patient_profile_creation_succeeds_with_valid_emergency_contact_phone():

    valid_phone = "+33142948800"

    patient = create_valid_patient_profile(emergency_contact_phone=valid_phone)

    assert patient.emergency_contact_phone == valid_phone


def test_patient_profile_creation_fails_when_insurance_info_is_not_valid():
    invalid_insurance_infos =[
        None,
        "",
        "   ",
         "12345",
         "ABC@XYZ",
         "!@#$%^&*()",
         "INSURANCE_INFO_123",
         "FOREVER HEALTHY INSURANCE!123",
         "FOREVER HEALTHY INSURANCE#",
         "FOREVER HEALTHY INSURANCE$",
    ]

    for insurance in invalid_insurance_infos:
        with pytest.raises(InvalidPatientProfileInsuranceInfoError):
            create_valid_patient_profile(insurance_info=insurance)


def test_patient_profile_creation_succeeds_with_valid_insurance_info():

    insurance_info = "Forever Healthy Insurance"

    patient = create_valid_patient_profile(insurance_info=insurance_info)

    assert patient.insurance_info == insurance_info


def test_patient_profile_creation_fails_when_preferred_language_is_not_valid():
    invalid_preferred_languages =[
        None,
        "",
        "   ",
         "12345",
         "ABC@XYZ",
         "!@#$%^&*()",
         "ENGLISH_123",
         "Portuguese!123",
         "Spanish#",
         "German$",
    ]

    for language in invalid_preferred_languages:
        with pytest.raises(InvalidPatientProfilePreferredLanguageError):
            create_valid_patient_profile(preferred_language=language)


def test_patient_profile_creation_succeeds_with_valid_preferred_language():

    preferred_language = "Portuguese"

    patient = create_valid_patient_profile(preferred_language=preferred_language)

    assert patient.preferred_language == preferred_language


def test_patient_profile_creation_fails_when_medical_history_summary_is_not_valid():
    medical_history_summaries = [
        None,
        "hypertension@2020",
        "asthma#treatment",
        "epilepsy$meds",

    ]

    for mhs in medical_history_summaries:
        with pytest.raises(InvalidPatientProfileMedicalHistorySummaryError):
            create_valid_patient_profile(medical_history_summary=mhs)


def test_patient_profile_creation_succeeds_with_valid_medical_history_summary():

    medical_history_summary = "Portuguese"

    patient = create_valid_patient_profile(medical_history_summary=medical_history_summary)

    assert patient.medical_history_summary == medical_history_summary


def test_patient_profile_creation_fails_when_created_at_is_not_a_datetime():

    invalid_values = [None, "", "2024-01-01", 123, {}, [], True, b"raw"]

    for value in invalid_values:
        with pytest.raises(InvalidPatientProfileCreatedAtError):
            create_valid_patient_profile(created_at=value)


def test_patient_profile_creation_fails_when_created_at_has_no_timezone():

    naive_dt = datetime(2024, 1, 1, 10, 0, 0)  # No timezone
    with pytest.raises(InvalidPatientProfileCreatedAtError):
        create_valid_patient_profile(created_at=naive_dt)


def test_patient_profile_creation_fails_when_created_at_is_not_in_utc():

    non_utc = datetime(2024, 1, 1, 10, 0, 0, tzinfo=timezone(timedelta(hours=-3)))  # UTC-3
    with pytest.raises(InvalidPatientProfileCreatedAtError):
        create_valid_patient_profile(created_at=non_utc)


def test_patient_profile_creation_fails_when_created_at_is_in_the_future():

    future_dt = datetime(3000, 1, 1, tzinfo=timezone.utc)
    with pytest.raises(InvalidPatientProfileCreatedAtError):
        create_valid_patient_profile(created_at=future_dt)


def test_patient_profile_creation_succeeds_with_valid_created_at():

    valid_dt = datetime(2024, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
    user = create_valid_patient_profile(created_at=valid_dt)
    assert user.created_at == valid_dt

#---------------------------------------------------------------------------------------------------------------------

def test_patient_profile_creation_fails_when_updated_at_is_not_a_datetime():
    """
    Verifies User instantiation fails when updated_at is not a datetime object.

    The domain requires updated_at to be a datetime instance.
    Inputs such as None, strings, integers, or other types should raise InvalidUpdatedAtError.
    """
    invalid_values = [None, "", "2024-01-01", 123, {}, [], True, b"raw"]

    for value in invalid_values:
        with pytest.raises(InvalidPatientProfileUpdatedAtError):
            create_valid_patient_profile(updated_at=value)


def test_patient_profile_creation_fails_when_updated_at_has_no_timezone():
    """
    Verifies User instantiation fails when updated_at is a naive datetime.

    The domain requires all timestamps to be timezone-aware.
    A datetime without tzinfo should raise InvalidUpdatedAtError.
    """
    naive_dt = datetime(2024, 1, 1, 10, 0, 0)  # No timezone
    with pytest.raises(InvalidPatientProfileUpdatedAtError):
        create_valid_patient_profile(updated_at=naive_dt)


def test_patient_profile_creation_fails_when_updated_at_is_not_in_utc():
    """
    Verifies User instantiation fails when updated_at uses a non-UTC timezone.

    The system standardizes on UTC for consistency and auditability.
    Any datetime with a non-UTC timezone should be rejected.
    """
    non_utc = datetime(2024, 1, 1, 10, 0, 0, tzinfo=timezone(timedelta(hours=-3)))  # UTC-3
    with pytest.raises(InvalidPatientProfileUpdatedAtError):
        create_valid_patient_profile(updated_at=non_utc)


def test_patient_profile_creation_fails_when_updated_at_is_in_the_future():
    """
    Verifies User instantiation fails when updated_at is in the future.

    Timestamps must represent real-world time. Future dates are invalid
    and should raise InvalidUpdatedAtError.
    """
    future_dt = datetime(3000, 1, 1, tzinfo=timezone.utc)
    with pytest.raises(InvalidPatientProfileUpdatedAtError):
        create_valid_patient_profile(updated_at=future_dt)


# tests/unit/user_management/domain/patient_profile/test_patient_profile_validation.py

def test_patient_profile_creation_succeeds_with_valid_updated_at():
    """
    Verifies that a PatientProfile can be created successfully with a valid updated_at timestamp.
    Ensures that valid timestamps (equal to or after created_at) are accepted.
    """
    # Arrange: Use consistent, valid timestamps
    # If the factory uses datetime.now(), we should control both values
    fixed_time = datetime(2024, 6, 15, 10, 30, 0, tzinfo=timezone.utc)
    # Or ensure updated_at is >= created_at

    # Option 1: Explicitly pass consistent values
    # created_at = fixed_time
    # updated_at = fixed_time # Equal is valid
    # Or
    # updated_at = datetime(2024, 6, 15, 11, 0, 0, tzinfo=timezone.utc) # Later is valid

    # Option 2: Modify the factory call to ensure consistency
    # Assuming create_valid_patient_profile uses datetime.now() internally for defaults,
    # we need to pass both to make sure they are consistent.
    created_at = datetime(2024, 6, 15, 10, 30, 0, tzinfo=timezone.utc)
    updated_at = datetime(2024, 6, 15, 10, 30, 0, tzinfo=timezone.utc) # Same time or later

    # Act
    patient_profile = create_valid_patient_profile(
        created_at=created_at,
        updated_at=updated_at
        # Pass other required fields if needed, or rely on factory defaults
    )

    # Assert
    assert patient_profile.updated_at == updated_at
    # Add other relevant assertions if needed


def test_patient_profile_creation_fails_when_updated_at_is_before_created_at():
    """
    Verifies that creating a PatientProfile fails if updated_at is set to a time
    before created_at, raising InvalidPatientProfileUpdatedAtError.
    """
    # Arrange
    created_at = datetime(2024, 1, 2, tzinfo=timezone.utc)  # Later date
    updated_at = datetime(2024, 1, 1, tzinfo=timezone.utc)  # Earlier date

    # Act & Assert
    with pytest.raises(InvalidPatientProfileUpdatedAtError) as exc_info:
        create_valid_patient_profile(created_at=created_at, updated_at=updated_at)

    # Optional: Check the error message
    assert "earlier than created_at" in str(exc_info.value)



def test_update_medical_info_succeeds_with_valid_data():
    patient_profile = create_valid_patient_profile()
    old_updated_at = patient_profile.updated_at

    patient_profile.update_medical_info(
        emergency_contact_name = "Lili Magalhaes",
        emergency_contact_phone = "+5521331410455",
        insurance_info = "Forever Healthy Insurance",
        preferred_language = "Portuguese",
        medical_history_summary = "Diabetes Mellitus",
    )

    assert patient_profile.emergency_contact_name == "Lili Magalhaes"
    assert patient_profile.emergency_contact_phone == "+5521331410455"
    assert patient_profile.insurance_info == "Forever Healthy Insurance"
    assert patient_profile.preferred_language == "Portuguese"
    assert patient_profile.medical_history_summary == "Diabetes Mellitus"
    assert patient_profile.updated_at > old_updated_at


def test_update_medical_info_fails_when_emergency_contact_name_is_invalid():
    patient_profile = create_valid_patient_profile()

    with pytest.raises(InvalidPatientProfileEmergencyContactNameError):
        patient_profile.update_medical_info(
            emergency_contact_name="",
            emergency_contact_phone="+5521331410455",
            insurance_info="Forever Healthy Insurance",
            preferred_language="Portuguese",
            medical_history_summary="Diabetes Mellitus",
        )


def test_update_medical_info_fails_when_emergency_contact_phone_is_invalid():
    patient_profile = create_valid_patient_profile()

    with pytest.raises(InvalidPatientProfileEmergencyContactPhoneError):
        patient_profile.update_medical_info(
            emergency_contact_name="Will Magalhaes",
            emergency_contact_phone="21331410455",
            insurance_info="Forever Healthy Insurance",
            preferred_language="Portuguese",
            medical_history_summary="Diabetes Mellitus",
        )


def test_update_medical_info_fails_when_insurance_info_is_invalid():
    patient_profile = create_valid_patient_profile()

    with pytest.raises(InvalidPatientProfileInsuranceInfoError):
        patient_profile.update_medical_info(
            emergency_contact_name="Will Magalhaes",
            emergency_contact_phone="+5521331410455",
            insurance_info="$#*3",
            preferred_language="Portuguese",
            medical_history_summary="Diabetes Mellitus",
        )

def test_update_medical_info_fails_when_preferred_language_is_invalid():
    patient_profile = create_valid_patient_profile()

    with pytest.raises(InvalidPatientProfilePreferredLanguageError):
        patient_profile.update_medical_info(
            emergency_contact_name="Lili Magalhaes",
            emergency_contact_phone="+5521331410455",
            insurance_info="Forever Healthy Insurance",
            preferred_language="$%6",
            medical_history_summary="Diabetes Mellitus",
        )


def test_update_medical_info_fails_when_medical_history_summary_is_invalid():
    patient_profile = create_valid_patient_profile()

    with pytest.raises(InvalidPatientProfileMedicalHistorySummaryError):
        patient_profile.update_medical_info(
            emergency_contact_name="Lili Magalhaes",
            emergency_contact_phone="+5521331410455",
            insurance_info="Forever Healthy Insurance",
            preferred_language="Portuguese",
            medical_history_summary="",
        )