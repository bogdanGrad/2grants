from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
user_name = "xxx"
password = "xxxx"
driver = webdriver.Chrome()
driver.get("https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F")
element = driver.find_element_by_id("loginUsername")
element.send_keys(user_name)
element = driver.find_element_by_id("loginPassword")
element.send_keys(password)
element.send_keys(Keys.RETURN)
link=None
time.sleep(10)
while not link:
    time.sleep(3)
    try:
        link = driver.find_element_by_link_text("VIEW ALL")
    except:
        print("searching")
    print(link)
link.click()
#driver.close()
