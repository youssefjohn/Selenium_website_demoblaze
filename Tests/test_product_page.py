import pytest
from Pages.home_page import HomePage
from Pages.product_page import ProductPage


@pytest.mark.usefixtures("setup")
class TestProductPage:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(driver=self.driver)
        self.PP = ProductPage(driver=self.driver)


    @pytest.mark.run(order=4)
    def test_add_to_cart_btn(self):
        self.hp.click_on_products()
        assert self.PP.click_add_to_cart_btn() == "Product added"


