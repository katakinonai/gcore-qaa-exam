import logging
import regex

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

        self.virtual_servers_btn_active = Button(
            driver,
            "//button[@type='button' and contains(text(), 'Virtual servers') and contains(@class, 'active')]",
            "active virtual servers button",
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

        self.out_of_range_min_lbl = Label(
            driver,
            "(//p[contains(@class, 'gc-input-validation')])[1]",
            "min out of range label",
        )

        self.out_of_range_max_lbl = Label(
            driver,
            "(//p[contains(@class, 'gc-input-validation')])[2]",
            "max out of range label",
        )

    def click_dedicated_servers_btn(self):
        return self.dedicated_servers_btn.click()

    def click_currency_switch(self):
        return self.currency_switch.click()

    def click_show_more_btn(self):
        return self.show_more_btn.click()

    def is_dedicated_active(self):
        return self.dedicated_servers_btn_active.is_displayed()

    def is_virtual_active(self):
        return self.virtual_servers_btn_active.is_displayed()

    def is_eur_label_active(self):
        return self.eur_label_active.is_displayed()

    def is_usd_label_active(self):
        return self.usd_label_active.is_displayed()

    def is_out_of_range_min_displayed(self):
        return self.out_of_range_min_lbl.is_displayed()

    def is_out_of_range_max_displayed(self):
        return self.out_of_range_max_lbl.is_displayed()

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
            price = float(regex.findall(r"[-+]?\d*\.\d+|\d+", el.text)[0])
            logging.info(f"Price of card number {idx+1} is equal to {price}")
            prices.append(price)
        return prices

    def get_all_currencies(self):
        els = self.price_card_label._find_elements()
        logging.info("Get all currencies from cards")
        curs = []
        for idx, el in enumerate(els):
            cur = regex.findall(r"\p{Sc}", el.text)[0]
            logging.info(f"Currency of card number {idx+1} is equal to {cur}")
            curs.append(cur)
        return curs

    def check_prices(self, prices, min, max):
        for idx, price in enumerate(prices):
            logging.info(
                f"Check if price of card number {idx+1} is in boundaries: {min} <= {price} <= {max}"
            )
            if float(max) <= price and price <= float(min):
                return False
        return True

    def check_currencies(self, curs, expected_cur):
        for idx, cur in enumerate(curs):
            logging.info(
                f"Check if currency of card number {idx+1} is equal to: {expected_cur}"
            )
            if cur != expected_cur:
                return False
        return True
