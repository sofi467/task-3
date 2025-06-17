from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from elements.input import Input
from elements.web_element import WebElement


class SliderElement(Input):
    RANGE_LOC = (By.ID, "range")

    def __init__(self, browser, locator, description=None):
        super().__init__(browser, locator, description)
        self.value_display = WebElement(self.browser, self.RANGE_LOC, description='Slider value')

    def move_slider(self, target_value):
        current_value = self.get_current_value()
        step = self.get_step()
        diff = target_value - current_value
        if diff == 0:
            return

        actions = ActionChains(self.browser.driver)
        key = Keys.ARROW_UP if diff > 0 else Keys.ARROW_DOWN
        presses = int(abs(diff) / step)
        actions.send_keys(key * presses)
        actions.perform()

    def get_current_value(self):
        text = self.value_display.get_text()
        return float(text)

    def get_min(self):
        return float(self.get_attribute("min"))

    def get_max(self):
        return float(self.get_attribute("max"))

    def get_step(self):
        return float(self.get_attribute("step"))

    def get_attributes(self):
        return {
            "min": self.get_min(),
            "max": self.get_max(),
            "step": self.get_step(),
        }
