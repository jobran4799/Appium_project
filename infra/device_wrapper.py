import json
from appium import webdriver
from appium.options.android import UiAutomator2Options


try:
    with open('../tests/config.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
    raise  # Raise the error to halt execution if the file is essential for the script to run


class deviceWrapper():

    def __init__(self):

        appium_server_url = 'http://127.0.0.1:4723'

        # Converts capabilities to AppiumOptions instance
        capabilities_options = UiAutomator2Options().load_capabilities(data)
        self.driver = webdriver.Remote(
            command_executor=appium_server_url,
            options=capabilities_options
        )


    def get_driver(self):
        return self.driver