import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture()
def set_up(): # Этот метод выполняется после каждого теста
    print("\nStart Test\n")
    yield
    print("\nFinish Test\n")

@pytest.fixture(scope="module")
def get_driver(): # Метод возвращает driver
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    url = "https://www.citilink.ru/"
    driver.maximize_window()
    driver.get(url)
    yield driver
    # driver.quit()