import pytest
from time import sleep
from .pages.product_page import ProductPage

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


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link2)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared()
    sleep(5)

