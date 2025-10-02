from datetime import date

from pydantic import BaseModel, Field, field_validator

from user_management.domain.exceptions import InvalidEmailError
from user_management.domain.specifications.user import ValidEmailSpecification


class FindUserByEmailQuery(BaseModel):

    email: str = Field(..., description="Valid email address for the user")

    @field_validator('email')
    @classmethod
    def validate_email(cls, v: str) -> str:
        """
        Validate email address using domain specification.

        Args:
            v (str): The email value to validate.

        Returns:
            str: The validated email.

        Raises:
            InvalidEmailError: If the email does not meet the specification criteria.
        """
        if not ValidEmailSpecification().is_satisfied_by(v):
            raise InvalidEmailError(f"Invalid email: {v}")
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

