from pages.alerts_page import AlertPage
from utils.random_utils import RandomUtils


def test_alert(browser, config_reader):
    url = config_reader.get_value("url_2")
    browser.get(url)

    alert_page = AlertPage(browser)
    alert_page.wait_for_open()
    alert_page.click_alert()

    browser.wait_alert_presence()
    alert_text = browser.get_alert_text()
    assert alert_text == 'I am a JS Alert'
    browser.close_alert()
    result_text = alert_page.get_result_text()
    assert result_text == "You successfully clicked an alert"

    alert_page.click_confirm()
    browser.wait_alert_presence()
    confirm_text = browser.get_alert_text()
    assert confirm_text == 'I am a JS Confirm'
    browser.close_alert()
    result_text = alert_page.get_result_text()
    assert result_text == "You clicked: Ok"

    alert_page.click_prompt()
    prompt_text = browser.get_alert_text()
    assert prompt_text == "I am a JS prompt"
    text = RandomUtils.random_text()
    browser.send_keys_alert(text)
    result_text = alert_page.get_result_text()
    assert result_text.strip() == f"You entered: {text}".strip()
