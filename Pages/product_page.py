import time
from Base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import random


class ProductPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    add_to_cart_btn = (By.XPATH, "//a[normalize-space()='Add to cart']")




    def click_add_to_cart_btn(self):
        try:
            self.driver.find_element(*self.add_to_cart_btn).click()
            self.wait_for_presence_of_alert()
            alert = self.driver.switch_to.alert.text
            self.driver.switch_to.alert.accept()
        except NoSuchElementException:
            print("*** Element not found ***")
            return False
        else:
            print("Item added to cart successfully")
            self.driver.get("https://www.demoblaze.com/index.html")
            return alert










