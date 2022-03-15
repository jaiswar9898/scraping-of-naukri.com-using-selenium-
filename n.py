from struct import pack
from selenium import webdriver
from  bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import requests
from openpyxl import Workbook
import time
import pandas as pd 


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.naukri.com/job-listings-looking-for-java-python-developers-freshers-osian-infotech-pvt-ltd-mumbai-0-to-1-years-080322004198?src=jobsearchDesk&sid=16473630263235582&xp=5&px=1")
time.sleep(6)

Job_titles=driver.find_elements(By.XPATH,'//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[1]/header/h1') 
for job in (Job_titles): 
    print('The job title is :-',job.text)
time.sleep(3)

locations=driver.find_elements(By.XPATH,'//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[2]/div[3]/span/a') 
for location in (locations): 
    print('The job location is :-',location.text)
time.sleep(3)

expereince=driver.find_elements(By.XPATH,'//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[2]/div[1]/span') 
for exp in (expereince): 
    print('Expereince :-',exp.text)
time.sleep(3)

package=driver.find_elements(By.XPATH,'//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[2]/div[2]/span') 
for pack in (package): 
    print('Package :-',pack.text)
time.sleep(3)

description=driver.find_elements(By.XPATH,'//*[@id="root"]/main/div[2]/div[2]/section[2]/div[2]') 
for des in (description): 
    print('Description :-',des.text)
time.sleep(3)


