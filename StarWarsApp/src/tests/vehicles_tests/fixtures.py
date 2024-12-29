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
                    "https://example.com/films/1/",
                    "https://example.com/films/5/",
                ],
                "created": "2014-12-10T15:36:25.724000Z",
                "edited": "2014-12-20T21:30:21.661000Z",
                "url": "https://example.com/vehicles/4/",
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
                "films": ["https://example.com/films/1/"],
                "created": "2014-12-10T16:01:52.434000Z",
                "edited": "2014-12-20T21:30:21.665000Z",
                "url": "https://example.com/vehicles/6/",
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
        "films": ["https://example.com/films/1/", "https://example.com/films/5/"],
        "created": "2014-12-10T15:36:25.724000Z",
        "edited": "2014-12-20T21:30:21.661000Z",
        "url": "https://example.com/vehicles/4/",
    }


@pytest.fixture
def mock_get_data_list_of_test_get_vehicles_success():
    return (
        None,
        2,
        [
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
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                ],
                "created": "2014-12-10T15:36:25.724000Z",
                "edited": "2014-12-20T21:30:21.661000Z",
                "url": "https://example.com/vehicles/1/",
            },
            {
                "name": "Snowspeeder",
                "model": "t-47 airspeeder",
                "manufacturer": "Incom corporation",
                "cost_in_credits": "unknown",
                "length": "36.8 ",
                "max_atmosphering_speed": "30",
                "crew": "46",
                "passengers": "30",
                "cargo_capacity": "50000",
                "consumables": "2 months",
                "vehicle_class": "wheeled",
                "pilots": [
                    "https://example.com/people/1/",
                    "https://example.com/people/2/",
                    "https://example.com/people/3/",
                ],
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                ],
                "created": "2014-12-10T15:36:25.724000Z",
                "edited": "2014-12-20T21:30:21.661000Z",
                "url": "https://example.com/vehicles/1/",
            },
        ],
    )


@pytest.fixture
def mock_get_data_of_test_get_vehicles_by_id_success():
    return {
        "name": "Snowspeeder",
        "model": "t-47 airspeeder",
        "manufacturer": "Incom corporation",
        "cost_in_credits": "unknown",
        "length": "36.8 ",
        "max_atmosphering_speed": "30",
        "crew": "46",
        "passengers": "30",
        "cargo_capacity": "50000",
        "consumables": "2 months",
        "vehicle_class": "wheeled",
        "pilots": [
            "https://example.com/people/1/",
            "https://example.com/people/2/",
            "https://example.com/people/3/",
        ],
        "films": [
            "https://example.com/films/1/",
            "https://example.com/films/2/",
        ],
        "created": "2014-12-10T15:36:25.724000Z",
        "edited": "2014-12-20T21:30:21.661000Z",
        "url": "https://example.com/vehicles/1/",
    }
