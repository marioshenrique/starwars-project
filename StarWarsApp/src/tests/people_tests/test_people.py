from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_people_success():
    response = client.get("/people")
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 87
    assert len(data["peoples"]) == 87


def test_get_person_by_id_success():
    person_id = 1
    response = client.get(f"/people/{person_id}")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Luke Skywalker"
    assert data["height"] == "172"
    assert data["mass"] == "77"
    assert data["hair_color"] == "blond"
    assert data["skin_color"] == "fair"
    assert data["eye_color"] == "blue"
    assert data["birth_year"] == "19BBY"
    assert data["gender"] == "male"
    assert len(data["films"]) == 5
    assert len(data["species"]) == 1
    assert len(data["vehicles"]) == 2
    assert len(data["starships"]) == 2


def test_get_person_by_id_not_found():
    person_id = 999
    response = client.get(f"/people/{person_id}")
    assert response.status_code == 404


def test_get_vehicles_by_person_success():
    person_id = 1
    response = client.get(f"/people/{person_id}/vehicles")
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 2
    assert len(data["vehicles"]) == 2


def test_get_vehicles_by_person_not_found():
    person_id = 999
    response = client.get(f"/people/{person_id}/vehicles")
    assert response.status_code == 404
