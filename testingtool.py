import json


if __name__ == '__main__':
    from TestingTool.testsuite import TestSuite
    from TestingTool.scenario import Scenario
    from TestingTool.task import Task

    task1 = Task(
        name="Go to Google",
        action="go_to_page",
        args={"url": "https://google.com"}
    )

    task2 = Task(
        name="Click GMail",
        action="click_element",
        args={"xpath": "/html/body/div/div[2]/div/div/div/div[1]/div[1]/a"}
    )

    scenario1 = Scenario(name="Google Test", url="https://google.com", tasks=[task1, task2])

    with open("TestingTool/tests/scenario_google.json", "r") as f:
        scenario2 = Scenario.from_json(f.read())
    test_suite = TestSuite(name="Default Test Suite", scenarios=[scenario1])
    test_suite.run()
    print("Done")
