
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

time.sleep(3)
# driver_path = 'C/Windows'
# web = webdriver.Chrome(executable_path=driver_path)
webdr = webdriver.Chrome()
webdr.get('http://192.168.0.253/webpages/login.html')

# wait to load the page
time.sleep(2)
# wait to load the page

PassForm = "admin"
# last = webdr.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/form[3]/div[2]/div/div/div[1]/span[2]/input[1]')
last = webdr.find_element(By.XPATH, '//*[@id="form-login"]/div[2]/div/div/div[1]/span[2]/input[1]')

# enter admin password
last.send_keys(PassForm)
# enter admin password

# click Login button
Submit = webdr.find_element(By.XPATH,'//*[@id="login-btn"]/span[2]')
Submit.click()
# click Login button

# wait to load page after logging in
time.sleep(4)
# wait to load page after logging in

# click Reboot button
Submit2 = webdr.find_element(By.XPATH,'//*[@id="txt-reboot"]')
Submit2.click()
# click Reboot button

# wait for the popup to show
time.sleep(2)
# wait for the popup to show

# click Yes at the popup to reboot
Submit3 = webdr.find_element(By.XPATH,'//*[@id="reboot_confirm_msg"]/div[4]/div/div/div[2]/div/div[2]/button/span[2]')
Submit3.click()
# click Yes at the popup to reboot