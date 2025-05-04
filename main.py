import os
import time
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

load_dotenv()

def init_webdriver(timeout):
    chrome_options = Options()

    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    chrome_service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    chrome_driver.implicitly_wait(timeout)

    return chrome_driver

def get_page(_driver, url):
    _driver.get(url)
    time.sleep(5)
    return BeautifulSoup(_driver.page_source, 'html.parser')

def dbmep_access_login_page(_driver):

    dpmep_url = os.getenv('BDMEP_URL')
    get_page(_driver, dpmep_url)

    _driver.find_element(By.LINK_TEXT, "Prosseguir").click()