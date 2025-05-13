from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators ():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    ALERT_BASKET_PRICE = (By.CSS_SELECTOR, "div.alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    
class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")