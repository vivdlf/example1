# Third Party Libs
import pytest
from .login_page import Login
from .product_page import ProductPage
from .cart_page import CartPage


class TestStandardUser:

    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce"),
                                                   ("performance_glitch_user", "secret_sauce")])
    def test_that_standard_user_can_log_in_successfully(self, driver, username, password):
        # User logs in
        login_page = Login(driver)
        login_page.login(username, password)

        # Verify login - check for product title
        product_page = ProductPage(driver)
        element = product_page.get_title()
        assert element.text == 'PRODUCTS'

    @pytest.mark.parametrize("username,password", [("locked_out_user", "secret_sauce")])
    def test_locked_out_user_functionality(self, driver, username, password):
        # User logs in
        login_page = Login(driver)

        # Verify login - check for error message
        element = login_page.login(username, password)
        assert element.text == 'Epic sadface: Sorry, this user has been locked out.'

    @pytest.mark.parametrize("username,password", [("performance_glitch_user", "secret_sauce")])
    def test_cart_incrementation(self, driver, username, password):
        # User logs in
        login_page = Login(driver)
        login_page.login(username, password)

        # User clicks 'ADD TO CART'
        product_page = ProductPage(driver)
        product_list = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt"]
        product_page.add_to_cart(product_list)

        # After the user has clicked 'ADD TO CART' the cart number should've increased
        element = product_page.get_total_items()
        temp = element.text
        assert temp.isdigit()

        # The user clicks add cart once more, the number should increase
        product_list = ["Sauce Labs Onesie"]
        product_page.add_to_cart(product_list)
        assert element.text == str(int(temp) + 1)

    @pytest.mark.parametrize("username,password",
                             [("standard_user", "secret_sauce"), ("performance_glitch_user", "secret_sauce")])
    def test_item_added_to_cart(self, driver, username, password):
        # User logs in
        login_page = Login(driver)
        login_page.login(username, password)

        # User clicks 'ADD TO CART'
        product_page = ProductPage(driver)
        product_list = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Test.allTheThings() T-Shirt (Red)",
                        "Sauce Labs Fleece Jacket", "Sauce Labs Bolt T-Shirt"]
        product_page.add_to_cart(product_list)

        # Navigate to cart page
        product_page.go_to_cart_page()

        # Verify the presence of the product
        cart_page = CartPage(driver)
        assert cart_page.verify_products_presence(product_list)






