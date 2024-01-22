import logging


class BrowserUtils:
    def __init__(self, driver) -> None:
        self._driver = driver

    def get_url(self) -> str | None:
        try:
            url = self._driver.current_url
            logging.info(f"Current url is equal to '{url}'")
            return url
        except:
            logging.error("Could not get current url")

    def check_url(self, actual, expected) -> bool:
        if actual == expected:
            return True
        else:
            logging.error("URL not matched")
            return False
