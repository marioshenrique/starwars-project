import pytest


@pytest.fixture
def mock_starships_data():
    return {
        "count": 2,
        "next": None,
        "previous": None,
        "results": [
            {
                "name": "CR90 corvette",
                "model": "CR90 corvette",
                "manufacturer": "Corellian Engineering Corporation",
                "cost_in_credits": "3500000",
                "length": "150",
                "max_atmosphering_speed": "950",
                "crew": "30-165",
                "passengers": "600",
                "cargo_capacity": "3000000",
                "consumables": "1 year",
                "hyperdrive_rating": "2.0",
                "MGLT": "60",
                "starship_class": "corvette",
                "pilots": [],
                "films": [
                    "https://swapi.dev/api/films/1/",
                    "https://swapi.dev/api/films/3/",
                ],
                "created": "2014-12-10T14:20:33.369000Z",
                "edited": "2014-12-20T21:23:49.867000Z",
                "url": "https://swapi.dev/api/starships/2/",
            },
            {
                "name": "Star Destroyer",
                "model": "Imperial I-class Star Destroyer",
                "manufacturer": "Kuat Drive Yards",
                "cost_in_credits": "150000000",
                "length": "1,600",
                "max_atmosphering_speed": "975",
                "crew": "47,060",
                "passengers": "n/a",
                "cargo_capacity": "36000000",
                "consumables": "2 years",
                "hyperdrive_rating": "2.0",
                "MGLT": "60",
                "starship_class": "Star Destroyer",
                "pilots": [],
                "films": [
                    "https://swapi.dev/api/films/1/",
                    "https://swapi.dev/api/films/2/",
                ],
                "created": "2014-12-10T15:08:19.848000Z",
                "edited": "2014-12-20T21:23:49.870000Z",
                "url": "https://swapi.dev/api/starships/3/",
            },
        ],
    }


@pytest.fixture
def mock_starship_data():
    return {
        "name": "CR90 corvette",
        "model": "CR90 corvette",
        "manufacturer": "Corellian Engineering Corporation",
        "cost_in_credits": "3500000",
        "length": "150",
        "max_atmosphering_speed": "950",
        "crew": "30-165",
        "passengers": "600",
        "cargo_capacity": "3000000",
        "consumables": "1 year",
        "hyperdrive_rating": "2.0",
        "MGLT": "60",
        "starship_class": "corvette",
        "pilots": [],
        "films": ["https://swapi.dev/api/films/1/", "https://swapi.dev/api/films/3/"],
        "created": "2014-12-10T14:20:33.369000Z",
        "edited": "2014-12-20T21:23:49.867000Z",
        "url": "https://swapi.dev/api/starships/2/",
    }
