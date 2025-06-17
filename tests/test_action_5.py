from utils.random_utils import RandomUtils

from pages.acthion_page import ActionPage


def test_alert(browser, config_reader):
    url = config_reader.get_value("url_5")
    browser.get(url)

    slider_page = ActionPage(browser)
    slider_page.wait_for_open()

    attributes = slider_page.get_slider_attributes()
    target_value = RandomUtils.get_random_num(attributes["min"], attributes["max"], attributes["step"])

    slider_page.move_slider(target_value)

    actual_value = slider_page.get_range_num()
    assert target_value == actual_value, \
        f"Expected result: Incorrect value is displayed {target_value}. " \
        f"Actual result: The displayed number is {actual_value}"
