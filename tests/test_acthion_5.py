from utils.random_utils import RandomUtils

from pages.acthion_page import ActhionPage


def test_alert(browser, config_reader):
    url = config_reader.get_value("url_5")
    browser.get(url)

    slider_page = ActhionPage(browser)
    attributes = slider_page.get_slider_attributes()
    target_value = RandomUtils.get_random_num(attributes["min"], attributes["max"], attributes["step"])
    slider_page.wait_for_open()
    slider_page.move_slider(target_value, attributes["step"])
    assert target_value == slider_page.get_range_num()
