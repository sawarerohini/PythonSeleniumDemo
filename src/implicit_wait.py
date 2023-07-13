from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.implicitly_wait(2)
driver.get("https://www.facebook.com/" )
driver.find_element(By.NAME,"websumit").click()
time.sleep(3)

driver.quit()