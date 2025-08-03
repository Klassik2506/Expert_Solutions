import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser(request):
    # Указываем пути
    CHROME_PORTABLE_PATH = r"D:\GCh_Portable\GoogleChromePortable\GoogleChromePortable.exe --test-type"
    CHROMEDRIVER_PATH = ChromeDriverManager().install()  # Автозагрузка chromedriver
    # Настройка ChromeOptions
    chrome_options = Options()
    chrome_options.binary_location = CHROME_PORTABLE_PATH
    options = webdriver.ChromeOptions()
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--disable-web-security')
    options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--test-type')
    # Инициализация драйвера
    driver = webdriver.Chrome()
    # Настройка окна браузера
    driver.set_window_size(1920, 1080)
    # Сохраняем драйвер в request (если нужно для других фикстур)
    request.node.driver = driver
    yield driver  # Передаём драйвер тесту
    # Завершение работы
    driver.quit()

@pytest.mark.testit_id('256')   # = ID кейса в Test IT
def test_open(browser):  # ✅ Фикстура передаётся как аргумент
    browser.get('https://10.10.105.153:97') # Открываем нужный стенд/сайт
    browser.find_element(By.XPATH, '//*[@id="details-button"]').click() #Скипаем ругань браузера на SSL сертификат
    browser.find_element(By.XPATH, '//*[@id="proceed-link"]').click() #Скипаем ругань браузера на SSL сертификат
    time.sleep(2)
    browser.find_element(By.XPATH, '//input[@name="username"]').send_keys("TestUserTD153_12") #Заполняем поле "Введите ваш УИУЛ"
    time.sleep(2)
    browser.find_element(By.XPATH, '//input[@name="password"]').send_keys("1234") #Заполняем поле "Введите ваш пароль"
    time.sleep(2)
    browser.find_element(By.XPATH, '//button[@type="submit"]').click() #Нажимаем кнопку "Войти"
    time.sleep(5)
    browser.find_element(By.XPATH, '//*[@id="helpService"]').click()
    time.sleep(5)


def test_header_text(browser):
    browser.get("https://10.10.105.153:97")
    elem.text = browser.find_element(By.XPATH, '//div[@class="text q-my-auto q-ml-md"][1]')
    assert elem.text == "Справочная служба"
