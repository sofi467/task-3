import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from elements.slider_el import SliderElement
from pages.base_page import BasePage


class ActhionPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//input[@type = 'range']")
    SLIDER = (By.XPATH, "//input[@type = 'range']")
    RANGE_LOC = (By.ID, "range")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Acthion_page"
        self.slider = SliderElement(self.browser.driver, self.SLIDER, description='Slider')
        self.value_display = SliderElement(self.browser.driver, self.RANGE_LOC, description='Slider value')
        self.unique_element = SliderElement(self.browser.driver, self.UNIQUE_ELEMENT_LOC, description='Slider header')

    def move_slider(self, target_value, step):
        self.focus_on_slider()
        self.slider.move_slider(target_value, self.get_range_num(), step)

    def focus_on_slider(self):
        slider = self.slider.wait_for_presence()
        actions = self.browser.action_chains
        actions.move_to_element(slider).click().perform()

    def get_range_num(self):
        text_value = self.value_display.get_text()
        num_value = float(text_value)
        return num_value

    def get_slider_attributes(self):
        return {
            "min": float(self.slider.get_attribute("min")),
            "max": float(self.slider.get_attribute("max")),
            "step": float(self.slider.get_attribute("step")),
        }
