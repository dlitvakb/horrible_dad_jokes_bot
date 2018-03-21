from controllers.utils import send_message, help_text


def help_(_message, _data, chat_id):
    send_message(help_text(), chat_id)
