from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from user_management.domain.entities.patient_profile import PatientProfile


class PatientProfileRepository(ABC):
    @abstractmethod
    def save(self, patient: PatientProfile) -> None:
        ...

    # @abstractmethod
    # def find_by_email(self, email: str) -> Optional[User]:
    #     ...
    #
    # @abstractmethod
    # def find_by_uuid(self, uuid: UUID) -> Optional[User]:
    #     ...