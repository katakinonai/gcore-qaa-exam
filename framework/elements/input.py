import logging

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.file_detector import LocalFileDetector

from framework.base_element import BaseElement


class Input(BaseElement):
    def __init__(self, _driver, _locator: str, _name: str):
        super().__init__(_driver, _locator, _name)

    def clear(self):
        el = self._find_element()
        if not isinstance(el, str):
            logging.info(f"Clear value of {self._name}")
            el.send_keys(Keys.CONTROL + "a")
            return el.send_keys(Keys.DELETE)

    def set_value(self, value):
        el = self._find_element()
        logging.info(f"Set {self._name} to a value of '{value}'")
        if not isinstance(el, str):
            return el.send_keys(value)

    def set_value_secret(self, value):
        el = self._find_element()
        logging.info(f"Setting {self._name} to a secret value of '{len(value) * '*'}'")
        if not isinstance(el, str):
            return el.send_keys(value)

    def upload_file(self, file_path: str) -> None:
        logging.info(f"Upload {file_path} to {self._name}")
        # return self.set_value(os.getcwd() + file_path)
        self._driver.execute_script("arguments[0].style.display = 'block';", self)
        self._driver.file_detector = LocalFileDetector()
        return self.set_value(file_path)  # REFERENCE: https://shorturl.at/lrOP7
