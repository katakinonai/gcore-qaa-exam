from framework.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, _driver, _locator: str, _name: str):
        super().__init__(_driver, _locator, _name)
