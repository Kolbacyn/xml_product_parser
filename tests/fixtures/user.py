import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.db import get_session

from conftest import override_db

@pytest.fixture
def test_client():
    app.dependency_overrides = {}
    app.dependency_overrides[get_session] = override_db
    with TestClient(app) as client:
        yield client
