# Selenoid Template 

Selenoid template with usage of Pytest and Allure.

## Secrets

Secrets must be put in `.env` file in the format:

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

### Selenoid
1. Make sure you have recent Docker version installed.
2. Download [Configuration Manager](http://aerokube.com/cm/latest/) (Selenoid quick installation binary) for your platform from releases page.
3. On Linux or Mac give execution permissions to binary:
```bash
$ chmod +x cm
```
Run one command to start Selenoid:
```bash
$ ./cm selenoid start --vnc
```
Running this command with sudo can lead to broken installation. Recommended way is running Selenoid as regular user. On Linux to have permissions to access Docker you may need to add your user to docker group:
```bash
$ sudo usermod -aG docker $USER
```
Optionally run one more command to start Selenoid UI:
```bash
$ ./cm selenoid-ui start
```
Open `http://localhost:8080/#/` to view Selenoid UI.
## Command to run tests:
```sh
PYTHONPATH=. python tests/main.py
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

Execute tests:
```sh
pytest tests/*.py --alluredir="allure-results"
```
or:

```sh
./test.sh
```

See documentation here:
- https://github.com/fescobar/allure-docker-service
- https://github.com/fescobar/allure-docker-service-ui

