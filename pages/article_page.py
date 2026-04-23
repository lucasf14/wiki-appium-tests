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

        self.government = (
            AppiumBy.XPATH,
            "//android.view.View[@text='Government']",
        )

        self.back_button = (
            AppiumBy.ACCESSIBILITY_ID,
            "Navigate up",
        )

    def get_quick_facts(
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
                self.logger.info(
                    f"Added quick fact [{len(quick_facts)}]: {label}: {value}"
                )

        return quick_facts
