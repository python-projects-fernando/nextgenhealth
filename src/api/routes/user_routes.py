# src/api/routes/user_routes.py
"""
API routes for user-related operations.

Exposes endpoints for user registration, login, and profile management.
Follows REST principles and integrates with domain use cases.
"""

import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

# ✅ Importa dependências de um lugar neutro (sem circular import)
from api.dependencies import get_register_user_use_case
from user_management.application.use_cases.register_user_command import RegisterUserCommand
from user_management.application.use_cases.register_user_use_case import RegisterUserUseCase

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


# @router.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
@router.post("/", status_code=status.HTTP_201_CREATED)
async def register_user(
    command: RegisterUserCommand,
    use_case: Annotated[RegisterUserUseCase, Depends(get_register_user_use_case)]
):
    logger.info("Received request to register user with email: %s", command.email)

    try:
        logger.debug("RegisterUserCommand validated successfully")
        logger.debug("Calling RegisterUserUseCase.execute")
        user = await use_case.execute(command)  # ✅ AGORA USA AWAIT
        logger.debug("RegisterUserUseCase executed successfully, user UUID: %s", user.uuid)
        logger.info("User registered successfully with UUID: %s", user.uuid)
        return {"uuid": str(user.uuid), "email": user.email}

    except ValueError as e:
        logger.warning("Validation error during user registration for email %s: %s", command.email, e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    except Exception as e:
        logger.error("Unexpected error during user registration for email %s: %s", command.email, e, exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error occurred during user registration."
        )
# async def register_user(
#     command: RegisterUserCommand,
#     use_case: Annotated[RegisterUserUseCase, Depends(get_register_user_use_case)]
# ):
#     """
#     Registers a new user in the system.
#
#     Receives user registration data, validates it using Pydantic,
#     orchestrates the creation of a User entity via the RegisterUserUseCase,
#     and persists it. Returns the UUID of the created user on success.
#     """
#     logger.info("Received request to register user with email: %s", command.email)
#
#     try:
#         logger.debug("RegisterUserCommand validated successfully")
#         logger.debug("Calling RegisterUserUseCase.execute")
#         user = await use_case.execute(command)
#         logger.debug("RegisterUserUseCase executed successfully, user UUID: %s", user.uuid)
#         logger.info("User registered successfully with UUID: %s", user.uuid)
#         return {"uuid": str(user.uuid), "email": user.email}
#
#     except ValueError as e:
#         logger.warning("Validation error during user registration for email %s: %s", command.email, e)
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail=str(e)
#         )
#
#     except Exception as e:
#         logger.error("Unexpected error during user registration for email %s: %s", command.email, e, exc_info=True)
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Internal server error occurred during user registration."
#         )