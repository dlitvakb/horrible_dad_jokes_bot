from models import User
from controllers.utils import send_message

def forget_me(_message, _data, chat_id):
    user = User.find(chat_id)
    if user is not None:
        User.delete(user)
        return send_message("Your user has been forgotten.", chat_id)
    return send_message("Your user has been already forgotten previously.", chat_id)
