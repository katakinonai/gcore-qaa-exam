import logging
import logging.config

import allure

from config import Config
from framework.utils.browser.browser_utils import BrowserUtils
from framework.utils.driver_utils import DriverUtils
from tests.pages.login import LoginPage


@allure.feature("VK Automation Tests")
@allure.title("Login page")
def test_login(driver):
    login_page = LoginPage(driver)
    driver_utils = DriverUtils(driver)
    browser_utils = BrowserUtils(driver)

    logging.config.fileConfig("logging.conf")
    logging.info("Test Execution Started")
    driver_utils.maximize_window()

    with allure.step("Check Base URL"):
        driver_utils.get(Config.URLS["BASE_URL"])
        assert browser_utils.get_url() == Config.URLS["BASE_URL"]
        assert login_page.is_page_open()

    with allure.step("Check if email input is enabled"):
        assert login_page.is_email_input_clickable()
        login_page.set_email()

    with allure.step("Check if email button is clickable"):
        assert login_page.is_email_button_clickable()
        login_page.click_email_submit()

    with allure.step("Check if password input is enabled"):
        assert login_page.is_password_input_clickable()
        login_page.set_password()

    with allure.step("Check if password button is clickable"):
        assert login_page.is_password_button_clickable()
        login_page.click_password_submit()
