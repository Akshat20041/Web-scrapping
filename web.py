import numpy as np
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://opstra.definedge.com')
time.sleep(4)

Start = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/nav/div/div[4]/button/div').click()

username = driver.find_element(By.ID, 'username').send_keys("akshatchouksey07@gmail.com")

password= driver.find_element(By.ID, 'password').send_keys(" *** ")

Click = driver.find_element(By.ID , 'kc-login').click()

driver.get('https://opstra.definedge.com/strategy-builder')
time.sleep(3)
NEXT = driver.find_element(By.XPATH, '//*[@id="app"]/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[1]/div[1]').click()

for i in range(1,11) :
    add = f'//*[@id="app"]/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[2]/div[1]/div[{i}]/button/div'
    A = driver.find_element(By.XPATH, add).click()
    
    CallLTP = driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
    itmprob = driver.find_elements(By.XPATH, '//tbody/tr/td[2]')
    CallIv = driver.find_elements(By.XPATH, '//tbody/tr/td[3]')
    CallDelta = driver.find_elements(By.XPATH, '//tbody/tr/td[4]')
    StrikePrice = driver.find_elements(By.XPATH, '//tbody/tr/td[5]')
    PutDelta = driver.find_elements(By.XPATH, '//tbody/tr/td[6]')
    PutIV = driver.find_elements(By.XPATH, '//tbody/tr/td[7]')
    ITMProb = driver.find_elements(By.XPATH, '//tbody/tr/td[8]')
    PutLTP = driver.find_elements(By.XPATH, '//tbody/tr/td[9]')
    DATA = []
    
    for i in range(len(CallLTP)):
        Tdata={'CallLTP': CallLTP[i].text,
                  'itmprob': itmprob[i].text,
                  'CallIv': CallIv[i].text,
                  'CallDelta': CallDelta[i].text,
                  'StrikePrice': StrikePrice[i].text,
                  'PutDelta': PutDelta[i].text,
                  'PutIV': PutIV[i].text,
                  'ITMProb': ITMProb[i].text,
                  'PutLTP': PutLTP[i].text}
        DATA.append(Tdata)

    df = pd.DataFrame(DATA)
    df
    output_file = 'output{i}.csv'

    df.to_csv(output_file, index=False)
