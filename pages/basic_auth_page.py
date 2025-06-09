from selenium.webdriver.common.by import By
from elements.input import Input
from elements.web_element import WebElement
from pages.base_page import BasePage


class BasicAuth(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, "content")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Basic_Auth_page"
        self.input = Input(self.browser.driver, self.UNIQUE_ELEMENT_LOC,
                           description="login and password page -> Result Lable")
        self.unique_element = WebElement(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description='Main Page -> Unique text')
