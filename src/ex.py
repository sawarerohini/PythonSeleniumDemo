import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


test_data = [["user1", "pass1"],
             ["user2", "pass2"],
             ["user3", "pass3"],
             ["user4", "pass4"],
             ["user5", "pass5"],
             ["user6", "pass6"],
             ]


@pytest.mark.parametrize("username, password", test_data)
def test_login(username, password):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.NAME,"username").clear()
    driver.find_element(By.NAME,"username").send_keys(username)
    driver.find_element(By.NAME,"password").clear()
    driver.find_element(By.NAME,"password").send_keys(password)
    time.sleep(3)
    # If username and password are correct
    # user lands on homepage
    driver.quit()



