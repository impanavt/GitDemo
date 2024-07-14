# Wait for the "ChatGPT by OpenAI" heading to be visible
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Open the website
with driver as wd:
    wd.get("https://chat.openai.com/")



WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[@aria-label='ChatGPT by OpenAI']")))

# Click the "Log in" link
wd.find_element(By.PARTIAL_LINK_TEXT, "Log in").click()

# Enter the username
wd.find_element(By.ID, "username").send_keys("impana.vt@cambiumnetworks.com")

# Click the submit button
wd.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()

# Wait for the password field to be visible
WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.ID, "password")))

# Enter the password
wd.find_element(By.ID, "password").send_keys("Thopes@15")

# Click the submit button to log in
wd.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()

