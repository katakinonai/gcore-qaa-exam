import logging
import logging.config

import allure

from config import Config
from framework.utils.browser_utils import BrowserUtils
from framework.utils.driver_utils import DriverUtils
from tests.pages.login import LoginPage


@allure.feature("VK Automation Tests")
@allure.title("Login page")
def test_login(driver):
    login_page = LoginPage()
    logging.config.fileConfig("logging.conf")
    logging.info("Test Execution Started")
    DriverUtils.maximize_window(driver)

    with allure.step("Check Base URL"):
        DriverUtils.get(Config.URLS["BASE_URL"], driver)
        assert BrowserUtils.get_url(driver) == Config.URLS["BASE_URL"]

    with allure.step("Check if email input is enabled"):
        assert login_page.is_email_input_clickable(driver)
        login_page.set_email(driver)

    with allure.step("Check if email button is clickable"):
        assert login_page.is_email_button_clickable(driver)
        login_page.click_email_submit(driver)

    with allure.step("Check if password input is enabled"):
        assert login_page.is_password_input_clickable(driver)
        login_page.set_password(driver)

    with allure.step("Check if password button is clickable"):
        assert login_page.is_password_button_clickable(driver)
        login_page.click_password_submit(driver)
