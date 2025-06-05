import logging

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
        self.close_alert()
        return text

    def close_alert(self):
        self.wait_alert_presence()
        self.switch_to_alert().accept()

    def get_alert_text(self):
        alert = self.switch_to_alert()
        return alert.text

    # def back(self):
