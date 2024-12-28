import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_ask_endpoint(client):
    response = client.post('/ask', json={"question": "Houston"})
    assert response.status_code == 200
    assert "response" in response.get_json()
