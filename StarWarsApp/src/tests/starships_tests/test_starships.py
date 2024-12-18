from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_starships_success():
    response = client.get(f"/starships")
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 37
    assert len(data["starships"]) == 37

def test_get_starships_by_id_success():
    starship_id = 2
    response = client.get(f"/starships/{starship_id}")
    data = response.json()
    assert data["name"] == "CR90 corvette"
    assert data["model"] == "CR90 corvette"
    assert data["manufacturer"] == "Corellian Engineering Corporation"
    assert len(data["pilots"]) == 0
    assert len(data["films"]) == 3

def test_get_starships_by_id_not_found():
    starship_id = 999
    response = client.get(f"/starships/{starship_id}")
    assert response.status_code == 404

def test_get_vehicles_by_starship_success():
    starship_id = 10
    response = client.get(f"/starships/{starship_id}/pilots")
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 4
    assert len(data["pilots"]) == 4

def test_get_vehicles_by_starship_not_found():
    starship_id = 999
    response = client.get(f"/starships/{starship_id}/pilots")
    assert response.status_code == 404