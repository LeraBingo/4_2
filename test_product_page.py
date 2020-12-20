from pages.product_page import ProductPage
import pytest


# goes through several urls: checks the page - adds to basket - solves the quiz - checks the data
# marks the failed one (== '?promo=offer7') as xfailed

@pytest.mark.parametrize('promo_offer',
                         [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='not for day one')) for i in
                          range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.check_this_is_product_page()
    product_page.add_to_basket()  # the method is from product_page.py
    product_page.solve_quiz()  # from base_page.py
    product_page.check_correct_data_for_product_added()  # from product_page.py


# check if this is a product page - adds to basket - checks the presence of a success message

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.check_this_is_product_page()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


# checks if this is a product page - checks the absence of a success message

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.check_this_is_product_page()
    product_page.should_not_be_success_message()


# checks if this is a product page - adds to basket - checks if the success  message disappears

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.check_this_is_product_page()
    product_page.add_to_basket()
    product_page.should_disappear_success_message()


# checks the presence of a login link

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()  # from base_page.py


# goes to the login link

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()   # from base_page.py
