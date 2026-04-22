from pages.explore_page import ExplorePage
from data.search_data import NO_RESULTS, SEARCH_WORD_INVALID, SEARCH_WORD_VALID


def test_unsuccessful_search(appium_driver) -> None:
    explore_page = ExplorePage(appium_driver)

    explore_page.click_button(explore_page.skip_button)

    explore_page.click_button(explore_page.search_container)

    explore_page.fill_input(explore_page.search_input, SEARCH_WORD_INVALID)

    search_results = explore_page.get_search_results(
        explore_page.search_results, explore_page.result_elements
    )

    assert len(search_results) == 1
    assert any(
        NO_RESULTS.lower() in result["title"].lower() for result in search_results
    )


def test_successful_search(appium_driver) -> None:
    explore_page = ExplorePage(appium_driver)

    explore_page.click_button(explore_page.skip_button)

    explore_page.click_button(explore_page.search_container)

    explore_page.fill_input(explore_page.search_input, SEARCH_WORD_VALID)

    search_results = explore_page.get_search_results(
        explore_page.search_results, explore_page.result_elements
    )

    assert len(search_results) >= 1
    assert any(
        SEARCH_WORD_VALID.lower() in result["title"].lower()
        for result in search_results
    )
