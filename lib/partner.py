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


def readPartnerInBrowser(browser):
    sleep(1)
    chat_container =  browser.find_element_by_xpath('//div[@aria-label="Chat"]')
    listUser = chat_container.find_elements_by_xpath('//a')
    count = 0
    for i in listUser:
        a =i.get_attribute('href')
        if('/t/' in a):
            print(a)
            # xu ly url doi tuong
    
def gotoPartner(browser,fileStream):
    pass

def writePartner2File(browser,fileStream):
    pass

def readPartnerFromFile(browser,fileStream):
    pass