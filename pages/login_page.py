from .base_page import BasePage
from .locators import LoginPageLocators as LPL


class LoginPage(BasePage):

    # checks the presence of the login form

    def should_be_login_form(self):
        self.is_element_present(*LPL.LOGIN_FORM), "Login form is not presented"  # the method is from base_page.py
        assert True

    # if all the methods inside return true - it`s a login page

    def should_be_login_page(self):
        self.should_be_login_url()  # these 3 methods are from login_page.py
        self.should_be_login_form()
        self.should_be_register_form()

    # checks the presence of the login url

    def should_be_login_url(self):
        assert self.browser.current_url == LPL.URL, "Login form is not presented"

    # checks the presence of the registration form

    def should_be_register_form(self):
        assert self.is_element_present(*LPL.REGISTRATION_FORM), "Registration form is not presented"
