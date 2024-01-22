import logging


class CookiesUtils:
    def __init__(self, driver) -> None:
        self._driver = driver

    def add_cookie(self, name, value):
        logging.info(f"Set cookie: {name}")
        cookie = {"name": name, "value": value}
        return self._driver.add_cookie(cookie)

    def get_cookies(self, names=None):
        logging.info(f"Get cookies: {names}")
        return self._driver.get_cookies(names)

    def delete_cookies(self, names):
        logging.info(f"Delete cookies: {names}")
        return self._driver.delete_cookies(names)

    def delete_all_cookies(self):
        logging.info("Delete all cookies")
        return self._driver.delete_all_cookies()
