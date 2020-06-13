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


# In[ ]:


#identify login section
form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="login-form"]//form')))
#enter the ID
driver.find_element_by_xpath("//*[@type='text']").send_keys("Your User Id Here")
#enter the password
driver.find_element_by_xpath("//*[@type='password']").send_keys("Your Password Here")
#submit
driver.find_element_by_xpath("//*[@type='submit']").click()
#import time
import time
from selenium.common.exceptions import NoSuchElementException
#sleep for a second so that the page can submit and proceed to upcoming question (2fa)
time.sleep(1)
#identify login section for 2fa
form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="login-form"]//form')))
#enter the 2fa code
driver.find_element_by_xpath("//*[@type='password']").send_keys("2 Factor Authentication Here")
#submit
driver.find_element_by_xpath("//*[@type='submit']").click()
#import time
import time
from selenium.common.exceptions import NoSuchElementException
time.sleep(1)

