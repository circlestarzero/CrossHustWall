from PIL import Image
import pytesseract
import os
import time
from libhustpass import main
import sys

ticket = main.doLogin(os.environ['USERNAME'],os.environ['PASSWORD'],"http://access.hust.edu.cn/IDKJ-P/P/studentApi")
print(os.environ['USERNAME'],os.environ['PASSWORD'])
print(ticket)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option('prefs',{
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False,
    },
    "download": {
        'default_directory': "/usr/local/download",
    }
})

driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
try:
    driver.get(ticket)
except Exception:
    print ("gg")


time.sleep(1)
driver.find_element_by_class_name("am-button").click()
time.sleep(1)
driver.find_element_by_class_name("textArea").send_keys("上课")
time.sleep(1)
driver.find_element_by_class_name("submitbtn").click()
time.sleep(5)
print (driver.title)


