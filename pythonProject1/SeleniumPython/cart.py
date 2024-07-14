from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Assuming you've initialized your WebDriver instance as `driver`
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
# Wait for results to load
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='products']/div")))

results_list = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results_list)
assert count > 0

for result in results_list:
    # Wait for the button to be clickable
    button = WebDriverWait(result, 10).until(EC.element_to_be_clickable((By.XPATH, "div/button")))
    button.click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Wait for input field to be visible and interactable
input_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='text']")))
input_field.send_keys("rahulshettyacademy")

# Wait for prices to load
prices = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//tr/td[5]/p")))
total_sum = 0
for price in prices:
    total_sum += int(price.text)

print("Sum of prices:", total_sum)

# Verify total amount
total_amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert total_sum == total_amount

# Navigate back to the main page
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")