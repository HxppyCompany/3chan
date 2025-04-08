FROM python:3.13-alpine AS install

WORKDIR /3chan

RUN apk add curl && curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$PATH:/root/.local/bin"

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry sync --no-cache --no-root

FROM install AS run

COPY three_chan/ three_chan/

ENTRYPOINT [ "poetry", "run", "python", "-m", "three_chan.main" ]

FROM install AS debug

COPY three_chan/ three_chan/

ENTRYPOINT [ "poetry", "run", "debugpy", "--listen", "0.0.0.0:1488", "--wait-for-client", \
    "-m", "uvicorn", "--host", "0.0.0.0", "--port" ,"8080", "--factory", "three_chan.common.setup:setup_app" ]