from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config_reader import ConfigReader
import logging


class BaseElement:
    cfg = ConfigReader()
    TIMEOUT = cfg.get_value("timeout")

    def __init__(self, browser, locator, description=None, timeout=None):
        self.driver = browser
        self.loc = locator
        self.description = description
        self.timeout = self.TIMEOUT
        self.wait = WebDriverWait(self.driver, BaseElement.TIMEOUT)

    def wait_for_presence(self) -> WebElement:
        logging.info(f"wait for {self.description} to be present")
        element = self.wait.until(EC.presence_of_element_located(self.loc))
        return element

    def wait_for_visible(self) -> WebElement:
        logging.info(f"wait for {self.description} to be visible")
        element = self.wait.until(EC.visibility_of_element_located(self.loc))
        return element

    def wait_for_clickable(self) -> WebElement:
        logging.info(f"wait for {self.description} to be clickable")
        element = self.wait.until(EC.element_to_be_clickable(self.loc))
        return element

    def is_exists(self):
        logging.info(f"Check if element {self.description} exists")
        try:
            self.wait_for_presence()
            return True
        except TimeoutException:
            return False

    def click(self):
        element = self.wait_for_clickable()
        logging.info(f"click on {self.description}")
        element.click()

    def js_click(self):
        web_element = self.wait.until(EC.element_to_be_clickable(self.loc))
        logging.info(f"click on {self.description} use JS")
        self.driver.execute_script("arguments[0].click();", web_element)  # добавить в броузер

    def get_attribute(self, attribute_name):
        logging.info(f"Get attribute '{attribute_name}' from element.")
        attribute_value = self.wait_for_presence().get_attribute(attribute_name)
        return attribute_value

    def get_text(self):
        logging.info("Get text  from an element")
        return self.wait_for_presence().text

    def context_click(self):
        element = self.wait.until(EC.element_to_be_clickable(self.loc))
        logging.info("right click")
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()

    def click_and_hold(self):
        logging.info(f"{self.description} click and hold")
        ActionChains(self.driver).click_and_hold(
            self.wait_for_presence()).release().perform()

    def move_to_element(self):
        logging.info(f"{self.description} move to element")
        ActionChains(self.driver).move_to_element(self.wait_for_presence()).perform()