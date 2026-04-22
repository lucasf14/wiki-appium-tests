from pages.explore_page import ExplorePage


def test_unsuccessful_wiki_search(appium_driver) -> None:
    explore_page = ExplorePage(appium_driver)

    explore_page.click_button(explore_page.skip_button)

    explore_page.click_button(explore_page.search_container)

    explore_page.fill_input(explore_page.search_input, "Invalid123")

    results = explore_page.find_inner_elements(
        explore_page.search_results, explore_page.result_elements
    )

    # assert len(results) == 1
    # assert "No results" in results[0].text.strip()
    for result in results:
        print(f"RESULT: {result.text.strip()}")
