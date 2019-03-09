from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import os
from collections import OrderedDict
import urllib.request
from pathlib import Path
from requests import get
import time
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd



delay=20
browser=webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.agencyspotter.com/search?industry_ids%5B%5D=20&location=INDIA&budget_min=0&budget_mid=infinity&optradio=project&q=&button=regular")    
myElm=WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#log_in_button')))
myElm.click()

uname='EnterUserName'
pwd='EnterPassword'
username=browser.find_element_by_id('user_email')
password=browser.find_element_by_id('user_password')
username.send_keys(uname)
password.send_keys(pwd)
conti = browser.find_element_by_name('commit')
conti.click()
sleep(10)


linksver1=browser.find_elements_by_xpath("//a[@href]")
linksver2 = [link.get_attribute('href') for link in browser.find_elements_by_xpath("//a[@href]")]
browser.implicitly_wait(30)
d=OrderedDict()
linksver2=[]
uselinks=[]
for i in range(len(linksver1)):
    try:
        if(linksver1[i].get_attribute('data-type')=='Agency'):
            linksver2.append(linksver1[i].get_attribute('href'))
            sleep(4)
    except:
	    browser.implicitly_wait(30)
for i in range(len(linksver2)):
    print(str(i)+'.'+linksver2[i]) 	
#for x in linksver2:
 #   d[x]=True
#for x in d:
 #   uselinks.append(x)
    #print(x+"\n")
browser.implicitly_wait(10)

listofagency=[]
listofln=[]
listofcontact=[]
listoftype=[]
listofloc=[]

for i in range(len(linksver2)):	
    browser.get(linksver2[i])
    element = browser.find_element_by_xpath('//div[@id="agency_name_and_industry"]/h1').text
    #element=browser.find_element_by_xpath('//div[@itemprop="name"]').text
    print(str(i)+'.'+element)
    try:
        div = browser.find_element_by_css_selector('a.connect-linkedin.linkedin')
        linksver3=div.get_attribute('href')
        print(linksver3)
    except:
	    linksver3='NA'
        
		 
    dive = browser.find_element_by_css_selector('a.contact.btn.lrg.gradOrange.white')
    linksver4=dive.get_attribute('href')
    print(linksver4)
    dive1 = browser.find_element_by_css_selector('a.blue.tsWhite').text
    print(dive1)
    dive2=browser.find_element_by_css_selector("div.location > div").text 
    print(dive2)	
    #dive3=browser.find_element_by_css_selector("div.location > div > span > span").text
    #print(dive3)
    listofagency.append(element)
    listofln.append(linksver3)
    listofcontact.append(linksver4)
    listoftype.append(dive1)
    listofloc.append(dive2)
data={'agency name':listofagency,'Agency Address':listofloc,'Agency Type':listoftype,'Agency web site':listofcontact,'Agency LinkedIn page':listofln}
df=pd.DataFrame(data)
print(df)
df.to_excel('C:\\Users\\Sarang RS\\Documents\\test.xlsx', sheet_name='sheet1', index=False)
  
	