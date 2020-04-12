import json
from webbrowser import get

from mongoengine import EmbeddedDocument
from mongoengine import StringField, EmbeddedDocumentListField
from .task import Task
from .result import Result
from selenium import webdriver


class Scenario(EmbeddedDocument):
    name = StringField(max_length=128, required=True)
    url = StringField(max_length=512, required=True)
    tasks = EmbeddedDocumentListField(Task)

    def run(self):
        with open('./config.json', 'r') as file:
            config_json_data = json.loads(file.read())
        driver_path = get(config_json_data)
        if driver_path is None:
            raise Exception("You didnt give me a selenium_driver_path")
        driver = webdriver.Firefox(driver_path)
        driver.maximize_window()
        data = []
        result = True
        for task in self.tasks:
            task.run(driver)
            result = task.result.result
            if result is False:
                data.append(task.result.data)
        if data:
            result = False
        response_result = Result(result=result, data=data)
        return response_result
