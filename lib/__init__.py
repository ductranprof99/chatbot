
import subprocess,os,sys,json
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:8000")

if(not os.path.isdir('./profileFolder')):
    os.mkdir('./profileFolder')
    print('profile Folder created by script')
else:
    print('profile Folder exist')


if(os.path.isfile('./shellscript.ps1')):
    profileFolder = "\'" + os.path.abspath('./profileFolder') + "\'" 
    p = subprocess.Popen(["powershell.exe", "./shellscript.ps1 "+ profileFolder], 
              stdout=sys.stdout)
    p.communicate()
    
account_stream = json.load(open('account.json'))
partner_stream = json.load(open('partner.json'))

def open_messenger(opt,iter):    
    try:
        # Connect
        global browser # this will prevent the browser variable from being garbage collected
        browser = webdriver.Chrome('./chromedriver.exe', options=opt)
        browser.set_window_size(1800, 900)
        browser.get("https://www.messenger.com/login/")
        nameField = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="email"]')))
        actionChains = ActionChains(browser)
        actionChains.double_click(nameField).perform()
        actionChains.send_keys(Keys.BACK_SPACE)
        nameField.send_keys(iter["username"],Keys.TAB,iter["password"],Keys.ENTER)
    except Exception as e:
        print (e, 'messenger')

open_messenger(chrome_options,account_stream)
sleep(5)

import lib.messageReader as msgReader

# msgReader.mazeRunner()

import lib.partner as usr

usr.readPartnerInBrowser()
usr.partnerMessageQueue()