from pages.dynamic_page import DynamicPage


def test_dynamic(browser, config_reader):
    url = config_reader.get_value("url_9")
    browser.get(url)

    dynamic_page = DynamicPage(browser)
    dynamic_page.wait_for_open()
    dynamic_page.refresh_to_2_img()
    src_list = [dynamic_page.get_src_by_index(i) for i in range(1, 4)]
    assert any(src_list.count(src) > 1 for src in src_list), "2 img do not match"
