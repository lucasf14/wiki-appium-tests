from pages.main_page import MainPage


def test_wiki_search(appium_driver) -> None:
    main_page = MainPage(appium_driver)

    main_page.click_button(main_page.skip_button)

    main_page.click_button(main_page.search_container)

    main_page.fill_input(main_page.search_input, "Lucas")

    main_page.print_results()
