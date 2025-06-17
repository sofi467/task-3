from selenium.webdriver.common.by import By

from elements.iframe import IFrame
from elements.web_element import WebElement
from pages.base_page import BasePage


class NestedPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//h1[contains(@class, 'text-center')]")
    CHILD_LOC = (By.XPATH, "//iframe[contains(@srcdoc, 'Child Iframe')]")
    PARENT_LOC = (By.ID, "frame1")
    FRAMES_CLICK_LOC = (By.XPATH, "//*[@id='item-2' and contains(.//span, 'Frames')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "nested_page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description='Main Page -> Nested header')
        self.child = IFrame(self.browser, self.CHILD_LOC,
                            description='Main Page -> Child element')
        self.parent = IFrame(self.browser, self.PARENT_LOC, description='Main Page -> Parent Element')
        self.frames = WebElement(self.browser, self.FRAMES_CLICK_LOC, description='Main Page -> Frames switch')

    def wait_presence_of_child(self):
        self.child.wait_for_presence()

    def wait_presence_of_parent(self):
        self.parent.wait_for_presence()

    def click_on_frames(self):
        self.frames.js_click()

    def switch_to_parent_iframe(self):
        self.browser.switch_to_iframe(self.parent)

    def switch_to_child_iframe(self):
        self.browser.switch_to_iframe(self.child)
