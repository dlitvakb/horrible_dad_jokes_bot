import random
from models import Joke
from controllers.utils import send_message


def tell_me_a_joke(_message, _data, chat_id):
    jokes = Joke.all()
    joke = random.choice(jokes)

    response = "Here you go:\n{0}\n\nSource: {1}".format(
        joke.content,
        joke.source
    )
    send_message(response, chat_id)
