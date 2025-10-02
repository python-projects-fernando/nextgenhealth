"""
Factory for creating User domain entities from application commands.

This module centralizes the logic for translating application-layer
data transfer objects (DTOs) like RegisterUserCommand into domain entities.
It ensures the User is constructed according to its invariants, hiding
the internal structure of the User constructor from the application layer
and generating system-controlled values like UUIDs and timestamps.
"""

from datetime import datetime, timezone
from uuid import uuid4

from user_management.domain.entities import User
from user_management.domain.enums import UserRole, UserStatus
from user_management.domain.value_objects import UserCredentials

class UserFactory:
    """
    Factory to create User instances from RegisterUserCommand.

    Encapsulates the translation from application command to domain entity,
    handling ID generation, timestamp creation, enum conversion, and value object instantiation.
    This ensures the User constructor only receives validated and processed data.
    """

    @staticmethod
    def create_from_command(command) -> User:
        """
        Creates a new User entity based on the data provided in the command.

        This method orchestrates the creation process:
        1. Generates a unique identifier (UUID).
        2. Sets creation and update timestamps.
        3. Converts string role to UserRole enum.
        4. Creates UserCredentials from the provided password.
        5. Instantiates the User entity with all necessary data.

        Args:
            command: An instance of RegisterUserCommand containing user registration data.

        Returns:
            User: A newly created User entity.

        Raises:
            ValueError: If the user_role in the command is invalid.
            InvalidPasswordError: If the password doesn't meet requirements (raised by UserCredentials.create).
            # Other exceptions from User constructor if validation fails unexpectedly.
        """

        # 1. Generate ID and timestamps
        user_id = uuid4()
        now = datetime.now(timezone.utc)

        # 2. Convert string to UserRole enum
        # The command validator should have normalized this, but we ensure it here too.
        try:
            role_enum = UserRole(command.user_role)
        except ValueError as e:
            # Re-raise with a clear message
            raise ValueError(f"Invalid user role provided during factory creation: {command.user_role}") from e

        # 3. Create credentials (handles password validation internally)
        try:
            credentials = UserCredentials.create(command.password)
        except Exception as e:
            # Re-raise the domain-specific exception
            raise

        # 4. Instantiate the User entity
        # The User constructor should ideally only accept validated data.
        try:
            user = User(
                uuid=user_id,
                email=command.email,
                first_name=command.first_name,
                last_name=command.last_name,
                phone=command.phone,
                date_of_birth=command.date_of_birth,
                user_role=role_enum,
                user_status=UserStatus.ACTIVE, # Default status upon registration
                created_at=now,
                updated_at=now,
                credentials=credentials
            )
        except Exception as e:
            # Re-raise any unexpected errors from the User constructor
            raise

        return user
