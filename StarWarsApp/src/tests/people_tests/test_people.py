from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_people_success():
    response = client.get("/people")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["count", "people"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 87
    assert len(data["people"]) == 87


def test_get_person_by_id_success():
    person_id = 1
    response = client.get(f"/people/{person_id}")
    data = response.json()
    assert response.status_code == 200
    expected_fields = [
        "person_id",
        "name",
        "height",
        "mass",
        "hair_color",
        "skin_color",
        "eye_color",
        "birth_year",
        "gender",
        "home_planet_id",
        "films_ids",
        "species_ids",
        "vehicles_ids",
        "starships_ids",
        "created",
        "edited",
    ]
    for field in expected_fields:
        assert field in data
    assert data["name"] == "Luke Skywalker"
    assert data["height"] == "172"
    assert data["mass"] == "77"
    assert data["hair_color"] == "blond"
    assert data["skin_color"] == "fair"
    assert data["eye_color"] == "blue"
    assert data["birth_year"] == "19BBY"
    assert data["gender"] == "male"
    assert len(data["films_ids"]) == 5
    assert len(data["species_ids"]) == 1
    assert len(data["vehicles_ids"]) == 2
    assert len(data["starships_ids"]) == 2
    expected_films_ids = ["1", "2", "3", "6", "7"]
    assert data["films_ids"] == expected_films_ids
    expected_species_ids = [
        "1",
    ]
    assert data["species_ids"] == expected_species_ids
    expected_vehicles_ids = ["14", "30"]
    assert data["vehicles_ids"] == expected_vehicles_ids
    expected_starships_ids = ["12", "22"]
    assert data["starships_ids"] == expected_starships_ids


def test_get_person_by_id_not_found():
    person_id = 999
    response = client.get(f"/people/{person_id}")
    assert response.status_code == 404


def test_get_vehicles_by_person_success():
    person_id = 1
    response = client.get(f"/people/{person_id}/vehicles")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["people_id", "count", "vehicles"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 2
    assert len(data["vehicles"]) == 2


def test_get_vehicles_by_person_not_found():
    person_id = 999
    response = client.get(f"/people/{person_id}/vehicles")
    assert response.status_code == 404
