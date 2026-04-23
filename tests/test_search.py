from pages.article_page import ArticlePage
from pages.explore_page import ExplorePage
from data.search_data import (
    NO_RESULTS,
    SEARCH_WORD_INVALID,
    SEARCH_WORD_VALID,
    AZORES_QUICK_FACTS,
)


def test_unsuccessful_article_search(appium_driver) -> None:
    explore_page = ExplorePage(appium_driver)

    explore_page.click_button(explore_page.skip_button)
    explore_page.click_button(explore_page.search_container)
    explore_page.fill_input(explore_page.search_input, SEARCH_WORD_INVALID)

    search_results = explore_page.get_search_results(
        explore_page.search_results_container,
        explore_page.all_result_elements,
        explore_page.row_value,
    )

    assert len(search_results) == 1
    assert any(
        NO_RESULTS.lower() in result["title"].lower() for result in search_results
    )


def test_successful_article_search(appium_driver) -> None:
    explore_page = ExplorePage(appium_driver)
    article_page = ArticlePage(appium_driver)

    explore_page.click_button(explore_page.skip_button)
    explore_page.click_button(explore_page.search_container)
    explore_page.fill_input(explore_page.search_input, SEARCH_WORD_VALID)

    search_results = explore_page.get_search_results(
        explore_page.search_results_container,
        explore_page.clickable_result_elements,
        explore_page.row_value,
    )

    assert len(search_results) >= 1
    assert any(
        SEARCH_WORD_VALID.lower() in result["title"].lower()
        for result in search_results
    )

    for result in search_results:
        if SEARCH_WORD_VALID.lower() == result["title"].lower():
            explore_page.click_button(result["element"])
            break

    article_page.click_button(article_page.close_button)
    article_page.click_button(article_page.expand_table_button)

    quick_facts = article_page.get_quick_facts(
        article_page.close_qf_button,
    )

    for label, value in AZORES_QUICK_FACTS.items():
        assert quick_facts[label.lower()] == value.lower()
