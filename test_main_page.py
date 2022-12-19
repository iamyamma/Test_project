from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"
login_link = "https://selenium1py.pythonanywhere.com/accounts/login/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_login_url(browser):
    url = LoginPage(browser, login_link)
    url.open()
    url.should_be_login_url()


def test_guest_should_see_login_form(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_login_form()


def test_guest_should_see_registration_form(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_register_form()