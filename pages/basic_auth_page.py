from selenium.webdriver.common.by import By
from elements.input import Input
from elements.web_element import WebElement
from pages.base_page import BasePage


class BasicAuth(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, "content")
    RESULT_TEXT_LOC = (By.XPATH, "//*[@id='content']//p")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "basic_auth_page"
        self.input = Input(self.browser, self.UNIQUE_ELEMENT_LOC,
                           description="login and password page -> Result Lable")
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description='Main Page -> Unique text')
        self.rezult_text = WebElement(self.browser, self.RESULT_TEXT_LOC,
                                      description='Main Page -> Get rezult text')

    def get_rezult_text(self):
        return self.rezult_text.get_text()
