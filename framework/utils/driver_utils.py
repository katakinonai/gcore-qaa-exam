import logging


class DriverUtils:
    def __init__(self, driver) -> None:
        self._driver = driver

    def get(self, url):
        logging.info(f"Open URL: '{url}'")
        return self._driver.get(url)

    def maximize_window(self):
        logging.info("Maximize window")
        return self._driver.maximize_window()

    def implicitly_wait(self, time):
        logging.info(f"Implicitly wait for {time} seconds")
        return self._driver.implicitly_wait(time)

    def close(self):
        logging.info("Close the driver")
        return self._driver.close()

    def quit(self):
        logging.info("Quit the driver")
        return self._driver.quit()
