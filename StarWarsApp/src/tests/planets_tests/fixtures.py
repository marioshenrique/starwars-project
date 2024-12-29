import pytest


@pytest.fixture
def mock_planets_data():
    return {
        "count": 2,
        "next": None,
        "previous": None,
        "results": [
            {
                "name": "Tatooine",
                "rotation_period": "23",
                "orbital_period": "304",
                "diameter": "10465",
                "climate": "arid",
                "gravity": "1 standard",
                "terrain": "desert",
                "surface_water": "1",
                "population": "200000",
                "residents": [
                    "https://example.com/people/1/",
                    "https://example.com/people/2/",
                    "https://example.com/people/4/",
                    "https://example.com/people/6/",
                    "https://example.com/people/7/",
                    "https://example.com/people/8/",
                    "https://example.com/people/9/",
                    "https://example.com/people/11/",
                    "https://example.com/people/43/",
                    "https://example.com/people/62/",
                ],
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/3/",
                    "https://example.com/films/4/",
                    "https://example.com/films/5/",
                    "https://example.com/films/6/",
                ],
                "created": "2014-12-09T13:50:49.641000Z",
                "edited": "2014-12-20T20:58:18.411000Z",
                "url": "https://example.com/planets/1/",
            },
            {
                "name": "Alderaan",
                "rotation_period": "24",
                "orbital_period": "364",
                "diameter": "12500",
                "climate": "temperate",
                "gravity": "1 standard",
                "terrain": "grasslands, mountains",
                "surface_water": "40",
                "population": "2000000000",
                "residents": [
                    "https://example.com/people/5/",
                    "https://example.com/people/68/",
                    "https://example.com/people/81/",
                ],
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/6/",
                ],
                "created": "2014-12-10T11:35:48.479000Z",
                "edited": "2014-12-20T20:58:18.420000Z",
                "url": "https://example.com/planets/2/",
            },
        ],
    }


@pytest.fixture
def mock_planet_data():
    return {
        "name": "Bespin",
        "rotation_period": "12",
        "orbital_period": "5110",
        "diameter": "118000",
        "climate": "temperate",
        "gravity": "1.5 (surface), 1 standard (Cloud City)",
        "terrain": "gas giant",
        "surface_water": "0",
        "population": "6000000",
        "residents": ["https://example.com/people/26/"],
        "films": ["https://example.com/films/2/"],
        "created": "2014-12-10T11:43:55.240000Z",
        "edited": "2014-12-20T20:58:18.427000Z",
        "url": "https://example.com/planets/6/",
    }


@pytest.fixture
def mock_get_data_list_of_test_get_planets_success():
    return (
        None,
        2,
        [
            {
                "name": "Tatooine",
                "rotation_period": "23",
                "orbital_period": "304",
                "diameter": "10465",
                "climate": "arid",
                "gravity": "1 standard",
                "terrain": "desert",
                "surface_water": "1",
                "population": "200000",
                "residents": [
                    "https://example.com/people/1/",
                    "https://example.com/people/2/",
                ],
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                ],
                "created": "2014-12-09T13:50:49.641000Z",
                "edited": "2014-12-20T20:58:18.411000Z",
                "url": "https://example.com/planets/1/",
            },
            {
                "name": "Alderaan",
                "rotation_period": "24",
                "orbital_period": "364",
                "diameter": "12500",
                "climate": "temperate",
                "gravity": "1 standard",
                "terrain": "grasslands, mountains",
                "surface_water": "40",
                "population": "2000000000",
                "residents": [
                    "https://example.com/people/1/",
                    "https://example.com/people/2/",
                ],
                "films": [
                    "https://example.com/films/1/",
                    "https://example.com/films/2/",
                ],
                "created": "2014-12-10T11:35:48.479000Z",
                "edited": "2014-12-20T20:58:18.420000Z",
                "url": "https://example.com/planets/2/",
            },
        ],
    )


@pytest.fixture
def mock_get_data_of_test_get_planet_by_id_success():
    return {
        "name": "Tatooine",
        "rotation_period": "23",
        "orbital_period": "304",
        "diameter": "10465",
        "climate": "arid",
        "gravity": "1 standard",
        "terrain": "desert",
        "surface_water": "1",
        "population": "200000",
        "residents": [
            "https://example.com/people/1/",
            "https://example.com/people/2/",
        ],
        "films": ["https://example.com/films/1/", "https://example.com/films/2/"],
        "created": "2014-12-09T13:50:49.641000Z",
        "edited": "2014-12-20T20:58:18.411000Z",
        "url": "https://example.com/planets/1/",
    }


@pytest.fixture
def mock_get_correlated_data_of_test_get_residents_by_planet_success():
    return {
        "count": 2,
        "residents": [
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
