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


# @allure.feature("VK Automation Tests")
# @allure.title("Login page")
# def test_login(driver) -> None:
#     login_page: BasePage = LoginPage(driver)
#     driver_utils = DriverUtils(driver)
#     browser_utils = BrowserUtils(driver)

#     logging.config.fileConfig("logging.conf")
#     logging.info("Test Execution Started")
#     driver_utils.maximize_window()

#     with allure.step("Check Base URL"):
#         driver_utils.get(Config.URLS["BASE_URL"])
#         assert browser_utils.get_url() == Config.URLS["BASE_URL"]
#         assert login_page.is_page_open()

#     with allure.step("Check if email input is enabled"):
#         assert login_page.is_email_input_clickable()
#         login_page.set_email()

#     with allure.step("Check if email button is clickable"):
#         assert login_page.is_email_button_clickable()
#         login_page.click_email_submit()

#     with allure.step("Check if password input is enabled"):
#         assert login_page.is_password_input_clickable()
#         login_page.set_password()

#     with allure.step("Check if password button is clickable"):
#         assert login_page.is_password_button_clickable()
#         login_page.click_password_submit()


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
        hosting_page.get_all_prices()
