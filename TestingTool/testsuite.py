import json

from mongoengine import Document
from mongoengine import StringField, EmbeddedDocumentListField
from .scenario import Scenario
from .result import Result


class TestSuite(Document):
    pass  # I'm just a placeholder
