import os
import json

from loader import load_env

load_env()

from contentful import Client as CDA

from models import User
from controllers.utils import send_message, help_text
from controllers import help_, start, create_broadcast, tell_me_a_joke, forget_me

def endpoint_dispatcher(event, context):
    data = json.loads(event['body'])
    message = str(data['message']['text'])
    chat_id = data['message']['chat']['id']

    registered_functions = {
        '/start': start,
        '/tellmeajoke': tell_me_a_joke,
        '/createbroadcast': create_broadcast,
        '/forgetme': forget_me,
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

def broadcast(event, context):
    webhook = json.loads(event['body'])

    # We are only interested in broadcast messages
    if webhook['sys']['contentType']['sys']['id'] != 'broadcast':
        return {"statusCode": 200}

    cda = CDA(os.environ['CF_SPACE_ID'], os.environ['CF_CDA_TOKEN'])
    broadcast_id = webhook['sys']['id']

    message = cda.entry(broadcast_id, {'include': 2})

    response = message.content

    if 'joke' in message.fields() and message.joke is not None:
        response += "\n\nAlso, we have a nice joke for you:\n{0}\n\nSource: {1}".format(
            message.joke.content,
            message.joke.source
        )

    users = User.all()
    for user in users:
        send_message(response, user.chat_id)

    return {"statusCode": 200}
