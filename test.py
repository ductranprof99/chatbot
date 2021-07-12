from os import name
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:8000")

def open_messenger(opt):    
    try:
        # Connect
        
        global browser # this will prevent the browser variable from being garbage collected
        browser = webdriver.Chrome('./chromedriver.exe', options=opt)
        browser.set_window_size(1800, 900)
        browser.get("https://www.messenger.com/login/")
        WebDriverWait(browser, 5)
        nameField = browser.find_element_by_xpath('//input[@id="email"]')
        passwordField = browser.find_element_by_xpath('//input[@id="pass"]')
        nameField.send_keys('email')
        passwordField.send_keys('passwd',Keys.ENTER)
        # browser.send_keys('0918139331',Keys.TAB)
        # for i in listTag:
        #     print(i)
    except Exception as e:
        print (e, 'messenger')

open_messenger(chrome_options)
