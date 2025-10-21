"""
Shared dependencies for the FastAPI application.

Imports dependency factories from the infrastructure layer to avoid
exposing infrastructure details directly to the presentation layer.
"""
import logging

from fastapi import Depends

from user_management.application.use_cases.register_patient_profile import RegisterPatientProfileUseCase
from user_management.application.use_cases.register_user import RegisterUserUseCase
from user_management.application.use_cases.find_user_by_email import FindUserByEmailUseCase
from user_management.application.use_cases.find_user_by_uuid import FindUserByUUIDUseCase
from user_management.infrastructure.database.postgres_dependencies import get_postgres_user_repository, \
    get_postgres_patient_profile_repository

logger = logging.getLogger(__name__)

def get_register_user_use_case(user_repo = Depends(get_postgres_user_repository)):
    """Factory function to provide RegisterUserUseCase via API dependency injection."""
    return RegisterUserUseCase(user_repository=user_repo)

def get_find_user_by_email_use_case(user_repo = Depends(get_postgres_user_repository)):
    return FindUserByEmailUseCase(user_repository=user_repo)


def get_find_user_by_uuid_use_case(user_repo = Depends(get_postgres_user_repository)):
    return FindUserByUUIDUseCase(user_repository=user_repo)


def get_register_patient_profile_use_case(patient_profile_repo = Depends(get_postgres_patient_profile_repository)):
    return RegisterPatientProfileUseCase(patient_profile_repository=patient_profile_repo)
