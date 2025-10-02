""""
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
    # Atributo que armazena o hash da senha (privado e imutável após inicialização)
    _hashed_password: str

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash the given password using SHA-256."""
        import hashlib
        # Gera o hash SHA-256 da senha fornecida
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    @classmethod
    def create(cls, password: str) -> 'UserCredentials':
        """
        Factory method to create UserCredentials from raw password.

        Validates input before hashing.
        """
        # Validações da senha fornecida
        if password is None:
            raise InvalidPasswordError("Password is required")
        if not isinstance(password, str):
            raise InvalidPasswordError("Password must be a string")
        if len(password.strip()) == 0:
            raise InvalidPasswordError("Password cannot be empty or whitespace")

        # Gera o hash e cria uma nova instância da classe com esse hash
        hashed = cls.hash_password(password)
        return cls(_hashed_password=hashed)

    @classmethod
    def _from_hashed(cls, stored_hash: str) -> 'UserCredentials':
        """
        Internal factory method to create UserCredentials from a pre-existing hash.
        Used during re-hydration from persistence (e.g., database read).
        Does not re-hash the password.

        Args:
            stored_hash (str): The hashed password retrieved from storage.

        Returns:
            UserCredentials: A new instance initialized with the stored hash.
        """
        # Cria diretamente uma instância com o hash armazenado
        # Como esta classe é frozen, só é possível definir o valor durante a inicialização.
        # Este método é seguro porque não aceita uma senha em texto claro.
        return cls(_hashed_password=stored_hash)

    def is_valid(self, provided: str) -> bool:
        """
        Check if the provided password matches the stored hash.

        Args:
            provided: The password attempt.

        Returns:
            bool: True if valid; False otherwise.
        """
        # Verifica se a entrada é uma string
        if not isinstance(provided, str):
            return False
        # Gera o hash da senha fornecida e compara com o hash armazenado
        provided_hash = self.hash_password(provided)
        return provided_hash == self._hashed_password

    @classmethod
    def with_new_password(cls, old_password: str, new_password: str) -> 'UserCredentials':
        """
        Creates a new UserCredentials instance if the old password is valid
        and the new password meets requirements.
        """
        # Cria instâncias temporárias para validar as senhas
        current = cls.create(old_password) # <-- Isso vai validar e gerar hash de old_password
        new = cls.create(new_password)    # <-- Isso vai validar e gerar hash de new_password

        # Verifica se as senhas são iguais (hash comparado)
        if current._hashed_password == new._hashed_password:
            raise InvalidPasswordError("New password cannot be the same as the current one")

        # Retorna a nova instância com o hash da nova senha
        return new # <-- Retorna 'new', que é a nova instância de UserCredentials