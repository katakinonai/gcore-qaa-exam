import logging
from selenium.webdriver.common.alert import Alert


class AlertUtils:
    def __init__(self, driver) -> None:
        self._driver = driver

    def accept_alert(self) -> None:
        logging.info("Accept alert")
        return Alert(self._driver).accept()

    def dismiss_alert(self) -> None:
        logging.info("Dismiss alert")
        return Alert(self._driver).dismiss()

    def get_alert_text(self) -> str:
        logging.info("Get alert text")
        return Alert(self._driver).text

    def alert_send_keys(self, str) -> None:
        logging.info(f'Send text to alert: "{str}"')
        return Alert(self._driver).send_keys(str)
