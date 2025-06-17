from enum import StrEnum

from selenium import webdriver


class BrowserType(StrEnum):
    CHROME = "chrome"


class BrowserFactory:
    @staticmethod
    def get_browser(browser_name: BrowserType = BrowserType.CHROME):
        if browser_name == BrowserType.CHROME:
            return webdriver.Chrome()
        else:
            raise NotImplemented(f"{browser_name} is not implemented")
