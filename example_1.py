import sys
sys.path.append(".")

import time
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://the-internet.herokuapp.com/login')

txt_username = browser.find_element_by_id('username')
txt_username.send_keys('tomsmith')


txt_password = browser.find_element_by_id('password')
txt_password.send_keys('SuperSecretPassword!')

btn_login = browser.find_element_by_xpath('//button[contains(text(), Login)]')
btn_login.click()

lbl_success = browser.find_element_by_id('flash')
message = lbl_success.text
print (message)

assert 'You logged into a secure area!' in message

time.sleep(5)

browser.quit()
