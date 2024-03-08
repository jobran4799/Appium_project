from appium.webdriver.common.appiumby import AppiumBy


class EventPage():

    DATE_FIELD ="//android.widget.TextView[@resource-id='com.claudivan.taskagenda:id/btData']"

    def __init__(self,driver):
        self.driver=driver
        self.init_elements()

    def init_elements(self):

        self.date_field =self.driver.find_element(by=AppiumBy.XPATH, value=self.DATE_FIELD)

    def get_date_field_text(self):
        return self.date_field.text