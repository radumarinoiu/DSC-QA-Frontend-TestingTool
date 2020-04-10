from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# def example_action(action_args, browser_instance):
#     some_arg = action_args.get("some_arg")
#     if some_arg is None:
#         return False, {"err": "Lipseste argumentul some_arg"}


def element_from_xpath(action_args, browser_instance):
    x_path_val = action_args.get("xpath")
    if x_path_val is None:
        return False, {"err": "You didnt give me an xpath in action_args"}
    wait = WebDriverWait(browser_instance, 2)
    try:
        element = wait.until(EC.presence_of_element_located(
            (By.XPATH, x_path_val)
        ))
    except TimeoutException:
        return False, {"err": "Timeout exception when looking for element at given xpath"}
    return True, element


def click_element(action_args, browser_instance):
    result, data = element_from_xpath(action_args, browser_instance)
    if result is False:
        return result, data
    data.click()
    return True, {"success": "Clicked on xpath given in action_args"}


def input_element(action_args, browser_instance):
    result, data = element_from_xpath(action_args, browser_instance)
    input_text = action_args.get("input_text")
    if result is False:
        return result, data
    if input_text is None:
        return False, {"err": {"You didnt give me an input text in action_args"}}
    data.sendKeys(input_text)
    return True, {"success": "Element from xpath took the received value"}


ACTION_LIST = {
    # "example_action": example_action,
    # element_from_xpath does not meet the standard to be here
    "click_element": click_element,
    "input_element": input_element
}
