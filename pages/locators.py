from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group>a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators():
    BASKET_TEXT = (By.CSS_SELECTOR, 'div>p')
    BASKET_TEXT_P = (By.CSS_SELECTOR, '#content_inner>p')


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL_FORM = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD_FORM = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD_FORM_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner>strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRICE = (By.CSS_SELECTOR, 'p.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')

