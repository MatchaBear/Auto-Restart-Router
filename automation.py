from selenium import webdriver
# from .edge.webdriver import WebDriver as ChromiumEdge
import time

time.sleep(3)
web = webdriver.Chrome()
web.get('http://192.168.0.253/webpages/login.html')

time.sleep(2)

PassForm = "admin"
# last = web.find_element((By.XPATH,"//*[@id="form-login"]/div[2]/div/div/div[1]/span[2]/input[1]"))
last = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/form[3]/div[2]/div/div/div[1]/span[2]/input[1]')

last.send_keys(PassForm)

Submit = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/form[3]/div[3]/div/div/div/div[1]/button')
# Submit = web.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/a[4]')
Submit.click()
# //*[@id="top-control-reboot"]
#
time.sleep(4)

# Submit2 = web.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/a[4]/span[1]')
Submit2 = web.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/a[4]')
Submit2.click()

time.sleep(2)

Submit3 = web.find_element_by_xpath('/html/body/div[5]/div[2]/div[4]/div/div/div[2]/div/div[2]/button')
Submit3.click()
