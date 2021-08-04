import subprocess,os,sys,json
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8000")
browser = webdriver.Chrome('./chromedriver.exe', options=opt)
 

def detectIncomingMessage():
    pass

def detectOutcomingMessage():
    pass


def readMessageWithOrder():
    oleum =  browser.find_elements_by_xpath('//div[@role="grid"]')
    message_section = oleum[1]
    div_es = message_section.find_elements_by_xpath('//div')
    orderMessages = []  # list of element
    for eachDiv in div_es:
        if(eachDiv.get_attribute('data-testid') == "outgoing_group" or eachDiv.get_attribute('data-testid') == "incoming_group"):
            orderMessages.append(eachDiv)
    for eachDiv in orderMessages:
        if(eachDiv.get_attribute('data-testid') == "outgoing_group"):
            print("Out")
            print(eachDiv.get_attribute('outerText'))
            # xu li out
        if(eachDiv.get_attribute('data-testid') == "incoming_group"):
            print("In")
            print(eachDiv.get_attribute('outerText'))
            # xu li in 


# readMessageWithOrder()

