FROM python:3.12-slim

RUN apt-get update

WORKDIR /app

ENV AWS_SHARED_CREDENTIALS_FILE=.aws/credentials
ENV AWS_CONFIG_FILE=.aws/config

COPY poetry.lock pyproject.toml /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-root

COPY . .

CMD ["pytest", "tests"]