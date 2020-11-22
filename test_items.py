import time

link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestLanguage():
    def test_check_button(self, browser):
        browser.get(link)
        time.sleep(5)
        self.btn=browser.find_element_by_xpath('// *[ @ id = "add_to_basket_form"] / button')
        assert self.btn

