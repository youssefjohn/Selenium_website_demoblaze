from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        """Scrolls the entire length of the page to make sure all elements have loaded"""
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(2)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            if lastCount == pageLength:
                match = True
        time.sleep(4)

    def random_word_generator(self, num=11):
        """Returns a random string - default to length of 11 characters"""
        word = ''.join(random.choice(string.ascii_letters) for _ in range(num))
        return word

    def wait_for_presence_of_element(self, locator_type, locator):
        """Generates an explicit wait for an elements presence - Returns element once found"""
        wait = WebDriverWait(driver=self.driver, timeout=60, poll_frequency=2)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return element
