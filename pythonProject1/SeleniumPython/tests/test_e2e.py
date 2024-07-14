from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass

from PageObjects.HomePage import HomePage
from PageObjects.CheckoutPage import CheckOutPage
import time
import pytest

import logging



log = logging.info('msg')


class TestOne(BaseClass):
    # @pytest.mark.usefixtures("setup")inheriting setup from parent class by using fixture baseclass

    def test_e2e(self, setup):
        # remove one locater and handle the below using PageObjects

        log=self.getLogger()
        self.driver = setup
        homepage = HomePage(self.driver)

        # setup.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
        # self.driver = setup
        # print("running case test_e2e")
        homepage.shopItems().click()
        # to skip object creation for next class
        checkoutpage=CheckOutPage(self.driver)
        log.info("getting all  card details")
        cards = checkoutpage.getcardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            # print(cardText)
            if cardText == "Blackberry":
                # to accesss calss variables inside test case method use self .way to pass from fixtures to test class
                # The purpose of using i in this context is to interact with each button element found by the CSS selector .card-footer button individually, presumably performing some action such as clicking on them.
                checkoutpage.getcardFooter()[i].click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        checkoutpage.checkOutItems().click()

        log.info("Entering country name as ind")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        # time.sleep(5)
        # self.verifyLinkPresence("India")
        # element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        log.info("Text received from application is " + textMatch)

        assert ("Success! Thaffnk you!" in textMatch)
