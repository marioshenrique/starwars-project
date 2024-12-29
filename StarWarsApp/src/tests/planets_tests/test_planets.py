from fastapi.testclient import TestClient
from main import app
from tests.conftest import mock_not_found
from tests.planets_tests.fixtures import (
    mock_get_data_list_of_test_get_planets_success,
    mock_get_data_of_test_get_planet_by_id_success,
    mock_get_correlated_data_of_test_get_residents_by_planet_success,
)
from tests.people_tests.fixtures import mock_people_data

client = TestClient(app)


def test_get_planets_success(mock_get_data_list_of_test_get_planets_success, mocker):
    mocker.patch(
        "services.planets_service.get_data_list",
        return_value=mock_get_data_list_of_test_get_planets_success,
    )
    response = client.get(f"/planets")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["count", "planets"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 2
    assert len(data["planets"]) == 2


def test_get_planet_by_id_success(
    mock_get_data_of_test_get_planet_by_id_success, mocker
):

    mocker.patch(
        "services.planets_service.get_data",
        return_value=mock_get_data_of_test_get_planet_by_id_success,
    )
    planet_id = 1
    response = client.get(f"/planets/{planet_id}")
    data = response.json()
    assert response.status_code == 200
    expected_fields = [
        "planet_id",
        "name",
        "rotation_period",
        "orbital_period",
        "diameter",
        "climate",
        "gravity",
        "terrain",
        "surface_water",
        "population",
        "residents_ids",
        "films_ids",
        "created",
        "edited",
    ]
    for field in expected_fields:
        assert field in data
    assert data["name"] == "Tatooine"
    assert data["rotation_period"] == "23"
    assert data["orbital_period"] == "304"
    assert data["diameter"] == "10465"
    assert data["climate"] == "arid"
    assert data["gravity"] == "1 standard"
    assert data["terrain"] == "desert"
    assert data["surface_water"] == "1"
    assert data["population"] == "200000"
    assert len(data["residents_ids"]) == 2
    assert len(data["films_ids"]) == 2
    expected_residents_ids = ["1", "2"]
    assert data["residents_ids"] == expected_residents_ids
    expected_films_ids = ["1", "2"]
    assert data["films_ids"] == expected_films_ids


def test_get_planets_by_id_not_found(mock_not_found, mocker):
    mocker.patch(
        "services.external.swapi_service.httpx.AsyncClient.get",
        side_effect=mock_not_found,
    )
    planet_id = 999
    response = client.get(f"/planets/{planet_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Resource not found in external API"}


def test_get_residents_by_planet_success(
    mock_get_correlated_data_of_test_get_residents_by_planet_success, mocker
):
    mocker.patch(
        "services.planets_service.get_correlated_data",
        return_value=mock_get_correlated_data_of_test_get_residents_by_planet_success,
    )
    planet_id = 1
    response = client.get(f"/planets/{planet_id}/residents")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["planet_id", "count", "residents"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 2
    assert len(data["residents"]) == 2


def test_get_residents_by_planet_not_found(mock_not_found, mocker):
    mocker.patch(
        "services.external.swapi_service.httpx.AsyncClient.get",
        side_effect=mock_not_found,
    )
    planet_id = 999
    response = client.get(f"/planets/{planet_id}/residents")
    assert response.status_code == 404
    assert response.json() == {"detail": "Resource not found in external API"}
