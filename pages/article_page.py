from appium.webdriver.common.appiumby import AppiumBy
from pages.page import Page


class ArticlePage(Page):
    def __init__(self, driver):
        super().__init__(driver)

        self.close_button = (
            AppiumBy.ID,
            "org.wikipedia:id/closeButton",
        )
        self.expand_table_button = (
            AppiumBy.XPATH,
            "//android.view.View[@text='Quick facts']",
        )

        self.quick_facts_container = (
            AppiumBy.XPATH,
            "//android.widget.GridView",
        )

        self.quick_facts_elements = (
            AppiumBy.XPATH,
            "//android.view.View",
        )

        self.row_value = (
            AppiumBy.XPATH,
            "//android.view.View[@text!='']",
        )

        self.close_qf_button = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Close']",
        )

        self.back_button = (
            AppiumBy.ACCESSIBILITY_ID,
            "Navigate up",
        )

    def get_quick_facts(
        self,
        target_locator: tuple,
        max_scrolls: int = 10,
    ) -> dict:
        labels = set()
        quick_facts = {}

        for _ in range(max_scrolls):
            parsed_quick_facts = self.parse_quick_facts(
                self.quick_facts_container,
                self.quick_facts_elements,
                self.row_value,
            )

            for label, value in parsed_quick_facts.items():
                # Only add new quick facts to the dictionary to avoid duplicates
                if label not in labels:
                    quick_facts[label] = value
                    labels.add(label)
                    self.logger.info(
                        f"Added quick fact [{len(quick_facts)}]: {label}: {value}"
                    )

            self.scroll("down")

            if self.driver.find_elements(*target_locator):
                self.logger.info("Target element found. Stopping scroll")
                break

            self.logger.info("Target element not found yet. Scrolling")
        return quick_facts

    def parse_quick_facts(
        self,
        parent_locator: tuple,
        child_locator: tuple = None,
        grandchild_locator: tuple = None,
    ) -> list:
        quick_facts = {}
        quick_facts_elements = self.get_elements(parent_locator, child_locator)

        for element in quick_facts_elements:
            row_elements = element.find_elements(*grandchild_locator)
            if len(row_elements) > 1:
                label = row_elements[0].text.strip().lower()
                value = row_elements[1].text.strip().lower()
                quick_facts[label] = value
                self.logger.info(f"Parsed quick fact: {label}: {value}")

        return quick_facts
