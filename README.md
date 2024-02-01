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

## Setup

To execute tests in a Docker container, run in terminal:

```sh
docker build -t qaa_exam . && docker-compose up
```
