import secrets
import string
from datetime import datetime


class StringUtils:
    @staticmethod
    def generate_random_string(length: int = 10) -> str:
        characters = string.ascii_letters + string.digits
        random_string = "".join(secrets.choice(characters) for _ in range(length))
        return random_string

    @staticmethod
    def validate_date(date_str: str) -> bool:
        try:
            parsed_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            print(f"Valid date: {parsed_date}")
            return True
        except ValueError:
            print("Invalid date format")
            return False
