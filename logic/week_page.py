import time
from appium.webdriver.common.appiumby import AppiumBy

class weekPage():
    ADD_EVENT= "com.claudivan.taskagenda:id/btNovoEvento"

    def __init__(self,driver):
        self.driver=driver
        self.init_elements()

    def init_elements(self):
        time.sleep(1)
        self.add_event_button = self.driver.find_element(by=AppiumBy.ID, value=self.ADD_EVENT)


    def click_add_event_button(self):
        self.add_event_button.click()

    def choose_add_event_day_element(self,text):
        time.sleep(1)
        self.driver.find_element(by=AppiumBy.XPATH, value=f"//android.widget.TextView[@resource-id='android:id/text1' and @text='{text}']").click()


