from pages.context_click_page import ContextClick


def test_alert(browser, config_reader):
    url = config_reader.get_value("url_4")
    browser.get(url)

    context_menu_page = ContextClick(browser)
    context_menu_page.wait_for_open()
    context_menu_page.context_click()
    assert browser.get_alert_text() == "You selected a context menu"
    browser.close_alert()
