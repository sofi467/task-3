from selenium.webdriver.common.by import By

from elements.web_element import WebElement
from pages.base_page import BasePage


class ContextClick(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, "hot-spot")

    def __init__(self, browser):
        super().__init__(browser)
        self.context_menu = WebElement(self.browser.driver, self.UNIQUE_ELEMENT_LOC,
                                       description='Main Page -> click on the selected area')
        self.page_name = "context_menu_page"
        self.unique_element = WebElement(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description='Main Page -> Unique text')

    def context_click(self):
        self.context_menu.context_click()
