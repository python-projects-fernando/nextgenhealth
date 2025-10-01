from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from user_management.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        ...

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        ...

    @abstractmethod
    def find_by_uuid(self, uuid: UUID) -> Optional[User]:
        ...