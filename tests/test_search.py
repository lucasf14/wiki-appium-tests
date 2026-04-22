from pages.explore_page import ExplorePage


def test_search(appium_driver) -> None:
    main_page = ExplorePage(appium_driver)

    main_page.click_button(main_page.skip_button)

    main_page.click_button(main_page.search_container)

    main_page.fill_input(main_page.search_input, "Lucas")

    main_page.print_results()
