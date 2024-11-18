import pytest
from tests.conftest import app, get_session, override_db
from fastapi.testclient import TestClient


@pytest.fixture
def test_client():
    app.dependency_overrides = {}
    app.dependency_overrides[get_session] = override_db
    with TestClient(app) as client:
        yield client
