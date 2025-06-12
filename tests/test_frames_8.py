from pages.frames_page import FramesPage
from pages.iframe_page import IframePage
from pages.nested_page import NestedPage


def test_frames(browser, config_reader):
    url = config_reader.get_value("url_8")
    browser.get(url)

    iframe_page = IframePage(browser)
    iframe_page.wait_for_open()
    iframe_page.click_on_nested()

    nested_page = NestedPage(browser)
    nested_page.wait_for_open()
    nested_page.wait_presence_of_parent()
    nested_page.switch_to_parent_iframe()
    assert "Parent frame" in browser.get_page_source()
    nested_page.wait_presence_of_child()
    nested_page.switch_to_child_iframe()
    assert "Child Iframe" in browser.get_page_source()
    browser.switch_to_default()
    nested_page.click_on_frames()

    frames_page = FramesPage(browser)
    frames_page.wait_for_open()
    frames_page.switch_to_big_iframe()
    big_text = frames_page.get_frames_text()
    browser.switch_to_default()
    frames_page.switch_to_small_iframe()
    small_text = frames_page.get_frames_text()
    browser.switch_to_default()
    assert big_text == small_text, f"Expected result:Texts inside the IFrames are equal: {big_text} == {small_text}" \
                                   f"Actual result: Texts inside the IFrames are not equal {big_text} != {small_text}"
