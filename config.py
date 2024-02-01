class Config:
    URLS: dict[str, str] = {"BASE_URL": "https://gcore.com/hosting"}

    ERROR_MSG: dict[str, str] = {
        "NOT_FOUND": "Can't find element by locator {locator}",
        "NOT_FOUND_PLURAL": "Can't find elements by locator {locator}",
    }

    TIMEOUT: int = 10

    DATA: dict = {
        "MIN_PRICE_1": "400",
        "MAX_PRICE_1": "800",
        "MIN_PRICE_2": "89",
        "MAX_PRICE_2": "1482",
        "CURRENCY_USD": "$",
        "CURRENCY_EUR": "€",
        "SERVER_TYPE_1": "virtual",
        "SERVER_TYPE_2": "dedicated",
    }

    COMMAND_EXECUTOR: str = "http://localhost:4444"

    LOG_FILE: str = "pytest_logs.txt"
