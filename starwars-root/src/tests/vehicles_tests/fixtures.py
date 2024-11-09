import pytest


@pytest.fixture
def mock_vehicles_data():
    return {
        "count": 2,
        "next": None,
        "previous": None,
        "results": [
            {
                "name": "Sand Crawler",
                "model": "Digger Crawler",
                "manufacturer": "Corellia Mining Corporation",
                "cost_in_credits": "150000",
                "length": "36.8 ",
                "max_atmosphering_speed": "30",
                "crew": "46",
                "passengers": "30",
                "cargo_capacity": "50000",
                "consumables": "2 months",
                "vehicle_class": "wheeled",
                "pilots": [],
                "films": [
                    "https://swapi.dev/api/films/1/",
                    "https://swapi.dev/api/films/5/",
                ],
                "created": "2014-12-10T15:36:25.724000Z",
                "edited": "2014-12-20T21:30:21.661000Z",
                "url": "https://swapi.dev/api/vehicles/4/",
            },
            {
                "name": "T-16 skyhopper",
                "model": "T-16 skyhopper",
                "manufacturer": "Incom Corporation",
                "cost_in_credits": "14500",
                "length": "10.4 ",
                "max_atmosphering_speed": "1200",
                "crew": "1",
                "passengers": "1",
                "cargo_capacity": "50",
                "consumables": "0",
                "vehicle_class": "repulsorcraft",
                "pilots": [],
                "films": ["https://swapi.dev/api/films/1/"],
                "created": "2014-12-10T16:01:52.434000Z",
                "edited": "2014-12-20T21:30:21.665000Z",
                "url": "https://swapi.dev/api/vehicles/6/",
            },
        ],
    }


@pytest.fixture
def mock_vehicle_data():
    return {
        "name": "Sand Crawler",
        "model": "Digger Crawler",
        "manufacturer": "Corellia Mining Corporation",
        "cost_in_credits": "150000",
        "length": "36.8 ",
        "max_atmosphering_speed": "30",
        "crew": "46",
        "passengers": "30",
        "cargo_capacity": "50000",
        "consumables": "2 months",
        "vehicle_class": "wheeled",
        "pilots": [],
        "films": ["https://swapi.dev/api/films/1/", "https://swapi.dev/api/films/5/"],
        "created": "2014-12-10T15:36:25.724000Z",
        "edited": "2014-12-20T21:30:21.661000Z",
        "url": "https://swapi.dev/api/vehicles/4/",
    }
