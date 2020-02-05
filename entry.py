from lagom import Container
from starlette.applications import Starlette
from starlette.routing import Route

from example.homepage import MessageGenerator, homepage_handler

WELCOME_MESSAGES = ["Hello", "Hej", "Hellå"]

container = Container()
container[MessageGenerator] = lambda: MessageGenerator(WELCOME_MESSAGES)

app = Starlette(debug=True, routes=[
    Route('/', container.partial(homepage_handler)),
])
