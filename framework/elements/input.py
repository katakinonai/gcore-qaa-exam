import logging

from framework.base_element import BaseElement


class Input(BaseElement):
    def set_value(self, value, driver):
        el = self._find_element(driver)
        logging.info(f"Set {self._name} to a value of '{value}'")
        if not isinstance(el, str):
            return el.send_keys(value)

    def set_value_secret(self, value, driver):
        el = self._find_element(driver)
        logging.info(f"Setting {self._name} to a secret value of '{len(value) * '*'}'")
        if not isinstance(el, str):
            return el.send_keys(value)
