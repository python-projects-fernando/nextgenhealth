from typing import Optional

from user_management.application.use_cases.find_user_by_email.query import FindUserByEmailQuery
from user_management.domain.entities.user import User
from user_management.application.repositories.user_repository import UserRepository


class FindUserByEmailUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, query: FindUserByEmailQuery) -> Optional[User]:
        email_to_search = query.email
        user = await self.user_repository.find_by_email(email_to_search)
        return user

    # def execute(self, email: str) -> Optional[User]:
    #     return self.user_repository.find_by_email(email)