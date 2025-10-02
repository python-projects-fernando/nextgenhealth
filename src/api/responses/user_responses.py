# src/api/responses/user_responses.py
from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import date, datetime
from user_management.domain.enums import UserRole, UserStatus # Importe os enums

class UserSummaryResponse(BaseModel):
    """
    DTO for user summary data returned by API endpoints.
    Excludes sensitive information like credentials.
    """
    uuid: uuid.UUID
    email: str
    first_name: str
    last_name: str
    phone: str
    date_of_birth: date
    user_role: UserRole  # ou str, se preferir serializar como string
    user_status: UserStatus # ou str
    created_at: datetime
    updated_at: datetime

    # Método de classe para converter da entidade User para este DTO
    # (Isso assume que a entidade User tem propriedades para todos esses campos)
    @classmethod
    def from_user_entity(cls, user: 'User') -> 'UserSummaryResponse': # Use 'User' como string para evitar import circular se necessário
        """
        Creates a UserSummaryResponse instance from a User domain entity.

        Args:
            user (User): The domain entity to convert.

        Returns:
            UserSummaryResponse: The response DTO with public user data.
        """
        return cls(
            uuid=user.uuid,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            phone=user.phone,
            date_of_birth=user.date_of_birth,
            user_role=user.user_role, # Se for um enum, o Pydantic serializa automaticamente
            user_status=user.user_status, # Se for um enum, o Pydantic serializa automaticamente
            created_at=user.created_at,
            updated_at=user.updated_at,
            # credentials=user._credentials # <- NUNCA inclua isso aqui!
        )