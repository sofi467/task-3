from selenium.webdriver.common.by import By

from elements.web_element import WebElement
from pages.base_page import BasePage


class DynamicPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    IMAGE_SRC_LOC = (By.XPATH, "(//div[contains(@class, 'large-2')]//img)[{}]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "dynamic_page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description='Main Page -> Dynamic header')

    def get_img_element(self, i):
        locator = (self.IMAGE_SRC_LOC[0], self.IMAGE_SRC_LOC[1].format(i))
        self.img_src = WebElement(self.browser, locator,
                                  description=f'Main Page -> Image {i}')
        return self.img_src

    def get_src_by_index(self, i):
        img_element = self.get_img_element(i)
        return img_element.get_attribute("src")

    def refresh_to_2_img(self):
        while True:
            src_list = []
            for i in range(1, 4):
                src_list.append(self.get_src_by_index(i))
            if any(src_list.count(src) > 1 for src in src_list):
                break
            self.browser.refresh_window()
