import json

from mongoengine import EmbeddedDocument
from mongoengine import StringField, EmbeddedDocumentListField
from .task import Task
from .result import Result
from .actions import ACTION_LIST


class Scenario(EmbeddedDocument):
    pass  # I'm just a placeholder
