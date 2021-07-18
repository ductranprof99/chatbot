import subprocess,os,sys,json
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8000")
browser = webdriver.Chrome('./chromedriver.exe', options=opt)


def sendMessage(browser):
    messageBox =  browser.find_element_by_xpath('//div[@contenteditable="true"]')
    actionChains = ActionChains(browser)
    actionChains.click(messageBox).perform()
    messageBox.send_keys("this message send by auto-reply program",Keys.ENTER)
    sleep(2)
    messageBox.send_keys("this message send after 2 secs, loop after 10 secs",Keys.ENTER)
    sleep(10)

while(True):
    sendMessage(browser)