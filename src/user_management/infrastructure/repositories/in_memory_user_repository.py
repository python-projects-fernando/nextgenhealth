from src.user_management.application.repositories.user_repository import UserRepository
from user_management.domain.entities.user import User


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users = {}

    def save(self, user: User) -> None:
        self._users[str(user.uuid)] = user

    def find_by_email(self, email: str) -> User | None:
        return next((u for u in self._users.values() if u.email == email), None)

    def find_by_uuid(self, uuid: str) -> User | None:
        return self._users.get(uuid)