from typing import Any


class Config:
    URLS: dict[str, str] = {
            "BASE_URL": "",
    }

    ERROR_MSG: dict[str, str] = {
        "NOT_FOUND": "Can't find element by locator {locator}",
        "NOT_FOUND_PLURAL": "Can't find elements by locator {locator}",
    }

    TIMEOUT: int = 10

    DATA: dict[str, Any] = {
        "": "",
    }
