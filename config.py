class Config:
    URLS: dict[str, str] = {"BASE_URL": "https://vk.com/"}

    ERROR_MSG: dict[str, str] = {
        "NOT_FOUND": "Can't find element by locator {locator}",
        "NOT_FOUND_PLURAL": "Can't find elements by locator {locator}",
    }

    DRIVER_LIST = ["Firefox"]

    TIMEOUT: int = 10

    DATA: dict[str, str] = {
        "group_name": "QAA City game",
        "message": "привет",
    }

    COMMAND_EXECUTOR: str = "http://localhost:4444/wd/hub"

    LOG_FILE: str = "pytest_logs.txt"
