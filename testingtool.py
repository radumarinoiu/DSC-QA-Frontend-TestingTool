import json

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


# opts = Options()
# opts.headless = False
# browser = Firefox(options=opts)

if __name__ == '__main__':
    from TestingTool.testsuite import TestSuite
    from TestingTool.scenario import Scenario
    from TestingTool.task import Task
    from TestingTool.result import Result
