import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser():
    service = Service(executable_path="chromedriver\\chromedriver.exe")
    chrome_options = Options()
    chrome_options.page_load_strategy = 'none'
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()