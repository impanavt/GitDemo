from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver_win32\chromedriver_win32(1)\chromedriver")

driver.get("http://demo.automationtesting.in/Index.html")
print(driver.title)
print(driver.current_url)
driver.get("http://newtours.demoaut.com/")
time.sleep(5)
print(driver.title)
driver.back()
time.sleep(5)
print(driver.title)
driver.forward()

 #driver.find_element_by_xpath("//*[@id='btn1']").click()

time.sleep(5)




