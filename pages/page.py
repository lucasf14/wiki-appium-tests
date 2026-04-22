from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_button(self, button_locator):
        button = self.wait.until(EC.element_to_be_clickable(button_locator))
        button.click()

    def fill_input(self, input_locator, text):
        input_element = self.wait.until(EC.visibility_of_element_located(input_locator))
        input_element.send_keys(text)
