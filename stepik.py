import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def test_browser(request):
    chrome_options = Options()
    chrome_options.binary_location = r"D:\GCh_Portable\GoogleChromePortable\GoogleChromePortable.exe"
    chrome_options.add_argument('--ignore-certificate-errors')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_size(1920, 1080)
    request.node.driver = driver          # для доступа из тестов
    yield driver                          # передаём тесту
    driver.quit()

@pytest.fixture
def test_open(browser):  # ✅ Фикстура передаётся как аргумент
    browser.get('https://10.10.105.153:97/Webarm.Root/login?redirect=/Webarm.Root/')
    time.sleep(5)