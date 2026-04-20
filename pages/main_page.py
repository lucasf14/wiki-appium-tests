from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.skip_button = (
            AppiumBy.ID,
            "org.wikipedia:id/fragment_onboarding_skip_button",
        )
        self.search_container = (
            AppiumBy.ID,
            "org.wikipedia:id/search_container",
        )

        self.search_input = (
            AppiumBy.ID,
            "org.wikipedia:id/search_src_text",
        )

        self.search_results = (
            AppiumBy.ID,
            "org.wikipedia:id/fragment_search_results",
        )

        self.result_elements = (
            AppiumBy.CLASS_NAME,
            "android.widget.TextView",
        )

    def click_button(self, button_locator):
        button = self.wait.until(EC.element_to_be_clickable(button_locator))
        button.click()

    def fill_input(self, input_locator, text):
        input_element = self.wait.until(EC.visibility_of_element_located(input_locator))
        input_element.send_keys(text)

    def print_results(self):
        search_results = self.wait.until(
            EC.visibility_of_element_located(self.search_results)
        )

        result_elements = search_results.find_elements(*self.result_elements)

        for element in result_elements:
            print(f"TEXT: {element.text.strip()}")
