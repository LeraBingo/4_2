from .base_page import BasePage
from .locators import ProductPageLocators as PPL


class ProductPage(BasePage):

    # to store book`s values that are shown before adding to the basket

    product_name = ''
    product_price = ''
    product_description = ''

    # methods (used in test_product_page.py) to check the presence of elements - add to the basket - solve the quiz -
    # check the success msg

    def check_this_is_product_page(self):
        self.should_be_name()
        self.should_be_price()
        self.should_be_description()
        self.should_be_add_button()

    def add_to_basket(self):
        btn = self.browser.find_element(*PPL.ADD_TO_BASKET)
        btn.click()

    def solve_quiz(self):
        self.solve_quiz_and_get_code()

    def check_correct_data_for_product_added(self):
        self.should_be_success()
        self.check_success_message()

    # check the presence of elements BEFORE adding to the basket

    def should_be_name(self):
        assert self.is_element_present(*PPL.PRODUCT_NAME), "Name of product not found"
        self.product_name = self.browser.find_element(*PPL.PRODUCT_NAME).text

    def should_be_price(self):
        assert self.is_element_present(*PPL.PRODUCT_PRICE), "Price of product not found"
        self.product_price = self.browser.find_element(*PPL.PRODUCT_PRICE).text

    def should_be_description(self):
        assert self.is_element_present(*PPL.PRODUCT_DESCRIPTION), "Description of product not found"
        self.product_description = self.browser.find_element(*PPL.PRODUCT_DESCRIPTION).text

    def should_be_add_button(self):
        assert self.is_element_present(*PPL.ADD_TO_BASKET), "Button 'Add to basket' is not available"

    # check the success message AFTER adding to the basket

    def should_be_success(self):
        assert self.is_element_present(*PPL.SUCCESS_MESSAGES), "Message of Success not found "

    def check_success_message(self):
        msg_lst = self.browser.find_elements(*PPL.SUCCESS_MESSAGES)
        assert len(msg_lst) > 0, "Success message not found"

        assert self.product_name == msg_lst[0].text, "Wrong name product added to basket"
        assert self.product_price == msg_lst[2].text, "Wrong price product added to basket"

    # negative cases

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*PPL.SUCCESS_MESSAGES), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*PPL.SUCCESS_MESSAGES), "Success message has not disappeared"
