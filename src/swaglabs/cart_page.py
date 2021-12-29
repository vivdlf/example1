from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        # Variables that will be available throughout the class
        self.driver = driver

    def create_xpath(self, name):
        # Create the xpath for each product using the tag name locator
        return f"//div[text()='" + name + "']"

    def verify_products_presence(self, product):
        # Verify the presence of a product(s) in the cart
        for item in product:
            try:
                self.driver.find_element(By.XPATH, self.create_xpath(item))
                return True
            except:
                return False
        return True


