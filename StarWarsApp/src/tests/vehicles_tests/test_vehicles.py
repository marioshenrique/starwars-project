from fastapi.testclient import TestClient
from main import app
from tests.conftest import mock_not_found
from tests.vehicles_tests.fixtures import (
    mock_get_data_list_of_test_get_vehicles_success,
    mock_get_data_of_test_get_vehicles_by_id_success,
)

client = TestClient(app)


def test_get_vehicles_success(mock_get_data_list_of_test_get_vehicles_success, mocker):
    mocker.patch(
        "services.vehicles_service.get_data_list",
        return_value=mock_get_data_list_of_test_get_vehicles_success,
    )
    response = client.get(f"/vehicles")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["count", "vehicles"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 2
    assert len(data["vehicles"]) == 2


def test_get_vehicles_by_id_success(
    mock_get_data_of_test_get_vehicles_by_id_success, mocker
):
    mocker.patch(
        "services.vehicles_service.get_data",
        return_value=mock_get_data_of_test_get_vehicles_by_id_success,
    )
    vehicle_id = 1
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
    assert len(data["films_ids"]) == 2
    assert len(data["pilots_ids"]) == 3
    expected_films_ids = ["1", "2"]
    assert data["films_ids"] == expected_films_ids
    expected_pilots_ids = ["1", "2", "3"]
    assert data["pilots_ids"] == expected_pilots_ids


def test_get_vehicles_by_id_not_found(mock_not_found, mocker):
    mocker.patch(
        "services.external.swapi_service.httpx.AsyncClient.get",
        side_effect=mock_not_found,
    )
    vehicle_id = 999
    response = client.get(f"/vehicles/{vehicle_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Resource not found in external API"}
