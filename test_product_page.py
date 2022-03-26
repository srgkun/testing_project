from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
# from .pages.base_page import BasePage
import pytest
import time
from random import randint

'''
@pytest.mark.parametrize('link', 
                        ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                         pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?\
                         promo=offer7", marks=pytest.mark.xfail),
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    '''


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = str(randint(0, 10000000000))
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        page.should_be_success_message()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_button()
        product_name = page.should_be_product_name()
        # print('-----------', product_name, '-------------')
        price = page.should_be_price()
        page.basket_click()
        # page.solve_quiz_and_get_code()
        page.should_be_correct_product_name(product_name)
        page.should_be_correct_price(price)


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    product_name = page.should_be_product_name()
    # print('-----------', product_name, '-------------')
    price = page.should_be_price()
    page.basket_click()
    # page.solve_quiz_and_get_code()
    page.should_be_correct_product_name(product_name)
    page.should_be_correct_price(price)
    # time.sleep(10)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.basket_click()
    # page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    # time.sleep(10)


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.basket_click()
    # page.solve_quiz_and_get_code()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()
