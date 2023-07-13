from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"/C:\Users\Samita\Downloads\chromedriver")

driver.get("http://www.seleniumframework.com/demo-sites/")

print("Page Title = ", driver.title)
print("Current URL = ", driver.current_url)
print("Page Source = ", driver.page_source)



driver.quit()

