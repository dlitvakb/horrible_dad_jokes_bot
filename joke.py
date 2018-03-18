from base_model import BaseModel

class Joke(BaseModel):
    __CONTENT_TYPE__ = 'joke'
    __SEARCH_FIELD__ = 'title'

    def __init__(self, title, content, source, author, image = None):
        self.title = title
        self.content = content
        self.source = source
        self.author = author
        self.image = image

    def _search_field(self):
        return self.title

    def _create_fields(self):
        return {
            'title': {'en-US': self.title},
            'content': {'en-US': self.content},
            'author': {'en-US': self.author},
            'image': {'en-US': self.image},
            'source': {'en-US': self.source}
        }
