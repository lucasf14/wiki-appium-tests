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

    def get_search_results(
        self, parent_locator: tuple, child_locator: tuple = None
    ) -> list:
        search_results = []
        result_elements = self.get_elements(parent_locator, child_locator)

        for i in range(0, len(result_elements), 2):
            payload = {
                "title": result_elements[i].text.strip(),
                "description": (
                    result_elements[i + 1].text.strip()
                    if len(result_elements) > 1
                    else ""
                ),
                "element": result_elements[i],
            }
            search_results.append(payload)
            self.logger.info(f"Added search result [{len(search_results)}]: {payload}")
        return search_results
