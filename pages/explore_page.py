from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from pages.page import Page


class ExplorePage(Page):
    def __init__(self, driver):
        super().__init__(driver)

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

    def print_results(self):
        search_results = self.wait.until(
            EC.visibility_of_element_located(self.search_results)
        )

        result_elements = search_results.find_elements(*self.result_elements)

        for element in result_elements:
            print(f"TEXT: {element.text.strip()}")
