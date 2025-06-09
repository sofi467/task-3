from selenium.webdriver.common.by import By

from elements.web_element import WebElement
from pages.base_page import BasePage


class DynamicPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    IMAGE1_SCR_LOC = (By.XPATH, "(//div[contains(@class, 'large-2')]//img)[1]")
    IMAGE2_SCR_LOC = (By.XPATH, "(//div[contains(@class, 'large-2')]//img)[2]")
    IMAGE3_SCR_LOC = (By.XPATH, "(//div[contains(@class, 'large-2')]//img)[2]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "dynamic_page"
        self.unique_element = WebElement(self.browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description='Main Page -> Dynamic header')
        self.img_1 = WebElement(self.browser.driver, self.IMAGE1_SCR_LOC,
                                description='Main Page -> Label IMG 1 ')
        self.img_2 = WebElement(self.browser.driver, self.IMAGE2_SCR_LOC,
                                description='Main Page -> Label IMG 2 ')
        self.img_3 = WebElement(self.browser.driver, self.IMAGE2_SCR_LOC,
                                description='Main Page -> Label IMG 3 ')

    def get_src_1(self):
        return self.img_1.get_attribute("scr")

    def get_src_2(self):
        return self.img_2.get_attribute("scr")

    def get_src_3(self):
        return self.img_3.get_attribute("scr")

    def refresh_to_2_img(self):
        while (self.get_src_1() != self.get_src_2()) and \
                (self.get_src_1() != self.get_src_3()) and \
                (self.get_src_2() != self.get_src_3()):
            self.browser.refresh_window()

    def is_2_img_corrected(self):
        return (self.get_src_1() == self.get_src_2()) or \
            (self.get_src_1() == self.get_src_3()) or \
            (self.get_src_2() == self.get_src_3())
