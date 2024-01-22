import logging
from framework.base_element import BaseElement


class BasePage(object):
    _uniqueElement: BaseElement
    _name: str

    def __init__(self, driver, unique_element: BaseElement, name):
        self._driver = driver
        self._uniqueElement: BaseElement = unique_element
        self._name: str = name

    def is_page_open(self) -> bool | str:
        logging.info(f"Check if {self._name} is open")
        return self._uniqueElement.is_displayed()
