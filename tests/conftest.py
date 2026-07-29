import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.db.database import get_session


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client