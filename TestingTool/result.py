import json

from mongoengine import EmbeddedDocument
from mongoengine import DictField, BooleanField


class Result(EmbeddedDocument):
     result = BooleanField(required = False)
     data = DictField()

