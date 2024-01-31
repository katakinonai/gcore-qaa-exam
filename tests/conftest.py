import logging
from typing import Any, Generator

import pytest
from pytest import FixtureRequest
from selenium import webdriver

from config import Config
from framework.utils.api.api_client import ApiClient
from framework.utils.driver_utils import DriverUtils


@pytest.fixture(scope="module")
def driver() -> Generator:
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor=Config.COMMAND_EXECUTOR, options=options)
    driver_utils = DriverUtils(driver)
    yield driver
    driver_utils.quit()


@pytest.fixture(scope="function")
def logger() -> Generator[None, Any, None]:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    file_handler = logging.FileHandler(Config.LOG_FILE, mode="a")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    yield
    logger.removeHandler(file_handler)


@pytest.fixture(scope="class")
def api_client(request: FixtureRequest) -> ApiClient:
    base_url: str = getattr(request.cls, "base_url", "")
    return ApiClient(base_url)
