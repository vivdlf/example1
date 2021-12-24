# Standard libs
import pdb
import time

# Third Party Libs
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Local libs


class TestStandardUser:

    def test_that_standard_user_can_log_in_successfully(self, driver):
        """ Verify Successful Login Functionality

        Given:
          - That the user has navigated to the login page (url: https://www.saucedemo.com/)
        When:
          - The user successfully logs in to an account.
        Expected:
          - The user should be taken to the inventory page (url:
            https://www.saucedemo.com/inventory.html)
          - The user should be presented with a page header at the upper left corner of the page
            that matches the following text: “PRODUCTS”.
        Note:
          - This test should be conducted with the following user accounts:
          - username: standard_user, passwd: secret_sauce
          - Username: performance_glitch_user, passwd: secret_sauce
        """
        username = "standard_user"
        password = "secret_sauce"

        driver.find_element(By.XPATH, "//input[@name='user-name']").send_keys(username)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)

        driver.find_element(By.XPATH, "//input[@type='submit' and @id='login-button']").send_keys(Keys.ENTER)

        element = driver.find_element(By.XPATH, "//span[@class='title']")
        assert element.text == 'PRODUCTS'
        time.sleep(5)
