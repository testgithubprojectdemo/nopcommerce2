import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException as EC
from selenium.webdriver.support.wait import WebDriverWait
class Loginpage:
    Text_Email_XPATH=(By.XPATH,"//input[@id='Email']")
    Text_Password_XPATH=(By.XPATH,"//input[@id='Password']")
    Click_Login_Button_XPATH=(By.XPATH,"//button[@type='submit']")
    Click_Logout_Button_XPATH=(By.XPATH,"//a[normalize-space()='Logout']")

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def Enter_Email(self, email):
        self.driver.find_element(*Loginpage.Text_Email_XPATH).clear()
        self.driver.find_element(*Loginpage.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self,password):
        self.driver.find_element(*Loginpage.Text_Password_XPATH).clear()
        self.driver.find_element(*Loginpage.Text_Password_XPATH).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*Loginpage.Click_Login_Button_XPATH).click()


    def Click_Logout(self):
        self.driver.find_element(*Loginpage.Click_Logout_Button_XPATH).click()


    # def Login_Status(self):
    #     self.driver.implicitly_wait(10)
    #     try:
    #         self.driver.find_element(*loginpage.Click_Menu_Button_XPATH)
    #         return True
    #
    #     except EC:
    #         return False
