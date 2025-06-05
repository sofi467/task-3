import logging


class BasePage:
    UNIQUE_ELEMENT_LOC = None
    def __init__(self, browser):
        self.browser = browser
        self. page_name = None
        self.unique_element = None

    def wait_for_open(self):
        logging.info(f"Wait for {self.page_name} to be open")
        self.unique_element.wait_for_presence()



