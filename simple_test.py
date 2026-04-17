import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = dict(
    platformName="Android",
    automationName="uiautomator2",
    deviceName="Android",
    appPackage="org.wikipedia",
    appActivity=".main.MainActivity",
    language="en",
    locale="US",
)

appium_server_url = "http://localhost:4723"


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            appium_server_url,
            options=UiAutomator2Options().load_capabilities(capabilities),
        )
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_wiki_search(self) -> None:
        skip_button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_skip_button")
            )
        )
        skip_button.click()

        search_container = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "org.wikipedia:id/search_container")
            )
        )
        search_container.click()

        search_input = self.wait.until(
            EC.visibility_of_element_located(
                (AppiumBy.ID, "org.wikipedia:id/search_src_text")
            )
        )
        search_input.send_keys("Lucas")

        search_results = self.wait.until(
            EC.visibility_of_element_located(
                (AppiumBy.ID, "org.wikipedia:id/fragment_search_results")
            )
        )

        result_elements = search_results.find_elements(
            AppiumBy.CLASS_NAME, "android.widget.TextView"
        )

        for element in result_elements:
            print(f"TEXT: {element.text.strip()}")


if __name__ == "__main__":
    unittest.main()
