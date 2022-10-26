import time

from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_login_page()
    time.sleep(2)
    page = LoginPage(browser, link)
    page.should_be_login_page()

    # @pytest.mark.open_page
    # @pytest.mark.smoke
    # @pytest.mark.view_product
    # @pytest.mark.xfail - if something wrong inside and need to note that can be failed


#we use fixture instead of it
# def teardown(self):
#     self.driver.quit()
#     #to run use in terminal comand pytest -s -v test_main_page.py
#if we use mark need to register them using File
#to run one of them use in terminal comand pytest -s -v -m open_page test_main_page.py
# pytest -s -v -m "open_page and smoke" test_main_page.py (if for the same function)


#we use fixture instead of it
    # def setup(self):
    #     self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

if __name__ == "__main__":
    pass



