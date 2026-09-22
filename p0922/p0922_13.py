from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

# 2.selenium 파일저장
browser = webdriver.Chrome()
url = "https://stock.naver.com/market/stock/kr/stocklist/priceTop"
browser.get(url)
time.sleep(3)
soup = BeautifulSoup(browser.page_source,'lxml')
with open('stock2.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())
