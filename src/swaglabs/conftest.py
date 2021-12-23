# Standard libs

# Third Party Libs
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

# Local libs


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    yield driver
    driver.close()
