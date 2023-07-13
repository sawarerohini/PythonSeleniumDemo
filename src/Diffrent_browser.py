from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options


browser = " "

if browser.lower() == "chrome":
    driver = webdriver.Chrome(executable_path=r"C:\Users\Samita\Downloads\chromedriver")
elif browser.lower() == "safari":
    driver = webdriver.Safari()
else:
    options=Options()
    options.binary_location=r"C:\Program Files\Mozilla Firefox\firefox.exe"
    driver = webdriver.Firefox(executable_path=r"c:\Users\samita\Desktop\geckodriver",options=options)

driver.get("http://www.seleniumframework.com/demo-sites/")

print("Page Title = ", driver.title)
print("Current URL = ", driver.current_url)
print("Page Source = ", driver.page_source)

time.sleep(5)

driver.quit()