# src/user_management/application/use_cases/register_user_use_case.py
"""
Application service to register a new user.

Orchestrates the entire user creation flow without embedding business rules.
Delegates validation and state management to the domain via UserFactory.
"""

import logging
from typing import Any, Dict

# Assume UserRepository is correctly defined elsewhere and imported
# from user_management.application.repositories.user_repository import UserRepository

from user_management.domain.factories import UserFactory
# from user_management.application.use_cases.register_user_command import RegisterUserCommand


logger = logging.getLogger(__name__)


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
        logger.debug("RegisterUserUseCase initialized with repository: %s", type(user_repository).__name__)

    async def execute(self, command): # Type hint: RegisterUserCommand -> User
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
        logger.info("Executing RegisterUserUseCase for email: %s", command.email)

        # --- STEP 1: Delegate User entity creation to the factory ---
        logger.debug("Delegating user creation to UserFactory for email: %s", command.email)
        try:
            user = UserFactory.create_from_command(command)
            logger.debug("User entity successfully created with UUID: %s", user.uuid)
            logger.debug("------->>>>>>>>>>>>>>>User entity successfully created: %s", user)
        except Exception as e:
            logger.error("Failed to create User entity from command for email %s: %s", command.email, e)
            # Re-raise any domain-specific or validation errors encountered during creation
            raise

        # --- STEP 2: Persist the user using the injected repository ---
        logger.debug("Saving user with UUID: %s to the repository", user.uuid)
        try:
            await self.user_repository.save(user)
            logger.info("User with UUID: %s successfully saved to the repository", user.uuid)
        except Exception as e:
            logger.error("Failed to save user with UUID: %s to the repository: %s", user.uuid, e)
            # Re-raise repository errors (e.g., database connection issues)
            raise

        # --- STEP 3: Return the created and persisted user ---
        logger.debug("Returning created user with UUID: %s", user.uuid)
        return user
