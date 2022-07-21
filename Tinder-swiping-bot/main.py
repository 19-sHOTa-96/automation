from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

url = "https://tinder.com"
chrome_driver_path = r"chrome-driver-path/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
driver.get(url)

FB_LOG = input("Enter facebook username: ")
FB_PAS = input("Enter facebook password: ")

#step 1
sleep(10)
log = driver.find_element_by_xpath('//*[@id="o1926512098"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]')
log.click()

#step 2
sleep(5)
log_fb = driver.find_element_by_xpath('//*[@id="o198131022"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
log_fb.click()

#step 3

sleep(5)
handles = driver.window_handles
fb_window = handles[1]
driver.switch_to.window(fb_window)
email_or_phone = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
email_or_phone.send_keys(FB_LOG)
password.send_keys(FB_PAS)
sleep(2)
password.send_keys(Keys.ENTER)

sleep(5)
driver.switch_to.window(handles[0])

sleep(5)
driver.find_element_by_xpath('//*[@id="o198131022"]/div/div/div/div/div[3]/button[1]').click()

sleep(5)
driver.find_element_by_xpath('//*[@id="o198131022"]/div/div/div/div/div[3]/button[2]').click()

sleep(5)

try:
    b = driver.find_element_by_xpath('//*[@id="o198131022"]/div/div/div[1]/div/div[2]/button[2]/span').click()
    sleep(2)
except:
    pass


sleep(5)
like = driver.find_element_by_xpath('//*[@id="o1926512098"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span')

for _ in range(100):
    try:
        sleep(2)
        like.click()
    except:
        driver.find_element_by_xpath('//*[@id="o198131022"]/div/div/div[2]/button[2]').click()
        continue
