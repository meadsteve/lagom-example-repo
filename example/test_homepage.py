from starlette.responses import JSONResponse

from .homepage import homepage_handler


def test_my_homepage_greets_my_guests():
    class FakeGreeter:
        def random_message(self):
            return "fake greeting"

    expected_response = JSONResponse({
        "message": "fake greeting"
    })
    assert homepage_handler({}, FakeGreeter()).body == expected_response.body  # type: ignore
