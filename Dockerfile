
FROM python:3.10.4

RUN mkdir -p /app
WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install --isolated --no-input --compile --exists-action=a --disable-pip-version-check --no-cache-dir -r requirements.txt \
    && rm -rf requirements.txt

COPY ./src /app/src
COPY api.py /app/api.py
COPY settings.toml /app/settings.toml


EXPOSE 8080
CMD ["gunicorn", "api:app", "--worker-tmp-dir=/tmp", "--bind=0.0.0.0:8080", "--workers=2", "--preload", "--chdir=/app", "--worker-class=uvicorn.workers.UvicornWorker", "--log-level=INFO" ]

