import logging
from typing import Type

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import Config


class BaseElement:
    def __init__(self, _locator: str, _name: str):
        self._locator = _locator
        self._name = _name

    def _find_element(self, driver) -> WebElement | str:
        if isinstance(self._locator, str):
            wait = WebDriverWait(driver, Config.TIMEOUT)
            el = wait.until(EC.visibility_of_element_located((By.XPATH, self._locator)))
            return el
        else:
            logging.error(f"Cannot find element {self._name}")
            return str(self._locator)

    def _find_elements(self, driver) -> list[WebElement]:
        elements: list[WebElement] = driver.find_elements(By.XPATH, self._locator)
        logging.info(f"Number of found '{self._name}' instances: {len(elements)}")
        return elements

    def get_elements_list(self, element_type: Type, driver) -> list[WebElement]:
        elements = self._find_elements(driver)
        elements_list = [
            element_type(el, f"{self._name} #{index}")
            for index, el in enumerate(elements)
        ]
        return elements_list

    def is_clickable(self, driver) -> WebElement | str:
        if isinstance(self._locator, str):
            wait = WebDriverWait(driver, Config.TIMEOUT)
            logging.info(f"Check if {self._name} is clickable")
            el = wait.until(EC.element_to_be_clickable((By.XPATH, self._locator)))
            return el
        else:
            logging.error(f"Cannot find element {self._name}")
            return str(self._locator)

    def get_text(self, driver) -> str:
        el = self._find_element(driver)
        if isinstance(el, str):
            logging.warning(f"Element '{self._name}' is not a WebElement but a string")
            return el
        el_text = el.text
        logging.info(f"'{self._name}' text is equal to '{el_text}'")
        return el_text

    def click(self, driver) -> None | str:
        el = self._find_element(driver)
        if isinstance(el, str):
            logging.warning(f"Element '{self._name}' is not a WebElement but a string")
            return el
        logging.info(f"Click {self._name}")
        return el.click()

    def double_click(self, driver) -> None | str:
        el = self._find_element(driver)
        if isinstance(el, str):
            logging.warning(f"Element '{self._name}' is not a WebElement but a string")
            return el
        actions = ActionChains(driver)
        logging.info(f"Double click 'f{self._name}'")
        return actions.double_click(el).perform()

    def scroll_to_element(self, driver) -> None | str:
        el = self._find_element(driver)
        if isinstance(el, str):
            logging.warning(f"Element '{self._name}' is not a WebElement but a string")
            return el
        actions = ActionChains(driver)
        logging.info(f"`Scroll 'f{self._name}' into view")
        return actions.scroll_to_element(el).perform()

    def get_attribute(self, attribute, driver) -> str | None:
        el = self._find_element(driver)
        if isinstance(el, str):
            logging.warning(f"Element '{self._name}' is not a WebElement but a string")
            return el
        att = el.get_attribute(attribute)
        logging.info(f"Getting attribute value: '{attribute}'")
        return att

    def is_displayed(self, driver) -> bool | str:
        el = self._find_element(driver)
        if isinstance(el, str):
            logging.warning(f"Element '{self._name}' is not a WebElement but a string")
            return el
        res = el.is_displayed()
        logging.info(
            f"""{self._name if res else 'Element'} is{' not' if not res else ''} displayed"""
        )
        return res

    def wait_until_enabled(self, driver):
        logging.info(f"Waiting for {self._name} to be enabled")
        return WebDriverWait(driver, Config.TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, self._locator))
        )
