#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import libraries
import selenium
#web automation framework
from selenium import webdriver
#used to ID the different keys on the keyboard
from selenium.webdriver.common.keys import Keys
#import time
import time
#define options
from selenium.webdriver.chrome.options import Options
#locate
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[ ]:


#my browser is safari
#make sure Remote Automation is enabled
driver = webdriver.Safari()


# In[ ]:


#the website we want to open
driver.get("https://kite.zerodha.com")


# In[ ]:


options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

# write your User Id
loginid = "AB1234"
# write your Password
password = "abc@123"
# write your PIN
loginpin = "123456"

def loginkite():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"userid"))).send_keys(loginid)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"password"))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@type='submit']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"pin"))).send_keys(loginpin)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@type='submit']"))).click()
loginkite()
