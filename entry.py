from lagom import Container
from lagom.integrations.starlette import StarletteIntegration
from starlette.applications import Starlette

from example.homepage import MessageGenerator, homepage_handler

WELCOME_MESSAGES = ["Hello", "Hej", "Hellå"]

container = Container()
container[MessageGenerator] = lambda: MessageGenerator(WELCOME_MESSAGES)

integration = StarletteIntegration(container)

app = Starlette(debug=True, routes=[
    integration.magic_route('/', homepage_handler),
])
