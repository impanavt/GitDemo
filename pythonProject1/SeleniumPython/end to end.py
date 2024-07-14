from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
# cleck on shop icon
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
# common xpath for all products
products=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    # to derive the name of product
    productName=product.find_element(By.XPATH,"div/h4/a").text
    if productName=="Blackberry":
        product.find_element(By.XPATH,"div/button").click()
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"a[class*='btn-primary']")))
driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id('country').send_keys("ind")
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'India')))
driver.find_element_by_link_text('India').click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
successText=driver.find_element_by_class_name('alert-success').text
assert "Thank you!"in successText