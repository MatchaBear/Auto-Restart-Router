import By as By
from selenium import webdriver
# from .edge.webdriver import WebDriver as ChromiumEdge
import time

time.sleep(3)
# driver_path = 'C/Windows'
# web = webdriver.Chrome(executable_path=driver_path)
web = webdriver.Chrome()
web.get('http://192.168.0.253/webpages/login.html')

# wait to load the page
time.sleep(2)
# wait to load the page

PassForm = "admin"
last = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/form[3]/div[2]/div/div/div[1]/span[2]/input[1]')

# enter admin password
last.send_keys(PassForm)
# enter admin password

# click Login button
Submit = web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/form[3]/div[3]/div/div/div/div[1]/button')
Submit.click()
# click Login button

# wait to load page after logging in
time.sleep(4)
# wait to load page after logging in

# click Reboot button
Submit2 = web.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/a[4]/span[1]')
Submit2.click()
# click Reboot button

time.sleep(2)

# click Yes at the popup to reboot
# Submit3 = web.find_element_by_xpath('/html/body/div[5]/div[2]/div[4]/div/div/div[2]/div/div[2]/button')
Submit3 = web.find_element(by=By.XPATH, value='/html/body/div[5]/div[2]/div[4]/div/div/div[2]/div/div[2]/button')
# Submit3.click()
# click Yes at the popup to reboot