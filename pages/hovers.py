from selenium.webdriver.common.by import By

from elements.web_element import WebElement
from pages.base_page import BasePage


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Hovers')]")
    IMG_USER_LOC = (By.XPATH, "//div[@class='figure'][{}]")
    USERNAME_LOC = (By.XPATH, "//div[@class='figure'][{}]//h5")
    PROFILE_LINK_LOC = (By.XPATH, "//div[@class='figure'][{}]//a")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "hover_page"
        self.unique_element = WebElement(self.browser.driver, self.UNIQUE_ELEMENT_LOC, description='Main Page ->Hover header')

    def move_to_image(self, i):
        locator = (self.IMG_USER_LOC[0], self.IMG_USER_LOC[1].format(i))
        self.image = WebElement(self.browser.driver, locator,
                                description=f'Main Page -> Hover over IMG {i}')
        self.image.move_to_element()

    def get_text_image(self, i):
        locator = (self.USERNAME_LOC[0], self.USERNAME_LOC[1].format(i))
        self.text = WebElement(self.browser.driver, locator,
                               description=f'Main Page -> follow link {i}')
        self.text.is_exists()
        return self.text.get_text()

    def click_on_link(self, i):
        locator = (self.PROFILE_LINK_LOC[0], self.PROFILE_LINK_LOC[1].format(i))
        self.link = WebElement(self.browser.driver, locator,
                               description=f'Main Page -> follow link {i}')
        self.link.click()
