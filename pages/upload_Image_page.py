from selenium.webdriver.common.by import By

from elements.button import Button
from elements.input import Input
from elements.web_element import WebElement
from pages.base_page import BasePage


class UploadImgPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    SELECT_FILE_LOC = (By.ID, "file-upload")
    UPLOAD_BUTTON_LOC = (By.ID, "file-submit")
    LABLE_TEXT_LOC = (By.XPATH, "//*[@id='content']//h3")
    FILENAME_LOC = (By.ID, "uploaded-files")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "upload_img_page"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description='Main Page -> File Upload header')
        self.select_button = Input(self.browser, self.SELECT_FILE_LOC,
                                   description='Main Page -> Select button click')
        self.upload_button = Button(self.browser, self.UPLOAD_BUTTON_LOC,
                                    description='Main Page -> Upload button click')
        self.text = WebElement(self.browser, self.LABLE_TEXT_LOC,
                               description='Main Page -> Title label')
        self.file_name = WebElement(self.browser, self.FILENAME_LOC,
                                    description='Main Page -> File name label')

    def upload_file(self, file):
        self.select_button.send_key(file)

    def click_upload(self):
        self.upload_button.click()

    def get_text_title(self):
        return self.text.get_text()

    def get_text_name(self):
        return self.file_name.get_text()
