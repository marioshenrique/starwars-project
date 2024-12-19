from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_vehicles_success():
    response = client.get(f"/vehicles")
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 39
    assert len(data["vehicles"]) == 39


def test_get_vehicles_by_id_success():
    vehicle_id = 4
    response = client.get(f"/vehicles/{vehicle_id}")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Sand Crawler"
    assert data["model"] == "Digger Crawler"
    assert data["manufacturer"] == "Corellia Mining Corporation"
    assert len(data["films"]) == 2
    assert len(data["pilots"]) == 0


def test_get_vehicles_by_id_not_found():
    vehicle_id = 999
    response = client.get(f"/vehicles/{vehicle_id}")
    assert response.status_code == 404
