from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "В корзине есть товары, но не должно быть"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Сообщение о пустой корзине отсутствует"
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "Your basket is empty" in message, \
            f"Некорректное сообщение о пустой корзине: '{message}'"