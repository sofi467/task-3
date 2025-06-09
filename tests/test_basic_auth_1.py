from pages.basic_auth_page import BasicAuth
import pytest


@pytest.mark.parametrize("param", [("admin", "admin")])
def test_basic_auth(browser, config_reader, param):
    username, password = param
    url_template = config_reader.get_value("url_1")
    url = url_template.format(username, password)
    browser.get(url)
    basic = BasicAuth(browser)
    basic.wait_for_open()
    assert True
