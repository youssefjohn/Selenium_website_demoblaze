import pytest
from Pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestHomePage:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(driver=self.driver)

    @pytest.mark.run(order=1)
    def test_sign_up_successful(self):
        assert self.hp.signup_outcome(name=self.hp.random_word_generator(),
                               password=self.hp.random_word_generator())

    @pytest.mark.run(order=2)
    def test_number_of_products_available(self):
        assert self.hp.confirm_num_of_products_on_homepage(9)

    @pytest.mark.run(order=3)
    def test_click_on_product(self):
        assert self.hp.click_on_products()
