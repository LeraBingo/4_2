from selenium.webdriver.common.by import By


class LoginPageLocators():
    URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FOR_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FOR_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FOR_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, "//*[@id=\'register_form\']/button")
    SUCCESS_REGISTRATION_MESSAGE = (By.CSS_SELECTOR, "#messages")


class MainPageLocators():
    VIEW_BASKET = (By.CSS_SELECTOR, '.btn-group a.btn-default')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form   button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description+p")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")


