import logging
from typing import Type
from venv import logger

import allure
import requests
from config import Config
from pydantic import BaseModel, ValidationError


class ApiClient:
    def __init__(self, base_url: str | None = None) -> None:
        print(f"base_url: {base_url}")
        self._base_url = base_url or Config.URLS.get("BASE_URL", "default_value")

    @allure.step("GET request to {path}")
    def get(self, path: str, params=None) -> requests.Response:
        logging.info(f"GET request to {path}")
        if params is None:
            params = []
        url = self._base_url + path
        return requests.get(url, params)

    @allure.step("POST request to {path}")
    def post(self, path: str, data: dict | None = None) -> requests.Response:
        logging.info(f"POST request to {path}")
        if data is None:
            data = {}
        url = self._base_url + path
        return requests.post(url, json=data)

    @allure.step("PATCH request to {path}")
    def patch(self, path: str, data: dict | None = None) -> requests.Response:
        logging.info(f"PATCH request to {path}")
        if data is None:
            data = {}
        url = self._base_url + path
        return requests.patch(url, json=data)

    @allure.step("PUT request to {path}")
    def put(self, path: str, data: dict | None = None) -> requests.Response:
        logging.info(f"PUT request to {path}")
        if data is None:
            data = {}
        url = self._base_url + path
        return requests.put(url, json=data)

    @allure.step("DELETE request to {path}")
    def delete(self, path: str) -> requests.Response:
        logging.info(f"DELETE request to {path}")
        url = self._base_url + path
        return requests.delete(url)

    @allure.step("Validate response status code")
    def validate_status(self, actual_code: int, expected_code: int) -> bool:
        logging.info(f"Validate response status code")
        if actual_code == expected_code:
            return True
        else:
            logger.error(
                f"STATUS CODE MISMATCH: Expected - {expected_code}, actual - {actual_code}"
            )
            return False

    @allure.step("Validate response data using the {model} model")
    def validate(self, result: object, model: Type[BaseModel]) -> BaseModel:
        logging.info(f"Validate response data using the {model} model")
        try:
            return model.model_validate(result)
        except ValidationError as e:
            logger.error(f"VALIDATION ERROR: {e}")
            return model.model_validate(result)
