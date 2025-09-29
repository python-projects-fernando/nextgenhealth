from datetime import datetime, timezone
from uuid import UUID

from user_management.domain.entities import PatientProfile


def create_valid_patient_profile(**kwargs):
    """
    Factory function to create a valid PatientProfile instance for testing.
    Allows override of any field via keyword arguments.
    """
    now = datetime.now(timezone.utc)
    defaults = {
        "user_uuid": UUID("12345678-1234-5678-1234-567812345678"),
        "emergency_contact_name": "Will Magalhaes",
        "emergency_contact_phone": "+5521861499435",
        "insurance_info": "Forever Healthy Insurance",
        "preferred_language": "English",
        "medical_history_summary": "Arterial hypertension",
        "created_at": now,
        "updated_at": now,
    }
    defaults.update(kwargs)
    return PatientProfile(**defaults)