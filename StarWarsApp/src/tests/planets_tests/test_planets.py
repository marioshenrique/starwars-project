from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_planets_success():
    response = client.get(f"/planets")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["count", "planets"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 61
    assert len(data["planets"]) == 61


def test_get_planet_by_id_success():
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
    assert len(data["residents_ids"]) == 10
    assert len(data["films_ids"]) == 5
    expected_residents_ids = ["1", "2", "4", "6", "7", "8", "9", "11", "43", "62"]
    assert data["residents_ids"] == expected_residents_ids
    expected_films_ids = ["1", "3", "4", "5", "6"]
    assert data["films_ids"] == expected_films_ids


def test_get_planets_by_id_not_found():
    planet_id = 999
    response = client.get(f"/planets/{planet_id}")
    assert response.status_code == 404


def test_get_residents_by_planet_success():
    planet_id = 1
    response = client.get(f"/planets/{planet_id}/residents")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["planet_id", "count", "residents"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 10
    assert len(data["residents"]) == 10


def test_get_residents_by_planet_not_found():
    planet_id = 999
    response = client.get(f"/planets/{planet_id}/residents")
    assert response.status_code == 404
