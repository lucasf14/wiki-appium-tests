from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging


class Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = logging.getLogger(__name__)

        self.clickable_result_elements = (
            AppiumBy.XPATH,
            "//android.view.View[@clickable='true']",
        )

        self.all_result_elements = (
            AppiumBy.XPATH,
            "//android.view.View",
        )

    def click_button(self, button_locator: tuple, retries: int = 5) -> None:
        for i in range(retries):
            try:
                button = self.wait.until(EC.element_to_be_clickable(button_locator))
                self.logger.info(f"Clicked {button_locator} element after {i} tries")
                button.click()
                return
            except:
                self.logger.info("Button not found. Retrying")
        raise Exception(f"Failed to click button after {retries} attempts.")

    def fill_input(self, input_locator: tuple, text: str, retries: int = 5) -> None:
        for i in range(retries):
            try:
                input_element = self.wait.until(
                    EC.visibility_of_element_located(input_locator)
                )
                self.logger.info(f"Filled input with text after {i} tries: {text}")
                input_element.clear()
                input_element.send_keys(text)
                return
            except:
                self.logger.info("Field not found. Retrying")
        raise Exception(f"Failed to fill input field after {retries} attempts.")

    def find_inner_elements(
        self, parent_locator: tuple, child_locator: tuple, retries: int = 5
    ) -> list:
        for i in range(retries):
            try:
                parent_element = self.wait.until(
                    EC.visibility_of_element_located(parent_locator)
                )

                child_element = parent_element.find_elements(*child_locator)
                self.logger.info(
                    f"Found {len(child_element)} inner elements after {i} tries"
                )
                return child_element
            except:
                self.logger.info("Inner elements not found. Retrying")
        raise Exception(f"Failed to find inner elements {retries} attempts.")

    def get_elements(self, parent_locator: tuple, child_locator: tuple = None) -> list:
        if child_locator is not None:
            return self.find_inner_elements(parent_locator, child_locator)
        return self.driver.find_elements(*parent_locator)

    def scroll_and_find(self, element_locator: tuple, max_scrolls: int = 10):
        for i in range(max_scrolls):
            try:
                element = self.driver.find_element(*element_locator)
                self.logger.info(f"Element found after {i} tries")
                return element
            except:
                self.logger.info("Element not found. Scrolling down")
                self.driver.execute_script(
                    "mobile: scrollGesture",
                    {
                        "left": 100,
                        "top": 100,
                        "width": 1000,
                        "height": 1000,
                        "direction": "down",
                        "percent": 3.0,
                    },
                )
        raise Exception(f"Element not found after {max_scrolls} tries.")

    def scroll(self, direction: str = "down"):
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": 100,
                "top": 100,
                "width": 1000,
                "height": 1000,
                "direction": direction,
                "percent": 1.0,
            },
        )
