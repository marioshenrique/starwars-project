import sys
import os
import json
from httpx import Response, Request

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import pytest


@pytest.fixture
def mock_not_found():
    def mock_response(url, **kwargs):
        return Response(
            status_code=404,
            request=Request(method="GET", url=url),
            content=json.dumps({"detail": "Not found"}),
        )

    return mock_response
