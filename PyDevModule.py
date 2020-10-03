from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 
user_name = "xxxx"
password = "xasdasda"
driver = webdriver.Chrome()
driver.get("https://granturi.imm.gov.ro/auth/login")

print("STARTING CREDENTIALS")
#login
element = driver.find_element_by_id("mat-input-0")
element.send_keys(user_name)
element = driver.find_element_by_id("mat-input-1")
element.send_keys(password)

# button.is_enabled()

# print("CHECKING ELEMENT TO BE CLICKABLE")
# element = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Autentifică-te')))

# print("CLiCKING ON ELEMENT")
# element.click()


print("CLICKING ON ELEMENT")
# button1 = driver.find_element_by_name('LOG IN')
# print("1",button1.is_enabled())
# button2 = driver.find_element_by_link_text('LOG IN')
# print("2",button2.is_enabled())
# button3 = driver.find_element_by_class_name('submit-button ng-tns-c65-1 mat-raised-button mat-button-base mat-accent')
# print("3",button3.is_enabled())
# button4 = driver.find_element_by_xpath('//button[contains(text(), "LOG IN")]')
# print("4",button4.is_enabled())
# button5 = driver.find_element_by_xpath('//button[contains(text(), "Autentifică-te")]')
# print("5",button5.is_enabled())

# button3 = driver.find_element_by_xpath("//input[@type='submit' and @value='LOG IN']")
# print("3",button3.is_enabled())
button4 = driver.find_element_by_css_selector(".submit-button")
print("4",button4.is_enabled())


# print(button.is_enabled())

# while not button.is_enabled():
#     time.sleep(5)
#     print('sleep')
#     button = driver.find_element_by_partial_link_text('Autentifică-te')

# print('button is enabled')
# button.click()
# element.send_keys(Keys.RETURN)

# topAlerts = driver.find_element_by_xpath("//*[contains(text(), 'Top Alerts')]") 
