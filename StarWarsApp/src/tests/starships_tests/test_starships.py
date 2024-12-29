from fastapi.testclient import TestClient
from main import app
from tests.conftest import mock_not_found
from tests.starships_tests.fixtures import (
    mock_get_data_list_of_test_get_starships_success,
    mock_get_data_of_test_get_starships_by_id_success,
    mock_get_correlated_data_of_test_get_pilots_by_starship_success,
)

client = TestClient(app)


def test_get_starships_success(
    mock_get_data_list_of_test_get_starships_success, mocker
):
    mocker.patch(
        "services.starships_service.get_data_list",
        return_value=mock_get_data_list_of_test_get_starships_success,
    )
    response = client.get(f"/starships")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["count", "starships"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 2
    assert len(data["starships"]) == 2


def test_get_starships_by_id_success(
    mock_get_data_of_test_get_starships_by_id_success, mocker
):
    mocker.patch(
        "services.starships_service.get_data",
        return_value=mock_get_data_of_test_get_starships_by_id_success,
    )
    starship_id = 2
    response = client.get(f"/starships/{starship_id}")
    data = response.json()
    assert response.status_code == 200
    expected_fields = [
        "starship_id",
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
        "hyperdrive_rating",
        "MGLT",
        "starship_class",
        "pilots_ids",
        "films_ids",
        "created",
        "edited",
    ]
    for field in expected_fields:
        assert field in data
    assert data["name"] == "X-wing"
    assert data["model"] == "T-65 X-wing"
    assert data["manufacturer"] == "Incom Corporation"
    assert len(data["pilots_ids"]) == 3
    assert len(data["films_ids"]) == 2
    expected_pilots_ids = ["1", "2", "3"]
    assert data["pilots_ids"] == expected_pilots_ids
    expected_films_ids = ["1", "2"]
    assert data["films_ids"] == expected_films_ids


def test_get_starships_by_id_not_found(mock_not_found, mocker):
    mocker.patch(
        "services.external.swapi_service.httpx.AsyncClient.get",
        side_effect=mock_not_found,
    )
    starship_id = 999
    response = client.get(f"/starships/{starship_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Resource not found in external API"}


def test_get_pilots_by_starship_success(
    mock_get_correlated_data_of_test_get_pilots_by_starship_success, mocker
):
    mocker.patch(
        "services.starships_service.get_correlated_data",
        return_value=mock_get_correlated_data_of_test_get_pilots_by_starship_success,
    )
    starship_id = 10
    response = client.get(f"/starships/{starship_id}/pilots")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["starship_id", "count", "pilots"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 2
    assert len(data["pilots"]) == 2


def test_get_vehicles_by_starship_not_found(mock_not_found, mocker):
    mocker.patch(
        "services.external.swapi_service.httpx.AsyncClient.get",
        side_effect=mock_not_found,
    )
    starship_id = 999
    response = client.get(f"/starships/{starship_id}/pilots")
    assert response.status_code == 404
    assert response.json() == {"detail": "Resource not found in external API"}
