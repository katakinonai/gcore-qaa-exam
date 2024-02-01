class Config:
    URLS: dict[str, str] = {"BASE_URL": "https://gcore.com/hosting"}

    ERROR_MSG: dict[str, str] = {
        "NOT_FOUND": "Can't find element by locator {locator}",
        "NOT_FOUND_PLURAL": "Can't find elements by locator {locator}",
    }

    TIMEOUT: int = 10

    DATA: dict = {
        "MIN_PRICE_1": "3",
        "MAX_PRICE_1": "117",
        "MIN_PRICE_2": "3",
        "MAX_PRICE_2": "97",
        "MIN_PRICE_3": "93",
        "MAX_PRICE_3": "1724",
        "MIN_PRICE_4": "93",
        "MAX_PRICE_4": "1482",
        "MIN_PRICE_1_NG": "2",
        "MAX_PRICE_1_NG": "118",
        "MIN_PRICE_2_NG": "2",
        "MAX_PRICE_2_NG": "98",
        "MIN_PRICE_3_NG": "92",
        "MAX_PRICE_3_NG": "1725",
        "MIN_PRICE_4_NG": "88",
        "MAX_PRICE_4_NG": "1483",
        "CURRENCY_USD": "$",
        "CURRENCY_EUR": "€",
        "SERVER_TYPE_1": "virtual",
        "SERVER_TYPE_2": "dedicated",
    }

    COMMAND_EXECUTOR: str = "http://localhost:4444"

    LOG_FILE: str = "pytest_logs.txt"
