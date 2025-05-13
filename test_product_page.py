import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(browser, self.link)
        self.page.open()
        
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        self.page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        self.page.should_be_login_link()

@pytest.mark.basket_guest
class TestBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(browser, self.link)
        self.page.open()
        
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        self.page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_products_in_basket()
        basket_page.should_be_empty_basket_message()