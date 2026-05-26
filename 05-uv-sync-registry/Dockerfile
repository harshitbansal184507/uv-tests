FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY hermeto-output /hermeto-output
COPY hermeto.env /hermeto.env
COPY pyproject.toml /app/pyproject.toml
COPY uv.lock /app/uv.lock

WORKDIR /app

RUN . /hermeto.env && uv sync --offline --verbose
RUN python -c "import click; print('click ok')"
