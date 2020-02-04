from starlette.responses import JSONResponse

from example import homepage, MessageGenerator


def test_my_homepage_greets_my_guests():
    class FakeGreeter:
        def random_message(self):
            return "fake greeting"

    expected_response = JSONResponse({
        "message": "fake greeting"
    })
    assert homepage({}, FakeGreeter()).body == expected_response.body  # type: ignore
