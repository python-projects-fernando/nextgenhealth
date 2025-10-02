"""
API routes for user-related operations.

Exposes endpoints for user registration, login, and profile management.
Follows REST principles and integrates with domain use cases.
"""

import logging
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status, Path
from api.dependencies import get_register_user_use_case, get_find_user_by_email_use_case
from api.responses import UserSummaryResponse
from user_management.application.use_cases.find_user_by_email import FindUserByEmailUseCase
from user_management.application.use_cases.find_user_by_email.query import FindUserByEmailQuery
from user_management.application.use_cases.register_user import RegisterUserUseCase, RegisterUserCommand

# logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def register_user(
    command: RegisterUserCommand,
    use_case: Annotated[RegisterUserUseCase, Depends(get_register_user_use_case)]
):

    try:
        user = await use_case.execute(command)
        return {"uuid": str(user.uuid), "email": user.email}

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error occurred during user registration."
        )


@router.get("/{email}", status_code=status.HTTP_200_OK, response_model=UserSummaryResponse) # <-- Defina o modelo de resposta
async def find_user_by_email(
        use_case: Annotated[FindUserByEmailUseCase, Depends(get_find_user_by_email_use_case)],
        email: str = Path(..., description="Email address of the user to find"),
):
    try:
        query = FindUserByEmailQuery(email=email)
        user_entity = await use_case.execute(query) # Obtém a entidade completa
        if not user_entity:
            raise HTTPException(status_code=404, detail="User not found")

        # Converte a entidade para o DTO de resposta (excluindo credenciais)
        return UserSummaryResponse.from_user_entity(user_entity) # <-- Retorna o DTO

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error occurred during user retrieval."
        )