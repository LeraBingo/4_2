from .base_page import BasePage
from .locators import ProductPageLocators as PPL

class ProductPage(BasePage):
    product_name = ''
    product_price = ''
    product_description = ''

    def add_to_basket(self):
        self.should_be_name()
        self.should_be_price()
        self.should_be_decription()
        self.should_be_add_button()

        btn = self.browser.find_element(*PPL.ADD_TO_BASKET)
        btn.click()
        self.solve_quiz_and_get_code()

        self.should_be_success()
        self.check_success_message()

    def should_be_name(self):
        assert self.is_element_present(*PPL.PRODUCT_NAME), "Name of product not found"
        self.product_name = self.browser.find_element(*PPL.PRODUCT_NAME).text

    def should_be_price(self):
        assert self.is_element_present(*PPL.PRODUCT_PRICE), "Price of product not found"
        self.product_price = self.browser.find_element(*PPL.PRODUCT_PRICE).text

    def should_be_decription(self):
        assert self.is_element_present(*PPL.PRODUCT_DESCRIPTION), "Description of product not found"
        self.product_description = self.browser.find_element(*PPL.PRODUCT_DESCRIPTION).text

    def should_be_add_button(self):
        assert self.is_element_present(*PPL.ADD_TO_BASKET), "Button 'Add to basket' is not available"

    def should_be_success(self):
        assert self.is_element_present(*PPL.SUCCESS_MESSAGES), "Message of Success not found "

    def check_success_message(self):
        msg_lst = self.browser.find_elements(*PPL.SUCCESS_MESSAGES)
        assert len(msg_lst) > 0, "Success message not found"

        assert self.product_name == msg_lst[0].text, "Wrong name product added to basket"
        assert self.product_price == msg_lst[2].text, "Wrong price product added to basket"



