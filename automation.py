from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('#url)

time.sleep(2)

LastName = "Berry"
last = web.find_element_by_xpath('#element)
last.send_keys(LastName)

