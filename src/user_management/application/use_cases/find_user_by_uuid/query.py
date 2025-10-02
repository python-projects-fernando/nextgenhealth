from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field, field_validator

from user_management.domain.exceptions import InvalidUUIDError
from user_management.domain.specifications.user import ValidUUIDSpecification


class FindUserByUUIDQuery(BaseModel):
    uuid: UUID = Field(..., description="Valid uuid for the user")

    @field_validator('uuid')
    @classmethod
    def validate_uuid(cls, v: str) -> str:
        if not ValidUUIDSpecification().is_satisfied_by(v):
            raise InvalidUUIDError(f"Invalid uuid: {v}")
        return v

    class Config:
        """
        Pydantic model configuration.
        """
        # Allows parsing of strings to date automatically
        from_attributes = True
        # JSON encoders for complex types
        json_encoders = {
            date: lambda v: v.isoformat()
        }
        # For immutability, uncomment below
        # frozen = True