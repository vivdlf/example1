from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Login:
    def __init__(self, driver):
        # Variables that will be available throughout the class
        self.driver = driver
        self.username = driver.find_element(By.XPATH, "//input[@name='user-name']")
        self.password = driver.find_element(By.XPATH, "//input[@name='password']")
        self.error_message = ""

    def login(self, uname, pwd):
        # Login with arguments passed
        self.username.send_keys(uname)
        self.password.send_keys(pwd, Keys.ENTER)

        # Search for an error message if any
        try:
            return self.driver.find_element(By.XPATH,
                                            "//h3[text()='Epic sadface: Sorry, this user has been locked out.']")
        except:
            pass









