import logging
import os
import re

from dotenv import load_dotenv
from selenium.webdriver.remote.webelement import WebElement

from framework.base_page import BasePage
from framework.elements.button import Button
from framework.elements.input import Input
from framework.elements.label import Label

load_dotenv()


class HostingPage(BasePage):
    def __init__(self, driver):
        super().__init__(
            driver,
            Input(
                driver,
                "//div[@class='gc-server-configurator-buttons']",
                "configuration switch",
            ),
            "hosting page",
        )
        self.dedicated_servers_btn = Button(
            driver,
            "//button[@type='button' and contains(text(), 'Dedicated servers')]",
            "dedicated servers button",
        )
        self.dedicated_servers_btn_active = Button(
            driver,
            "//button[@type='button' and contains(text(), 'Dedicated servers') and contains(@class, 'active')]",
            "active dedicated servers button",
        )

        self.currency_switch = Button(
            driver, "//div[@class='gc-switcher-toggler']", "currency switch"
        )

        self.eur_label_active = Label(
            driver,
            "//label[@for='left' and contains(text(), 'EUR') and contains(@class, 'active')]",
            "active EUR currency label",
        )

        self.usd_label_active = Label(
            driver,
            "//label[@for='right' and contains(text(), 'USD') and contains(@class, 'active'])",
            "active USD currency label",
        )

        self.min_price_input = Input(
            driver,
            "(//input[contains(@class, 'gc-input')])[1]",
            "min price input field",
        )

        self.max_price_input = Input(
            driver,
            "(//input[contains(@class, 'gc-input')])[2]",
            "max price input field",
        )

        self.price_card_label = Label(
            driver, "//div[@class='price-card_price']", "price card label"
        )

        self.show_more_btn = Button(
            driver,
            "//div[contains(@class, 'gc-server-configurator-more')]",
            "show more button",
        )

    def click_dedicated_servers_btn(self):
        return self.dedicated_servers_btn.click()

    def click_currency_switch(self):
        return self.currency_switch.click()

    def click_show_more_btn(self):
        return self.show_more_btn.click()

    def is_dedicated_active(self):
        return self.dedicated_servers_btn_active.is_displayed()

    def is_eur_label_active(self):
        return self.eur_label_active.is_displayed()

    def is_usd_label_active(self):
        return self.usd_label_active.is_displayed()

    def clear_min_price(self):
        return self.min_price_input.clear()

    def clear_max_price(self):
        return self.max_price_input.clear()

    def set_min_price(self, price):
        return self.min_price_input.set_value(price)

    def set_max_price(self, price):
        return self.max_price_input.set_value(price)

    def get_all_prices(self):
        els = self.price_card_label._find_elements()
        logging.info("Get all prices from cards")
        prices = []
        for idx, el in enumerate(els):
            price = int(re.findall(r"[-+]?\d*\.\d+|\d+", el.text)[0])
            logging.info(
                f"Price of card number {idx+1} is equal to {price}"
            )  # ADD CUR VALUE HERE
            prices.append(price)
        return prices

    def check_prices(self, prices, min, max):
        for idx, price in enumerate(prices):
            logging.info(
                f"Check if price of card number {idx+1} is in boundaries: {min} <= {price} <= {max}"
            )
            if int(max) <= price and price <= int(min):
                return False
        return True
