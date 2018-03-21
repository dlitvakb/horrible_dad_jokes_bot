from .base_model import BaseModel


class Broadcast(BaseModel):
    __CONTENT_TYPE__ = 'broadcast'
    __SEARCH_FIELD__ = 'identifier'

    def __init__(self, identifier, content, joke_link=None):
        self.identifier = identifier
        self.content = content
        self.joke = joke_link

    def _search_field(self):
        return self.identifier

    def _create_fields(self):
        return {
            'identifier': {'en-US': self.identifier},
            'content': {'en-US': self.content},
            'joke': {'en-US': self.joke}
        }
