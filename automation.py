from selenium import webdriver
# from .edge.webdriver import WebDriver as ChromiumEdge
import time

web = webdriver.Chrome()
web.get('http://192.168.0.253/webpages/login.html')

time.sleep(2)

LastName = "Berry"
last = web.find_element_by_xpath('//*[@id="form-login"]/div[2]/div/div/div[1]/span[2]/input[1]')
last.send_keys(LastName)

