import math
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_product_added(self):
        product_name = self.get_product_name()
        product_price = self.get_product_price()
        self.should_be_correct_product_name(product_name)
        self.should_be_correct_basket_price(product_price)

    def should_be_correct_product_name(self, product_name):
        alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        assert product_name == alert_product_name, \
            f"Product name in alert '{alert_product_name}' doesn't match actual product '{product_name}'"

    def should_be_correct_basket_price(self, product_price):
        basket_price = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_PRICE).text
        assert product_price == basket_price, \
            f"Basket price '{basket_price}' doesn't match product price '{product_price}'"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"