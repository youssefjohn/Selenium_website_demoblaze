import pytest
from Pages.cart_page import CartPage
from Pages.home_page import HomePage
from Pages.product_page import ProductPage


@pytest.mark.usefixtures("setup")
class TestCartPage:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.cp = CartPage(driver=self.driver)
        self.hp = HomePage(driver=self.driver)
        self.pp = ProductPage(driver=self.driver)

    def test_remove_lowest_price(self):
        for _ in range(3):
            self.hp.click_on_products()
            self.pp.click_add_to_cart_btn()
        self.cp.click_on_cart_page()
        assert self.cp.finish_transaction(name="Apperio", credit_card="Apperio card")
