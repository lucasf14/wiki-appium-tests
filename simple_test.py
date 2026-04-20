from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_wiki_search(appium_driver) -> None:
    wait = WebDriverWait(appium_driver, 10)

    skip_button = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_skip_button")
        )
    )
    skip_button.click()

    search_container = wait.until(
        EC.element_to_be_clickable((AppiumBy.ID, "org.wikipedia:id/search_container"))
    )
    search_container.click()

    search_input = wait.until(
        EC.visibility_of_element_located(
            (AppiumBy.ID, "org.wikipedia:id/search_src_text")
        )
    )
    search_input.send_keys("Lucas")

    search_results = wait.until(
        EC.visibility_of_element_located(
            (AppiumBy.ID, "org.wikipedia:id/fragment_search_results")
        )
    )

    result_elements = search_results.find_elements(
        AppiumBy.CLASS_NAME, "android.widget.TextView"
    )

    for element in result_elements:
        print(f"TEXT: {element.text.strip()}")
