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
        button.click()

    def fill_input(self, input_locator: tuple, text: str):
        input_element = self.wait.until(EC.visibility_of_element_located(input_locator))
        input_element.send_keys(text)

    def find_inner_elements(self, parent_locator: tuple, child_locator: tuple) -> None:
        parent_element = self.wait.until(
            EC.visibility_of_element_located(parent_locator)
        )

        child_element = parent_element.find_elements(*child_locator)
        return child_element
