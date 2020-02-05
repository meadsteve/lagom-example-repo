import random

from starlette.responses import JSONResponse


class MessageGenerator:
    def __init__(self, messages):
        self._messages = messages

    def random_message(self):
        return random.choice(self._messages)


def homepage_handler(request, messages: MessageGenerator):
    return JSONResponse({
        'message': messages.random_message()
    })
