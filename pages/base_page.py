from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from .locators import BasePageLocators as BPL, MainPageLocators as MPL
import math


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # goes to the basket page by clicking the basket icon

    def go_to_basket_page(self):
        link = self.browser.find_element(*MPL.VIEW_BASKET)  # finds "View basket" button
        link.click() # goes to the basket page

    # waits for an element to disappear

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # checks the presence of an element

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # checks the absence of an element

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # goes to the login page.

    def go_to_login_page(self):
        link = self.browser.find_element(*BPL.LOGIN_LINK)  # find a login link
        link.click()  # goes to login link

    # gets a link

    def open(self):
        self.browser.get(self.url)

    # checks if a user is authorized

    def should_be_authorized_user(self):
        assert self.is_element_present(*BPL.USER_ICON), "User icon is not presented," \
                                                        " probably unauthorised user"

    # checks the presence of the login link

    def should_be_login_link(self):
        assert self.is_element_present(*BPL.LOGIN_LINK), "Login link is not presented"  # from base_page.py

    # checks the presence of the "View basket" button

    def should_be_view_basket_button(self):
        assert self.is_element_present(*MPL.VIEW_BASKET), "The view basket button is not presented"

    # solves the quiz in the alert

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
