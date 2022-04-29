import time
import allure
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from utilities.common_ops import get_timestamp, get_data

driver = None
action = None
# eyes = Eyes()

@pytest.fixture(scope='class')
def init_desktop_driver(request):
    edriver = get_desktop_driver()
    globals()['driver']= edriver
    driver=globals()['driver']
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    request.cls.action = globals()['action']
    driver.implicitly_wait(int(get_data('WaitTime')))
    yield
    driver.quit()

def get_desktop_driver():
    dc = {}
    dc['app'] = get_data('Application_name')
    dc["platformName"] = "Windows"
    dc["deviceName"] = "WindowsPC"
    driver = webdriver.Remote(get_data('WinAppDriver_service'), dc)
    return driver

def pytest_exception_interact(node, call, report):
    image = "/desktopProject/allure-screen-shots/screen"+str(get_timestamp())+'.png'
    if globals()['driver']:
        globals()['driver'].get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)