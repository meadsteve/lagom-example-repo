import random
from typing import NewType, List

from starlette.responses import JSONResponse

Greeting = NewType("Greeting", str)


class MessageGenerator:
    def __init__(self, messages: List[Greeting]):
        self._messages = messages

    def random_message(self):
        return random.choice(self._messages)


def homepage_handler(request, messages: MessageGenerator):
    return JSONResponse({
        'message': messages.random_message()
    })
