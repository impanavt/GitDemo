import pytest
from selenium import webdriver

from selenium.webdriver.support.select import Select

import HomePageData
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
import logging



class TestHomePage(BaseClass):

    def test_formSubmission(self,setup,getData):
        self.driver = setup
        log=self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is"+getData["firstname"])

        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        checkbox_element=homepage.getCheckBox()
        checkbox_element.click()
        self.selectOptionByText(homepage.getGender(),getData["gender"])
        submit_form=homepage.getSubmitForm()
        submit_form.click()
        alertText=homepage.getSuccessMessage().text

        # driver.find_element_by_name("name").send_keys("Rahul")
        # driver.find_element_by_css_selector("input[name='name']").send_keys("Rahul")
        # driver.find_element_by_name("email").send_keys("Shetty")
        #
        # driver.find_element(By.ID, "exampleCheck1")

        # select class provide the methods to handle the options in dropdown
        # dropdown = Select(driver.find_element_by_id("exampleFormContrSelect1"))
        # dropdown.select_by_visible_text("Female")
        # dropdown.select_by_index(1)
        # driver.find_element_by_name("bday").send_keys("15/12/1999")
        #
        # driver.find_element_by_xpath("//input[@type='submit']").click()
        #
        # message = driver.find_element_by_class_name("alert-success").text

        assert ("success" in alertText)
        # for refreshing browser after each test case execution
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.HomePageData.test_homepagedata)
    # send data to get Data fixture at run time
    def getData(self,request):
        return request.param
