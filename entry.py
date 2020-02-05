from typing import List

from lagom import Container
from starlette.applications import Starlette
from starlette.routing import Route

from example.homepage import homepage_handler, Greeting

container = Container()
container[List[Greeting]] = [
    Greeting("Hello"),
    Greeting("Hej"),
    Greeting("Hellå")
]

app = Starlette(debug=True, routes=[
    Route('/', container.partial(homepage_handler)),
])
