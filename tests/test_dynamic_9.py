from pages.dynamic_page import DynamicPage


def test_dynamic(browser, config_reader):
    url = config_reader.get_value("url_9")
    browser.get(url)

    dynamic_page = DynamicPage(browser)
    dynamic_page.wait_for_open()
    dynamic_page.refresh_to_2_img()
    assert dynamic_page.is_2_img_corrected(), "2 img do not match"
