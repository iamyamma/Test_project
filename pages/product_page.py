from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait


class ProductPage(BasePage):
    # Добавить в корзину
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.PRODUCT_TO_BASKET)
        button.click()

    # Возвращает кортеж из названия и цены на товар
    def get_product_and_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT).text, \
               self.browser.find_element(*ProductPageLocators.PRICE).text

    # Возвращает сообщение, что товар успешно добавлен в корзину
    def message_success(self):
        return self.browser.find_element(*ProductPageLocators.MESSAGE_SUCCESS).text

    # Сравнивает название и цену товара с названием и ценой в корзине
    def product_and_price_is_same_in_basket(self, product, price):
        WebDriverWait(self.browser, 20).until(presence_of_element_located(ProductPageLocators.MESSAGE_PRODUCT))
        add_product = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT).text
        add_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        assert product == add_product, \
            f"Name of product({product}) does no match name of product in basket({add_product})"
        assert price == add_price, \
            f"Price of product({price}) does no match price of product in basket({add_price})."

    # Проверяет, что сообщение исчезает
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_SUCCESS), \
            "Success message is nor disappeared, but should be"

    # Проверяет принадлежность товара к группе Промо по URL
    def should_be_promo(self):
        assert '/?promo=' in self.browser.current_url, "Page is not in PROMO..."

    # Проверяет отсутствие сообщения
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_SUCCESS), \
            "Success message is presented, but should not be"
