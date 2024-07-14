from selenium import webdriver
BrowserSortedVeggie=[]
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-error")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# click on browser header
driver.find_element_by_xpath("//span[text()='Veg/fruit name']").click()
vegElements=driver.find_elements_by_xpath("//tr/td[1]")
# clllect all veggie names- browserveggielist(A,B,C)
for ele in vegElements:
    # assert the vegetables bname one by one to this browser list so text is used
    BrowserSortedVeggie.append(ele.text)
#     sort thos browservefggie list-==>new sorted lsit(A,B,C)
originalBrowserSortedList=BrowserSortedVeggie.copy()
BrowserSortedVeggie.sort()
# compare brwoser sorted list with newsorted lsit
assert BrowserSortedVeggie==originalBrowserSortedList

