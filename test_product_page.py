from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time
import secrets
import string

# NOTE! For all the functions below: If you want to check it for another product, you must change the link


# checks if a guest can add product to the basket for different promo offers
# NOTE! promo_offer7 is marked as xfailed

@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer',
                         [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='not for day one')) for i in
                          range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    product_page = ProductPage(browser, link)
    product_page.open()  # opens the product page
    product_page.check_this_is_product_page()  # checks if this is really a product page
    product_page.add_to_basket()  # adds the product to the basket
    product_page.solve_quiz()  # solves the quiz
    product_page.check_correct_data_for_product_added()  # checks that the correct product has been added

# checks if the basket is empty from the PRODUCT page.
# NOTE! If you want to check it for another product, you must change the link

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, request):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.check_this_is_product_page()  # check if this is really product page
    page.should_be_view_basket_button()  # checks the presence of "View basket" button
    page.go_to_basket_page()  # goes to the basket
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_no_items_in_basket()   # checks the absence of items in the basket
    basket.should_be_basket_is_empty_text(request)  # checks the presence of the text telling that the basket is empty


# checks if a guest can NOT see a success message after adding a product to the basket

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()  # opens the product page
    product_page.check_this_is_product_page()  # checks if this is really a product page
    product_page.add_to_basket() # adds the product to the basket
    product_page.should_not_be_success_message()  # checks the absence of the success message





# checks if the success message disappears after adding the product to the basket

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()  # opens the product page
    product_page.check_this_is_product_page()  # checks if this is really a product page
    product_page.add_to_basket()  # adds the product to the basket
    product_page.should_disappear_success_message()  # checks if the message disappears


# checks the presence of a login link

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()  # opens the product page
    page.should_be_login_link()  # checks the presence of the login link


# goes to the login page from the product page

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open() # opens the product page
    page.go_to_login_page()  # goes to the login page


class TestUserAddToBasketFromProductPage:

    # goes to the login page and registers a guest using a random email and a random 20-character password

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"  # this is a login page
        email = str(time.time()) + "@fakemail.org"  # to generate a random email
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(20))  # to generate a 20-character password

        login_page = LoginPage(browser, link)
        login_page.open()  # opens the login page
        login_page.register_new_user(email, password)  # registers a new user
        login_page.should_be_authorized_user()  # checks if the user has been authorized

    # checks if a REGISTERED user can add a product to the basket

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()  # opens the product page
        product_page.check_this_is_product_page()  # checks if this is really a product page
        product_page.add_to_basket()  # adds the product to the basket
        product_page.check_correct_data_for_product_added()  # checks that the correct product has been added

    # checks if a REGISTERED user can NOT see a success message after opening the product page

    def test_user_cant_see_success_message(self, browser, setup):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()  # opens the product page
        product_page.check_this_is_product_page()  # checks if this is really a product page
        product_page.should_not_be_success_message()  # checks the absence of the success message
