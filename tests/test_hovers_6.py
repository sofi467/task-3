from pages.hovers import HoversPage

INDEX = 3


def test_hovers(browser, config_reader):
    url = config_reader.get_value("url_6")
    browser.get(url)
    hovers = HoversPage(browser)
    hovers.wait_for_open()
    for i in range(1, INDEX + 1):
        hovers.move_to_image(i)
        expected = f'user{i}'
        assert expected in hovers.get_text_image(i), f"{expected} Incorrect username is displayed"
        hovers.click_on_link(i)
        img_url = browser.get_current_url().split("/")[-1].strip()
        assert img_url == str(i), f"The link was not opened for that user {i}"
        browser.back()
        hovers.wait_for_open()
