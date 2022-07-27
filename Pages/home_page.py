from Base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *



class HomePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    signup_btn = (By.XPATH, "//a[@id='signin2']")
    username_field = (By.XPATH, "//input[@id='sign-username']")
    password_field = (By.XPATH, "//input[@id='sign-password']")
    signup_btn_popup = (By.XPATH, "//button[contains(text(),'Sign up')]")

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
            print("Element not found")
            return False
        else:
            print("Sign up actions completed")
            return alert


    def signup_outcome(self, name, password):
        if self.sign_up(name, password) == "Sign up successful.":
            print("Sign up successful - New user created")
            return True
        print("**** Sign up UNSUCCESSFUL ****")
        return False







