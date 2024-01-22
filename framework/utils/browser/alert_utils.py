import logging
from selenium.webdriver.common.alert import Alert


class AlertUtils:
    @staticmethod
    def accept_alert(driver) -> None:
        logging.info("Accept alert")
        return Alert(driver).accept()

    @staticmethod
    def dismiss_alert(driver) -> None:
        logging.info("Dismiss alert")
        return Alert(driver).dismiss()

    @staticmethod
    def get_alert_text(driver) -> str:
        logging.info("Get alert text")
        return Alert(driver).text

    @staticmethod
    def alert_send_keys(str, driver) -> None:
        logging.info(f'Send text to alert: "{str}"')
        return Alert(driver).send_keys(str)
