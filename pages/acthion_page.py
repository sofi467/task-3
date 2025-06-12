from selenium.webdriver.common.by import By

from elements.slider_element import SliderElement
from pages.base_page import BasePage


class ActionPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//input[@type = 'range']")
    SLIDER_LOC = (By.XPATH, "//input[@type = 'range']")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "action_page"
        self.slider = SliderElement(self.browser, self.SLIDER_LOC, description='Slider')
        self.unique_element = SliderElement(self.browser, self.UNIQUE_ELEMENT_LOC, description='Slider header')

    def move_slider(self, target_value):
        self.focus_on_slider()
        step = self.slider.get_step()
        self.slider.move_slider(target_value, step)

    def focus_on_slider(self):
        slider_element = self.slider.wait_for_presence()
        actions = self.browser.action_chains
        actions.move_to_element(slider_element).click().perform()

    def get_range_num(self):
        return self.slider.get_current_value()

    def get_slider_attributes(self):
        return self.slider.get_attributes()
