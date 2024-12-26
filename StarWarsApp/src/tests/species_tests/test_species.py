from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_species_success():
    response = client.get(f"/species")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["count", "species"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 37
    assert len(data["species"]) == 37


def test_get_species_by_id_success():
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
    assert len(data["people_ids"]) == 35
    assert len(data["films_ids"]) == 7
    expected_people_ids = [
        "1",
        "4",
        "5",
        "6",
        "7",
        "9",
        "10",
        "11",
        "12",
        "14",
        "18",
        "21",
        "22",
        "25",
        "26",
        "28",
        "29",
        "32",
        "34",
        "35",
        "39",
        "42",
        "43",
        "51",
        "62",
        "66",
        "67",
        "68",
        "69",
        "74",
        "81",
        "84",
        "85",
        "86",
        "88",
    ]
    assert data["people_ids"] == expected_people_ids
    expected_films_ids = ["1", "2", "3", "4", "5", "6", "7"]
    assert data["films_ids"] == expected_films_ids


def test_get_species_by_id_not_found():
    specie_id = 999
    response = client.get(f"/species/{specie_id}")
    assert response.status_code == 404


def test_get_people_by_specie_success():
    specie_id = 1
    response = client.get(f"species/{specie_id}/people")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["specie_id", "count", "people"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 35
    assert len(data["people"]) == 35


def test_get_people_by_specie_not_found():
    specie_id = 999
    response = client.get(f"/species/{specie_id}/people")
    assert response.status_code == 404


def test_get_films_by_specie_success():
    specie_id = 1
    response = client.get(f"/species/{specie_id}/films")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["specie_id", "count", "films"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 7
    assert len(data["films"]) == 7


def test_get_films_by_specie_not_found():
    specie_id = 999
    response = client.get(f"/species/{specie_id}/films")
    assert response.status_code == 404
