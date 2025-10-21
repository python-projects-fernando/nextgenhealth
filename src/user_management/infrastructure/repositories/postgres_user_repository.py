"""
PostgreSQL implementation of the UserRepository interface.

Uses SQLAlchemy async ORM to persist User entities in a relational database.
Maps domain User to UserModel and vice versa.
"""
from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from user_management.domain.entities import User
from user_management.application.repositories import UserRepository
from user_management.infrastructure.models import UserModel
from user_management.infrastructure.models import UserCredentialsModel

# import logging
# logger = logging.getLogger(__name__)


class PostgresUserRepository(UserRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, user: User) -> None:
        user_model = UserModel(
            uuid=str(user.uuid),
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            phone=user.phone,
            date_of_birth=user.date_of_birth,
            user_role=user.user_role.value,
            user_status=user.user_status.value,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

        credentials_model = UserCredentialsModel(
            user_uuid=str(user.uuid),
            hashed_password=user._credentials._hashed_password.encode('utf-8')
        )

        self.session.add(user_model)
        await self.session.flush()

        self.session.add(credentials_model)
        await self.session.commit()

    async def find_by_email(self, email: str) -> Optional[User]:
        stmt = select(UserModel).where(UserModel.email == email)
        result = await self.session.execute(stmt)
        user_model = result.scalar_one_or_none()

        if user_model:
            return await self._to_domain(user_model)
        return None

    async def find_by_uuid(self, uuid: UUID) -> Optional[User]:
        stmt = select(UserModel).where(UserModel.uuid == str(uuid))
        result = await self.session.execute(stmt)
        user_model = result.scalar_one_or_none()

        if user_model:
            return await self._to_domain(user_model)
        return None

    async def _to_domain(self, user_model: UserModel) -> User:
        from user_management.domain.value_objects.user_credentials import UserCredentials
        from user_management.domain.enums import UserRole, UserStatus
        from uuid import UUID

        stmt = select(UserCredentialsModel).where(UserCredentialsModel.user_uuid == user_model.uuid)
        result = await self.session.execute(stmt)
        credentials_model = result.scalar_one_or_none()

        if not credentials_model:
            raise ValueError(f"Credentials not found for user {user_model.uuid}")

        hashed_password_str = credentials_model.hashed_password.decode('utf-8')

        credentials = UserCredentials._from_hashed(hashed_password_str)

        return User(
            uuid=UUID(user_model.uuid),
            email=user_model.email,
            first_name=user_model.first_name,
            last_name=user_model.last_name,
            phone=user_model.phone,
            date_of_birth=user_model.date_of_birth,
            user_role=UserRole(user_model.user_role),
            user_status=UserStatus(user_model.user_status),
            created_at=user_model.created_at,
            updated_at=user_model.updated_at,
            credentials=credentials
        )
