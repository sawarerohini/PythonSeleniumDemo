from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://demo.guru99.com/test/newtours/register.php")

drpCountry = Select(driver.find_element(By.NAME,"country"))

drpCountry.select_by_visible_text("ANTARCTICA")
time.sleep(2)
drpCountry.select_by_index(3)
time.sleep(2)
drpCountry.select_by_value("ALBANIA")
driver.save_screenshot("my_screenshot.png")
time.sleep(3)
drpCountry.select_by_index(0)
# Selecting Items in a multiple select elements

driver.get("http://jsbin.com/osebed/2")

fruits = Select(driver.find_element(By.ID,"fruits"))

assert fruits.is_multiple

fruits.select_by_visible_text("Banana")
time.sleep(2)
fruits.deselect_by_visible_text("Banana")
time.sleep(2)
fruits.deselect_by_visible_text("Apple")
time.sleep(2)
fruits.select_by_index(1)
time.sleep(2)
fruits.select_by_index(3)
time.sleep(2)
driver.quit()

