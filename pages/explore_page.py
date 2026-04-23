from appium.webdriver.common.appiumby import AppiumBy
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

        self.search_button = (
            AppiumBy.ID,
            "org.wikipedia:id/nav_tab_search",
        )

        self.search_results_container = (
            AppiumBy.ID,
            "org.wikipedia:id/fragment_search_results",
        )

        self.row_value = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text!='']",
        )

        self.history_container = (
            AppiumBy.ID,
            "org.wikipedia:id/history_list",
        )

        self.history_elements = (
            AppiumBy.ID,
            "org.wikipedia:id/page_list_item_container",
        )

    def get_search_results(
        self,
        parent_locator: tuple,
        child_locator: tuple = None,
        grandchild_locator: tuple = None,
    ) -> list:
        titles = set()
        search_results = []
        search_results_elements = self.get_elements(parent_locator, child_locator)

        for element in search_results_elements:
            row_elements = element.find_elements(*grandchild_locator)
            if len(row_elements) >= 1:
                title = row_elements[0].text.strip()
                description = (
                    row_elements[1].text.strip() if len(row_elements) > 1 else ""
                )
                payload = {
                    "title": title,
                    "description": description,
                    "element": row_elements[0],
                }
                if title not in titles:
                    search_results.append(payload)
                    titles.add(title)
                    self.logger.info(
                        f"Added search result [{len(search_results)}]: {payload}"
                    )

        return search_results
