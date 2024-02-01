# Gcore QAA Selenium Test

## Task: Automated test for hosting calculator.

Need to create automated test to check Server configuration calculator using steps described below using technologies - Python 3.9+, Selenium, Pytest, Docker. Test should be executed using Docker (Python code should be containerised). Result should be uploaded to your GitHub account. The repository has to contain the README.md file with comprehensive explanation of how to execute the test.

### Steps
1. Go to https://gcore.com/hosting
2. Choose servers type Dedicated/Virtual
3. Choose the currency
4. Enter price min and max values
5. Assert search result contains:
    - Servers with price between min and max values entered at step 4
    - Server price currency is equal to currency chosen at step 3

## Credentials

Secrets must be put in `.env` file:

```python
EMAIL = "email"
PASSWORD = "password"
```
It might be necessary to login in the test browser before running the tests in order to bypass the 2FA.

## Installation
- Download Python 3
https://www.python.org/downloads/

- Check Python version
```sh
python3 --version
```
- Go to project
- Install dependencies

```sh
pip3 install -r requirements.txt
 ```

### Selenium
Run standalone Chrome driver in Docker:

```
docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:4.17.0-20240123
```

### Allure
Execute Allure Docker Service from this directory
```sh
docker-compose up -d allure allure-ui
```
- Verify if Allure API is working. Go to -> http://localhost:5050/allure-docker-service/latest-report

- Verify if Allure UI is working. Go to -> http://localhost:5252/allure-docker-service-ui/

Each time you run tests, the Allure report will be updated.

On *NIX, give permissions to create reports in folders:

```bash
chmod -R 777 allure-reports/ allure-results/
```

See documentation here:
- https://github.com/fescobar/allure-docker-service
- https://github.com/fescobar/allure-docker-service-ui

## Command to run tests
Run in terminal:
```sh
PYTHONPATH=. pytest -v -s tests/*.py --alluredir="allure-results"
```
Or, you can run `run_test.py` to execute the test files:

```sh
./run_test.py
```
