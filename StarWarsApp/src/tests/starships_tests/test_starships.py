from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_starships_success():
    response = client.get(f"/starships")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["count", "starships"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 37
    assert len(data["starships"]) == 37


def test_get_starships_by_id_success():
    starship_id = 10
    response = client.get(f"/starships/{starship_id}")
    data = response.json()
    assert response.status_code == 200
    expected_fields = [
        "starship_id",
        "name",
        "model",
        "manufacturer",
        "cost_in_credits",
        "length",
        "max_atmosphering_speed",
        "crew",
        "passengers",
        "cargo_capacity",
        "consumables",
        "hyperdrive_rating",
        "MGLT",
        "starship_class",
        "pilots_ids",
        "films_ids",
        "created",
        "edited",
    ]
    for field in expected_fields:
        assert field in data
    assert data["name"] == "Millennium Falcon"
    assert data["model"] == "YT-1300 light freighter"
    assert data["manufacturer"] == "Corellian Engineering Corporation"
    assert len(data["pilots_ids"]) == 4
    assert len(data["films_ids"]) == 4
    expected_pilots_ids = ["13", "14", "25", "31"]
    assert data["pilots_ids"] == expected_pilots_ids
    expected_films_ids = ["1", "2", "3", "7"]
    assert data["films_ids"] == expected_films_ids


def test_get_starships_by_id_not_found():
    starship_id = 999
    response = client.get(f"/starships/{starship_id}")
    assert response.status_code == 404


def test_get_vehicles_by_starship_success():
    starship_id = 10
    response = client.get(f"/starships/{starship_id}/pilots")
    data = response.json()
    assert response.status_code == 200
    expected_fields = ["starship_id", "count", "pilots"]
    for field in expected_fields:
        assert field in data
    assert data["count"] == 4
    assert len(data["pilots"]) == 4


def test_get_vehicles_by_starship_not_found():
    starship_id = 999
    response = client.get(f"/starships/{starship_id}/pilots")
    assert response.status_code == 404
