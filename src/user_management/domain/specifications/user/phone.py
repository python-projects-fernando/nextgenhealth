import re
from .. import Specification


class ValidPhoneE164Specification(Specification[str]):
    """
    Specification that validates whether a given phone number follows the E.164 format.

    A valid phone number must:
    - Be None (optional field) or a non-empty string
    - Start with '+' followed by country code and subscriber number
    - Contain only digits after the '+'
    - Have 1 to 15 digits in total (country code + number)

    This rule is enforced during user creation and profile updates to ensure interoperability
    with communication services such as SMS and calling platforms.
    """

    def is_satisfied_by(self, phone: str) -> bool:
        """
        Checks if the provided phone number satisfies the E.164 format requirements.

        Args:
            phone (str): The phone number to validate. Can be None or a string.

        Returns:
            bool: True if the phone number is None or correctly formatted; False otherwise.
        """
        if phone is None:
            return True
        pattern = r"^\+[1-9]\d{1,14}$"
        return re.match(pattern, phone) is not None