import os
from loader import load_env
from contentful_management import Client as CMA
from contentful import Client as CDA


load_env()

class BaseModel(object):
    __CONTENT_TYPE__ = None
    __SEARCH_FIELD__ = None

    @classmethod
    def find(klass, field):
        cda = CDA(os.environ['CF_SPACE_ID'], os.environ['CF_CDA_TOKEN'])
        return cda.entries({
            'content_type': klass.__CONTENT_TYPE__,
            'fields.{0}'.format(klass.__SEARCH_FIELD__): field
        })[0]

    @classmethod
    def all(klass):
        cda = CDA(os.environ['CF_SPACE_ID'], os.environ['CF_CDA_TOKEN'])
        return cda.entries({'content_type': klass.__CONTENT_TYPE__})

    def save(self):
        cma = CMA(os.environ['CF_CMA_TOKEN'])
        entries_proxy = cma.entries(os.environ['CF_SPACE_ID'])

        entries = entries_proxy.all({
            'content_type': self.__class__.__CONTENT_TYPE__,
            'fields.{0}'.format(self.__class__.__SEARCH_FIELD__): self._search_field()
        })

        if entries:
            # We found a matching entry, therefore we don't do anything
            return False
        return entries_proxy.create(None,
            {
                'content_type_id': self.__class__.__CONTENT_TYPE__,
                'fields': self._create_fields()
            }
        ).publish()
