import time
import unittest
from infra.device_wrapper import deviceWrapper
from logic.event_page import EventPage
from logic.week_page import weekPage

class newEventTest(unittest.TestCase):
    def setUp(self):
        self.wrapper = deviceWrapper()
        self.driver = self.wrapper.get_driver()
        time.sleep(2)
        self.week_page = weekPage(self.driver)

    def test_today_datetime_in_event_pag(self):
        self.week_page.click_add_event_button()
        self.week_page.choose_add_event_day_element('Today')
        self.event_page = EventPage(self.driver)
        calender_date = self.event_page.get_date_field_text()
        self.assertEqual(calender_date,"Fri, 8 Mar 2024")



    def test_tommorow_date_in_event_page(self):
        self.week_page.click_add_event_button()
        self.week_page.choose_add_event_day_element('Tomorrow')
        self.event_page = EventPage(self.driver)
        calender_date = self.event_page.get_date_field_text()
        self.assertEqual(calender_date, "Sat, 9 Mar 2024")



def tearDown(self) -> None:
    if self.driver:
        self.driver.quit()