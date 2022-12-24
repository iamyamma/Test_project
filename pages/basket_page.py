from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Проверка сообщения, что корзина пуста
    def is_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "No message that basket is empty"

    # Проверка отсутствия товаров в корзине
    def is_not_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Any items in basket"
