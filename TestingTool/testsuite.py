import json
import os

from mongoengine import Document
from mongoengine import StringField, EmbeddedDocumentListField
from .scenario import Scenario


class TestSuite(Document):
    name = StringField(max_length=128, required=True)
    scenarios = EmbeddedDocumentListField(Scenario)
    scenarios_folder = StringField(required=False)

    def run(self):
        if self.scenarios_folder:
            self.scenarios = self.from_folder(directory=self.scenarios_folder)
        for scenario in self.scenarios:
            result = scenario.run()
            if result.result:
                print("Scenario {} completed successfully!".format(scenario.name))
            else:
                print("Scenario {} failed, reason:\n{}".format(scenario.name, json.dumps(result.data, indent=2)))

    @staticmethod
    def from_folder(directory):
        file_names = os.listdir(directory)
        scenarios = []
        
        for file_name in file_names:
            file_path = os.path.join(directory, file_name)
            with open(file_path, "r") as file:
                scenario = Scenario.from_json(file.read())
                scenarios.append(scenario)
        return scenarios
