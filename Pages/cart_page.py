import logging
from Base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from Utilities.utils import custom_logger


class CartPage(BaseDriver):
    log = custom_logger(logLevel=logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    cart_page_btn = (By.XPATH, "//a[normalize-space()='Cart']")
    product_prices = (By.XPATH, "//div[@class='col-lg-8']//tr/td[3]")
    delete_buttons = (By.XPATH, "//div[@class='col-lg-8']//tr/td[4]/a")
    place_order_btn = (By.XPATH, "//button[normalize-space()='Place Order']")
    name_field = (By.XPATH, "//input[@id='name']")
    credit_card_field = (By.XPATH, "//input[@id='card']")
    purchase_btn = (By.XPATH, "//button[normalize-space()='Purchase']")
    purchase_message = (By.XPATH, "//h2[normalize-space()='Thank you for your purchase!']")

    def click_on_cart_page(self):
        """Clicks on the cart button in the navigation bar"""
        self.log.info("Clicking on cart page")
        self.driver.find_element(*self.cart_page_btn).click()

    def find_lowest_price_in_cart(self):
        """Searches through the texts of the element list (product).
            Finds the lowest text,converts to an int and then stored in a list by itself.
            Iterates through the Product list again to find the index position of the lowest_price
            Returns the position
        """
        products = self.driver.find_elements(*self.product_prices)
        lowest_price = min([int(product.text) for product in products])
        position = [products.index(product) for product in products if lowest_price == int(product.text)]
        self.log.info("Lowest price in the cart found")
        return position[0]

    def match_lowest_price_and_its_delete_button(self):
        """Match the index of the lowest price product with its delete button index"""
        product_index = self.find_lowest_price_in_cart()
        deleted_buttons = self.driver.find_elements(*self.delete_buttons)
        element_to_delete = deleted_buttons[product_index]
        element_to_delete.click()
        self.wait_for_absence_of_element(element_to_delete)

    def finish_transaction(self, name, credit_card):
        self.match_lowest_price_and_its_delete_button()
        self.driver.find_element(*self.place_order_btn).click()
        self.driver.find_element(*self.name_field).send_keys(name)
        self.driver.find_element(*self.credit_card_field).send_keys(credit_card)
        self.driver.find_element(*self.purchase_btn).click()
        purchase = self.driver.find_element(*self.purchase_message)
        if self.driver.find_element(*self.purchase_message):
            self.log.info("Purchase complete")
            return True
        else:
            self.log.error("**** Purchase INCOMPLETE ****")
            return False
