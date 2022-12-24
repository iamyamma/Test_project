from .base_page import BasePage
from .locators import LoginPageLocators
from time import time


class LoginPage(BasePage):
    # Регистрация нового пользователя
    def register_new_user(self):
        email = "test" + str(int(time())) + "@test.test"
        password = str(time())
        self.go_to_login_page()
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FORM)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FORM)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FORM)
        confirm_password_field.send_keys(password)
        registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration.click()

    # Проверка страницы Логина
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Проверка, что в URL страницы присутствует login
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL is not correct or not Login Page..."

    # Проверка присутствия полей для логина
    def should_be_login_form(self):
        email = self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FORM)
        password = self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FORM)
        button = self.is_element_present(*LoginPageLocators.LOGIN_BUTTON)
        assert all((email, password, button)), "Login form is corrupted..."

    # Проверка присутствия полей для регистрации
    def should_be_register_form(self):
        email = self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_FORM)
        password = self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_FORM)
        confirm_password = self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FORM)
        button = self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON)
        assert all((email, password, confirm_password, button)), "Registration form is corrupted"
