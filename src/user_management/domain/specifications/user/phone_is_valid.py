"""
Specification that validates whether a given value is a valid phone number in E.164 format.

A valid phone number must:
- Be None (as the field is optional) or a string
- If provided, start with '+' followed by the country code and subscriber number
- Contain only digits after the '+'
- Have a total length of 1 to 15 digits (after '+')
- Begin with a digit from 1–9 (e.g., +1 for US, +44 for UK)

This rule ensures global interoperability with communication systems such as SMS gateways,
voice services, and emergency contact routing in healthcare applications.
"""

import re
from .. import Specification


class ValidPhoneE164Specification(Specification):
    """
    Specification to validate that a phone number conforms to the E.164 international standard.

    Enforces consistent formatting across user profiles and supports integration
    with third-party telephony providers. Used within the User aggregate for fail-fast validation.
    """

    def is_satisfied_by(self, phone) -> bool:
        """
        Checks if the provided value is a valid E.164 phone number or None.

        Args:
            phone: The value to validate. Expected to be a string or None.

        Returns:
            bool: True if the phone is None or correctly formatted; False otherwise.
        """
        if phone is None:
            return True

        if not isinstance(phone, str):
            return False

        # E.164 format: +[1-9][0-9]{1,14}
        pattern = r"^\+[1-9]\d{1,14}$"
        return re.match(pattern, phone) is not None