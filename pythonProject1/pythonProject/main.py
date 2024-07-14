# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome('.chromedriver.exe')
with driver as wd:
    wd.maximize_window()
    wd.get('https://qa.cloud.cambiumnetworks.com/')
    wd.implicitly_wait(10)
    WebDriverWait(wd, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(text(),'Sign In')]"))).click()
    wd.find_element(By.ID,'cs-email').send_keys('ctaf@cambiumnetworks.com')
    wd.find_element(By.XPATH, "//button[@type='submit']").click()
    wd.find_element(By.ID, 'cs-password').send_keys('Cnauto@246')
    wd.find_element(By.XPATH, "//button[@type='submit']").click()
    a = WebDriverWait(wd, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//a[@title='Cambium Networks | cnMaestro™']//span"))).text

    print(a)
