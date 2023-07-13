#Changed to show git commit and push
from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://demo.guru99.com/popup.php")

driver.maximize_window()

driver.get("http://demo.guru99.com/test/delete_customer.php")

driver.find_element(By.NAME,"cusid").send_keys("53920")

driver.find_element(By.NAME,"submit").submit()

alert = driver.switch_to.alert
time.sleep(3)
alert_message = alert.text

print("ALERT TEXT = ", alert_message)

alert.accept()
time.sleep(3)

driver.quit()