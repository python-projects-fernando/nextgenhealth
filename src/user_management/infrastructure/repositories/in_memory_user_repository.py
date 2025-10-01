from typing import Dict, Optional
from uuid import UUID

from user_management.domain.entities.user import User
from user_management.application.repositories.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users: Dict[UUID, User] = {}
        self._emails: Dict[str, UUID] = {}

    def save(self, user: User) -> None:
        self._users[user.uuid] = user
        self._emails[user.email.lower()] = user.uuid

    def find_by_email(self, email: str) -> Optional[User]:
        if not email:
            return None

        uuid = self._emails.get(email.lower())
        if uuid:
            return self._users.get(uuid)
        return None

    def find_by_uuid(self, uuid: UUID) -> Optional[User]:
        return self._users.get(uuid)