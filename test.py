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

browser.get("https://www.messenger.com/t/*khach_id")
while(True):
    sleep(1)
    section_container =  browser.find_elements_by_xpath('//div[@data-testid="incoming_group"]')
    section_container =  browser.find_elements_by_xpath('//div[@data-testid="outgoing_group"]')
    for i in section_container:
        print(i.get_attribute('outerText'))
    