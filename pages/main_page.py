from pages.base_page import BasePage
from pages.locators import MainPageLocators

class MainPage(BasePage):

    def should_be_view_product(self):
        assert self.element_is_present(*MainPageLocators.CATALOGUE_LINK)

    def go_to_catalogue(self):
        self.browser.find_element(*MainPageLocators.CATALOGUE_LINK).click()
