import pytest
from selenium.webdriver.common.by import By



def test_header_text(browser):
    browser.get("https://10.10.105.153:97")
    elem = browser.find_element(By.XPATH, '//div[normalize-space()="Справочная служба"]')
    assert elem.text == "Справочная служба"