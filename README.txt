Appium Test Automation Project
    Overview
    This project contains Python scripts for automating tests on a mobile application using Appium. The tests are designed to run on an Android emulator and interact with the specified application.

Classes
    weekPage Class
    Description: Represents the Week Page of the mobile application.
File: week_page.py
    Dependencies: Requires time and appium.webdriver.common.appiumby.AppiumBy modules.
Methods:
    __init__(driver): Initializes an instance of the Week Page class.
    init_elements(): Initializes elements on the page.
    click_add_event_button(): Clicks the "Add Event" button on the page.
    choose_add_event_day_element(text): Chooses the specified day element to add an event.
newEventTest Class
    Description: Contains test cases for adding new events to the mobile application.
File: new_event_test.py
    Dependencies: Requires time, unittest, infra.device_wrapper.deviceWrapper, logic.event_page.EventPage, and logic.week_page.weekPage modules.
    Methods:
    setUp(): Sets up the test environment before each test case.
    tearDown(): Cleans up the test environment after each test case.
    test_today_datetime_in_event_pag(): Tests adding an event for today's date and verifies the date in the Event Page.
    test_tommorow_date_in_event_page(): Tests adding an event for tomorrow's date and verifies the date in the Event Page.
Installation and Usage
    Set up Appium server and Android emulator.
    Clone the repository.
    Run the test scripts using Python.