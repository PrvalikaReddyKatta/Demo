from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get('https://www.facebook.com/')
print(driver.title)   #if you want to know about the tab title
print(driver.current_url)  #To know the landing on the correct URL or Not
driver.get('https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0') #Access to another part
driver.back()
driver.refresh()
driver.forward()
driver.close()