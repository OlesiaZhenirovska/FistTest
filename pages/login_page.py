from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_link(self):
        assert 'login' in self.browser.current_url, 'wrong url'

    def should_be_login_form(self):
        assert self.element_is_present(*LoginPageLocators.LOGIN_Form)

    def should_be_register_form(self):
        assert self.element_is_present(*LoginPageLocators.REGISTER_FORM)
