from selenium.webdriver.common.by import By

class MainPageLocators():
    CATALOGUE_LINK = (By.XPATH ,"//ul[@id='browse']//ul//a")
    LOGIN_BTN = (By.CSS_SELECTOR,"#login_link")

class LoginPageLocators():
    LOGIN_Form = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

