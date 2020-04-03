import json

from mongoengine import Document
from mongoengine import StringField, EmbeddedDocumentListField
from .scenario import Scenario


class TestSuite(Document):
    pass  # I'm just a placeholder
