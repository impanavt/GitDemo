import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions
expectedList= ['Cucumber-1Kg','Raspberry-1/4Kg','Strawberry-1/4Kg']
actualList= []
# name='impanagowda'

driver = webdriver.Chrome()
driver.implicitly_wait(2)

# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/")  #get method to hit url on  browser
#
# print(driver.title)
# print(driver.current_url)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.minimize_window()
# driver.back()
# driver.refresh()
# driver.close()

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




# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# radioButton=driver.find_elements(By.CSS_SELECTOR,".radioButton")
# radioButton[2].click()
# assert radioButton[2].is_selected()
# assert driver.find_element(By.ID,"displayed-text").is_displayed()
# driver.find_element(By.CSS_SELECTOR,'#name').send_keys(name)
# driver.find_element(By.ID,'alertbtn').click()
# alert=driver.switch_to.alert
# alertText=alert.text
# print(alertText)
# assert name in alertText
# alert.accept()
#
#
# driver.find_element(By.ID,"hide-textbox").click()
# checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# for checkbox in checkboxes:
#     if checkbox.get_attribute("value")=='option2':
#         checkbox.click()
#         assert checkbox.is_selected()
#         break
# globally waiting for 5 sec until elements get located
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR,"input.search-keyword").send_keys("ber")
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='products']/div")))

results_list=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(results_list)
assert count>0
for result in results_list:
    actualList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()
assert expectedList == actualList,f"Expected: {expectedList}, Actual: {actualList}"

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
prices=driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum=0
for price in prices:
    sum=sum+int(price.text)
print(sum)
totalamount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum==totalamount




driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait=WebdriverWait(driver,10)
wait.until(expected_conditions.presenece_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
discountedamount=int(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert totalamount>discountedamount