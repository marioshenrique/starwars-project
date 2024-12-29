from fastapi.testclient import TestClient
from main import app
from tests.conftest import mock_not_found
from tests.species_tests.fixtures import (
    mock_get_data_list_of_test_get_species_success,
    mock_get_data_of_test_get_species_by_id_success,
    mock_get_correlated_data_of_test_get_people_by_specie_success,
    mock_get_correlated_data_of_test_get_films_by_specie_success,
)

client = TestClient(app)


def test_get_species_success(mock_get_data_list_of_test_get_species_success, mocker):
    mocker.patch(
        "services.species_service.get_data_list",
        return_value=mock_get_data_list_of_test_get_species_success,
    )
    response = client.get(f"/species")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["count", "species"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 2
    assert len(data["species"]) == 2


def test_get_species_by_id_success(
    mock_get_data_of_test_get_species_by_id_success, mocker
):
    mocker.patch(
        "services.species_service.get_data",
        return_value=mock_get_data_of_test_get_species_by_id_success,
    )
    specie_id = 1
    response = client.get(f"/species/{specie_id}")
    data = response.json()
    assert response.status_code == 200
    expected_fields = [
        "specie_id",
        "name",
        "classification",
        "designation",
        "average_height",
        "skin_colors",
        "hair_colors",
        "eye_colors",
        "average_lifespan",
        "home_planet_id",
        "language",
        "people_ids",
        "films_ids",
        "created",
        "edited",
    ]
    for field in expected_fields:
        assert field in data
    assert data["name"] == "Human"
    assert data["classification"] == "mammal"
    assert data["designation"] == "sentient"
    assert data["average_height"] == "180"
    assert data["skin_colors"] == "caucasian, black, asian, hispanic"
    assert data["hair_colors"] == "blonde, brown, black, red"
    assert data["eye_colors"] == "brown, blue, green, hazel, grey, amber"
    assert data["average_lifespan"] == "120"
    assert data["language"] == "Galactic Basic"
    assert len(data["people_ids"]) == 2
    assert len(data["films_ids"]) == 3
    expected_people_ids = ["1", "2"]
    assert data["people_ids"] == expected_people_ids
    expected_films_ids = ["1", "2", "3"]
    assert data["films_ids"] == expected_films_ids


def test_get_species_by_id_not_found(mock_not_found, mocker):
    mocker.patch(
        "services.external.swapi_service.httpx.AsyncClient.get",
        side_effect=mock_not_found,
    )
    specie_id = 999
    response = client.get(f"/species/{specie_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Resource not found in external API"}


def test_get_people_by_specie_success(
    mock_get_correlated_data_of_test_get_people_by_specie_success, mocker
):
    mocker.patch(
        "services.species_service.get_correlated_data",
        return_value=mock_get_correlated_data_of_test_get_people_by_specie_success,
    )
    specie_id = 1
    response = client.get(f"species/{specie_id}/people")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["specie_id", "count", "people"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 2
    assert len(data["people"]) == 2


def test_get_people_by_specie_not_found(mock_not_found, mocker):
    mocker.patch(
        "services.external.swapi_service.httpx.AsyncClient.get",
        side_effect=mock_not_found,
    )
    specie_id = 999
    response = client.get(f"/species/{specie_id}/people")
    assert response.status_code == 404
    assert response.json() == {"detail": "Resource not found in external API"}


def test_get_films_by_specie_success(
    mock_get_correlated_data_of_test_get_films_by_specie_success, mocker
):
    mocker.patch(
        "services.species_service.get_correlated_data",
        return_value=mock_get_correlated_data_of_test_get_films_by_specie_success,
    )
    specie_id = 1
    response = client.get(f"/species/{specie_id}/films")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["specie_id", "count", "films"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 2
    assert len(data["films"]) == 2


def test_get_films_by_specie_not_found(mock_not_found, mocker):
    mocker.patch(
        "services.external.swapi_service.httpx.AsyncClient.get",
        side_effect=mock_not_found,
    )
    specie_id = 999
    response = client.get(f"/species/{specie_id}/films")
    assert response.status_code == 404
    assert response.json() == {"detail": "Resource not found in external API"}
