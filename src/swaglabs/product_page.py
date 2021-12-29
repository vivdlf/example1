from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ProductPage:
    def __init__(self, driver):
        # Variables that will be available throughout the class
        self.driver = driver
        self.title = driver.find_element(By.XPATH, "//span[@class='title']")
        self.total_items = ''

    def get_title(self):
        # Return 'PRODUCTS' title found on the inventory.html
        return self.title

    def create_xpath(self, name):
        # Create the xpath for each product using the name locator
        split_name = name.lower().split()
        name_xpath = "//button[@name='add-to-cart-"
        for character in split_name:
            name_xpath += character + '-'

        name_xpath = name_xpath[0:len(name_xpath) - 1]
        name_xpath += "']"

        return name_xpath

    def add_to_cart(self, product):
        # Add items to cart - individual items or a list of items
        for item in product:
            self.driver.find_element(By.XPATH, self.create_xpath(item)).send_keys(Keys.ENTER)

        self.total_items = self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")

    def get_total_items(self):
        # Return the total amount of items within the cart
        return self.total_items

    def go_to_cart_page(self):
        # Redirect to the cart page
        return self.driver.get('https://www.saucedemo.com/cart.html')