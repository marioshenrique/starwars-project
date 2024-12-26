from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_vehicles_success():
    response = client.get(f"/vehicles")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["count", "vehicles"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 39
    assert len(data["vehicles"]) == 39


def test_get_vehicles_by_id_success():
    vehicle_id = 14
    response = client.get(f"/vehicles/{vehicle_id}")
    data = response.json()
    assert response.status_code == 200
    expected_fiels = [
        "vehicle_id",
        "name",
        "model",
        "manufacturer",
        "cost_in_credits",
        "length",
        "max_atmosphering_speed",
        "crew",
        "passengers",
        "cargo_capacity",
        "consumables",
        "vehicle_class",
        "pilots_ids",
        "films_ids",
        "created",
        "edited",
    ]
    for field in expected_fiels:
        assert field in data
    assert data["name"] == "Snowspeeder"
    assert data["model"] == "t-47 airspeeder"
    assert data["manufacturer"] == "Incom corporation"
    assert len(data["films_ids"]) == 1
    assert len(data["pilots_ids"]) == 2
    expected_films_ids = ["2"]
    assert data["films_ids"] == expected_films_ids
    expected_pilots_ids = ["1", "18"]
    assert data["pilots_ids"] == expected_pilots_ids


def test_get_vehicles_by_id_not_found():
    vehicle_id = 999
    response = client.get(f"/vehicles/{vehicle_id}")
    assert response.status_code == 404
