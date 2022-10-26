import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def browser(scoop='class'):
    print('\nstart browser..')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    print('\nquite browser..')
    driver.quit()
