
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
import time
import os, sys
import numpy as numpy

driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get("http://zzzscore.com/1to50/en/?ts=1586677882244;")
assert "1to50" in driver.title

grid = driver.find_element_by_id("grid")
x = 1
y = 1
locations = numpy.zeros((50,), dtype=int)

for x in range(1,51):
    y = 1
    cellValue = 0
    while cellValue != str(x):
        cellLocation = '//*[@id="grid"]/div[' + str(y) + ']'
        #print(cellLocation)
        cell = driver.find_element(By.XPATH, cellLocation)
        cellValue = cell.text
        

        if cellValue != '':
            locations[int(cellValue) - 1] = y
            if (x != 1) and locations[x-1] != 0:
                y = locations[x-1]
                cellLocation = '//*[@id="grid"]/div[' + str(y) + ']'
                cell = driver.find_element(By.XPATH, cellLocation)
                cell.click()
                break
            elif cellValue == str(x):
                cell.click()
                print(cellValue)
                break
            else:
                y+=1
        else: y+=1
            
        #element.send_keys(username)
        #print("logged in")


# //*[@id="grid"]/div[1]
# //*[@id="grid"]/div[2]
# //*[@id="grid"]/div[7]
# //*[@id="grid"]/div[25]
# //*[@id="grid"]/div[23]/span
#//*[@id="grid"]/div[1]/span
#//*[@id="grid"]/div[1]/text()