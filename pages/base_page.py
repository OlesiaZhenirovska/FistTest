from selenium.common.exceptions import NoSuchElementException

from pages.locators import MainPageLocators



class BasePage():
    def __init__(self,browser, link):
        self.browser=browser
        self.link=link

    def open_page(self):
        self.browser.get(self.link)

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_BTN).click()


