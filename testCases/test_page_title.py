from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class Test_page_Title():


    def test_pageTitle(self, setup):
        self.driver = setup
        self.wait = WebDriverWait(self.driver, 10)

        print(self.driver.title)
        if self.driver.title == "Your store. Login":
            assert True
        else:
            assert False
        #self.driver.close()
