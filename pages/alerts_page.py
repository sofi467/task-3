from selenium.webdriver.common.by import By

from elements.button import Button
from elements.web_element import WebElement

from pages.base_page import BasePage


class AlertPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'JavaScript')]")
    BUTTON_JS_ALERT_LOC = (By.XPATH, "//button[@onclick = 'jsAlert()']")
    RESULT_LOC = (By.ID, "result")
    BUTTON_JS_CONF_LOC = (By.XPATH, "//button[@onclick = 'jsConfirm()']")
    BUTTON_JS_PROMPT_LOC = (By.XPATH, "//button[@onclick = 'jsPrompt()']")

    def __init__(self, browser):
        super().__init__(browser)
        self.alert_button = Button(self.browser, self.BUTTON_JS_ALERT_LOC,
                                   description='Main Page -> Click for js alert')
        self.confirm_button = Button(self.browser, self.BUTTON_JS_CONF_LOC,
                                     description='Main Page -> Click for js confirm')
        self.prompt_button = Button(self.browser, self.BUTTON_JS_PROMPT_LOC,
                                    description='Main Page -> Click for js prompt')
        self.result_text = WebElement(self.browser, self.RESULT_LOC,
                                      description='Main Page -> Result text')
        self.page_name = "alert_page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description='Main Page -> Unique element')

    def click_alert(self):
        self.alert_button.click()

    def click_confirm(self):
        self.confirm_button.click()

    def click_prompt(self):
        self.prompt_button.click()

    def get_result_text(self):
        text = self.result_text.get_text()
        return text

    def click_js_alert(self):
        self.alert_button.js_click()

    def click_js_confirm(self):
        self.confirm_button.js_click()

    def click_js_prompt(self):
        self.prompt_button.js_click()
