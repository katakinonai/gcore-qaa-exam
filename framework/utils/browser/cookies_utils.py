import logging


class CookiesUtils:
    @staticmethod
    def add_cookie(name, value, driver):
        logging.info(f"Set cookie: {name}")
        cookie = {"name": name, "value": value}
        return driver.add_cookie(cookie)

    @staticmethod
    def get_cookies(driver, names=None):
        logging.info(f"Get cookies: {names}")
        return driver.get_cookies(names)

    @staticmethod
    def delete_cookies(names, driver):
        logging.info(f"Delete cookies: {names}")
        return driver.delete_cookies(names)

    @staticmethod
    def delete_all_cookies(driver):
        logging.info(f"Delete all cookies")
        return driver.delete_all_cookies()
