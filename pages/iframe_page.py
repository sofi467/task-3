from selenium.webdriver.common.by import By

from elements.web_element import WebElement
from pages.base_page import BasePage


# главная страница
class IframePage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//h1[contains(@class, 'text-center')]")
    ALERT_FRAME_LOC = (By.XPATH, "//*[contains(text(), 'Alerts, Frame')]")
    NESTER_LOC = (By.XPATH, "//*[contains(text(), 'Nested')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "iframe_page"
        self.unique_element = WebElement(self.browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description='Main Page -> Frames header')
        self.click_frame = WebElement(self.browser.driver, self.ALERT_FRAME_LOC,
                                      description='Main Page -> Click on frame,alert,window')
        self.click_nester = WebElement(self.browser.driver, self.NESTER_LOC,
                                       description='Main Page -> Click on nester')

    def click_on_section(self):
        self.click_frame.click()

    def click_on_nested(self):
        self.click_nester.click()
