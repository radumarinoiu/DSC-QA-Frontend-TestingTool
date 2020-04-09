import json

from mongoengine import EmbeddedDocument
from mongoengine import Document
from mongoengine import StringField, EmbeddedDocumentListField
from .scenario import Scenario
from .result import Result


class TestSuite(Document):
    name = StringField(max_length=128, required=True)
    scenarios = EmbeddedDocumentListField(Scenario)

    def run(self):
        data = []
        result = True
        for scenario in self.scenarios:
            scenario.run()
            result = scenario.result.result
            if result is False:
                data.append(scenario.result.data)

        if data:
            result = False

        response_result = Result(result=result, data=data)
        return response_result
