from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://demo.guru99.com/popup.php")

driver.maximize_window()

driver.find_element(By.XPATH,"//*[contains(@href,'popup.php')]").click()
time.sleep(3)

windows = driver.window_handles

for window in windows:
    driver.switch_to.window(window)
    time.sleep(3)
    try:
        driver.find_element(By.NAME,"emailid").send_keys("kapil@gmail.com")
        driver.find_element(By.NAME,"btnLogin").click()
    except Exception:
        pass
    time.sleep(3)
    driver.close()


driver.quit()