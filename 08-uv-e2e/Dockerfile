FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY hermeto-output /hermeto-output
COPY hermeto.env /hermeto.env
COPY pyproject.toml /app/pyproject.toml
COPY uv.lock /app/uv.lock
COPY README.md /app/README.md

WORKDIR /app

# uv build path
RUN . /hermeto.env && uv build --wheel --verbose

# uv sync path
RUN . /hermeto.env && uv sync  --verbose


RUN .venv/bin/python -c "import click; import flask; import httpx; print('all imports ok')"
