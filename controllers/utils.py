import os
import requests


BASE_URL = "https://api.telegram.org/bot{0}".format(os.environ['TG_BOT_TOKEN'])


def message_url():
    return "{0}/sendMessage".format(BASE_URL)


def send_message(response, chat_id):
    requests.post(message_url(), {'text': response, 'chat_id': chat_id})


def help_text():
    available_commands = {
        "/start": "Starts the bot",
        "/tellmeajoke": "Tells you a random horrible dad joke",
        "/forgetme": "Removes this chat from receiving notices and updates",
        "/help": "Prints this message"
    }

    response = "Here are the available commands:\n"
    for command, description in available_commands.items():
        response += "\t{0}: {1}\n".format(command, description)

    return response


def admin_only(fn):
    def authenticated(message, data, chat_id):
        if int(chat_id) == int(os.environ['TG_ADMIN_ID']):
            fn(message, data, chat_id)
            return {"statusCode": 200}
        send_message("You're not authorized for this operation", chat_id)
        return {"statusCode": 200}
    return authenticated
