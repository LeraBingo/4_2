from .base_page import BasePage
from .locators import ProductPageLocators as PPL


class ProductPage(BasePage):
    # to store book`s values that are shown before adding to the basket

    product_name = ''
    product_price = ''
    product_description = ''

    # adds a product to the basket

    def add_to_basket(self):
        btn = self.browser.find_element(*PPL.ADD_TO_BASKET)  # finds the button to add a product to the basket
        btn.click()  # adds the product to the basket

    # checks that after adding a product to the basket correct data is shown

    def check_correct_data_for_product_added(self):
        self.should_be_success()  # checks the presence of the success message
        self.check_success_message()  # checks the data in the message == the data of the product added

    # checks that after adding a product to the basket the  data in the message == the data of the product added

    def check_success_message(self):
        msg_lst = self.browser.find_elements(*PPL.SUCCESS_MESSAGES)  # finds the success message
        assert len(msg_lst) > 0, "Success message not found"

        assert self.product_name == msg_lst[0].text, "Wrong name product added to basket"
        assert self.product_price == msg_lst[2].text, "Wrong price product added to basket"

    # checks if this is really a product page

    def check_this_is_product_page(self):
        self.should_be_name()  # checks the presence of a product name
        self.should_be_price()  # checks the presence of a product price
        self.should_be_description()  # checks the presence of a product description
        self.should_be_add_button()  # checks the presence of "add to basket" button

    # checks the presence of "add to basket" button

    def should_be_add_button(self):
        assert self.is_element_present(*PPL.ADD_TO_BASKET), "Button 'Add to basket' is not available"

    # checks the presence of a product description

    def should_be_description(self):
        assert self.is_element_present(*PPL.PRODUCT_DESCRIPTION), "Description of product not found"
        self.product_description = self.browser.find_element(*PPL.PRODUCT_DESCRIPTION).text

    # checks the presence of a product name

    def should_be_name(self):
        assert self.is_element_present(*PPL.PRODUCT_NAME), "Name of product not found"
        self.product_name = self.browser.find_element(*PPL.PRODUCT_NAME).text

    # checks the presence of a product price

    def should_be_price(self):
        assert self.is_element_present(*PPL.PRODUCT_PRICE), "Price of product not found"
        self.product_price = self.browser.find_element(*PPL.PRODUCT_PRICE).text

    # checks the presence of the success message

    def should_be_success(self):
        assert self.is_element_present(*PPL.SUCCESS_MESSAGES), "Message of Success not found "

    # checks if the success message disappears

    def should_disappear_success_message(self):
        assert self.is_disappeared(*PPL.SUCCESS_MESSAGES), "Success message has not disappeared"

    # checks the absence of the success message

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*PPL.SUCCESS_MESSAGES), "Success message is presented, but should not be"

    # solves the quiz

    def solve_quiz(self):
        self.solve_quiz_and_get_code()
