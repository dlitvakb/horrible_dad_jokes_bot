import os
import json
import random

from loader import load_env

load_env()

import requests
from joke import Joke
from user import User

BASE_URL = "https://api.telegram.org/bot{0}".format(os.environ['TG_BOT_TOKEN'])

def message_url():
    return "{0}/sendMessage".format(BASE_URL)

def send_message(response, chat_id):
    requests.post(message_url(), {'text': response, 'chat_id': chat_id})

def endpoint_dispatcher(event, context):
    data = json.loads(event['body'])
    message = str(data['message']['text'])
    chat_id = data['message']['chat']['id']

    registered_functions = {
        '/start': start,
        '/tellmeajoke': tell_me_a_joke,
        '/help': help_
    }

    command = message.lower().split()[0]
    print('Called command: {0}'.format(command))

    if '/' not in command or command not in registered_functions:
        print('Command not recognized')
        send_message(help_text(), chat_id)
        return {"statusCode": 200}

    registered_functions[command](message, data, chat_id)
    return {"statusCode": 200}

def help_text():
    available_commands = {
        "/start": "Starts the bot",
        "/tellmeajoke": "Tells you a random horrible dad joke",
        "/help": "Prints this message"
    }

    response = "Here are the available commands:\n"
    for command, description in available_commands.items():
        response += "\t{0}: {1}\n".format(command, description)

    return response

def help_(_message, _data, chat_id):
    send_message(help_text(), chat_id)

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

def tell_me_a_joke(_message, _data, chat_id):
    jokes = Joke.all()
    joke = random.choice(jokes)

    response = "Here you go:\n{0}\n\nSource: {1}".format(
        joke.content,
        joke.source
    )
    send_message(response, chat_id)
