import json

from gadget import create_app


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_hello(client):
    response = client.get("/version")
    assert json.loads(response.data) == dict(api="Gadget", version="1.2.3")
