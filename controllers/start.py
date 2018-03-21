from models import User
from controllers.utils import send_message, help_text

def start(_message, _data, chat_id):
    print('Registering user')
    User(chat_id).save()

    send_message(
        "{0}\n\n{1}".format(
            "Welcome to the Horrible Dad Jokes Bot!",
            help_text()
        ),
        chat_id
    )

