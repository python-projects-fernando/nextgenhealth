from pydantic import BaseModel
import uuid
from datetime import date, datetime
from user_management.domain.enums import UserRole, UserStatus

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
    user_role: UserRole
    user_status: UserStatus
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_user_entity(cls, user: 'User') -> 'UserSummaryResponse':
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
            user_role=user.user_role,
            user_status=user.user_status,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )