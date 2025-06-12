from selenium.webdriver.common.by import By

from elements.web_element import WebElement
from pages.base_page import BasePage


class HadlersPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//h3[contains(text(), 'Opening')]")
    CLICK_URL_LOC = (By.XPATH, "//a[contains(text(), 'Click')]")
    TEXT_LOC = (By.XPATH, "//h3")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "handlers_page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description='Main Page -> Handlers header')
        self.click_link = WebElement(self.browser, self.CLICK_URL_LOC, description='Main Page -> Click on link')
        self.text_link = WebElement(self.browser, self.TEXT_LOC, description='Main Page -> Get text')

    def click_on_url(self):
        self.click_link.click()

    def get_text_window(self):
        return self.text_link.get_text()
