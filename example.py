import random

from lagom import Container, bind_to_container
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

container = Container()


class MessageGenerator:
    def __init__(self):
        self._messages = ["Hello", "Hej", "Hellå"]

    def random_message(self):
        return random.choice(self._messages)


@bind_to_container(container)
def homepage(request, messages: MessageGenerator):
    return JSONResponse({
        'message': messages.random_message()
    })


app = Starlette(debug=True, routes=[
    Route('/', homepage),
])
