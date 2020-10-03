from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import configparser

config = configparser.RawConfigParser()
config.read('config.properties')

user_name = config.get('Credentials', 'user')
password = config.get('Credentials', 'password')
site_url = config.get('Credentials', 'site_url')
driver = webdriver.Chrome()
driver.get(site_url)

print("STARTING CREDENTIALS")
#login
element = driver.find_element_by_id("mat-input-0")
element.send_keys(user_name)
element = driver.find_element_by_id("mat-input-1")
element.send_keys(password)

print("CLICKING ON ELEMENT")

button = driver.find_element_by_css_selector(".submit-button")
print("button",button.is_enabled())
while not button.is_enabled():
    time.sleep(2)
    print('sleep')
    button4 = driver.find_element_by_css_selector(".submit-button")
print('button is enabled',button4.is_enabled())
time.sleep(1)
button.click()
