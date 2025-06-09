import pytest

from pages.infinite_scroll import InfiniteScrollPage


@pytest.mark.parametrize("age", [25])
def test_infinite_scroll(browser, config_reader, age):
    url = config_reader.get_value("url_10")
    browser.get(url)

    scroll = InfiniteScrollPage(browser)
    scroll.wait_for_open()

    count_paragraphs = scroll.scroll_to_paragraph(age)
    assert count_paragraphs == age,f"{count_paragraphs} The number of paragraphs does not match the age"
