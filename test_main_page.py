from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:

    # checks that there is a login link available on the main page

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open() # opens the main page
        page.should_be_login_link()  # check if there is a login link available

    # goes to the login page and than check if this is really login page

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()  # opens the main page
        page.go_to_login_page()  # goes to the login page
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()  # checks if this is really a login page


# checks if the basket is empty from the MAIN page.

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, request):
    link = "http://selenium1py.pythonanywhere.com"  # this is main page
    page = MainPage(browser, link)
    page.open()                          # opens the main page
    page.should_be_view_basket_button()  # checks the presence of "View basket" button
    page.go_to_basket_page()             # goes to the basket
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_no_items_in_basket()   # checks the absence of items
    basket.should_be_basket_is_empty_text(request)  # checks the text telling that the basket is empty



