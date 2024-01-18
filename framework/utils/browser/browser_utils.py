import logging


class BrowserUtils:
    @staticmethod
    def get_url(driver):
        try:
            url = driver.current_url
            logging.info(f"Current url is equal to '{url}'")
            return url
        except:
            logging.error("Could not get current url")

    @staticmethod
    def check_url(actual, expected, driver):
        if actual == expected:
            return True
        else:
            logging.error("URL not matched")
            return False
