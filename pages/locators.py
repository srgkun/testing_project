from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner>strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRICE = (By.CSS_SELECTOR, 'p.price_color')
