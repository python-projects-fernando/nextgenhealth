from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from user_management.infrastructure.database.postgres_config import async_sessionmaker_instance
from user_management.infrastructure.repositories.postgres_user_repository import PostgresUserRepository


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Provides a database session for dependency injection."""
    async with async_sessionmaker_instance() as session:
        yield session


def get_postgres_user_repository(session: AsyncSession = Depends(get_db_session)):
    """Factory function to provide PostgresUserRepository."""
    return PostgresUserRepository(session)
