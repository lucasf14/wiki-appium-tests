from appium.webdriver.common.appiumby import AppiumBy
from pages.page import Page


class ArticlePage(Page):
    def __init__(self, driver):
        super().__init__(driver)

        self.close_button = (
            AppiumBy.ID,
            "org.wikipedia:id/closeButton",
        )
        self.expand_table = (
            AppiumBy.XPATH,
            "//android.widget.TextView[@text='Quick facts']",
        )

        self.table = (
            AppiumBy.XPATH,
            "//android.widget.GridView",
        )

        self.row = (
            AppiumBy.XPATH,
            "//android.view.View",
        )

        self.label_value = (
            AppiumBy.XPATH,
            "//android.view.View[@text!='']",
        )

        self.government = (
            AppiumBy.XPATH,
            "//android.view.View[@text='Government']",
        )

    def get_quick_facts(
        self,
        table_locator: tuple,
        row_locator: tuple = None,
        fact_locator: tuple = None,
    ) -> list:
        quick_facts = {}
        quick_facts_elements = self.get_elements(table_locator, row_locator)

        for element in quick_facts_elements:
            fact_elements = element.find_elements(*fact_locator)
            if len(fact_elements) > 1:
                label = fact_elements[0].text.strip().lower()
                value = fact_elements[1].text.strip().lower()
                quick_facts[label] = value
                self.logger.info(
                    f"Added quick fact [{len(quick_facts)}]: {label}: {value}"
                )

        return quick_facts
