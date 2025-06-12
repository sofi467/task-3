import logging

from elements.base_element import BaseElement


class Input(BaseElement):
    def clear(self):
        element = self.wait_for_visible()
        logging.info(f"{self} is clear")
        element.clear()

    def send_key(self, keys: str, clear: bool = True):
        if clear:
            self.clear()
        element = self.wait_for_visible()
        logging.info(f"{self} send key = '{keys} {self.description}'")
        element.send_keys(keys)
