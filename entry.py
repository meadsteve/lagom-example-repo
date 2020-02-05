from typing import List

from lagom import Container
from lagom.decorators import dependency_definition
from starlette.applications import Starlette
from starlette.routing import Route

from example.homepage import homepage_handler, Greeting

container = Container()


@dependency_definition(container, singleton=True)
def greetings() -> List[Greeting]:
    return [
        Greeting("Hello"),
        Greeting("Hej"),
        Greeting("Hellå")
    ]


app = Starlette(debug=True, routes=[
    Route('/', container.partial(homepage_handler)),
])
