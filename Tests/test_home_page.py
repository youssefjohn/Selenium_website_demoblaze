import pytest
from Pages.home_page import HomePage

@pytest.mark.usefixtures("setup")
class TestHomePage:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hp = HomePage(driver=self.driver)

    @pytest.mark.run(order=1)
    def test_sign_up(self):
        assert self.hp.signup_outcome(name=self.hp.random_word_generator(),
                               password=self.hp.random_word_generator())

