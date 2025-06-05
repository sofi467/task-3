import pytest

from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from config_reader import ConfigReader


@pytest.fixture(scope="session")
def config_reader():
    return ConfigReader()


@pytest.fixture
def browser():
    browser = Browser(BrowserFactory.get_browser())
    yield browser
    browser.quit()
