import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from pageObjects.login_page import Loginpage

class Test_Login:
    def test_login(self,setup):
        self.driver=setup
        self.lp=Loginpage(self.driver)
        self.lp.Enter_Email("admin@yourstore.com")
        self.lp.Enter_Password("admin")
        self.lp.Click_Login()
        if self.driver.title=="Dashboard / nopCommerce administration":
            self.driver.save_screenshot("C:\\Users\\HP\PycharmProjects\\Nopcommerce\\Screenshots\\Test_Login-pass.png")
            self.lp.Click_Logout()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\HP\PycharmProjects\\Nopcommerce\\Screenshots\\Test_Login-fail.png")
            assert False
