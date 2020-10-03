from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import configparser
import sys

def get_config_data():

	config = configparser.RawConfigParser()
	config.read('config.properties')

	user_name = config.get('Credentials', 'user')
	password = config.get('Credentials', 'password')
	site_url = config.get('Credentials', 'site_url')

	return user_name, password, site_url


user_name, password, site_url = get_config_data()

driver  = webdriver.Chrome()
driver.maximize_window()
driver.get(site_url)

print("STARTING CREDENTIALS")
#login
element = driver.find_element_by_id("mat-input-0")
element.send_keys(user_name)
element = driver.find_element_by_id("mat-input-1")
element.send_keys(password)

print("CLICKING ON ELEMENT")

login = driver.find_element_by_css_selector(".submit-button")
print("button",login.is_enabled())
while not login.is_enabled():
    time.sleep(2)
    print('sleep')
    login = driver.find_element_by_css_selector(".submit-button")
print('button is enabled',login.is_enabled())
time.sleep(1)
login.click()


depunere = None
depunere = driver.find_element_by_css_selector(".nav-link-title")

if not depunere:
	depunere = driver.find_element_by_link_text("Depunere")

if not depunere:
	print("SUCK A DICK")
	sys.exit(1)

time.sleep(1)
depunere.click()

alegere = driver.find_element_by_link_text("alege")

if not alege:
	print("SUCK A SECOND DICK")
	sys.exit(1)

time.sleep(1)
alegere.click()

firma = driver.find_element_by_name("legalEntitySelection")

if not firma:
	print("SUCK A THIRD DICK")
	sys.exit(1)

time.sleep(1)
firma.send_keys("BEST EQUIPMENT TECHNOLOGY S.R.L.")

submit_firma = driver.find_element_by_css_selector("mat-raised-button")

if not submit_firma:
	print("SUCK A FORTH DICK")
	sys.exit(1)

submit_firma.click()











