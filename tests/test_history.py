from pages.article_page import ArticlePage
from pages.explore_page import ExplorePage
from data.search_data import (
    SEARCH_WORDS,
)


def test_history(appium_driver) -> None:
    explore_page = ExplorePage(appium_driver)
    article_page = ArticlePage(appium_driver)

    explore_page.click_button(explore_page.skip_button)
    explore_page.click_button(explore_page.search_container)
    for i, search_word in enumerate(SEARCH_WORDS):
        explore_page.fill_input(explore_page.search_input, search_word)

        search_results = explore_page.get_search_results(
            explore_page.search_results_container,
            explore_page.clickable_result_elements,
            explore_page.row_value,
        )

        for result in search_results:
            if search_word.lower() == result["title"].lower():
                explore_page.click_button(result["element"])
                break

        if i == 0:
            article_page.click_button(article_page.close_button)
        article_page.click_button(article_page.back_button)
    article_page.click_button(article_page.back_button)
    explore_page.click_button(explore_page.search_button)

    history_results = explore_page.get_search_results(
        explore_page.history_container,
        explore_page.history_elements,
        explore_page.row_value,
    )

    titles = [result["title"].lower() for result in history_results]
    for search_word in SEARCH_WORDS:
        assert search_word.lower() in titles
