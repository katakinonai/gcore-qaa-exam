class Config:
    URLS: dict[str, str] = {"BASE_URL": "https://gcore.com/hosting"}

    ERROR_MSG: dict[str, str] = {
        "NOT_FOUND": "Can't find element by locator {locator}",
        "NOT_FOUND_PLURAL": "Can't find elements by locator {locator}",
    }

    TIMEOUT: int = 10

    DATA: dict = {
        "MIN_PRICE": "400",
        "MAX_PRICE": "800",
    }

    COMMAND_EXECUTOR: str = "http://localhost:4444"

    LOG_FILE: str = "pytest_logs.txt"
