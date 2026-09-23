from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv


# for i in range(2016,2021):
#     m_url = f'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={i}%EB%85%84+%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84'
#     print(m_url)

#     # 2. selenium : 자동화 구현
#     # 상단 제어창문구 삭제
#     options = Options()
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option("useAutomationExtension", False)
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     browser = webdriver.Chrome(options=options)
#     browser.maximize_window() # 화면 최대창 확대
#     url = m_url
#     browser.get(url)
#     time.sleep(3)   

#     # 파일저장
#     soup = BeautifulSoup(browser.page_source,'lxml')
#     os.makedirs('./p0923/file',exist_ok=True)
#     with open(f'p0923/file/movie_{i}.html','w',encoding='utf-8') as f:
#         f.write(soup.prettify())
#         time.sleep(2)

with open('p0923/file/movie_2016.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')        