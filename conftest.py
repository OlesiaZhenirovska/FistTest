import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser(scoop='class'):
    print('\nstart browser..')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    print('\nquite browser..')
    driver.quit()
