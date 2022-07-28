from Base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from Utilities.utils import custom_logger
import logging


class ProductPage(BaseDriver):
    log = custom_logger(logLevel=logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    add_to_cart_btn = (By.XPATH, "//a[normalize-space()='Add to cart']")

    def click_add_to_cart_btn(self):
        try:
            self.driver.find_element(*self.add_to_cart_btn).click()
            self.wait_for_presence_of_alert()
            alert = self.driver.switch_to.alert.text
            self.driver.switch_to.alert.accept()
        except NoSuchElementException:
            self.log.error("**** Element not found. Not added to cart - Product page ****")
            print("*** Element not found ***")
            return False
        else:
            self.log.info("Item added to cart successfully")
            self.driver.get("https://www.demoblaze.com/index.html")
            return alert
