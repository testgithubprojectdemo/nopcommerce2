import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/")
    yield driver
    driver.quit()
