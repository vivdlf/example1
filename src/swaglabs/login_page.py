from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Login:
    """
           A class used to represent the login.html page of the website SwagLabs.

           ...

           Attributes
           ----------
           driver :
               The driver is the object that connects to the browser
           username : str
                The username used to login.
           password : str
               The password corresponding to the username entered.
           error_msg: str
                The error message shown to the user when there is an invalid login.


           Methods
           -------
           login(self, uname, pwd)
               Attempts to log in with the credentials passed
    """
    def __init__(self, driver):
        """
        Parameters
        ----------
        driver :
            The driver is the object that connects to the browser
        """
        self.driver = driver
        self.username = driver.find_element(By.XPATH, "//input[@name='user-name']")
        self.password = driver.find_element(By.XPATH, "//input[@name='password']")
        self.error_message = ""

    def login(self, uname, pwd):
        """ Attempts to log in with the credentials passed.


                   Parameters
                   ----------
                   uname : str
                       The username used to login.
                   pwd : str
                      The password corresponding to the username entered.

        """
        # Login with arguments passed
        self.username.send_keys(uname)
        self.password.send_keys(pwd, Keys.ENTER)

        # Search for an error message if any
        try:
            return self.driver.find_element(By.XPATH,
                                            "//h3[text()='Epic sadface: Sorry, this user has been locked out.']")
        except:
            pass









