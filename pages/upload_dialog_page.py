from selenium.webdriver.common.by import By

from elements.input import Input
from elements.web_element import WebElement
from pages.base_page import BasePage


class UploadImgDialogPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    UPLOAD_FILE_LOC = (By.ID, "drag-drop-upload")
    LABLE_TEXT_LOC = (By.XPATH, "//div[contains(@class, 'dz-filename')]//span")
    CHECK_MARK_LOC = (By.XPATH, "//div[contains(@class, 'dz-success-mark')]//span")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "upload_img_dialog_page"
        self.unique_element = WebElement(self.browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description='Main Page -> File Upload header')
        self.loading_field = Input(self.browser.driver, self.UPLOAD_FILE_LOC,
                                   description='Main Page -> Select button click')

        self.text = WebElement(self.browser.driver, self.LABLE_TEXT_LOC,
                               description='Main Page -> File name  label')
        self.file_name = WebElement(self.browser.driver, self.CHECK_MARK_LOC,
                                    description='Main Page -> Check mark label')

    def upload_file(self, file):
        self.loading_field.send_key(file)

    def click_on_upload_section(self):
        section = self.loading_field.wait_for_presence()
        section.click()

    def get_text_name(self):
        return self.text.get_text()

    def get_check_mark(self):
        return self.file_name.is_exists()
