# from typing import Annotated
# from fastapi import APIRouter, Depends, status
#
# from api.dependencies import get_register_patient_profile_use_case
# from user_management.application.use_cases.register_patient_profile import RegisterPatientProfileCommand, \
#     RegisterPatientProfileUseCase
#
# router = APIRouter(
#     prefix="/patient",
#     tags=["patient"]
# )
#
#
# @router.post("/", status_code=status.HTTP_201_CREATED)
# async def register_patient_profile(
#         command: RegisterPatientProfileCommand,
#         use_case: Annotated[RegisterPatientProfileUseCase, Depends(get_register_patient_profile_use_case)]
# ):
#     pass

from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
import logging

from user_management.application.use_cases.register_patient_profile import RegisterPatientProfileCommand
from user_management.application.use_cases.register_patient_profile import RegisterPatientProfileUseCase
from api.dependencies import get_register_patient_profile_use_case

logger = logging.getLogger(__name__)

patient_router = APIRouter(
    prefix="/patient",
    tags=["patient"]
)

@patient_router.post("/", status_code=status.HTTP_201_CREATED)
async def register_patient_profile(
    command: RegisterPatientProfileCommand,
    use_case: Annotated[RegisterPatientProfileUseCase, Depends(get_register_patient_profile_use_case)]
):
    logger.info("Received request to register patient profile for user UUID: %s", command.user_uuid)
    try:
        patient_profile = await use_case.execute(command)
        logger.info("Patient profile registered successfully for user UUID: %s", command.user_uuid)
        return {
            "user_uuid": str(patient_profile.user_uuid),
            "emergency_contact_name": patient_profile.emergency_contact_name,
            # ou só: "message": "Patient profile created"
        }
    except Exception as e:
        logger.error("Error registering patient profile for user %s: %s", command.user_uuid, e, exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to register patient profile."
        )