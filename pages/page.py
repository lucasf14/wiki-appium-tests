from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.webdriver import WebDriver
import logging


class Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = logging.getLogger(__name__)

    def click_button(self, button_locator: tuple):
        button = self.wait.until(EC.element_to_be_clickable(button_locator))
        self.logger.info(f"Clicked {button_locator} element")
        button.click()

    def fill_input(self, input_locator: tuple, text: str):
        input_element = self.wait.until(EC.visibility_of_element_located(input_locator))
        self.logger.info(f"Filled input with text: {text}")
        input_element.send_keys(text)

    def find_inner_elements(self, parent_locator: tuple, child_locator: tuple) -> list:
        parent_element = self.wait.until(
            EC.visibility_of_element_located(parent_locator)
        )

        child_element = parent_element.find_elements(*child_locator)
        self.logger.info(f"Found {len(child_element)} inner elements")
        return child_element

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
