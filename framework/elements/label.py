from framework.base_element import BaseElement


class Label(BaseElement):
    def __init__(self, _locator: str, _name: str):
        super().__init__(_locator, _name)
