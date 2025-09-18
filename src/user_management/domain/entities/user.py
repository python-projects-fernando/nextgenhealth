from uuid import UUID
from ..enums import UserRole, UserStatus
from ..validation.user.user_validator import UserValidator


class User:
    """
    Represents a user in the system with core identity attributes and role-based access.

    This entity serves as the foundation for all authenticated actors, including
    Patients, Nurses, Doctors, and Administrators. It enforces data integrity through
    centralized validation before instantiation.

    Attributes:
        uuid (UUID): Unique identifier for the user.
        email (str): Email address used for login and communication.
        first_name (str): User's first name.
        last_name (str): User's last name.
        phone (str, optional): Phone number in E.164 format. Can be None.
        date_of_birth (date): User's date of birth.
        role (UserRole): Role assigned to the user, determining permissions.
        status (UserStatus): Current account status (e.g., Active, Inactive and Locked).
    """
    def __init__(
        self,
        uuid: UUID,
        email: str,
        first_name: str,
        last_name: str,
        phone,
        date_of_birth,
        role: UserRole,
        status: UserStatus
    ):
        """
        Initializes a new User instance after validating all input data.

        Validation is delegated to UserValidator to ensure domain rules are enforced,
        such as valid email format, proper name characters, correct phone format (E.164),
        realistic date of birth, and valid role/status values.

        Args:
            uuid (UUID): Unique system identifier.
            email (str): Valid email address, must be properly formatted.
            first_name (str): First name containing only letters and spaces.
            last_name (str): Last name containing only letters and spaces.
            phone (str, optional): Phone number in E.164 format (e.g., +1234567890).
                                          May be None if not provided.
            date_of_birth (date): Date of birth; must not be in the future.
            role (UserRole): The user's role within the system.
            status (UserStatus): The current status of the user account.

        Raises:
            InvalidEmailError: If the email format is invalid.
            InvalidUserError: If name, phone, or other fields fail validation.
            InvalidPhoneNumberError: If phone is provided but not in E.164 format.
            InvalidDateOfBirthError: If date of birth is in the future or unrealistic.
        """

        UserValidator.validate(uuid, email, first_name, last_name, phone,
                               date_of_birth, role, status)

        self.uuid = uuid
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.role = role
        self.status = status
