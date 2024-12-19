from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_species_success():
    response = client.get(f"/species")
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 37
    assert len(data["species"]) == 37


def test_get_species_by_id_success():
    specie_id = 1
    response = client.get(f"/species/{specie_id}")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Human"
    assert data["classification"] == "mammal"
    assert data["designation"] == "sentient"
    assert data["average_height"] == "180"
    assert data["skin_colors"] == "caucasian, black, asian, hispanic"
    assert data["hair_colors"] == "blonde, brown, black, red"
    assert data["eye_colors"] == "brown, blue, green, hazel, grey, amber"
    assert data["average_lifespan"] == "120"
    assert data["language"] == "Galactic Basic"
    assert len(data["people"]) == 35
    assert len(data["films"]) == 7


def test_get_species_by_id_not_found():
    specie_id = 999
    response = client.get(f"/species/{specie_id}")
    assert response.status_code == 404


def test_get_people_by_specie_success():
    specie_id = 1
    response = client.get(f"species/{specie_id}/people")
    data = response.json()
    assert response.status_code == 200
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
    assert data["count"] == 7
    assert len(data["films"]) == 7


def test_get_films_by_specie_not_found():
    specie_id = 999
    response = client.get(f"/species/{specie_id}/films")
    assert response.status_code == 404
