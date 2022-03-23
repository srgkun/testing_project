from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_basket_button(self):
        # проверка на наличие кнопки "Добавить в корзину"
        assert self.is_element_present(*ProductPageLocators.BASKET_BTN), \
            "'Add to basket button' is not presented"

    def basket_click(self):
        # нажатие кнопки "Добавить в корзину"
        link = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        link.click()
        # print("Clicked!")

    def should_be_product_name(self):
        # проверка того что имя продукта существует и возврат его по запросу
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME, returned=1), \
            "Product name is not presented"
        return self.is_element_present(*ProductPageLocators.PRODUCT_NAME, returned=1)

    def should_be_price(self):
        # проверка того что цена существует и возврат ее по запросу
        assert self.is_element_present(*ProductPageLocators.PRICE, returned=1), \
            "Price is not presented"
        return self.is_element_present(*ProductPageLocators.PRICE, returned=1)

    def should_be_correct_product_name(self, product_name):
        # проверка на совпадение имени товара в корзине
        # print('--', product_name)
        assert product_name == self.is_element_present(*ProductPageLocators.BASKET_PRODUCT_NAME, returned=1), \
            "The product name is not matches with the product name in the basket"

    def should_be_correct_price(self, price):
        # print('--', price)
        # стоимость корзины совпадает со стоимостью товара
        assert price == self.is_element_present(*ProductPageLocators.BASKET_PRICE, returned=1), \
            "The price is not matches with the price in the basket"
