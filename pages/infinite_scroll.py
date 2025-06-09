from selenium.webdriver.common.by import By

from elements.web_element import WebElement
from pages.base_page import BasePage
from bs4 import BeautifulSoup


class InfiniteScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    PARAGRAPH_LAST = (By.XPATH, "//div[@class='jscroll-added'][last()]")
    ALL_PARAGRAPH = (By.XPATH, "//div[@class='jscroll-added']")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "infinite_scroll_page"
        self.unique_element = WebElement(self.browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description='Main Page -> Infinite header')
        self.last_paragraph = WebElement(self.browser.driver, self.PARAGRAPH_LAST,
                                         description='Main Page -> Scroll paragraph')
        self.all_paragraph = WebElement(self.browser.driver, self.ALL_PARAGRAPH,
                                         description='Main Page -> All paragraph')

    def scroll_to_paragraph(self, count):
        while True:
            self.last_paragraph.scroll()
            src = self.all_paragraph.get_attribute("innerHTML")
            soup = BeautifulSoup(src, "html.parser")
            if len(soup.find_all(class_="jscroll-added")) == count:
                break
        return len(soup.find_all(class_="jscroll-added"))
