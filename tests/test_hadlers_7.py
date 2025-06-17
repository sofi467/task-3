from pages.hadelrs_page import HadlersPage


def test_handlers(browser, config_reader):
    url = config_reader.get_value("url_7")
    browser.get(url)
    handlers_page = HadlersPage(browser)
    handlers_page.wait_for_open()
    handlers_page.click_on_url()
    browser.switch_to_window(-1)
    window_1_text = handlers_page.get_text_window()
    window_1_title_text = browser.get_title_window()
    assert window_1_text == "New Window" == window_1_title_text
    browser.switch_to_window(0)
    handlers_page.wait_for_open()

    handlers_page.click_on_url()
    browser.switch_to_window(-2)
    window_2_text = handlers_page.get_text_window()
    window_2_title_text = browser.get_title_window()
    assert window_2_text == "New Window" == window_2_title_text
    browser.switch_to_window(0)
    handlers_page.wait_for_open()

    browser.switch_to_window(-2)
    browser.close()

    assert len(browser.driver.window_handles) == 2, f"Expected result:Window closed" \
                                                    f"Actual result: Window not closed"

    browser.switch_to_window(-1)
    browser.close()

    assert len(browser.driver.window_handles) == 1, f"Expected result:Window closed" \
                                                    f"Actual result: Window not closed"
