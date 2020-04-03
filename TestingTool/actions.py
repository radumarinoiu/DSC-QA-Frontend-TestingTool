
def example_action(action_args, browser_instance):
    some_arg = action_args.get("some_arg")
    if some_arg is None:
        return False, {"err": "Lipseste argumentul some_arg"}


ACTION_LIST = {
    "example_action": example_action
}
