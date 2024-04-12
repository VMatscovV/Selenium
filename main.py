# 'utf-8'
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.page_load_strategy = 'normal'
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument( "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

tinurl = 'https://www.tinkoff.ru/cards/debit-cards/tinkoff-black/tariffs/'

driver.get(tinurl)
tininf = driver.find_elements(By.CLASS_NAME, "abawiNcsW")
for element in tininf:
    print(element.text)



