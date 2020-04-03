import json

from mongoengine import EmbeddedDocument
from mongoengine import StringField, DictField, BooleanField, EmbeddedDocumentField
from .task_result import TaskResult


class Task(EmbeddedDocument):
    pass  # I'm just a placeholder
