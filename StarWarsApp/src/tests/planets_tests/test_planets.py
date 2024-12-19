from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_planets_success():
    response = client.get(f"/planets")
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 61
    assert len(data["planets"]) == 61


def test_get_planet_by_id_success():
    planet_id = 1
    response = client.get(f"/planets/{planet_id}")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Tatooine"
    assert data["rotation_period"] == "23"
    assert data["orbital_period"] == "304"
    assert data["diameter"] == "10465"
    assert data["climate"] == "arid"
    assert data["gravity"] == "1 standard"
    assert data["terrain"] == "desert"
    assert data["surface_water"] == "1"
    assert data["population"] == "200000"
    assert len(data["residents"]) == 10
    assert len(data["films"]) == 5


def test_get_planets_by_id_not_found():
    planet_id = 999
    response = client.get(f"/planets/{planet_id}")
    assert response.status_code == 404


def test_get_residents_by_planet_success():
    planet_id = 1
    response = client.get(f"/planets/{planet_id}/residents")
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 10
    assert len(data["residents"]) == 10


def test_get_residents_by_planet_not_found():
    planet_id = 999
    response = client.get(f"/planets/{planet_id}/residents")
    assert response.status_code == 404
