from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class ProductPage:
    """
        A class used to represent the inventory.html page of the website SwagLabs.

        ...

        Attributes
        ----------
        driver :
            The driver is the object that connects to the browser
        title : str
            the title of the inventory page found in the top left corner of the page
        total_items : str
            the total number of items in the cart

        Methods
        -------
        get_title(self)
            Returns the title found on the inventory page
        create_xpath(self, name)
            Creates a xpath locator of the given argument.
        add_to_cart(self, product)
            Adds the arguments passed to the cart.
        get_total_items(self)
            Returns the total number of items in the cart.
        go_to_cart_page(self)
            Redirects the user the cart page.
    """
    def __init__(self, driver):
        """
        Parameters
        ----------
        driver :
            The driver is the object that connects to the browser
        """
        self.driver = driver
        self.title = driver.find_element(By.XPATH, "//span[@class='title']")
        self.total_items = ''

    def get_title(self):
        """Returns the title found on the inventory page"""
        # Return 'PRODUCTS' title found on the inventory.html
        return self.title

    def create_xpath(self, name):
        """Creates a xpath locator of the given argument.


              Parameters
              ----------
              name : str
                  The name of the object from which the xpath locator will be created from
        """
        # Create the xpath for each product using the name locator
        split_name = name.lower().split()
        name_xpath = "//button[@name='add-to-cart-"
        for character in split_name:
            name_xpath += character + '-'

        name_xpath = name_xpath[0:len(name_xpath) - 1]
        name_xpath += "']"

        return name_xpath

    def add_to_cart(self, product):
        """Adds the arguments passed to the cart.


              Parameters
              ----------
              product : str or list
                  The product name(s) that will be added to the cart
        """
        # Add items to cart - individual items or a list of items
        for item in product:
            self.driver.find_element(By.XPATH, self.create_xpath(item)).send_keys(Keys.ENTER)

        self.total_items = self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")

    def get_total_items(self):
        """Returns the total number of items in the cart."""
        # Return the total amount of items within the cart
        return self.total_items

    def go_to_cart_page(self):
        """Redirects the user the cart page."""
        # Redirect to the cart page
        return self.driver.get('https://www.saucedemo.com/cart.html')