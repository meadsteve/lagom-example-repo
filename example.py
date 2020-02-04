import random

from lagom import Container
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


class MessageGenerator:
    def __init__(self, messages):
        self._messages = messages

    def random_message(self):
        return random.choice(self._messages)


WELCOME_MESSAGES = ["Hello", "Hej", "Hellå"]


container = Container()
container[MessageGenerator] = lambda: MessageGenerator(WELCOME_MESSAGES)


def homepage(request, messages: MessageGenerator):
    return JSONResponse({
        'message': messages.random_message()
    })


app = Starlette(debug=True, routes=[
    Route('/', container.partial(homepage)),
])
