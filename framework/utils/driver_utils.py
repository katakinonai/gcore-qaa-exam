import logging


class DriverUtils:
    def __init__(self, driver) -> None:
        self._driver = driver

    def get(self, url: str) -> str:
        logging.info(f"Open URL: '{url}'")
        return self._driver.get(url)

    def current_url(self) -> str:
        url = self._driver.current_url
        logging.info(f"Current url is: {url}")
        return url

    def maximize_window(self) -> None:
        logging.info("Maximize window")
        return self._driver.maximize_window()

    def implicitly_wait(self, time_to_wait: float) -> None:
        logging.info(f"Implicitly wait for {time_to_wait} seconds")
        return self._driver.implicitly_wait(time_to_wait)

    def close(self) -> None:
        logging.info("Close the driver")
        return self._driver.close()

    def quit(self) -> None:
        logging.info("Quit the driver")
        return self._driver.quit()
