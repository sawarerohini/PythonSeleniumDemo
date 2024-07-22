from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def test_abc():
    # Initialize Firefox WebDriver
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


    driver.get("https://www.facebook.com/campaign/landing.php?campaign_id=14884913640&extra_1=s%7Cc%7C589460569891%7Cb%7Cfacebook%20signin%7C&placement=&creative=589460569891&keyword=facebook%20signin&partner_id=googlesem&extra_2=campaignid%3D14884913640%26adgroupid%3D128696221832%26matchtype%3Db%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-3821998899%26loc_physical_ms%3D9040229%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=CjwKCAjwpuajBhBpEiwA_ZtfhYOUN3f61gMqn-EWjxqcm0EEcR2GmAWBTRGX-bDq7k4oaBlGhrzzIRoCjlUQAvD_BwE")
    driver.maximize_window()
    driver.find_element(By.NAME,"firstname").clear()
    driver.find_element(By.NAME, "firstname").send_keys("saware")
    time.sleep(2)

    driver.find_element(By.NAME,"lastname").clear()
    driver.find_element(By.NAME,"lastname").send_keys("rohini")
    time.sleep(3)

    driver.find_element(By.NAME,"reg_email__").clear()
    driver.find_element(By.NAME,"reg_email__").send_keys("8087914589")
    time.sleep(3)

    driver.find_element(By.NAME,"reg_passwd__").clear()
    driver.find_element(By.NAME,"reg_passwd__").send_keys("Rohi123")
    time.sleep(2)

    DOBD = Select(driver.find_element(By.ID, "day"))
    DOBD.select_by_visible_text("22")

    DOBM = Select(driver.find_element(By.ID, "month"))
    DOBM.select_by_value("8")
    time.sleep(3)

    DOBY = Select(driver.find_element(By.ID, "year"))
    DOBY.select_by_visible_text("2001")
    time.sleep(2)

    time.sleep(2)
    redio1 = driver.find_element(By.NAME,"sex")
    redio1.click()
    time.sleep(3)

    driver.quit()







