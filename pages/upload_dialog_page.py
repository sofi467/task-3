from selenium.webdriver.common.by import By

from elements.button import Button
from elements.input import Input
from elements.web_element import WebElement
from pages.base_page import BasePage


class UploadImgPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    UPLOAD_FILE_LOC = (By.ID, "drag-drop-upload")
    LABLE_TEXT_LOC = (By.XPATH, "//div[contains(@class, 'dz-filename')]//span")
    CHECK_MARK_LOC = (By.XPATH,"//div[contains(@class, 'dz-success-mark')]//span")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "upload_img_dialog_page"
        self.unique_element = WebElement(self.browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description='Main Page -> File Upload header')
        self.loading_field = Input(self.browser.driver, self.UPLOAD_FILE_LOC,
                                   description='Main Page -> Select button click')
        # self.upload_button = Button(self.browser.driver, self.UPLOAD_BUTTON_LOC,
        #                             description='Main Page -> Upload button click')
        self.text = WebElement(self.browser.driver, self.LABLE_TEXT_LOC,
                               description='Main Page -> File name  label')
        self.file_name = WebElement(self.browser.driver, self.CHECK_MARK_LOC,
                                    description='Main Page -> Check mark label')

    def upload_file(self, file):
        self.loading_field.send_key(file)
