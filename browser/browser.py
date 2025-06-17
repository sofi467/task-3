import logging
from operator import index

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait

from config_reader import ConfigReader
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


class Browser:
    cfg = ConfigReader()
    DEFAULT_TIMEOUT = cfg.get_value("timeout")

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.DEFAULT_TIMEOUT)
        self.action_chains = ActionChains(driver)

    def get(self, url):
        logging.info(f"Login browser")
        self.driver.get(url)

    def quit(self):
        logging.info(f"Quit browser")
        self.driver.quit()

    def close(self):
        logging.info("Close")
        self.driver.close()

    def wait_alert_presence(self):
        logging.info(f"wait for the alert to be presence")
        self.wait.until(EC.alert_is_present())

    def switch_to_alert(self):
        logging.info(f"{self} switch to alert")
        self.wait_alert_presence()
        return self.driver.switch_to.alert

    def get_alert_text(self):
        logging.info(f"Get the alert text")
        return self.switch_to_alert().text

    def send_keys_alert(self, text):
        logging.info(f"send {text} to alert")
        self.switch_to_alert().send_keys(text)
        return text

    def close_alert(self):
        self.wait_alert_presence()
        self.switch_to_alert().accept()

    def get_alert_text(self):
        alert = self.switch_to_alert()
        return alert.text

    def back(self):
        logging.info("Back")
        self.driver.back()

    def get_current_url(self):
        logging.info("Get url")
        return self.driver.current_url

    def get_title_window(self):
        logging.info("Get title")
        return self.driver.title

    def switch_to_window(self, index):
        logging.info("Switch to window{index}")
        self.driver.switch_to.window(self.driver.window_handles[index])

    def switch_to_iframe(self, iframe):
        iframe_element = iframe.wait_for_presence()
        logging.info("Switch to IFrame")
        self.driver.switch_to.frame(iframe_element)

    def get_page_source(self):
        logging.info("Sourse HTML")
        return self.driver.page_source

    def switch_to_default(self):
        logging.info("Switch to Default content")
        self.driver.switch_to.default_content()

    def refresh_window(self):
        logging.info("Refresh window")
        self.driver.refresh()
