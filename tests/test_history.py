from pages.article_page import ArticlePage
from pages.explore_page import ExplorePage
from data.search_data import (
    SEARCH_WORDS,
)


def test_history(
    appium_driver,
) -> None:
    explore_page = ExplorePage(appium_driver)
    article_page = ArticlePage(appium_driver)

    # Assumption: Skip button appears when the app is launched (app fresh state handling)
    explore_page.click_button(explore_page.skip_button)
    explore_page.click_button(explore_page.search_container)

    # Iterate through search words, open articles, and finally return to search page to validate history
    for i, search_word in enumerate(SEARCH_WORDS):
        explore_page.fill_input(explore_page.search_input, search_word)

        search_results = explore_page.get_search_results(
            explore_page.search_results_container,
            explore_page.clickable_result_elements,
            explore_page.row_value,
        )

        explore_page.open_article(search_word.lower(), search_results)

        # Assumption: Close article only on first iteration (app fresh state handling)
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

    # Extract titles from history results and assert that each search word is present in the titles
    titles = [result["title"].lower() for result in history_results]
    for search_word in SEARCH_WORDS:
        assert search_word.lower() in titles
