from framework.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, driver, locator: str, name: str):
        super().__init__(driver, locator, name)
