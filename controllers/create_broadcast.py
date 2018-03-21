import json

from models import Broadcast
from controllers.utils import admin_only, send_message


@admin_only
def create_broadcast(message, _data, chat_id):
    identifier = None
    content = None
    joke = None

    message = message.replace('/createbroadcast ', '')
    parts = message.split(', ')

    if len(parts) < 2:
        return send_message("Cannot create Broadcast", chat_id)

    for index, part in enumerate(parts):
        if index == 0:
            identifier = part
        elif index == 1:
            content = part
        elif index == 2:
            joke = json.loads(part)

    Broadcast(identifier, content, joke).save()

    send_message("Broadcast saved!", chat_id)
