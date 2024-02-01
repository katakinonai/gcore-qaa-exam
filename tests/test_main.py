import logging
import logging.config

import allure

from config import Config
from framework.base_page import BasePage
from framework.utils.browser.browser_utils import BrowserUtils
from framework.utils.driver_utils import DriverUtils
from framework.utils.wait_utils import WaitUtils
from tests.pages.hosting import HostingPage
from tests.pages.login import LoginPage


@allure.feature("Gcore QAA Exam")
@allure.title("Hosting Page")
def test_hosting(driver) -> None:
    hosting_page: BasePage = HostingPage(driver)
    driver_utils = DriverUtils(driver)
    browser_utils = BrowserUtils(driver)

    logging.config.fileConfig("logging.conf")
    logging.info("Test Execution Started")
    driver_utils.maximize_window()

    with allure.step(f"Step 1: Go to {Config.URLS['BASE_URL']}"):
        driver_utils.get(Config.URLS["BASE_URL"])
        assert browser_utils.get_url() == Config.URLS["BASE_URL"]
        assert hosting_page.is_page_open()

    with allure.step("Step 2: Choose servers type Dedicated/Virtual"):
        hosting_page.click_dedicated_servers_btn()
        assert hosting_page.is_dedicated_active()

    with allure.step("Step 3: Choose the currency"):
        assert hosting_page.is_eur_label_active()
        hosting_page.click_currency_switch()
        # assert hosting_page.is_usd_label_active()

    with allure.step("Step 4: Enter price min and max values"):
        assert hosting_page.min_price_input.is_clickable()
        hosting_page.clear_min_price()
        hosting_page.set_min_price(Config.DATA["MIN_PRICE"])
        assert hosting_page.max_price_input.is_clickable()
        hosting_page.clear_max_price()
        hosting_page.set_max_price(Config.DATA["MAX_PRICE"])

    with allure.step("Step 5: Assert search result contains"):
        hosting_page.click_show_more_btn()
        prices = hosting_page.get_all_prices()
        hosting_page.check_prices(
            prices, Config.DATA["MIN_PRICE"], Config.DATA["MAX_PRICE"]
        )
