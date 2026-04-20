import pytest
from time import sleep
from appium import webdriver
from appium.options.android import UiAutomator2Options


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
