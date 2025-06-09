import time

import pyautogui


class DialogWindowUtils:
    @staticmethod
    def write_and_enter(text):
        time.sleep(1)
        pyautogui.write(text)
        pyautogui.press("enter")