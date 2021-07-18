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

# while(True):
#     sleep(1)
#     section_container_in =  browser.find_elements_by_xpath('//div[@data-testid="incoming_group"]')
#     section_container_out =  browser.find_elements_by_xpath('//div[@data-testid="outgoing_group"]')
#     for i in section_container_out:
#         print(i.get_attribute('outerText'))
    

def detectIncomingMessage(browser):
    sleep(1)
    section_container_in =  browser.find_elements_by_xpath('//div[@data-testid="messenger_incoming_text_row"]')
    for i in section_container_in:
        print(i.get_attribute('outerText'))

def detectOutcomingMessage(browser):
    section_container_out =  browser.find_elements_by_xpath('//div[@data-testid="outgoing_group"]')
    for i in section_container_out:
        print(i.get_attribute('outerText'))

detectIncomingMessage(browser=browser)