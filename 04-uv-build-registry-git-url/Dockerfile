FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY hermeto-output/deps/uv /hermeto-output/deps/uv
COPY hermeto.env /hermeto.env
COPY README.md /app/README.md
COPY pyproject.toml /app/pyproject.toml
COPY uv.lock /app/uv.lock
WORKDIR /app

RUN . /hermeto.env && uv build --sdist --verbose
RUN . /hermeto.env && uv build --wheel --verbose
#uv build with --sdist and --wheel flags produces both together,
# but is separated  for testing
