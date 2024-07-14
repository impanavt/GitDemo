
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
with driver as wd:
    try:
      wd.get("https://www.instagram.com/")
      wd.maximize_window()
      user_field=WebDriverWait(wd, 10, ).until(EC.presence_of_element_located((By.XPATH,"//input[@aria-label='Phone number, username, or email']")))
      user_field.send_keys("impanavt1999@gmail.com")
      wd.find_element(By.XPATH,"//input[@aria-label='Password']").send_keys("Rajalakshmi")
      wd.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button").click()
      WebDriverWait(wd, 10).until(
             EC.presence_of_element_located((By.XPATH,"//button[@type='button']")))

      print("Login successful!")
         # Rest of your automation code goes here...
    except Exception as e:
        print(f"Login failed")
    finally:
        # Close the browser window
        driver.quit()