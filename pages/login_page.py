from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL is not correct or not Login Page..."

    def should_be_login_form(self):
        email = self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FORM)
        password = self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FORM)
        button = self.is_element_present(*LoginPageLocators.LOGIN_BUTTON)
        assert all((email, password, button)), "Login form is corrupted..."

    def should_be_register_form(self):
        email = self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_FORM)
        password = self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_FORM)
        confirm_password = self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FORM)
        button = self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON)
        assert all((email, password, confirm_password, button)), "Registration form is corrupted"
