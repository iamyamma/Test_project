from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
promo_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


# @pytest.mark.parametrize('promo', [str(x) if x != 7 else
#                                    pytest.param(str(x), marks=pytest.mark.xfail(reason="coders at work"))
#                                    for x in range(10)])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    product = page.get_name_product()
    price = page.get_price_product()
    if page.is_promo():
        page.add_to_basket()
        page.solve_quiz_and_get_code()
    else:
        page.add_to_basket()
    assert product == page.get_message_product(), \
        f"Name of product({product}) does no match name of product in basket({page.get_message_product()})"
    assert price == page.get_message_price(), \
        f"Price of product({price}) does no match price of product in basket({page.get_message_price()})."


def test_guest_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


@pytest.mark.xfail(reason="fake test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link2)
    page.open()
    page.go_to_basket_page()
    page.is_not_items()
    page.is_empty_basket()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail(reason="success message should not disappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared()
