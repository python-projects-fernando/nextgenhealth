"""
Value Object representing user authentication credentials.

Encapsulates secure password handling and validation.
Immutable by design.
"""

from dataclasses import dataclass
from ..exceptions import InvalidPasswordError


@dataclass(frozen=True)
class UserCredentials:
    """
    Immutable value object for user credentials.
    Stores hashed password and provides validation logic.
    """
    _hashed_password: str

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash the given password using SHA-256."""
        import hashlib
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    @classmethod
    def create(cls, password: str) -> 'UserCredentials':
        """
        Factory method to create UserCredentials from raw password.

        Validates input before hashing.
        """
        if password is None:
            raise InvalidPasswordError("Password is required")
        if not isinstance(password, str):
            raise InvalidPasswordError("Password must be a string")
        if len(password.strip()) == 0:
            raise InvalidPasswordError("Password cannot be empty or whitespace")

        hashed = cls.hash_password(password)
        return cls(_hashed_password=hashed)

    def is_valid(self, provided: str) -> bool:
        """
        Check if the provided password matches the stored hash.

        Args:
            provided: The password attempt.

        Returns:
            bool: True if valid; False otherwise.
        """
        if not isinstance(provided, str):
            return False
        provided_hash = self.hash_password(provided)
        return provided_hash == self._hashed_password

    @classmethod
    def with_new_password(cls, old_password: str, new_password: str) -> 'UserCredentials':
        """
        Creates a new UserCredentials instance if the old password is valid
        and the new password meets requirements.
        """

        current = cls.create(old_password)

        new = cls.create(new_password)

        if current._hashed_password == new._hashed_password:
            raise InvalidPasswordError("New password cannot be the same as the current one")

        return new


