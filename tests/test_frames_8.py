from pages.frames_page import FramesPage
from pages.iframe_page import IframePage
from pages.nested_page import NestedPage


def test_frames(browser, config_reader):
    url = config_reader.get_value("url_8")
    browser.get(url)

    iframe_page = IframePage(browser)
    iframe_page.wait_for_open()
    # iframe_page.click_on_section()
    iframe_page.click_on_nested()

    nested_page = NestedPage(browser)
    nested_page.wait_for_open()
    nested_page.presence_of_parent()
    browser.switch_to_iframe(nested_page.parent)
    assert "Parent frame" in browser.page_source()
    nested_page.presence_of_child()
    browser.switch_to_iframe(nested_page.child)
    assert "Child Iframe" in browser.page_source()
    browser.switch_to_default()
    nested_page.click_on_frames()

    frames_page = FramesPage(browser)
    frames_page.wait_for_open()
    browser.switch_to_iframe(frames_page.big_iframe)
    big_text = frames_page.get_frames_text()
    browser.switch_to_default()
    browser.switch_to_iframe(frames_page.small_iframe)
    small_text = frames_page.get_frames_text()
    browser.switch_to_default()
    assert big_text == small_text, f"Texts inside the IFrames are equal: {big_text} == {small_text}"

