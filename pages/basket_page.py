from .base_page import BasePage
from .locators import BasketPageLocators as BPL


class BasketPage(BasePage):

    # the dictionary stores "Your basket is empty." text in all the available languages

    languages = {
        "ar": "سلة التسوق فارغة",
        "ca": "La seva cistella està buida.",
        "cs": "Váš košík je prázdný.",
        "da": "Din indkøbskurv er tom.",
        "de": "Ihr Warenkorb ist leer.",
        "en": "Your basket is empty.",
        "el": "Το καλάθι σας είναι άδειο.",
        "es": "Tu carrito esta vacío.",
        "fi": "Korisi on tyhjä",
        "fr": "Votre panier est vide.",
        "it": "Il tuo carrello è vuoto.",
        "ko": "장바구니가 비었습니다.",
        "nl": "Je winkelmand is leeg",
        "pl": "Twój koszyk jest pusty.",
        "pt": "O carrinho está vazio.",
        "pt-br": "Sua cesta está vazia.",
        "ro": "Cosul tau este gol.",
        "ru": "Ваша корзина пуста",
        "sk": "Váš košík je prázdny",
        "uk": "Ваш кошик пустий.",
        "zh-cn": "Your basket is empty.",
    }

    # NOTE! startswith is used because txt_to_check_if_basket_is_empty will ALSO store "Continue shopping" text from
    # <a> checks if the basket is empty -> if true, checks that the 1st sentence of txt == the value in the
    # dictionary for the language specified

    def should_be_basket_is_empty_text(self, request):
        current_language = request.config.option.language  # to take --language value from the console
        txt_to_check_if_basket_is_empty = self.browser.find_element(*BPL.EMPTY_BASKET_TEXT).text
        assert txt_to_check_if_basket_is_empty.startswith(self.languages[current_language]), "The basket is not empty"

    # checks the absence of items in the basket

    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BPL.ITEMS), "There is 1 or more items in the basket"
