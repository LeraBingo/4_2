from .base_page import BasePage
from .locators import LoginPageLocators as LPL


class LoginPage(BasePage):

    # checks the presence of the registration form

    def should_be_register_form(self):
        assert self.is_element_present(*LPL.REGISTRATION_FORM), "Registration form is not presented"

    # registers a user

    def register_new_user(self, email, password):
        self.should_be_register_form()  # from login_page
        self.browser.find_element(*LPL.EMAIL_FOR_REGISTRATION).send_keys(email)
        self.browser.find_element(*LPL.PASSWORD_FOR_REGISTRATION).send_keys(password)
        self.browser.find_element(*LPL.CONFIRM_PASSWORD_FOR_REGISTRATION).send_keys(password)
        self.browser.find_element(*LPL.REGISTER_BUTTON).click()
        self.should_be_success_registration_message()

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

    # checks if the message about a successful registration is present

    def should_be_success_registration_message(self):
        assert self.is_element_present(*LPL.SUCCESS_REGISTRATION_MESSAGE), "Success message is not presented"
