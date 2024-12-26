from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_films_success():
    response = client.get("/films")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["count", "films"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 7
    assert len(data["films"]) == 7


def test_get_film_by_id_success():
    film_id = 1
    response = client.get(f"/films/{film_id}")
    data = response.json()
    assert response.status_code == 200
    expected_fields = [
        "film_id",
        "title",
        "episode_id",
        "opening_crawl",
        "director",
        "producer",
        "release_date",
        "created",
        "edited",
        "characters_ids",
        "planets_ids",
        "starships_ids",
        "vehicles_ids",
        "species_ids",
    ]
    for field in expected_fields:
        assert field in data
    assert data["film_id"] == "1"
    assert data["title"] == "A New Hope"
    assert data["director"] == "George Lucas"
    assert data["producer"] == "Gary Kurtz, Rick McCallum"
    assert data["release_date"] == "1977-05-25"
    expected_characters_ids = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "12",
        "13",
        "14",
        "15",
        "16",
        "18",
        "19",
        "81",
    ]
    assert data["characters_ids"] == expected_characters_ids
    expected_planets_ids = [
        "1",
        "2",
        "3",
    ]
    assert data["planets_ids"] == expected_planets_ids
    expected_starships_ids = ["2", "3", "5", "9", "10", "11", "12", "13"]
    assert data["starships_ids"] == expected_starships_ids
    expected_vehicles_ids = ["4", "6", "7", "8"]
    assert data["vehicles_ids"] == expected_vehicles_ids
    expected_species_ids = ["1", "2", "3", "4", "5"]
    assert data["species_ids"] == expected_species_ids


def test_get_film_by_id_not_found():
    film_id = 9999
    response = client.get(f"/films/{film_id}")
    assert response.status_code == 404


def test_get_characters_by_film_success():
    film_id = 1
    response = client.get(f"/films/{film_id}/characters")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["film_id", "count", "characters"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 18
    assert len(data["characters"]) == 18
    assert data["film_id"] == "1"


def test_get_characters_by_film_not_found():
    film_id = 9999
    response = client.get(f"/films/{film_id}/characters")
    assert response.status_code == 404
