# import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
 
# Informations d'identification de compte TikTok
username = "youtubevid.ontiktok"
password = "JrF6RcEbdNdMBKf&"

# this upload needs an open firefix browser connected to tiktok
# luanch CMD > "C:\Program Files\Mozilla Firefox\firefox.exe" --marionette

# create webdriver object
firefox_services = Service(executable_path='firefoxdriver', port=3000, service_args=['--marionette-port', '2828', '--connect-existing'])
driver = webdriver.Firefox(service=firefox_services)

"""
driver.get("https://www.tiktok.com/login/phone-or-email/email")
driver.implicitly_wait(10)
input_name = driver.find_element(By.NAME,"username")
input_name.send_keys(username)
input_pwd = driver.find_element(By.CSS_SELECTOR,"input[type='password']")
input_pwd.send_keys(password)
driver.implicitly_wait(5)
button = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
button.click()
"""
# fileuploader_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.file-select-button")))
try:
    driver.get("https://www.tiktok.com/upload?lang=fr")
    driver.implicitly_wait(10)

    iframe = driver.find_element(By.CSS_SELECTOR, "iframe")

    # switch to selected iframe
    driver.switch_to.frame(iframe)

    vid_title = driver.find_element(By.CSS_SELECTOR,"div[contenteditable='true']")
    vid_title.send_keys("part1")

    fileinput = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
    fileinput.send_keys("c:\dev\\tmp\smalltiktok.mp4")

    time.sleep(45)

    button_publish = driver.find_element(By.CSS_SELECTOR, ".btn-post button")
    button_publish.click()
   
except Exception as e:
    print(str(e))
    driver.quit()

