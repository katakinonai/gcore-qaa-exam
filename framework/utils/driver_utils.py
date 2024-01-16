import logging

from config import Config


class DriverUtils:
    @staticmethod
    def get(url, driver):
        logging.info(f"Open URL: '{url}'")
        return driver.get(url)

    @staticmethod
    def maximize_window(driver):
        logging.info("Maximize window")
        return driver.maximize_window()

    @staticmethod
    def implicitly_wait(time, driver):
        logging.info(f"Implicitly wait for {time} seconds")
        return driver.implicitly_wait(time)

    @staticmethod
    def close(driver):
        logging.info("Close the driver")
        return driver.close()

    @staticmethod
    def quit(driver):
        logging.info("Quit the driver")
        return driver.quit()
