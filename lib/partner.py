from time import sleep, time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8000")
browser = webdriver.Chrome('./chromedriver.exe', options=opt)


def readPartnerInBrowser():
    sleep(1)
    chat_container =  browser.find_element_by_xpath('//div[@data-testid="MWJewelThreadListContainer"]')
    listUser = chat_container.find_elements_by_xpath('//a')
    count = 0
    for i in listUser:
        a =i.get_attribute('href')
        if('/t/' in a):
            b = str(a).split('/t/')[1].split('/')[0]
            print(b)
            # xu ly url doi tuong
    
def gotoPartner(fileStream):
    pass

def writePartner2File(fileStream):
    pass

def readPartnerFromFile(fileStream):
    pass

def partnerMessageQueue():
    sleep(1)
    usrNameList =  browser.find_elements_by_xpath('//div[@data-testid="mwthreadlist-item"]/div[@role="gridcell"]/div/a/div/div/div/div/div/div/span/span')[0::2]
    messageList =  browser.find_elements_by_xpath('//div[@data-testid="mwthreadlist-item"]/div[@role="gridcell"]/div/a/div/div/div/div/div/div/span/span/div/span')[0::3]
    timerList =  browser.find_elements_by_xpath('//div[@data-testid="mwthreadlist-item"]/div[@role="gridcell"]/div/a/div/div/div/div/div/div/span/span/div/span')[2::3]
    listPair = []
    for i in range(0,len(usrNameList)):
        listPair.append({"user":usrNameList[i].get_attribute("innerText"),"message": messageList[i].get_attribute("innerText"),"send_time":timerList[i].get_attribute("innerText"),"colors":messageList[i].value_of_css_property("color")})
    for x in listPair:
        print(x)
        # content = x.find_element_by_xpath('//div')   # [1].find_element_by_xpath('//span/span/div')
        # messageText = content.find_elements_by_xpath('//div')[1]
        # time = prevMessageBox.find_elements_by_xpath('//*')[2]
        # print(messageText.get_attribute("innerText"))
        # print(time.get_attribute('innerText'))