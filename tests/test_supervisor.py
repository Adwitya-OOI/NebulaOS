import pytest
from fastapi.testclient import TestClient
from supervisor.main import app

client = TestClient(app)

def test_stats_endpoint():
    response = client.get("/stats")
    assert response.status_code == 200
    data = response.json()
    assert "cpu_percent" in data
    assert "ram" in data
    assert "disk" in data
    assert "network" in data

def test_services_endpoint():
    response = client.get("/services")
    assert response.status_code == 200
    data = response.json()
    assert "ssh" in data
    assert "docker" in data
