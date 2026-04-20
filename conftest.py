import pytest
from time import sleep
from appium import webdriver
from appium.options.android import UiAutomator2Options

"""
def setUp(self) -> None:
    appium_server_url = "http://localhost:4723"
    capabilities = dict(
        platformName="Android",
        automationName="uiautomator2",
        deviceName="Android",
        appPackage="org.wikipedia",
        appActivity=".main.MainActivity",
        language="en",
        locale="US",
    )

    self.driver = webdriver.Remote(
        appium_server_url,
        options=UiAutomator2Options().load_capabilities(capabilities),
    )
    self.wait = WebDriverWait(self.driver, 10)


def tearDown(self) -> None:
    if self.driver:
        self.driver.quit()
"""


@pytest.fixture
def appium_driver():
    appium_server_url = "http://localhost:4723"
    capabilities = dict(
        platformName="Android",
        automationName="uiautomator2",
        deviceName="Android",
        appPackage="org.wikipedia",
        appActivity=".main.MainActivity",
        language="en",
        locale="US",
    )

    driver = webdriver.Remote(
        appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities)
    )

    yield driver
    sleep(2)
    driver.quit()
