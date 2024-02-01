FROM python:3.12-alpine

WORKDIR /qaa_exam

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=.

ENTRYPOINT ["pytest", "-v", "-s", "--alluredir", "allure-results"]
CMD ["test_hosting_positive.py"]