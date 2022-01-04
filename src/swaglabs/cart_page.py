from selenium.webdriver.common.by import By


class CartPage:
    """
            A class used to represent the cart.html page of the website SwagLabs.

            ...

            Attributes
            ----------
            driver :
                The driver is the object that connects to the browser

            Methods
            -------
            create_xpath(self, name)
                Creates a xpath locator of the given argument.
            verify_products_presence(self, product)
                Verifies if the arguments passed exist within the page.
    """
    def __init__(self, driver):
        """
        Parameters
        ----------
        driver :
            The driver is the object that connects to the browser
        """
        self.driver = driver

    def create_xpath(self, name):
        """Creates a xpath locator of the given argument.


               Parameters
               ----------
                name : str
                     The name of the object from which the xpath locator will be created from

        """
        # Create the xpath for each product using the tag name locator
        return f"//div[text()='{name}']"

    def verify_products_presence(self, product):
        """Verifies if the arguments passed exist within the page.


               Parameters
               ----------
               product : str or list
                   The product name(s) that will be added to the cart

        """
        for item in product:
            try:
                self.driver.find_element(By.XPATH, self.create_xpath(item))
            except:
                return False
        return True


