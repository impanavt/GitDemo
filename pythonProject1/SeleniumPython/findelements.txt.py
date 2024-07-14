from selenium import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
# import os
#
# current_directory = os.getcwd()
# print("Current working directory:", current_directory)

driver = webdriver.Chrome()

# driver.get("https://www.makemytrip.com/")
# driver.find_element_by_id("fromCity").click()
# driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
# time.sleep(2)
# cities =driver.find_elements_by_css_selector("p[class*='blackText']")
# print (len(cities))
# for city in cities:
#     if city.text =="Del Rio, United States":
#         city.click()
#         break
#
#
# driver.find_element_by_xpath("//p[text()='Delhi, India']").click()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")