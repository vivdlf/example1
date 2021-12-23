# Standard libs
import pdb

# Third Party Libs
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

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
        pass
