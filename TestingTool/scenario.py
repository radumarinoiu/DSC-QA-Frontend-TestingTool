import json

from mongoengine import EmbeddedDocument
from mongoengine import StringField, EmbeddedDocumentListField
from .task import Task


class Scenario(EmbeddedDocument):
    pass  # I'm just a placeholder
