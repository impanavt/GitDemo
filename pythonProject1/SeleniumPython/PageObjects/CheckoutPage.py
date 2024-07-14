from selenium.webdriver.common.by import By
from PageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver
    # locator value
    # driver.find_element(By.CSS_SELECTOR,".card-title a")
    # driver.find_element(By.CSS_SELECTOR,".card-footer button")
    # driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter=(By.CSS_SELECTOR,".card-footer button")
    checkout=(By.XPATH,"//button[@class='btn btn-success']")

    def getcardTitles(self):
        # locator strategy
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getcardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutItems(self):
         return self.driver.find_element(*CheckOutPage.checkout)
#     creating object for my naext class confirm page
#          confirmPage=ConfirmPage(self.driver)
#          return confirmPage

