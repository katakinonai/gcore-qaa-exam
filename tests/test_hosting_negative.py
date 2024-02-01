import logging
import logging.config

import allure
import pytest

from config import Config
from framework.base_page import BasePage
from framework.utils.browser.browser_utils import BrowserUtils
from framework.utils.driver_utils import DriverUtils
from tests.pages.hosting import HostingPage


@allure.feature("Gcore QAA Exam")
@allure.title("Hosting Page: Negative Tests")
@pytest.mark.parametrize(
    "server_type,currency,min_price,max_price",
    [
        (
            Config.DATA["SERVER_TYPE_1"],
            Config.DATA["CURRENCY_USD"],
            Config.DATA["MIN_PRICE_1_NG"],
            Config.DATA["MAX_PRICE_1_NG"],
        ),
        (
            Config.DATA["SERVER_TYPE_1"],
            Config.DATA["CURRENCY_EUR"],
            Config.DATA["MIN_PRICE_2_NG"],
            Config.DATA["MAX_PRICE_2_NG"],
        ),
        (
            Config.DATA["SERVER_TYPE_2"],
            Config.DATA["CURRENCY_USD"],
            Config.DATA["MIN_PRICE_3_NG"],
            Config.DATA["MAX_PRICE_3_NG"],
        ),
        (
            Config.DATA["SERVER_TYPE_2"],
            Config.DATA["CURRENCY_EUR"],
            Config.DATA["MIN_PRICE_4_NG"],
            Config.DATA["MAX_PRICE_4_NG"],
        ),
    ],
)
def test_hosting_negative(driver, server_type, currency, min_price, max_price) -> None:
    driver_utils = DriverUtils(driver)
    browser_utils = BrowserUtils(driver)
    hosting_page: BasePage = HostingPage(driver)

    logging.config.fileConfig("logging.conf")
    logging.info("Test Execution Started")
    driver_utils.maximize_window()

    with allure.step(f"Step 1: Go to {Config.URLS['BASE_URL']}"):
        driver_utils.get(Config.URLS["BASE_URL"])
        assert browser_utils.get_url() == Config.URLS["BASE_URL"]
        assert hosting_page.is_page_open()

    with allure.step("Step 2: Choose servers type Dedicated/Virtual"):
        if server_type == Config.DATA["SERVER_TYPE_2"]:
            hosting_page.click_dedicated_servers_btn()
            assert hosting_page.is_dedicated_active()
        else:
            assert hosting_page.is_virtual_active()

    with allure.step("Step 3: Choose the currency"):
        assert hosting_page.is_eur_label_active()
        if currency == Config.DATA["CURRENCY_USD"]:
            hosting_page.click_currency_switch()

    with allure.step("Step 4: Enter price min and max values"):
        assert hosting_page.min_price_input.is_clickable()
        hosting_page.clear_min_price()
        hosting_page.set_min_price(min_price)
        assert hosting_page.is_out_of_range_min_displayed()
        assert hosting_page.max_price_input.is_clickable()
        hosting_page.clear_max_price()
        hosting_page.set_max_price(max_price)
        assert hosting_page.is_out_of_range_max_displayed()

    with allure.step("Step 5: Assert search result contains"):
        hosting_page.click_show_more_btn()
        with allure.step(
            "Servers with price between min and max values entered at step 4"
        ):
            prices = hosting_page.get_all_prices()
            assert hosting_page.check_prices(prices, min_price, max_price)
        with allure.step("Server price currency is equal to currency chosen at step 3"):
            currencies = hosting_page.get_all_currencies()
            assert hosting_page.check_currencies(currencies, currency)
