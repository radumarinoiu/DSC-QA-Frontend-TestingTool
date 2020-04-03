import json

from mongoengine import EmbeddedDocument
from mongoengine import StringField, DictField, BooleanField, EmbeddedDocumentField
from .result import Result


class Task(EmbeddedDocument):
    pass  # I'm just a placeholder
