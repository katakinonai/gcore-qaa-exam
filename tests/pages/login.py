import email
import logging
import os

from dotenv import load_dotenv
from selenium.webdriver.remote.webelement import WebElement

from framework.base_page import BasePage
from framework.elements.button import Button
from framework.elements.input import Input

load_dotenv()


class LoginPage(BasePage):
    def __init__(self):
        super().__init__(
            Input("//input[@id='index_email']", "email input"), "login page"
        )
        self.email_input = Input("//input[@id='index_email']", "email input")
        self.password_input = Input("//input[@type='password']", "password input")
        self.email_submit_button = Button(
            "//button[contains(@class, 'VkIdForm__signInButton')]",
            "confirm email button",
        )
        self.password_submit_button = Button(
            "//button[contains(@class, 'vkuiButton')]",
            "confirm password button",
        )

        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")

    def set_email(self, driver):
        return self.email_input.set_value(self.email, driver)

    def click_email_submit(self, driver):
        return self.email_submit_button.click(driver)

    def is_email_input_clickable(self, driver):
        if isinstance(self.email_input.is_clickable(driver), WebElement):
            return True
        else:
            logging.error("Email input is disabled")
            return False

    def is_email_button_clickable(self, driver):
        if isinstance(self.email_submit_button.is_clickable(driver), WebElement):
            return True
        else:
            logging.error("Submit email button is not clickable")
            return False

    def set_password(self, driver):
        return self.password_input.set_value_secret(self.password, driver)

    def click_password_submit(self, driver):
        return self.password_submit_button.click(driver)

    def is_password_input_clickable(self, driver):
        if isinstance(self.password_input.is_clickable(driver), WebElement):
            return True
        else:
            logging.error("Password input is disabled")
            return False

    def is_password_button_clickable(self, driver):
        if isinstance(self.password_submit_button.is_clickable(driver), WebElement):
            return True
        else:
            logging.error("Submit password button is not clickable")
            return False
