import json

from mongoengine import Document, EmbeddedDocument
from mongoengine import StringField, DictField, BooleanField, EmbeddedDocumentField, EmbeddedDocumentListField


class EmbeddedDocumentExample(EmbeddedDocument):
    string_example = StringField(max_length=128, required=True)
    dict_example = DictField()
    bool_example = BooleanField()


class DocumentExample(Document):
    string_example = StringField(max_length=128, required=True)
    dict_example = DictField()
    bool_example = BooleanField()

    # This will contain a EmbeddedDocumentExample
    embedded_document_example = EmbeddedDocumentField(EmbeddedDocumentExample)

    # This will contain a list of EmbeddedDocumentExample
    embedded_document_list_example = EmbeddedDocumentListField(EmbeddedDocumentExample)