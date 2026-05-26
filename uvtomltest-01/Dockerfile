FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

RUN uv init

RUN printf '[sources]\ndoesntmatter = { index = "doesnt_matter"}\n' > /app/uv.toml

RUN uv sync