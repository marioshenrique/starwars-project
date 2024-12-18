from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_films_success():
    response = client.get("/films")
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 7
    assert len(data["films"]) == 7

def test_get_film_by_id_success():
    film_id = 1
    response = client.get(f"/films/{film_id}")
    data = response.json()
    assert response.status_code == 200
    assert data["title"] == "A New Hope"
    assert data["director"] == "George Lucas"
    assert data["producer"] == "Gary Kurtz, Rick McCallum"
    assert data["release_date"] == "1977-05-25"

def test_get_film_by_id_not_found():
    film_id = 9999
    response = client.get(f"/films/{film_id}")
    assert response.status_code == 404

def test_get_characters_by_film_success():
    film_id = 1
    response = client.get(f"/films/{film_id}/characters")
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 18
    assert len(data["characters"]) == 18

def test_get_characters_by_film_not_found():
    film_id = 9999
    response = client.get(f"/films/{film_id}/characters")
    assert response.status_code == 404