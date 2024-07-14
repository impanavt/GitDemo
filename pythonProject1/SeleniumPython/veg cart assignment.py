import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
expectedList= ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actualList= []
driver = webdriver.Chrome()
driver.implicitly_wait(2)

# wait until 5 seconds if object is not displayed
#Global wait
#1.5 second to reach next page- execution will resume in 1.5 seconds
#if object do not show up at all, then max time your test waits for 5 seconds
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
results_list=driver.find_elements_by_xpath("//div[@class='products']/div")
count=len(results_list)
assert count == 3
for result in results_list:
    actualList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()
assert expectedList == actualList,f"Expected: {expectedList}, Actual: {actualList}"
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

# for button in buttons:
#     button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
prices=driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum=0
for price in prices:
    sum=sum+int(price.text)
print(sum)
totalamount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum==totalamount
driver.find_element_by_css_selector(".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
discountedamount=float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert totalamount>discountedamount


