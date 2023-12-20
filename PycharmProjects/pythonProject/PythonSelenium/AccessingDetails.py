import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/angularpractice/')

driver.find_element(By.NAME, 'email').send_keys('test@gmail.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123456')
driver.find_element(By.ID, 'exampleCheck1').click()
driver.find_element(By.CLASS_NAME, 'btn-success').click()
#driver.find_element(By.XPATH, "//input[@type='submit']").click()  #if we want to use xpath for loocator Syntax: tagname[@attribute=’value’]
driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()
message = driver.find_element(By.CLASS_NAME, 'alert ').text
print(message)
time.sleep(5)
assert 'Success' in message  #if we want to know that is the correct message
driver.close()
