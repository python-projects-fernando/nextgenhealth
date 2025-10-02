"""
Application service to register a new user.

Orchestrates the entire user creation flow without embedding business rules.
Delegates validation and state management to the domain via UserFactory.
"""


from typing import Any, Dict

# Assume UserRepository is correctly defined elsewhere and imported
# from user_management.application.repositories.user_repository import UserRepository

from user_management.domain.factories import UserFactory


class RegisterUserUseCase:
    """
    Application service to register a new user.

    Orchestrates the entire user creation flow without embedding business rules.
    Delegates validation and state management to the domain via UserFactory.
    """

    def __init__(self, user_repository): # Type hint: UserRepository
        """
        Initializes the use case with a user repository.

        Args:
            user_repository: Repository to persist the user.
                             This should be an instance of a class implementing
                             the UserRepository interface/protocol.
        """
        self.user_repository = user_repository


    async def execute(self, command):
        """
        Executes the user registration workflow.

        This method orchestrates the process:
        1. Delegates the creation of the User entity to the UserFactory.
        2. Saves the created user using the injected repository.
        3. Returns the persisted user instance.

        Args:
            command: A validated RegisterUserCommand containing user registration data.

        Returns:
            User: The created and persisted user instance.

        Raises:
            ValueError: If role is invalid (delegated from UserFactory).
            InvalidPasswordError: If password doesn't meet requirements (delegated from UserFactory/UserCredentials).
            # Other exceptions might propagate from the repository (e.g., database errors).
        """


        # --- STEP 1: Delegate User entity creation to the factory ---

        try:
            user = UserFactory.create_from_command(command)

        except Exception as e:
            # Re-raise any domain-specific or validation errors encountered during creation
            raise

        # --- STEP 2: Persist the user using the injected repository ---
        try:
            await self.user_repository.save(user)
        except Exception as e:
            # Re-raise repository errors (e.g., database connection issues)
            raise

        # --- STEP 3: Return the created and persisted user ---
        return user
