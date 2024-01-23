import logging
import os

from framework.base_element import BaseElement


class Input(BaseElement):
    def __init__(self, _driver, _locator: str, _name: str):
        super().__init__(_driver, _locator, _name)

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
        return self.set_value(os.getcwd() + file_path)
