from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def is_promo(self):
        return True if '/?promo=' in self.browser.current_url else False

    def should_be_promo(self):
        assert self.is_promo(), "Page is not in PROMO..."

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.PRODUCT_TO_BASKET)
        button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_SUCCESS), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_SUCCESS), \
            "Success message is nor disappeared, but should be"

    def message_success(self):
        return self.browser.find_element(*ProductPageLocators.MESSAGE_SUCCESS).text

    def get_name_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT).text

    def get_price_product(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text

    def get_message_product(self):
        return self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT).text

    def get_message_price(self):
        return self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
