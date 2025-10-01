from typing import Optional

from user_management.domain.entities.user import User
from user_management.application.repositories.user_repository import UserRepository


class FindUserByEmailUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str) -> Optional[User]:
        return self.user_repository.find_by_email(email)