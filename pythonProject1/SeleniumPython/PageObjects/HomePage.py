from selenium.webdriver.common.by import By
from selenium import webdriver

from PageObjects.CheckoutPage import CheckOutPage

# if it's instance variables call with self . if it's class variable call with howepage
class HomePage:

    # to pass driver from main test_e2e file to here call a constructor actual driver is passed to local class driver
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name=(By.CSS_SELECTOR,"[name='name']")
    email=(By.NAME,'email')
    check=(By.ID,"exampleCheck1")
    gender=(By.ID,"exampleFormControlSelect1")
    submit=(By.XPATH,"//input[@type='submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        return  self.driver.find_element(*HomePage.shop)
        # return checkOutPage = CheckOutPage(self.driver)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)


