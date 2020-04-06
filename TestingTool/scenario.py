import json

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
        driver = webdriver.Firefox()
        driver.implicity_wait(5)
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
        response_result = Result(result, data)
        return response_result
