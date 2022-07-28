import time
from Base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import random


class CartPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    cart_page_btn = (By.XPATH, "//a[normalize-space()='Cart']")
    product_prices = (By.XPATH, "//div[@class='col-lg-8']//tr/td[3]")
    delete_buttons = (By.XPATH, "//div[@class='col-lg-8']//tr/td[4]/a")

    def click_on_cart_page(self):
        """Clicks on the cart button in the navigation bar"""
        print("Clicking on cart page")
        self.driver.find_element(*self.cart_page_btn).click()
        time.sleep(5)

    def find_lowest_price_in_cart(self):
        """Find the lowest price out of all products in the cart"""
        products = self.driver.find_elements(*self.product_prices)
        minimum_value = 0
        for product in products:
            if int(product.text) > minimum_value:
                minimum_value = int(product.text)
        return minimum_value

    def find_index_position_of_lowest_price_product(self):
        """Match the lowest price with the element in the list of elements and find its index"""
        lowest = self.find_lowest_price_in_cart()
        products = self.driver.find_elements(*self.product_prices)
        for product in products:
            if lowest == int(product.text):
                position = products.index(product)
                #target_product = product
        #print(target_product)
        return position

    def gather_delete_buttons(self):
        delete_btns = self.driver.find_elements(*self.delete_buttons)
        return delete_btns


    def match_product_index_and_delete_button(self):
        """Match the index of the lowest price product with its delete button index"""
        product_index = self.find_index_position_of_lowest_price_product()
        deleted_buttons = self.gather_delete_buttons()
        print(product_index)

        print(deleted_buttons[0])
        print(deleted_buttons.index(product_index))
        