from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\Samita\Downloads\chromedriver")
driver.get("https://www.seleniumhg.org or http://www.selenium.dev")
driver.get("http://en.wik")

driver.find_element(By.LINK_TEXT, value= "Create account").click()


time.sleep(2)
print("Current URL = ", driver.current_url)
driver.back()
driver.find_element(By.LINK_TEXT, value="selenium.dev").click()
print("Current URL = ", driver.current_url)
driver.quit()
