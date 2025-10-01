# from user_management.infrastructure.repositories import InMemoryUserRepository
#
# _shared_user_repository = InMemoryUserRepository()
#
# def get_shared_user_repository():
#     return _shared_user_repository



"""
Shared dependencies for the FastAPI application.

Centralizes dependency injection logic to avoid circular imports.
"""

from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from user_management.application.use_cases.register_user_use_case import RegisterUserUseCase
from user_management.infrastructure.repositories.postgres_user_repository import PostgresUserRepository

# Configuração do banco (replicada aqui para evitar circular import)
DATABASE_URL = "postgresql+asyncpg://user:cesi01371803Fm@localhost/nextgenhealth"
engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Provides a database session for dependency injection."""
    async with async_session_maker() as session:
        yield session


def get_register_user_use_case(session: AsyncSession = Depends(get_db_session)):
    """Factory function to provide RegisterUserUseCase with PostgreSQL repository."""
    repo = PostgresUserRepository(session)
    return RegisterUserUseCase(user_repository=repo)