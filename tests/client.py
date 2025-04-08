import os

import pytest
from fastapi.testclient import TestClient

from three_chan.common.setup import setup_app


@pytest.fixture(scope="session")
def api_client():
    os.environ["DB_URL"] = "sqlite+aiosqlite:///:memory:"

    app = setup_app()

    with TestClient(app) as client:
        yield client

    del os.environ["DB_URL"]
