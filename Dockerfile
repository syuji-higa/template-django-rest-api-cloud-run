FROM python:3.8-slim as builder

WORKDIR /code

COPY pyproject.toml poetry.lock ./

RUN pip install poetry --no-cache-dir && \
    poetry export -f requirements.txt > requirements.txt && \
    pip uninstall -y poetry

FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

RUN mkdir /code

WORKDIR /code

COPY --from=builder /code/requirements.txt .

RUN pip install -r requirements.txt

ADD . /code/

ENV PORT 8080

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 config.wsgi:application
