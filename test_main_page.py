from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage


# checks, that there is a login link available on the main page

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()  # method is from base_page.py


# go to login page and than check if this is really the login page

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()  # method is from base_page.py
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()  # method is from login_page.py


# check the presence of View basket button - go to basket - check the absence of items - check the text telling that
# the basket is empty

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, request):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_view_basket_button()
    page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_no_items_in_basket()
    basket.should_be_basket_is_empty_text(request)

# checks if the basket is empty from the product page. Work for the SPECIFIED link

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, request):
    link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.check_this_is_product_page()
    page.should_be_view_basket_button()
    page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_no_items_in_basket()
    basket.should_be_basket_is_empty_text(request)

