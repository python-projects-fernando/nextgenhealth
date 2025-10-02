import logging
from typing import Optional

from user_management.application.repositories import UserRepository
from user_management.domain.entities import User
from user_management.application.use_cases.find_user_by_uuid.query import FindUserByUUIDQuery

# logger = logging.getLogger(__name__)

class FindUserByUUIDUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, query: FindUserByUUIDQuery) -> Optional[User]:
        user = await self.user_repository.find_by_uuid(query.uuid)
        return user
