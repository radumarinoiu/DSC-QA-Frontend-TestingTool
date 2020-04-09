from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# trebuiau oare si import urile astea?


# def example_action(action_args, browser_instance):
#     some_arg = action_args.get("some_arg")
#     if some_arg is None:
#         return False, {"err": "Lipseste argumentul some_arg"}


def click_element(action_args, browser_instance):
    x_path_val = action_args.get("xpath")
    if x_path_val is None:
        return False, {"err": "You didnt give me an xpath in action_args"}
    else:
        wait = WebDriverWait(browser_instance, 2)
        element = wait.until(EC.presence_of_element_located(
            (By.XPATH, x_path_val)
        ))

        if len(element) > 0:
            element.click()
            return True, {"success": "clicked on xpath given in action_args"}

        return False, {"err": "element at given xpath didnt appear on the web page"}


ACTION_LIST = {
    # "example_action": example_action,
    "click_element": click_element
}
