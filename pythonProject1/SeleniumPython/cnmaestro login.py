from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

with driver as wd:
    wd.get("https://qa.cloud.cambiumnetworks.com/")
    wd.maximize_window()
    wd.implicitly_wait(10)
    WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@type='button']"))).click()
    wd.find_element(By.ID, 'cs-email').send_keys('ivt100@cambiumnetworks.com')
    wd.find_element(By.XPATH, "//button[@type='submit']").click()
    wd.find_element(By.ID, 'cs-password').send_keys('BAngalore@1234')
    wd.find_element(By.XPATH, "//button[@type='submit']").click()
    wd.find_element((By))

    # Wait for the search input to be present and visible before interacting with it
    search_input = WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='search']")))
    search_input.clear()  # Clear any existing text in the search input
    search_input.send_keys('26_OCT_USA_SRV3')

    # Click on the first result in the search
    import time
    time.sleep(2)
    element = WebDriverWait(wd, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'26_OCT_USA_SRV3')]")))
    ActionChains(wd).move_to_element(element).click().perform()
