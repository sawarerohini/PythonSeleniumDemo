from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\Samita\Downloads\chromedriver")   # also use // to remove yellow line

driver.get("http://www.seleniumframework.com/demo-sites/")

driver.refresh()

time.sleep(2)

driver.find_element(By.XPATH, value="//a[@href='http://www.seleniumframework.com/introduction/']").click()

time.sleep(2)

driver.find_element(By.LINK_TEXT, value="SELENIUM").click()

time.sleep(2)

driver.back()

time.sleep(2)

driver.forward()

time.sleep(2)







driver.quit()
