from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest

start_page = "http://selenium1py.pythonanywhere.com"
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
promo_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"


@pytest.mark.new_user_tests
class TestUserAddToBasketFromProductPage:
    # Регистрация нового пользователя перед запуском каждого теста в классе
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, start_page)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()

    # Не должно быть сообщения, что товар добавлен в корзину
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link2)
        page.open()
        page.should_not_be_success_message()

    # Пользователь может добавить товар в корзину,
    # проверяется соответствие названия товара и его цены
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link2)
        page.open()
        product_and_price = page.get_product_and_price()
        page.add_to_basket()
        if page.check_alert():
            page.solve_quiz_and_get_code()
        page.product_and_price_is_same_in_basket(*product_and_price)


# Гость может добавить товар в корзину
# проверяется соответствие названия товара и его цены
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link2)
    page.open()
    product_and_price = page.get_product_and_price()
    page.add_to_basket()
    if page.check_alert():
        page.solve_quiz_and_get_code()
    page.product_and_price_is_same_in_basket(*product_and_price)


# Если не добавлять товар в корзину, товара в корзине нет
# Проверяется, что товаров в корзине нет и есть уведомление, что она пуста
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link2)
    page.open()
    page.go_to_basket_page()
    page.is_not_items()
    page.is_empty_basket()


# Не должно быть сообщения, что товар добавлен в корзину
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_not_be_success_message()


# Гость может перейти на страницу Логина со страницы товара
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


# Гость может видеть ссылку перехода на станицу Логина
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_login_link()


# Заведомо ложный тест
@pytest.mark.xfail(reason="fake test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


# Заведомо ложный тест
@pytest.mark.xfail(reason="success message should not disappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared()
