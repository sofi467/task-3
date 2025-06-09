from selenium.webdriver.common.by import By

from elements.iframe import IFrame
from elements.web_element import WebElement
from pages.base_page import BasePage


class FramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(@class, 'text-center')]")
    BIG_IFRAME_LOC = (By.ID, 'frame1')
    SMALL_IFRAME_LOC = (By.ID, 'frame2')
    FRAMES_TEXT_LOC = (By.ID, 'sampleHeading')

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "frames_page"
        self.unique_element = WebElement(self.browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description='Main Page -> Frames header')
        self.text_frame = WebElement(browser.driver, self.FRAMES_TEXT_LOC, description='Text inside of IFrame')
        self.big_iframe = IFrame(browser.driver, self.BIG_IFRAME_LOC, description='Big IFrame')
        self.small_iframe = IFrame(browser.driver, self.SMALL_IFRAME_LOC, description='Small IFrame')

    def get_frames_text(self):
        return self.text_frame.get_text()
