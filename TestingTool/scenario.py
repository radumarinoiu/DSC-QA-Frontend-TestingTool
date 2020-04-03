import json

from mongoengine import EmbeddedDocument
from mongoengine import StringField, EmbeddedDocumentListField
from .task import Task
from .result import Result


class Scenario(EmbeddedDocument):
    pass  # I'm just a placeholder
