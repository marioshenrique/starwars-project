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
                    "https://example.com/films/1/",
                    "https://example.com/films/3/",
                ],
                "created": "2014-12-10T14:20:33.369000Z",
                "edited": "2014-12-20T21:23:49.867000Z",
                "url": "https://example.com/starships/2/",
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
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                ],
                "created": "2014-12-10T15:08:19.848000Z",
                "edited": "2014-12-20T21:23:49.870000Z",
                "url": "https://example.com/starships/3/",
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
        "films": ["https://example.com/films/1/", "https://example.com/films/3/"],
        "created": "2014-12-10T14:20:33.369000Z",
        "edited": "2014-12-20T21:23:49.867000Z",
        "url": "https://example.com/starships/2/",
    }


@pytest.fixture
def mock_get_data_list_of_test_get_starships_success():
    return (
        None,
        2,
        [
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
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                ],
                "created": "2014-12-10T14:20:33.369000Z",
                "edited": "2014-12-20T21:23:49.867000Z",
                "url": "https://example.com/starships/1/",
            },
            {
                "name": "X-wing",
                "model": "T-65 X-wing",
                "manufacturer": "Incom Corporation",
                "cost_in_credits": "149999",
                "length": "12.5",
                "max_atmosphering_speed": "1050",
                "crew": "1",
                "passengers": "0",
                "cargo_capacity": "110",
                "consumables": "1 week",
                "hyperdrive_rating": "1.0",
                "MGLT": "100",
                "starship_class": "Starfighter",
                "pilots": [
                    "https://example.com/people/1/",
                    "https://example.com/people/2/",
                    "https://example.com/people/3/",
                ],
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                ],
                "created": "2014-12-12T11:19:05.340000Z",
                "edited": "2014-12-20T21:23:49.886000Z",
                "url": "https://example.com/starships/2/",
            },
        ],
    )


@pytest.fixture
def mock_get_data_of_test_get_starships_by_id_success():
    return {
        "name": "X-wing",
        "model": "T-65 X-wing",
        "manufacturer": "Incom Corporation",
        "cost_in_credits": "149999",
        "length": "12.5",
        "max_atmosphering_speed": "1050",
        "crew": "1",
        "passengers": "0",
        "cargo_capacity": "110",
        "consumables": "1 week",
        "hyperdrive_rating": "1.0",
        "MGLT": "100",
        "starship_class": "Starfighter",
        "pilots": [
            "https://example.com/people/1/",
            "https://example.com/people/2/",
            "https://example.com/people/3/",
        ],
        "films": ["https://example.com/films/1/", "https://example.com/films/2/"],
        "created": "2014-12-12T11:19:05.340000Z",
        "edited": "2014-12-20T21:23:49.886000Z",
        "url": "https://example.com/starships/2/",
    }


@pytest.fixture
def mock_get_correlated_data_of_test_get_pilots_by_starship_success():
    return {
        "count": 2,
        "pilots": [
            {
                "name": "Luke Skywalker",
                "height": "172",
                "mass": "77",
                "hair_color": "blond",
                "skin_color": "fair",
                "eye_color": "blue",
                "birth_year": "19BBY",
                "gender": "male",
                "homeworld": "https://example.com/planets/1/",
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                ],
                "species": ["https://example.com/species/1/"],
                "vehicles": [
                    "https://example.com/vehicles/1/",
                    "https://example.com/vehicles/2/",
                ],
                "starships": [
                    "https://example.com/starships/1/",
                    "https://example.com/starships/2/",
                ],
                "created": "2014-12-09T13:50:51.644000Z",
                "edited": "2014-12-20T21:17:56.891000Z",
                "url": "https://example.com/people/1/",
            },
            {
                "name": "C-3PO",
                "height": "167",
                "mass": "75",
                "hair_color": "n/a",
                "skin_color": "gold",
                "eye_color": "yellow",
                "birth_year": "112BBY",
                "gender": "n/a",
                "homeworld": "https://example.com/planets/1/",
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                ],
                "species": ["https://example.com/species/1/"],
                "vehicles": [
                    "https://example.com/vehicles/1/",
                    "https://example.com/vehicles/2/",
                ],
                "starships": [
                    "https://example.com/starships/1/",
                    "https://example.com/starships/2/",
                ],
                "created": "2014-12-10T15:10:51.357000Z",
                "edited": "2014-12-20T21:17:50.309000Z",
                "url": "https://example.com/people/2/",
            },
        ],
    }
