from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_EMAIL_FORM = (By.ID, "id_login-username")
    LOGIN_PASSWORD_FORM = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTRATION_EMAIL_FORM = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD_FORM = (By.ID, "id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_FORM = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    PRODUCT = (By.TAG_NAME, "h1")
    PRICE_PRODUCT = (By.CLASS_NAME, "price_color")
    PRODUCT_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_PRODUCT = (By.CSS_SELECTOR, "#messages .alert:first-child strong")
    MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages .alert:last-child strong")
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, "#messages .alert:first-child div")
