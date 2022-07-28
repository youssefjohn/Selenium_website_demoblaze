from Base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from Utilities.utils import custom_logger
import random
import logging


class HomePage(BaseDriver):
    log = custom_logger(logLevel=logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    signup_btn = (By.XPATH, "//a[@id='signin2']")
    username_field = (By.XPATH, "//input[@id='sign-username']")
    password_field = (By.XPATH, "//input[@id='sign-password']")
    signup_btn_popup = (By.XPATH, "//button[contains(text(),'Sign up')]")
    product_list = (By.XPATH, "//div[@id='tbodyid']/div")
    product_list_a_tags = (By.XPATH, "//div[@id='tbodyid']/div/div/a")
    home_page_url = "https://www.demoblaze.com/index.html"

    def sign_up(self, name, password):
        """Find all web elements and perform actions on them to sign up.
            Wait for alert to be present. If a single element is missing,
            Return False, if not then return True"""
        try:
            self.driver.find_element(*self.signup_btn).click()
            self.driver.find_element(*self.username_field).send_keys(name)
            self.driver.find_element(*self.password_field).send_keys(password)
            self.driver.find_element(*self.signup_btn_popup).click()
            self.wait_for_presence_of_alert()
            alert = self.driver.switch_to.alert.text
            self.driver.switch_to.alert.accept()
        except NoSuchElementException:
            self.log.error("**** Element not found while Signing Up ****")
            return False
        else:
            self.log.info("Clicking on Sign Up alert box...")
            return alert

    def signup_outcome(self, name, password):
        """Check whether the successful sign up text is present
            if not it returns as False"""
        if self.sign_up(name, password) == "Sign up successful.":
            self.log.info("Sign up successful - New user created")
            return True
        self.log.error("**** Sign up UNSUCCESSFUL ****")
        return False

    def confirm_num_of_products_on_homepage(self, num):
        """Check that the number of products on the homepage is correct"""
        num_of_products = len(self.driver.find_elements(*self.product_list))
        if num_of_products == num:
            self.log.info("The correct number of products are displayed on the home page...")
            return True
        else:
            print(f"**** {num_of_products} displayed != to {num} needed ****")
            return False

    def click_on_products(self):
        product = random.choice(self.driver.find_elements(*self.product_list_a_tags))
        product.click()
        if self.home_page_url != self.driver.current_url:
            self.log.info("Clicked on product - Moving to product page...")
            return product
        else:
            self.log.error("**** Still on the homepage - Click UNSUCCESSFUL ****")
            return False
