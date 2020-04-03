import json

from mongoengine import EmbeddedDocument
from mongoengine import StringField, DictField, BooleanField, EmbeddedDocumentField
from .result import Result
from .actions import ACTION_LIST


class Task(EmbeddedDocument):
    pass  # I'm just a placeholder
