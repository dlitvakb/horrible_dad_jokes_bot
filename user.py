from base_model import BaseModel

class User(BaseModel):
    __CONTENT_TYPE__ = 'registeredUser'
    __SEARCH_FIELD__ = 'chatId'

    def __init__(self, chat_id):
        self.chat_id = chat_id

    def _search_field(self):
        return self.chat_id

    def _create_fields(self):
        return {
            'chatId': {'en-US': self.chat_id}
        }
