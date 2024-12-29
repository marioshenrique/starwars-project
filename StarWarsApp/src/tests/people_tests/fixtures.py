import pytest


@pytest.fixture
def mock_peoples_data():
    return {
        "count": 2,
        "next": None,
        "previous": None,
        "results": [
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
                "species": [],
                "vehicles": [
                    "https://example.com/vehicles/14/",
                    "https://example.com/vehicles/30/",
                ],
                "starships": [
                    "https://example.com/starships/12/",
                    "https://example.com/starships/22/",
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
                "species": ["https://example.com/species/2/"],
                "vehicles": [],
                "starships": [],
                "created": "2014-12-10T15:10:51.357000Z",
                "edited": "2014-12-20T21:17:50.309000Z",
                "url": "https://example.com/people/2/",
            },
        ],
    }


@pytest.fixture
def mock_people_data():
    return {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male",
        "homeworld": "https://example.com/planets/1/",
        "films": ["https://example.com/films/1/", "https://example.com/films/2/"],
        "species": [],
        "vehicles": [
            "https://example.com/vehicles/14/",
            "https://example.com/vehicles/30/",
        ],
        "starships": [
            "https://example.com/starships/12/",
            "https://example.com/starships/22/",
        ],
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-20T21:17:56.891000Z",
        "url": "https://example.com/people/1/",
    }


@pytest.fixture
def mock_get_data_list_of_test_get_people_success():
    return (
        None,
        2,
        [
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
    )


@pytest.fixture
def mock_get_data_of_test_get_person_by_id_success():
    return {
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
    }


@pytest.fixture
def mock_get_correlated_data_of_test_get_vehicles_by_person_success():
    return {
        "count": 2,
        "vehicles": [
            {
                "name": "Snowspeeder",
                "model": "t-47 airspeeder",
                "manufacturer": "Incom corporation",
                "cost_in_credits": "unknown",
                "length": "4.5",
                "max_atmosphering_speed": "650",
                "crew": "2",
                "passengers": "0",
                "cargo_capacity": "10",
                "consumables": "none",
                "vehicle_class": "airspeeder",
                "pilots": [
                    "https://example.com/people/1/",
                    "https://example.com/people/2/",
                    "https://example.com/people/3/",
                ],
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                ],
                "created": "2014-12-15T12:22:12Z",
                "edited": "2014-12-20T21:30:21.672000Z",
                "url": "https://example.com/vehicles/1/",
            },
            {
                "name": "TIE bomber",
                "model": "TIE/sa bomber",
                "manufacturer": "Sienar Fleet Systems",
                "cost_in_credits": "unknown",
                "length": "7.8",
                "max_atmosphering_speed": "850",
                "crew": "1",
                "passengers": "0",
                "cargo_capacity": "none",
                "consumables": "2 days",
                "vehicle_class": "space/planetary bomber",
                "pilots": [],
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                ],
                "created": "2014-12-15T12:22:12Z",
                "edited": "2014-12-20T21:30:21.672000Z",
                "url": "https://example.com/vehicles/2/",
            },
        ],
    }
