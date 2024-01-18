import logging
from framework.base_element import BaseElement


class BasePage(object):
    _uniqueElement: BaseElement
    _name: str

    def __init__(self, unique_element, name):
        self._uniqueElement = unique_element
        self._name = name

    def is_page_open(self, driver):
        logging.info(f"Check if {self._name} is open")
        return self._uniqueElement.is_displayed(driver)
