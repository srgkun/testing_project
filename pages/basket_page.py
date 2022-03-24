from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_empty(self):
        # print("проверка на пустую корзину")
        assert "Your basket is empty." in self.is_element_present(*BasketPageLocators.BASKET_TEXT, returned=1), \
            "The basket is not empty"
