from abc import ABC, abstractmethod
from user_management.domain.entities.user import User


class UserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> None:
        ...

    @abstractmethod
    def find_by_email(self, email: str) -> User | None:
        ...

    @abstractmethod
    def find_by_uuid(self, uuid: str) -> User | None:
        ...