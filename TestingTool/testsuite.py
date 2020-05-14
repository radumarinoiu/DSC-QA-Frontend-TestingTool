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
        scenarios_folder = self.scenarios_folder
        if scenarios_folder:
            self.from_folder(directory=scenarios_folder)
        for scenario in self.scenarios:
            result = scenario.run()
            if result.result:
                print("Scenario {} completed successfully!".format(scenario.name))
            else:
                print("Scenario {} failed, reason:\n{}".format(scenario.name, json.dumps(result.data, indent=2)))

    def from_folder(self, directory):
        file_names = os.listdir(directory)

        for file_name in file_names:
            file_path = os.path.join(directory, file_name)
            with open(file_path, "r") as file:
                scenario = Scenario.from_json(file.read())
                self.scenarios.append(scenario)
