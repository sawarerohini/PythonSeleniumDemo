from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://www.facebook.com/" )

try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "websubmit")))
    element.click()
except Exception as msg:
    print("massage = ",msg)
    print(f"massage ={msg}")

driver.quit()